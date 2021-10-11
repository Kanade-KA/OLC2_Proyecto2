from TablaSimbolo.Error import Error
from Expresiones.Arreglo import Arreglo
from Abstract.NodoAST import NodoAST


class Pop(NodoAST):
    def __init__(self, operando, fila, columna):
        self.operando=operando
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        simbolo = entorno.retornarSimbolo(self.operando)
        arreglo = simbolo.getValor()
        if isinstance(arreglo, Arreglo):
            elemento = arreglo.PopDato()
            return elemento.interpretar(arbol, entorno)
        else:
            arbol.addExcepcion(Error("SEMANTICO", "Error, no es de tipo matriz", self.fila, self.columna)) 
        return
