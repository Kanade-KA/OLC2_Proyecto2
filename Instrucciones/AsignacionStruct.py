from Abstract.NodoAST import NodoAST
from TablaSimbolo.Simbolo import Simbolo
class AsignacionStruct(NodoAST):
    def __init__(self, identificador, expresion, tipo, fila, columna):
        self.identificador = identificador
        self.expresion = expresion
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, table):
        valor = self.expresion
        simbolo = Simbolo(self.identificador, valor, self.tipo, self.fila, self.columna)
        table.addSimbolo(simbolo)
        return