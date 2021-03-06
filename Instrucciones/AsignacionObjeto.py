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

    def interpretar(self, arbol, entorno):
        simbolo1 = entorno.retornarSimbolo(self.identificador)
        struct = simbolo1.getValor()
        if isinstance(struct, Struct):
            x = struct.setSimbolo(self.atributo, self.expresion, arbol, entorno)
        else:
            arbol.addExcepcion(Error("Semantico", "No es de tipo struct", self.fila, self.columna))
        return
    
    def graficar(self, nodo):
        padre = nodo.getContador()
        nodo.newLabel("ASIGNACION STRUCT")
        nodo.IncrementarContador()

        atributo = nodo.getContador()
        nodo.newLabel(self.identificador)
        nodo.IncrementarContador()
        nodo.newEdge(padre, atributo)

        atributo = nodo.getContador()
        nodo.newLabel(".")
        nodo.IncrementarContador()
        nodo.newEdge(padre, atributo)

        atributo = nodo.getContador()
        nodo.newLabel(self.atributo)
        nodo.IncrementarContador()
        nodo.newEdge(padre, atributo)

        atributo = self.expresion.graficar(nodo)
        nodo.newEdge(padre, atributo)

        return padre

    def traducir(self, traductor, entorno):
        return "Asignacion Objeto"