class Arbol:
    def __init__(self):
        self.excepciones = []
        self.consola = ""
        self.grafica = ""

    def getExcepciones(self):
        return self.excepciones

    def addExcepcion(self, excepciones):
        self.excepciones.append(excepciones)

    def getConsola(self):
        return self.consola

    def AgregaraConsola(self,cadena):
        self.consola += str(cadena)

    def AgregarGrafica(self, grafo):
        self.grafica += str(grafo) + "\n"

    def getGrafica(self):
        self.grafica