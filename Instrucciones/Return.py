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

    def graficar(self, nodo):
        padre = nodo.getContador()
        nodo.newLabel("RETURN")
        nodo.IncrementarContador()

        return padre
    
    def traducir(self, traductor, entorno):
        retorno = self.expresion.traducir(traductor, entorno)
        #VER SI ES ID...
        idinicio = traductor.EsIdentificador(self.expresion, retorno, entorno, self.fila, self.columna)
        if idinicio[0]:
            retorno = [idinicio[1], idinicio[2]]
        traductor.addCodigo("stack[int(S)] = "+str(retorno[0])+";\n")
        traductor.setReturn(retorno)
        return 