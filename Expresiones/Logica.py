from Abstract.NodoAST import NodoAST
from TablaSimbolo.Tipo import OperadorLogico
from Expresiones.Constante import Constante

class Logica(NodoAST):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        self.operador = operador
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperacionDer
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        opi = self.OperacionIzq.interpretar(arbol, entorno)
        if self.operador == OperadorLogico.AND:
            opd = self.OperacionDer.interpretar(arbol, entorno)
            if opi == True and opd == True:
                return True
            else:
                return False
        if self.operador == OperadorLogico.OR:
            opd = self.OperacionDer.interpretar(arbol, entorno)
            if opi == True or opd == True:
                return True
            else:
                return False
        if self.operador == OperadorLogico.NOT:
            if not opi == True:
                return True
            else:
                return False       
        return
