from Abstract.NodoAST import NodoAST
from TablaSimbolo.Simbolo import Simbolo
class AsignacionStruct(NodoAST):
    def __init__(self, identificador, expresion, tipo, fila, columna):
        self.identificador = identificador
        self.expresion = expresion
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        valor = self.expresion
        simbolo = Simbolo(entorno.getNombre(), self.identificador, valor, "" , self.tipo, 0, self.fila, self.columna)
        arbol.addSimbolo(simbolo)
        entorno.addSimbolo(simbolo)
        return

    def graficar(self, graf, nodo):
        graf += "Asingacion\n"
        return
    
    def traducir(self, traductor, entorno):
        return "Asignacion Struct"