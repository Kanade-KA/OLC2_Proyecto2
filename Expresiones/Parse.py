from Instrucciones.LlamaMatriz2D import LlamaMatriz2D
from Expresiones.Arreglo2D import Arreglo2D
from TablaSimbolo.Error import Error
from Expresiones.Arreglo import Arreglo
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Tipo import OperadorNativo
from Expresiones.Constante import Constante
from Instrucciones.LlamaMatriz import LlamaMatriz
import math

class Parse(NodoAST):
    def __init__(self, tipo, expresion, fila, columna):
        self.operador = tipo
        self.operando=expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, table):
        op = self.operando.interpretar(arbol, table)
        if isinstance(op, int):
            return "Int64"
        if isinstance(op, float):
            return "Float64"
        if isinstance(op, str):
            return "String"
        if isinstance(op, bool):
            return "Booleano"