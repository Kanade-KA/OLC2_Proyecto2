from Abstract.NodoAST import NodoAST

class Continue(NodoAST):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        return self
    
    def graficar(self, nodo):
        nodo += "Asingacion\n"
        return
    
    def traducir(self, traductor, entorno):
        return "iscontinue"