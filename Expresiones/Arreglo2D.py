from Expresiones.Constante import Constante
from Expresiones.Aritmetica import Aritmetica

class Arreglo2D:
    def __init__(self, id, datos):
        self.id = id
        self.datos = datos

    def getDatos(self):
        return self.datos

    def retornarArray(self, arbol, tabla):
        x = "["
        contador = 0
        for i in self.datos:
            x+="["
            cont = 0
            for j in i:
                x += str(j.interpretar(arbol, tabla))
                if cont + 1 < len(i):
                    x+=","
                cont = cont + 1
            x+= "]"
            if contador + 1 < len(self.datos):
                x+=","
            contador = contador + 1
        x += "]"
        return x

    def setearDato(self, posicion, subposicion, dato):
        sublista = self.datos[posicion]
        sublista[subposicion] = dato
        return
    
    def PushearDato(self, dato):
        self.datos.append(dato)
        return
        