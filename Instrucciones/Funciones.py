from Instrucciones.Continue import Continue
from Instrucciones.Return import Return
from Expresiones.Identificador import Identificador
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Error import Error
from TablaSimbolo.TS import TablaSimbolos
from Instrucciones.Break import Break
from TablaSimbolo.Simbolo import Simbolo

class Funcion(NodoAST):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
    
    def interpretar(self, arbol, table):
        y = None
        for instruccion in self.instrucciones:
            y = instruccion.interpretar(arbol, table) 
            if y != None:
                return y         

            if isinstance(instruccion, Break):
                arbol.addExcepcion(Error("Semántico", "No se puede usar el Break en una funcion", self.fila, self.columna))
            if isinstance(instruccion, Continue):
                arbol.addExcepcion(Error("Semántico", "No se puede usar el Continue en una funcion", self.fila, self.columna))
        return y


    def getParametros(self):
        return self.parametros