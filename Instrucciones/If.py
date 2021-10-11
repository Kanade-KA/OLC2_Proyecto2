from Instrucciones.Return import Return
from Instrucciones.Continue import Continue
from TablaSimbolo.Entorno import Entorno
from TablaSimbolo.Error import Error
from Abstract.NodoAST import NodoAST
from Instrucciones.Break import Break
class If(NodoAST):
    def __init__(self, condicion, instruccionesIf, instruccionesElse, ElseIf, fila, columna):
        self.condicion = condicion
        self.instruccionesIf = instruccionesIf
        self.instruccionesElse = instruccionesElse
        self.elseIf = ElseIf
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        x = ""
        condicional = self.condicion.interpretar(arbol, entorno)
        if condicional == True:
            if self.instruccionesIf != None:
                nuevoentorno = Entorno("IF", entorno)
                for instruccion in self.instruccionesIf:
                    if isinstance(instruccion, Break):
                        return instruccion
                    if isinstance(instruccion, Continue):
                        return instruccion
                    if isinstance(instruccion, Return):
                        return instruccion.interpretar(arbol, nuevoentorno)
                    else:
                        instruccion.interpretar(arbol, nuevoentorno)
            return None
        else:
            if not self.instruccionesElse == None:
                nuevoentorno2 = Entorno("ELSE", entorno)
                for instruccion in self.instruccionesElse:
                    if isinstance(instruccion, Break):
                        return instruccion
                    if isinstance(instruccion, Continue):
                        return instruccion
                    if isinstance(instruccion, Return):
                        return instruccion.interpretar(arbol, nuevoentorno2)
                    else:
                        instruccion.interpretar(arbol, nuevoentorno2)
        if self.elseIf != None:
                return self.elseIf.interpretar(arbol, entorno)
        
        return None
