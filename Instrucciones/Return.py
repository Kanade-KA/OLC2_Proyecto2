from Abstract.NodoAST import NodoAST


class Return(NodoAST):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        retorna = self.expresion.interpretar(arbol, entorno)
        return retorna