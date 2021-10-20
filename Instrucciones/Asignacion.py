from Abstract.Objeto import TipoObjeto
from Expresiones.Aritmetica import Aritmetica
from Instrucciones.LlamaMatriz import LlamaMatriz
from Instrucciones.Return import Return
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Simbolo import Simbolo
from TablaSimbolo.Error import Error
from Instrucciones.Retonar import Retornar
class Asignacion(NodoAST):
    def __init__(self, identificador, expresion, tipo, fila, columna):
        self.identificador = identificador
        self.expresion = expresion
        self.tipo = tipo
        self.fila = fila
        self.columna = columna
        
    def interpretar(self, arbol, entorno):
        value = None
        if not self.expresion == None:
            value = self.expresion.interpretar(arbol, entorno)
        if self.tipo.lower() == "int64": #Es por que tiene un tipo (se declaró con tipo)
            if not isinstance(value, int):
                arbol.addExcepcion(Error("Semántico","La variable "+self.identificador+", no es de tipo int", self.fila, self.columna))
                return
        if self.tipo.lower() == "float64":
            if not isinstance(value, float):
                arbol.addExcepcion(Error("Semántico","La variable "+self.identificador+", no es de tipo float", self.fila, self.columna))
                return
        if self.tipo.lower() == "string":
            if not isinstance(value, str):
                arbol.addExcepcion(Error("Semántico","La variable "+self.identificador+", no es de tipo string", self.fila, self.columna))
                return
        if self.tipo.lower() == "global":
            simbolo = Simbolo(entorno.getNombre(), self.identificador, value, arbol.getTipo(value),  self.tipo, 0, self.fila, self.columna)
            arbol.addSimbolo(simbolo)
            entorno.AgregarGlobal(simbolo)
            return
        valor = self.expresion.interpretar(arbol, entorno)
        simbolo = Simbolo(entorno.getNombre(), self.identificador, valor, arbol.getTipo(valor), "Variable", 0, self.fila, self.columna)
        arbol.addSimbolo(simbolo)
        entorno.addSimbolo(simbolo)
        return


    def traducir(self, traductor, entorno):
        value = None
        if not self.expresion == None:
            value = self.expresion.traducir(traductor, entorno)
        #----------------------------SI SE DECLARA CON TIPO-----------------------------------------------------
        if self.tipo.lower() == "int64":
            if not isinstance(value[0], int):
                traductor.addExcepcion(Error("Semántico","La variable "+self.identificador+", no es de tipo int", self.fila, self.columna))
                return
        if self.tipo.lower() == "float64":
            if not isinstance(value[0], float):
                traductor.addExcepcion(Error("Semántico","La variable "+self.identificador+", no es de tipo float", self.fila, self.columna))
                return
        if self.tipo.lower() == "string":
            if not isinstance(value[0], str):
                traductor.addExcepcion(Error("Semántico","La variable "+self.identificador+", no es de tipo string", self.fila, self.columna))
                return
        if self.tipo.lower() == "bool":
            if not isinstance(value[0], bool):
                traductor.addExcepcion(Error("Semántico","La variable "+self.identificador+", no es de tipo string", self.fila, self.columna))
                return
        if isinstance(self.expresion, Aritmetica):
            if value != "error":
                tipo = value[1]
                if tipo == TipoObjeto.ENTERO or tipo == TipoObjeto.DECIMAL:
                    cadena = "stack[int("+str(traductor.getStack())+")] = "+str(value[0])+";//Agrego la variable\n"
                    cadena += "S = S + 1;\n"
                    simbolo = Simbolo(entorno.getNombre(), self.identificador, value[0], tipo, "Variable", traductor.getStack(), self.fila, self.columna)
                    traductor.IncrementarStack()
                    traductor.addCodigo(cadena)
                    entorno.addSimbolo(simbolo)
                    traductor.addSimbolo(simbolo)
                    return
                elif tipo == TipoObjeto.CADENA:#Es un string
                    ptero = traductor.putStringHeap(value[0])
                    cadena = ""
                    cadena += "t"+str(traductor.getContador())+" = "+str(ptero) + ";//Guardo en un temporal el integer del heap\n"
                    cadena += "stack[int("+str(traductor.getStack())+")] = t"+str(traductor.getContador())+";//Guardo en el stack el puntero del heap\n"
                    cadena += "S = S + 1;//Se aumenta el stack para poder meter otro numero\n\n"
                    traductor.addCodigo(cadena)
                    apuntastack = traductor.getStack()
                    traductor.IncrementarStack()#Incrementamos el stack para que agarre el nuevo
                    traductor.IncrementarContador()
                    simbolo = Simbolo(entorno.getNombre(), self.identificador, value[0], tipo, "Variable", apuntastack, self.fila, self.columna)
                    traductor.addSimbolo(simbolo)
                    entorno.addSimbolo(simbolo)
                    return
        else:
            if value != "error":
                self.Asignar(value[1], value[0], self.identificador, entorno, traductor)
            return 

    def Asignar(self, tipo, valor, id, entorno, traductor):
        if tipo == TipoObjeto.ENTERO:
            apuntador = traductor.putIntStack(valor)
            simbolo = Simbolo(entorno.getNombre(), id, valor, tipo, "Variable", apuntador, self.fila, self.columna)
            entorno.addSimbolo(simbolo)
            traductor.addSimbolo(simbolo)
        if tipo == TipoObjeto.CADENA:
            apuntadorheap = traductor.putStringHeap(valor)
            #Tengo que guardar el apuntador del heap en el stack
            cadena = ""
            cadena += "t"+str(traductor.getContador())+" = "+str(apuntadorheap) + ";//Guardo en un temporal el integer del heap\n"
            cadena += "stack[int("+str(traductor.getStack())+")] = t"+str(traductor.getContador())+";//Guardo en el stack el puntero del heap\n"
            cadena += "S = S + 1;//Se aumenta el stack para poder meter otro numero\n\n"
            traductor.addCodigo(cadena)
            apuntastack = traductor.getStack()
            traductor.IncrementarStack()#Incrementamos el stack para que agarre el nuevo
            traductor.IncrementarContador()
            simbolo = Simbolo(entorno.getNombre(), id, valor, tipo, "Variable", apuntastack, self.fila, self.columna)
            traductor.addSimbolo(simbolo)
            entorno.addSimbolo(simbolo)
        if tipo == TipoObjeto.DECIMAL:
            apuntador = traductor.putDoubleStack(valor)
            simbolo = Simbolo(entorno.getNombre(), id, valor, tipo, "Variable", apuntador, self.fila, self.columna)
            entorno.addSimbolo(simbolo)
            traductor.addSimbolo(simbolo)
        if tipo == TipoObjeto.BOOLEANO:
            apuntador = traductor.putBooleanStack(valor)
            simbolo = Simbolo(entorno.getNombre(), id, valor, tipo, "Variable", apuntador, self.fila, self.columna)
            entorno.addSimbolo(simbolo)
            traductor.addSimbolo(simbolo)
            return
        return