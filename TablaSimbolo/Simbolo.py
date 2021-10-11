class Simbolo:
    def __init__(self, entorno, identificador, valor, tipo, posicion, fila, columna ):
        self.id = identificador
        self.ent = entorno
        self.valor = valor  ## instancia de clase OBJETO
        self.tipo = tipo
        self.fila = fila
        self.columna = columna
        self.posicion = posicion 

    def getID(self):
        return self.id

    def setID(self, id):
        self.id = id

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo  

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor

    def getFila(self):
        return self.fila
    
    def getColumna(self):
        return self.columna

    def getPosicion(self):
        return self.posicion
    
    def getEntorno(self):
        return self.ent
