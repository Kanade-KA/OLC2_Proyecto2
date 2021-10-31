from Abstract.NodoAST import NodoAST
from Expresiones.Identificador import Identificador


class Return(NodoAST):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        retorna = self.expresion.interpretar(arbol, entorno)
        return retorna

    def traducir(self, traductor, entorno):
        retorno = self.expresion.traducir(traductor, entorno)
        if isinstance(self.expresion, Identificador):
            parametro = False
            busqueda = entorno.retornarSimbolo(self.expresion.getIdentificador())
            if busqueda != None:
                if busqueda.getRol() == "Parametro":
                    parametro = True
                tipo = self.expresion.getTipo(traductor, entorno)
                resultado = ""
                if tipo != "error":
                    resultado = traductor.ExtraerVariable(retorno, parametro)
                    retorno=[resultado, tipo]
                else:
                    return "error"
            else:
                #traductor.addExcepcion(Error("Semantico", "No existe la variable", self.fila, self.columna))
                return "error"
        traductor.addCodigo("stack[int(S)] = "+str(retorno[0])+";\n")
        traductor.setReturn(retorno)
        return 