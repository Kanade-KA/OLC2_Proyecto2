from Expresiones.Constante import Constante
from Expresiones.Aritmetica import Aritmetica


class Arreglo:
    def __init__(self, id, datos):
        self.id = id
        self.datos = datos

    def getDatos(self):
        return self.datos

    def retornarArray(self, arbol, tabla):
        contador = 0
        x = "["
        for i in self.datos:
            x += str(i.interpretar(arbol, tabla))
            if contador + 1 < len(self.datos):
                x+=","
            contador = contador + 1
        x += "]"
        return x

    def setearDato(self, posicion, dato):
        self.datos[posicion] = dato
        return

    def PushDato(self, dato):
        self.datos.append(dato)
        return

    def PopDato(self):
        return self.datos.pop()