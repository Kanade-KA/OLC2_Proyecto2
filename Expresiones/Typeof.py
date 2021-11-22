from Instrucciones.LlamaMatriz2D import LlamaMatriz2D
from Expresiones.Arreglo2D import Arreglo2D
from TablaSimbolo.Error import Error
from Expresiones.Arreglo import Arreglo
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Tipo import OperadorNativo
from Expresiones.Constante import Constante
from Instrucciones.LlamaMatriz import LlamaMatriz
import math

class Typeof(NodoAST):
    def __init__(self, operando, fila, columna):
        self.operando=operando
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        op = self.operando.interpretar(arbol, entorno)
        if isinstance(op, int):
            return "Int64"
        if isinstance(op, float):
            return "Float64"
        if isinstance(op, str):
            return "String"
        if isinstance(op, bool):
            return "Booleano"

    def graficar(self, nodo):
        nodo += "Asingacion\n"
        return

    def traducir(self, traductor, entorno):
        return "typeof"