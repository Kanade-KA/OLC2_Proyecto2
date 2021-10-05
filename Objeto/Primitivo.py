from Abstract.Objeto import Objeto
from abc import ABC, abstractmethod

class Primitivo(Objeto):
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor=valor

    def toString(self):
        return str(self.valor)

    def toInt(self):
        return int(self.valor)

    def toDouble(self):
        return float(self.valor)

    def toBoolean(self):
        if self.valor == "true":
            return True
        else:
            return False