from Abstract.Objeto import TipoObjeto
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
        return "Asignacion"