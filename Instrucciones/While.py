from Instrucciones.Return import Return
from Instrucciones.Continue import Continue
from Instrucciones.Break import Break
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Error import Error
from TablaSimbolo.TS import TablaSimbolos

class While(NodoAST):
    def __init__(self, condicion, instrucciones, fila, columna):
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, table):
        continuar = True
        while continuar:
            condicion = self.condicion.interpretar(arbol, table)#este se va a ctualizar
            if condicion == True:
                nuevaTabla = TablaSimbolos(table)
                for instruccion in self.instrucciones:
                    y = instruccion.interpretar(arbol, nuevaTabla)
                    if isinstance(instruccion, Return):
                        arbol.addExcepcion(Error("Semántico", "No se puede usar el Return con un Loop", self.fila, self.columna))
                    if isinstance(y, Break):
                        continuar = False
                        return None
                    if isinstance(y, Continue):
                        break
            else:
                break
        return None