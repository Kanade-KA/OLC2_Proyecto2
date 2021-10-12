from Expresiones.Arreglo import Arreglo
from TablaSimbolo.Simbolo import Simbolo
from Abstract.NodoAST import NodoAST

class Identificador(NodoAST):
    def __init__(self, identificador, fila, columna):
        self.identificador = identificador
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        simbolo = entorno.retornarSimbolo(self.identificador.lower())
        if simbolo == None:
            return "No existe la variable"
        else:
            return simbolo.getValor()

    def getIdentificador(self):
        return self.identificador

    def traducir(self, arbol, TS):
        return "Identificador"