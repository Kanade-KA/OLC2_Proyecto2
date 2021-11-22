from Expresiones.Arreglo2D import Arreglo2D
from re import sub
from Expresiones.Arreglo import Arreglo
from Expresiones.Identificador import Identificador
from TablaSimbolo.Error import Error

from Abstract.NodoAST import NodoAST

class LlamaMatriz2D(NodoAST):
    def __init__(self, identificador, expresion, submat, fila, columna):
        self.identificador = identificador
        self.expresion = expresion
        self.subindice = submat
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        posicion = self.expresion.interpretar(arbol, entorno)
        subposicion = self.subindice.interpretar(arbol, entorno)
        x = entorno.retornarSimbolo(self.identificador.lower())
        simbolo = x.getValor()
        if isinstance(simbolo, Arreglo2D):
            arreglo = simbolo.getDatos()
            if posicion > len(arreglo):
                arbol.addExcepcion(Error("Semantico", "Error el indice pasa los limites de la matriz", self.fila, self.columna))
            else:
                subArreglo = arreglo[posicion-1]
                if subposicion > len(subArreglo):
                    arbol.addExcepcion(Error("Semantico", "Error, el índice pasa los límites de la matriz", self.fila, self.columna))
                else:
                    dato = subArreglo[subposicion-1]
                    return dato.interpretar(arbol, entorno)
        else:
            arbol.addExcepcion(Error("Semantico", "La variable no es de tipo arreglo", self.fila, self.columna))
        return

    def graficar(self, graf, nodo):
        graf += "Asingacion\n"
        return
    
    def graficar(self, graf, nodo):
        graf += "Asingacion\n"
        return
    
    def traducir(self, traductor, entorno):
        return "Llamada a matriz 2D"