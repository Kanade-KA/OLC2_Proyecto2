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

    def interpretar(self, arbol, entorno):
        iden = self.identificador.getIdentificador()
        atr = self.atributo.getIdentificador()
        simbolo = entorno.retornarSimbolo(iden)
        struct = simbolo.getValor()
        if isinstance(struct, Struct):
            dato = struct.getSimbolo(atr)
            atrib = dato.getValor()
            return atrib.interpretar(arbol, entorno)
        else:
            arbol.addExcepcion(Error("Semantico", "No es de tipo struct", self.fila, self.columna))
        return

    def graficar(self, nodo):
        padre = nodo.getContador()
        nodo.newLabel("LLAMADA STRUCT")
        nodo.IncrementarContador()

        hijo = nodo.getContador()
        nodo.newLabel(self.identificador)
        nodo.IncrementarContador()
        nodo.newEdge(padre, hijo)

        hijo = nodo.getContador()
        nodo.newLabel(".")
        nodo.IncrementarContador()
        nodo.newEdge(padre, hijo)

        hijo = nodo.getContador()
        nodo.newLabel(self.atributo)
        nodo.IncrementarContador()
        nodo.newEdge(padre, hijo)

        return padre
    
    def traducir(self, traductor, entorno):
        return "Llamada a Struct"