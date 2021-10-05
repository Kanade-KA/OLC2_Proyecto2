from Expresiones.Constante import Constante
from Expresiones.Aritmetica import Aritmetica

class Arreglo3D:
    def __init__(self, id, datos):
        self.id = id
        self.datos = datos

    def getDatos(self):
        return self.datos

    def retornarArray(self, arbol, tabla):
        x = ""
        x += "[ "
        contador1 = 0
        for i in self.datos:
            x+="[ "
            contador2 = 0
            for j in i:
                x += "[ "
                contador3 = 0
                for k in j:
                    x += str(k.interpretar(arbol, tabla))
                    if contador3 + 1 < len(j):
                        x += ", "
                    contador3 = contador3 + 1
                x += " ]"
                if contador2 + 1 < len(i):
                    x += ", "
                contador2 = contador2 + 1
            x += " ]"
            if contador1 + 1 < len(self.datos):
                x += ", "
            contador1 = contador1 + 1
        x += " ]"
        return x

    def setearDato(self, posicion, subposicion, subsub, dato):
        primerarreglo = self.datos[posicion]
        segundoarreglo = primerarreglo[subposicion]
        segundoarreglo[subsub] = dato
        return
    
        