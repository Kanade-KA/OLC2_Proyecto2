from Expresiones.Arreglo import Arreglo
from TablaSimbolo.Simbolo import Simbolo
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

    def traducir(self, traductor, entorno):
        simbolo = entorno.retornarSimbolo(self.identificador.lower())
        if simbolo == None:
            traductor.addExcepcion(Error("Semántico","La variable "+self.identificador+", no existe.", self.fila, self.columna))
            return 
        else:
            return simbolo.getPosicion()

    def getTipo(self, entorno):
        simbolo = entorno.retornarSimbolo(self.identificador.lower())
        return simbolo.getTipo()