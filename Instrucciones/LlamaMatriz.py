from Expresiones.Arreglo import Arreglo
from Expresiones.Identificador import Identificador
from TablaSimbolo.Error import Error

from Abstract.NodoAST import NodoAST

class LlamaMatriz(NodoAST):
    def __init__(self, identificador, expresion, fila, columna):
        self.identificador = identificador
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        posicion = self.expresion.interpretar(arbol, entorno)
        x = entorno.retornarSimbolo(self.identificador.lower())
        simbolo = x.getValor()
        if isinstance(simbolo, Arreglo):
            arreglo = simbolo.getDatos()
            if posicion > len(arreglo):
                arbol.addExcepcion(Error("Semantico", "Error el indice pasa los limites de la matriz", self.fila, self.columna))
            else:
                elemento = arreglo[posicion-1]
                resultado = elemento.interpretar(arbol, entorno)
                return resultado
        else:
            arbol.addExcepcion(Error("Semantico", "La variable no es de tipo arreglo", self.fila, self.columna))
        return
    
    def traducir(self, traductor, entorno):
        return "Llamada a matriz"