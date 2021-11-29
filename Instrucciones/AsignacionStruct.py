from Abstract.NodoAST import NodoAST
from TablaSimbolo.Simbolo import Simbolo
class AsignacionStruct(NodoAST):
    def __init__(self, identificador, expresion, tipo, fila, columna):
        self.identificador = identificador
        self.expresion = expresion
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        valor = self.expresion
        simbolo = Simbolo(entorno.getNombre(), self.identificador, valor, "" , self.tipo, 0, self.fila, self.columna)
        arbol.addSimbolo(simbolo)
        entorno.addSimbolo(simbolo)
        return

    def graficar(self, nodo):
        padre = nodo.getContador()
        nodo.newLabel("ASIGNACION STRUCT")
        nodo.IncrementarContador()

        atributo = nodo.getContador()
        nodo.newLabel(self.identificador)
        nodo.IncrementarContador()
        nodo.newEdge(padre, atributo)

        structt = self.expresion
        atributo = nodo.getContador()
        nodo.newLabel(str(structt.getMutable()))
        nodo.IncrementarContador()
        nodo.newEdge(padre, atributo)
        
        for ins in structt.getDatos():
            if type(ins) is str:
                atributo = nodo.getContador()
                nodo.newLabel(ins)
                nodo.IncrementarContador()
                nodo.newEdge(padre, atributo)
            else:
                atributo = ins.graficar(nodo)
                nodo.newEdge(padre, atributo)

        return padre
    
    def traducir(self, traductor, entorno):
        return "Asignacion Struct"