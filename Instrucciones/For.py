from Abstract.Objeto import TipoObjeto
from TablaSimbolo.Entorno import Entorno
from Expresiones.Identificador import Identificador
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Simbolo import Simbolo
from TablaSimbolo.Error import Error
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
from Instrucciones.Return import Return
class For(NodoAST):
    def __init__(self, indice, inicio, fin, instrucciones, fila, columna):
        self.indice = indice
        self.inicio = inicio
        self.fin = fin
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        #Hay que ver que el identificador sea identificador :v 
        if isinstance(self.indice, Identificador):
            ind = self.indice.getIdentificador()    
            simbolo = Simbolo(entorno.getNombre(), ind, "", "", "Variable", 0, self.fila, self.columna)
            entorno.addSimbolo(simbolo)
            if self.fin != None:#quiere decir que traía 2 puntos
                inicio = self.inicio.interpretar(arbol, entorno)
                fin = self.fin.interpretar(arbol, entorno)
                if not isinstance(inicio, str) or not isinstance(fin, str):
                    if not fin < inicio:
                        #NUEVO ENTORNO
                        if isinstance(inicio, int) and isinstance(fin, int):
                                nuevoentorno = Entorno("For", entorno)
                                for i in range(inicio, fin +1):
                                    #Hay que actualizar la variable
                                    simbolo = Simbolo(entorno.getNombre(), ind, i,"", "Variable", 0, self.fila, self.columna)
                                    
                                    entorno.tabla[ind] = simbolo
                                    for instrucciones in self.instrucciones:
                                        y = instrucciones.interpretar(arbol, nuevoentorno)
                                        if y != None and y!="":
                                            return y
                                        if isinstance(y, Return):
                                            return y
                                        if isinstance(y, Break):
                                            return None
                                        if isinstance(y, Continue):
                                            break
                            
                        else:
                            nuevoentorno = Entorno("For", entorno)
                            iniciofloat = 0
                            if isinstance(fin, float):
                                #Parsear el inicio
                                iniciofloat = float(inicio)
                            while(True):
                                if(iniciofloat > fin):
                                    break
                                #Hay que actualizar la variable
                                simbolo = Simbolo(entorno.getNombre(), ind, iniciofloat, "", "Variable", 0, self.fila, self.columna)
                                
                                entorno.tabla[ind] = simbolo
                                for instrucciones in self.instrucciones:
                                    y = instrucciones.interpretar(arbol, nuevoentorno)
                                    if y != None and y!="":
                                        return y
                                    if isinstance(y, Return):
                                        arbol.addExcepcion(Error("Semántico", "No se puede usar el Return con un Loop", self.fila, self.columna))
                                    if isinstance(y, Break):
                                        return None
                                    if isinstance(y, Continue):
                                        break
                                iniciofloat = iniciofloat + 1.0
                            return None
                    else:
                            arbol.addExcepcion(Error("Semantico", "No se puede iterar, el numero final es menor al inicial", self.fila, self.columna))
                else:
                        arbol.addExcepcion(Error("Semantico", "No se puede iterar Con cadenas en un intervalo", self.fila, self.columna))
            else:#Quiere decir que solo viene una cadena
                iterador = self.inicio.interpretar(arbol, entorno)
                if isinstance(iterador, str):
                    nuevoentorno = Entorno("For",entorno)
                    for i in iterador:
                        #Hay que actualizar la variable
                        simbolo = Simbolo(entorno.getNombre(), ind, i, "", "Variable", 0, self.fila, self.columna)
                        
                        entorno.tabla[ind] = simbolo
                        for instrucciones in self.instrucciones:
                            y = instrucciones.interpretar(arbol, nuevoentorno)
                            if y != None and y!="":
                                return y
                            if isinstance(y, Return):
                                arbol.addExcepcion(Error("Semántico", "No se puede usar el Return con un Loop", self.fila, self.columna))
                            if isinstance(y, Break):
                                return None
                            if isinstance(y, Continue):
                                break
                else:#o un numero
                    nuevoentorno = Entorno("For", entorno)
                    simbolo = Simbolo(entorno.getNombre(), ind, iterador, "", "Variable", 0, self.fila, self.columna)
                    
                    entorno.tabla[ind] = simbolo#no estoy segura de si es entorno o tabla normal
                    for instrucciones in self.instrucciones:
                            y = instrucciones.interpretar(arbol, nuevoentorno)
                            if y != None and y!="":
                                return y
                            if isinstance(y, Return):
                                arbol.addExcepcion(Error("Semántico", "No se puede usar el Return con un Loop", self.fila, self.columna))
                            if isinstance(y, Break):
                                return ""
                            if isinstance(y, Continue):
                                break

        return None

    def traducir(self, traductor, entorno):
        traductor.addCodigo("//------------------------------------for--------------------------------\n")
        etiquetainicio="L"+str(traductor.getGotos())
        etiquetaejecutar = "L"+ str(traductor.getGotos()+1)
        etiquetareinicio = "L"+ str(traductor.getGotos()+2)
        etiquetafin = "L"+str(traductor.getGotos()+3)
        traductor.IncrementarGotos(4)
        nuevoentorno = Entorno("FOR", entorno)
        indice = self.indice.getIdentificador()
        if self.fin != None:#Quiere decir que es un rango 
            inicio = self.inicio.traducir(traductor, entorno)
            fin = self.fin.traducir(traductor, entorno)
            #VER SI ES ID...
            if isinstance(self.inicio, Identificador):
                tipo = self.inicio.getTipo(traductor, entorno)
                traer = "t"+str(traductor.getContador())+" = stack[int("+str(inicio)+")];//Traemos la variable\n"
                resultado = "t"+str(traductor.getContador())
                traductor.addCodigo(traer)
                traductor.IncrementarContador()
                inicio = [resultado, tipo]
            if isinstance(self.fin, Identificador):
                tipo = self.fin.getTipo(traductor, entorno)
                traer = "t"+str(traductor.getContador())+" = stack[int("+str(fin)+")];//Traemos la variable\n"
                resultado = "t"+str(traductor.getContador())
                traductor.addCodigo(traer)
                traductor.IncrementarContador()
                fin = [resultado, tipo]

            if self.verificarTipo(inicio[1], fin[1]):
                #Agregando el indice
                guardavariable = "t"+str(traductor.getContador())
                cadena = guardavariable +" = S + "+ str(traductor.getStack())+"; //generando un tmp para meter la variable\n"
                cadena += "stack[int("+str(guardavariable)+")] = "+str(inicio[0])+";//Inicializando el indice\n"
                simbolo = Simbolo("FOR", indice, inicio[0], inicio[1], "Variable", traductor.getStack(), self.fila, self.columna)
                nuevoentorno.addSimbolo(simbolo)
                traductor.addSimbolo(simbolo)
                traductor.IncrementarStack()
                traductor.addCodigo(cadena)
                traductor.IncrementarContador()
                traductor.addCodigo(etiquetainicio+":\n")
                #Aqui debo de traer la variable, y hacer el if:
                cadena = "t"+str(traductor.getContador())+" = stack[int("+guardavariable+")];//Traigo el indice\n"
                cadena += "if t"+str(traductor.getContador()) +" <= "+str(fin[0])+"{ goto "+etiquetaejecutar+"; }//Lo comparo\n"
                cadena += "goto "+etiquetafin +";\n"
                cadena += etiquetaejecutar + "://EJECUTA LAS INSTRUCCIONES\n"
                traductor.addCodigo(cadena)
                traductor.IncrementarContador()
                for i in self.instrucciones:
                    i.traducir(traductor, nuevoentorno)
                cadena = "goto "+etiquetareinicio+";\n"
                cadena += etiquetareinicio+"://ETIQUETA PARA REALIZAR EL INCREMENTO Y QUE REGRESE\n"
                cadena += "t"+str(traductor.getContador())+" = stack[int("+guardavariable+")];\n"
                traductor.IncrementarContador()
                cadena += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador()-1)+" + 1;\n"
                cadena += "stack[int("+guardavariable+")] = t"+str(traductor.getContador())+";\n"
                cadena += "goto "+etiquetainicio+";\n"
                cadena += etiquetafin+":\n"
                traductor.IncrementarContador()
                traductor.addCodigo(cadena)
        return

    def verificarTipo(self, opi, opd):
        if opi == TipoObjeto.ENTERO or opi == TipoObjeto.DECIMAL:
            if opd == TipoObjeto.ENTERO or opd == TipoObjeto.DECIMAL:
                return True
        return False