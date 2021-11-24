from Abstract.NodoAST import NodoAST

class Typeof(NodoAST):
    def __init__(self, operando, fila, columna):
        self.operando=operando
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        op = self.operando.interpretar(arbol, entorno)
        if isinstance(op, int):
            return "Int64"
        if isinstance(op, float):
            return "Float64"
        if isinstance(op, str):
            return "String"
        if isinstance(op, bool):
            return "Booleano"

    def graficar(self, nodo):
        padre = nodo.getContador()
        nodo.newLabel("TYPE OF")
        nodo.IncrementarContador()

        hijo = self.operando.graficar(nodo)
        nodo.newEdge(padre, hijo)
        return padre

    def traducir(self, traductor, entorno):
        return "typeof"