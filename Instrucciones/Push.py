from TablaSimbolo.Error import Error
from Instrucciones.LlamaMatriz2D import LlamaMatriz2D
from Expresiones.Arreglo2D import Arreglo2D
from Expresiones.Arreglo import Arreglo
from Abstract.NodoAST import NodoAST
import math

class Push(NodoAST):
    def __init__(self, id, dato, fila, columna):
        self.identificador = id
        self.dato=dato
        self.fila = fila
        self.columna = columna
    
    def interpretar(self, arbol, entorno):   
        simbolo = entorno.retornarSimbolo(self.identificador)
        arreglo = simbolo.getValor()
        if isinstance(arreglo, Arreglo):
            arreglo.PushDato(self.dato)
            return
        if isinstance(arreglo, Arreglo2D):
            arreglo.PushearDato(self.dato)
            return
        else:
            arbol.addExcepcion(Error("SEMANTICO", "Error, no es de tipo matriz", self.fila, self.columna))
        return

    def graficar(self, nodo):
        padre = nodo.getContador()
        nodo.newLabel("PUSH")
        nodo.IncrementarContador()

        atributo = nodo.getContador()
        nodo.newLabel(self.identificador)
        nodo.IncrementarContador()
        nodo.newEdge(padre, atributo)

        atributo = self.dato.graficar(nodo)
        nodo.newEdge(padre, atributo)

        return padre
    
    def traducir(self, traductor, entorno):
        return "Push"