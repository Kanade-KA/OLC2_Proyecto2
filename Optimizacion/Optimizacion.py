class Optimizacion():
    def __init__(self, tipo, regla, descripcion, original, optimizada, fila):
        self.tipo = tipo
        self.regla = regla
        self.descripcion = descripcion
        self.original = original
        self.optimizada = optimizada
        self.fila = fila

    
    def getTipo(self):
        return self.tipo

    def getRegla(self):
        return self.regla

    def getOriginal(self):
        return self.original

    def getOptimizado(self):
        return self.optimizada

    def  getDescripcion(self):
        return self.descripcion

    def getFila(self):
        return str(self.fila)