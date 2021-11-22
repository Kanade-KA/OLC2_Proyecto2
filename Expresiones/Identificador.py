from Abstract.NodoAST import NodoAST
from TablaSimbolo.Error import Error

class Identificador(NodoAST):
    def __init__(self, identificador, fila, columna):
        self.identificador = identificador
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        simbolo = entorno.retornarSimbolo(self.identificador.lower())
        if simbolo == None:
            arbol.addExcepcion(Error("Semántico","La variable "+self.identificador+", no existe.", self.fila, self.columna))
            return 
        else:
            return simbolo.getValor()

    def getIdentificador(self):
        return self.identificador

    def graficar(self, graf, nodo):
        graf += "Asingacion\n"
        return
#-------------------------------------------------------------------------------------------------------------------
    def traducir(self, traductor, entorno):
        simbolo = entorno.retornarSimbolo(self.identificador.lower())
        if simbolo == None:
            traductor.addExcepcion(Error("Semántico","La variable "+self.identificador+", no existe.", self.fila, self.columna))
            return 
        else:
            return simbolo.getPosicion()

    def getTipo(self, traductor, entorno):
        simbolo = entorno.retornarSimbolo(self.identificador.lower())
        if simbolo == None:
            traductor.addExcepcion(Error("Semántico","La variable "+self.identificador+", no existe.", self.fila, self.columna))
            return "error"
        else:
            return simbolo.getTipo()

    def getValor(self, traductor, entorno):
        simbolo = entorno.retornarSimbolo(self.identificador.lower())
        if simbolo == None:
            traductor.addExcepcion(Error("Semántico","La variable "+self.identificador+", no existe.", self.fila, self.columna))
            return "error"
        else:
            return simbolo.getValor()