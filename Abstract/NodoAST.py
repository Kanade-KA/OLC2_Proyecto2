from abc import ABC, abstractmethod

class NodoAST(ABC):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        super().__init__()

    @abstractmethod
    def interpretar(self, arbol, TS):
        pass

    @abstractmethod
    def traducir(self, traductor, entorno):
        pass

    @abstractmethod
    def graficar(self, graf, nodo):
        pass
