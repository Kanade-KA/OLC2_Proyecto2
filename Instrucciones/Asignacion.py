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
        if self.tipo.lower() == "int64": #Es por que tiene un tipo (se declaró con tipo)
            if not isinstance(value, int):
                traductor.addExcepcion(Error("Semántico","La variable "+self.identificador+", no es de tipo int", self.fila, self.columna))
                return
        if self.tipo.lower() == "float64":
            if not isinstance(value, float):
                traductor.addExcepcion(Error("Semántico","La variable "+self.identificador+", no es de tipo float", self.fila, self.columna))
                return
        if self.tipo.lower() == "string":
            if not isinstance(value, str):
                traductor.addExcepcion(Error("Semántico","La variable "+self.identificador+", no es de tipo string", self.fila, self.columna))
                return
        if self.tipo.lower() == "bool":
            if not isinstance(value, bool):
                traductor.addExcepcion(Error("Semántico","La variable "+self.identificador+", no es de tipo string", self.fila, self.columna))
                return
        if isinstance(self.expresion, Aritmetica):
            if value == None:
                value = self.expresion.traducir(traductor, entorno)
            #Tengo que ver que no sea un string
            tipo = traductor.getTipoActual()
            if tipo == "int" or tipo == "doble":
                cadena = "stack[int(S)] = "+value+"//Agrego la variable\n"
                cadena += "S = S + 1\n"
                simbolo = Simbolo(entorno.getNombre(), self.identificador, value, tipo, "Variable", traductor.getStack(), self.fila, self.columna)
                traductor.IncrementarStack()
                traductor.addCodigo(cadena)
                entorno.addSimbolo(simbolo)
                traductor.addSimbolo(simbolo)
                return
            elif tipo == "string":#Es un string
                ptero = traductor.putStringHeap(value)
                cadena = ""
                cadena += "t"+str(traductor.getContador())+" = "+str(ptero) + ";//Guardo en un temporal el integer del heap\n"
                cadena += "stack[int(S)] = t"+str(traductor.getContador())+";//Guardo en el stack el puntero del heap\n"
                cadena += "S = S + 1 //Se aumenta el stack para poder meter otro numero\n\n"
                traductor.addCodigo(cadena)
                apuntastack = traductor.getStack()
                traductor.IncrementarStack()#Incrementamos el stack para que agarre el nuevo
                traductor.IncrementarContador()
                simbolo = Simbolo(entorno.getNombre(), self.identificador, value, "string", "Variable", apuntastack, self.fila, self.columna)
                traductor.addSimbolo(simbolo)
                entorno.addSimbolo(simbolo)
                return
        else:
            valor = self.expresion.traducir(traductor, entorno)
            self.Asignar(traductor.getTipo(valor), valor, self.identificador, entorno, traductor)
            return 

    def Asignar(self, tipo, valor, id, entorno, traductor):
        if tipo == TipoObjeto.ENTERO or tipo == "int":
            apuntador = traductor.putIntStack(valor)
            simbolo = Simbolo(entorno.getNombre(), id, valor, "int", "Variable", apuntador, self.fila, self.columna)
            entorno.addSimbolo(simbolo)
            traductor.addSimbolo(simbolo)
        if tipo == TipoObjeto.CADENA or tipo == "string":
            apuntadorheap = traductor.putStringHeap(valor)
            #Tengo que guardar el apuntador del heap en el stack
            cadena = ""
            cadena += "t"+str(traductor.getContador())+" = "+str(apuntadorheap) + ";//Guardo en un temporal el integer del heap\n"
            cadena += "stack[int(S)] = t"+str(traductor.getContador())+";//Guardo en el stack el puntero del heap\n"
            cadena += "S = S + 1 //Se aumenta el stack para poder meter otro numero\n\n"
            traductor.addCodigo(cadena)
            apuntastack = traductor.getStack()
            traductor.IncrementarStack()#Incrementamos el stack para que agarre el nuevo
            traductor.IncrementarContador()
            simbolo = Simbolo(entorno.getNombre(), id, valor, "string", "Variable", apuntastack, self.fila, self.columna)
            traductor.addSimbolo(simbolo)
            entorno.addSimbolo(simbolo)
        if tipo == TipoObjeto.DECIMAL or tipo == "doble":
            apuntador = traductor.putDoubleStack(valor)
            simbolo = Simbolo(entorno.getNombre(), id, valor, "doble", "Variable", apuntador, self.fila, self.columna)
            entorno.addSimbolo(simbolo)
            traductor.addSimbolo(simbolo)
        if tipo == TipoObjeto.BOOLEANO or tipo == "bool":
            apuntador = traductor.putBooleanStack(valor)
            simbolo = Simbolo(entorno.getNombre(), id, valor, "bool", "Variable", apuntador, self.fila, self.columna)
            entorno.addSimbolo(simbolo)
            traductor.addSimbolo(simbolo)
            return
        return