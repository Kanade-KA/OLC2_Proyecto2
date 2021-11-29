from Instrucciones.Return import Return
from Instrucciones.Continue import Continue
from TablaSimbolo.Entorno import Entorno
from TablaSimbolo.Error import Error
from Abstract.NodoAST import NodoAST
from Instrucciones.Break import Break
class If(NodoAST):
    def __init__(self, condicion, instruccionesIf, instruccionesElse, ElseIf, fila, columna):
        self.condicion = condicion
        self.instruccionesIf = instruccionesIf
        self.instruccionesElse = instruccionesElse
        self.elseIf = ElseIf
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        x = ""
        condicional = self.condicion.interpretar(arbol, entorno)
        if condicional == True:
            if self.instruccionesIf != None:
                nuevoentorno = Entorno("IF", entorno)
                for instruccion in self.instruccionesIf:
                    if isinstance(instruccion, Break):
                        return instruccion
                    if isinstance(instruccion, Continue):
                        return instruccion
                    if isinstance(instruccion, Return):
                        return instruccion.interpretar(arbol, nuevoentorno)
                    else:
                        instruccion.interpretar(arbol, nuevoentorno)
            return None
        else:
            if not self.instruccionesElse == None:
                nuevoentorno2 = Entorno("ELSE", entorno)
                for instruccion in self.instruccionesElse:
                    if isinstance(instruccion, Break):
                        return instruccion
                    if isinstance(instruccion, Continue):
                        return instruccion
                    if isinstance(instruccion, Return):
                        return instruccion.interpretar(arbol, nuevoentorno2)
                    else:
                        instruccion.interpretar(arbol, nuevoentorno2)
        if self.elseIf != None:
                return self.elseIf.interpretar(arbol, entorno)
        return None

    def graficar(self, nodo):
        padre = nodo.getContador()
        nodo.newLabel("IF")
        nodo.IncrementarContador()

        if self.condicion != None:
            hijo = self.condicion.graficar(nodo)
            nodo.newEdge(padre, hijo)

        if self.instruccionesIf != None:
            for ins in self.instruccionesIf:
                hijo = ins.graficar(nodo)
                nodo.newEdge(padre, hijo)

        if self.instruccionesElse != None:
            nelse = nodo.getContador()
            nodo.newLabel("ELSE")
            nodo.IncrementarContador()
            nodo.newEdge(padre, nelse)
            for ins in self.instruccionesElse:
                hijo = ins.graficar(nodo)
                nodo.newEdge(nelse, hijo)

        if self.elseIf:
            hijo = self.elseIf.graficar(nodo)
            nodo.newEdge(padre, hijo)
        return padre
    
    def traducir(self, traductor, entorno):
        traductor.addCodigo("//**************************IF**************************\n")
        condicional = self.condicion.traducir(traductor, entorno)
        if condicional != "error":#para evitar errores
            #ETIQUETA PARA SALIR DEL IF
            salida = "L" + str(traductor.getGotos())
            traductor.IncrementarGotos(1)
            #ETIQUETA DE ACEPTACION
            traductor.addCodigo(str(condicional[0])+":\n")
            if self.instruccionesIf != None:
                nuevoentorno = Entorno("IF", entorno)
                for i in self.instruccionesIf:
                    x = i.traducir(traductor, nuevoentorno)
                    if x == "isbreak":
                        traductor.addCodigo("goto L"+str(traductor.getGotos())+";\n")
                        traductor.setBreak(traductor.getGotos())
                        traductor.IncrementarGotos(1)
                    if x == "iscontinue":
                        traductor.addCodigo("goto "+traductor.getContinue()+";\n")
            traductor.addCodigo("goto "+salida+";\n")#PARA QUE YA NO HAGA EL ELSE O ELSEIF
            #ETIQUETA DE RECHAZO
            traductor.addCodigo(str(condicional[1])+": \n")
            
            if self.instruccionesElse != None:
                nuevoentorno2 = Entorno("ELSE", entorno)
                for i in self.instruccionesElse:
                    x = i.traducir(traductor, nuevoentorno2)
                    if x == "isbreak":
                        traductor.addCodigo("goto L"+str(traductor.getGotos())+";\n")
                        traductor.setBreak(traductor.getGotos())
                        traductor.IncrementarGotos(1)
                    if x == "iscontinue":
                        traductor.addCodigo("goto "+traductor.getContinue()+";\n")
            if self.elseIf != None:
                self.elseIf.traducir(traductor, entorno)
            #ETIQUETA DE SALIDA
            traductor.addCodigo(salida+": \n") 
        return 