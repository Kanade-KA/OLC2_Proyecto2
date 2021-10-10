from Instrucciones.LlamaMatriz2D import LlamaMatriz2D
from Expresiones.Arreglo2D import Arreglo2D
from TablaSimbolo.Error import Error
from Expresiones.Arreglo import Arreglo
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Tipo import OperadorNativo
from Expresiones.Constante import Constante
from Instrucciones.LlamaMatriz import LlamaMatriz
import math

class Length(NodoAST):
    def __init__(self, matriz, fila, columna):
        self.operando=matriz
        self.fila = fila
        self.columna = columna


    def interpretar(self, arbol, table):
        if isinstance(self.operando, LlamaMatriz):
            #Si entra aca es por que puede que sea una matriz que no sea de una dimension
            Matriz = self.operando
            iden = Matriz.identificador
            pos = Matriz.expresion.interpretar(arbol, table)
            simbolo = table.retornarSimbolo(iden)
            valorsimbolo = simbolo.getValor()
            if isinstance(valorsimbolo, Arreglo2D):
                sublista = valorsimbolo.getDatos()
                return int(len(sublista[pos -1]))
            else:
                arbol.addExcepcion(Error("SEMANTICO", "Error, no es de tipo matriz", self.fila, self.columna))
            return
        else:
            iden = self.operando.getIdentificador()
            simbolo = table.retornarSimbolo(iden)
            array = simbolo.getValor()
            if isinstance(array, Arreglo):
                datos = array.getDatos()
                return int(len(datos))
            if isinstance(array, Arreglo2D):
                datos = array.getDatos()
                return int(len(datos))
            else:
                arbol.addExcepcion(Error("SEMANTICO", "Error, no es de tipo matriz", self.fila, self.columna))
                return "nothing"

