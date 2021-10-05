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
        if self.operador != OperadorNativo.PARSE and self.operador != OperadorNativo.PUSH and self.operador != OperadorNativo.POP and self.operador != OperadorNativo.LENGTH:
            op = self.operando.interpretar(arbol, table)
        
        if self.operador == OperadorNativo.LOGARITMOD:
            if isinstance(op, int) or isinstance(op, float):
                    return float(math.log(10, op))
        if self.operador == OperadorNativo.LOGARITMOB:
            base = self.base.interpretar(arbol, table)
            if isinstance(op, int) or isinstance(op, float):
                if isinstance(base, int) or isinstance(base, float):
                    return float(math.log(base, op))
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
        if self.operador == OperadorNativo.PARSE:
            tipo = self.operando.lower()
            if tipo == "int64":
                x = self.base.interpretar(arbol, table)
                return int(float(x))
            if tipo == "float64":
                x = self.base.interpretar(arbol, table)
                return float(str(x))
        if self.operador == OperadorNativo.TRUNC:
            return int(float(self.operando.interpretar(arbol, table)))
        if self.operador == OperadorNativo.FLOAT:
            return float(int(self.operando.interpretar(arbol, table)))
        if self.operador == OperadorNativo.STRING:
            return str(self.operando.interpretar(arbol, table))
        if self.operador == OperadorNativo.TYPEOF:
            op = self.operando.interpretar(arbol, table)
            if isinstance(op, int):
                return "Int64"
            if isinstance(op, float):
                return "Float64"
            if isinstance(op, str):
                return "String"
            if isinstance(op, bool):
                return "Booleano"
        if self.operador == OperadorNativo.LENGTH:
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
        if self.operador == OperadorNativo.POP:
            simbolo = table.retornarSimbolo(self.operando)
            arreglo = simbolo.getValor()
            if isinstance(arreglo, Arreglo):
                elemento = arreglo.PopDato()
                return elemento.interpretar(arbol, table)
            else:
                arbol.addExcepcion(Error("SEMANTICO", "Error, no es de tipo matriz", self.fila, self.columna))
            
        return
