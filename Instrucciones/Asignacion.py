from Instrucciones.LlamaMatriz import LlamaMatriz
from Instrucciones.Return import Return
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Simbolo import Simbolo
from TablaSimbolo.Error import Error
from Instrucciones.Retonar import Retornar
class Asignacion(NodoAST):
    def __init__(self, identificador, expresion, tipo, fila, columna):
        self.identificador = identificador
        self.expresion = expresion
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, table):
        value = None
        if self.tipo == "clase":
            valor = self.expresion
            simbolo = Simbolo(self.identificador, valor, self.tipo, self.fila, self.columna)
            table.addSimbolo(simbolo)
            return
        if self.tipo != "funcion" and self.tipo != "any" and self.tipo != "arreglo" and self.tipo != "2d" and self.tipo != "3d":
            if not self.expresion == None:
                value = self.expresion.interpretar(arbol, table)
            if self.tipo.lower() == "int64": #Es por que tiene un tipo (se declaró con tipo)
                if not isinstance(value, int):
                    arbol.addExcepcion(Error("Semántico","La variable "+self.identificador+", no es de tipo int", self.fila, self.columna))
                    return
            if self.tipo.lower() == "float64":
                if not isinstance(value, float):
                    arbol.addExcepcion(Error("Semántico","La variable "+self.identificador+", no es de tipo float", self.fila, self.columna))
                    return
            if self.tipo.lower() == "string":
                if not isinstance(value, str):
                    arbol.addExcepcion(Error("Semántico","La variable "+self.identificador+", no es de tipo string", self.fila, self.columna))
                    return
            if self.tipo.lower() == "global":
                simbolo = Simbolo(self.identificador, value,  self.tipo, self.fila, self.columna)
                table.AgregarGlobal(simbolo)
                return
            valor = self.expresion.interpretar(arbol, table)
            simbolo = Simbolo(self.identificador, valor, "id", self.fila, self.columna)
            table.addSimbolo(simbolo)
            return
        if self.tipo == "any":
            if isinstance(self.expresion, Retornar):
                x = self.expresion.interpretar(arbol, table)
                simbolo = Simbolo(self.identificador, x, "id", self.fila, self.columna)
                table.addSimbolo(simbolo)
                return
            else:#AQUÍ ENTRA SI NO LE PONEMOS TIPO A LA ASIGNACION
                value = self.expresion.interpretar(arbol, table)
                simbolo = Simbolo(self.identificador, value, self.tipo, self.fila, self.columna)
                table.addSimbolo(simbolo)
                return
        if self.tipo == "arreglo":
            simbolo = Simbolo(self.identificador, self.expresion, self.tipo, self.fila, self.columna)
            table.addSimbolo(simbolo)
            return
        if self.tipo == "2d":
            simbolo = Simbolo(self.identificador, self.expresion, self.tipo, self.fila, self.columna)
            table.addSimbolo(simbolo)
            return
        if self.tipo == "3d":
            simbolo = Simbolo(self.identificador, self.expresion, self.tipo, self.fila, self.columna)
            table.addSimbolo(simbolo)
        else:
        #ASIGNACION DE UNA FUNCION
            simbolo = Simbolo(self.identificador, self.expresion, self.tipo, self.fila, self.columna)
            table.addSimbolo(simbolo)
        return