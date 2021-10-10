from Expresiones.Struct import Struct
from Expresiones.Constante import Constante
from Expresiones.Identificador import Identificador
from TablaSimbolo.Simbolo import Simbolo
from Expresiones.Arreglo import Arreglo
from TablaSimbolo.Error import Error

from Abstract.NodoAST import NodoAST

class AsignaObjeto(NodoAST):
    def __init__(self, identificador, atributo, expresion, fila, columna):
        self.identificador = identificador
        self.atributo = atributo
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, table):
        simbolo1 = table.retornarSimbolo(self.identificador)
        struct = simbolo1.getValor()
        if isinstance(struct, Struct):
            x = struct.setSimbolo(self.atributo, self.expresion, arbol, table)
        else:
            arbol.addExcepcion(Error("Semantico", "No es de tipo struct", self.fila, self.columna))
        return