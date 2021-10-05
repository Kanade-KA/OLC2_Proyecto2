from Expresiones.Struct import Struct
from Expresiones.Arreglo import Arreglo
from Expresiones.Identificador import Identificador
from TablaSimbolo.Error import Error

from Abstract.NodoAST import NodoAST

class LlamaStruct(NodoAST):
    def __init__(self, identificador, atributo, fila, columna):
        self.identificador = identificador
        self.atributo = atributo
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, table):
        iden = self.identificador.getIdentificador()
        atr = self.atributo.getIdentificador()
        simbolo = table.retornarSimbolo(iden)
        struct = simbolo.getValor()
        if isinstance(struct, Struct):
            dato = struct.getSimbolo(atr)
            atrib = dato.getValor()
            return atrib.interpretar(arbol, table)
        else:
            arbol.addExcepcion(Error("Semantico", "No es de tipo struct", self.fila, self.columna))
        return