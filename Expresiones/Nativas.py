from Instrucciones.LlamaMatriz2D import LlamaMatriz2D
from Expresiones.Arreglo2D import Arreglo2D
from TablaSimbolo.Error import Error
from Expresiones.Arreglo import Arreglo
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Tipo import OperadorNativo
from Expresiones.Constante import Constante
from Instrucciones.LlamaMatriz import LlamaMatriz
import math

class Nativas(NodoAST):
    def __init__(self, operador, operando, base, fila, columna):
        self.operador = operador
        self.operando=operando
        self.base = base
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, table):
        op = self.operando.interpretar(arbol, table)
        if self.operador == OperadorNativo.LOGARITMO:
            base = self.base.interpretar(arbol, table)
            if isinstance(op, int) or isinstance(op, float):
                if isinstance(base, int) or isinstance(base, float):
                    return float(math.log(op, base))
        if self.operador == OperadorNativo.LOWERCASE:
            if isinstance(op, str):
                return str.lower(op)
        if self.operador == OperadorNativo.UPPERCASE:
            if isinstance(op, str):
                return str.upper(op)
        if self.operador == OperadorNativo.SENO:
            if isinstance(op, float) or isinstance(op, int):
                return float(math.sin(op))
        if self.operador == OperadorNativo.COSENO:
            if isinstance(op, float) or isinstance(op, int):
                return float(math.cos(op))
        if self.operador == OperadorNativo.TANGENTE:
            if isinstance(op, float) or isinstance(op, int):
                return float(math.tan(op))
        if self.operador == OperadorNativo.CUADRADA:
            if isinstance(op, float) or isinstance(op, int):
                return float(math.sqrt(op))
        if self.operador == OperadorNativo.TRUNC:
            return int(float(op))
        if self.operador == OperadorNativo.FLOAT:
            return float(int(op))
        if self.operador == OperadorNativo.STRING:
            return str(op)
        return
