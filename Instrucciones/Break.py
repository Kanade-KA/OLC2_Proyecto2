from Abstract.NodoAST import NodoAST

class Break(NodoAST):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        return self

    def graficar(self, nodo):
        padre = nodo.getContador()
        nodo.newLabel("BREAK")
        nodo.IncrementarContador()
        return padre
    
    def traducir(self, traductor, entorno):
        return "isbreak"