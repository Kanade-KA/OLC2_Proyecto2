from Abstract.NodoAST import NodoAST
from TablaSimbolo.Simbolo import Simbolo
class AsignacionFuncion(NodoAST):
    def __init__(self, identificador, expresion, tipo, fila, columna):
        self.identificador = identificador
        self.expresion = expresion
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        simbolo = Simbolo(entorno.getNombre(), self.identificador, self.expresion, self.tipo, 0, self.fila, self.columna)
        entorno.addSimbolo(simbolo)
        return