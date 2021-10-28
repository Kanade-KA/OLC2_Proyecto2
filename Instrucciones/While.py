from Instrucciones.Return import Return
from Instrucciones.Continue import Continue
from Instrucciones.Break import Break
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Error import Error
from TablaSimbolo.Entorno import Entorno

class While(NodoAST):
    def __init__(self, condicion, instrucciones, fila, columna):
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        continuar = True
        while continuar:
            condicion = self.condicion.interpretar(arbol, entorno)#este se va a ctualizar
            if condicion == True:
                nuevaTabla = Entorno("WHILE", entorno)
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

    def traducir(self, traductor, entorno):
        traductor.addCodigo("//******************WHILE************************\n")
        inicio="L"+str(traductor.getGotos())
        traductor.IncrementarGotos(1)
        traductor.addCodigo(inicio+":\n")
        op = self.condicion.traducir(traductor, entorno)
        traductor.addCodigo(op[0]+":\n")
        for i in self.instrucciones:#TENGO QUE CAMBIAR ENTORNO OJO
            i.traducir(traductor, entorno)
        traductor.addCodigo("goto "+inicio+";\n")
        traductor.addCodigo(op[1]+":\n")
        return