from Instrucciones.Continue import Continue
from Instrucciones.Return import Return
from Expresiones.Identificador import Identificador
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Error import Error
from Instrucciones.Break import Break

class Funcion(NodoAST):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
    
    def interpretar(self, arbol, entorno):
        y = None
        for instruccion in self.instrucciones:
            y = instruccion.interpretar(arbol, entorno) 
            if y != None:
                return y         
            if isinstance(instruccion, Break):
                arbol.addExcepcion(Error("Semántico", "No se puede usar el Break en una funcion", self.fila, self.columna))
            if isinstance(instruccion, Continue):
                arbol.addExcepcion(Error("Semántico", "No se puede usar el Continue en una funcion", self.fila, self.columna))
        return y

    def getParametros(self):
        return self.parametros

    def traducir(self, traductor, entorno):
        traductor.addCodigo(str(self.nombre) + "();\n")
        return

    def getInstrucciones(self):
        return self.instrucciones

    def getNombre(self):
        return self.nombre