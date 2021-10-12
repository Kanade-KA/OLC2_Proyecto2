from Expresiones.Constante import Constante
from Objeto.Primitivo import Primitivo
from Abstract.Objeto import TipoObjeto
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Tipo import OperadorRelacional
from Expresiones.Constante import Constante

class Relacional(NodoAST):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        self.operador = operador
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperacionDer
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        opi = self.OperacionIzq.interpretar(arbol, entorno)
        opd = self.OperacionDer.interpretar(arbol, entorno)
        if self.operador == OperadorRelacional.MAYORQUE:
            if opi > opd:
                return True
            else:
                return False
        if self.operador == OperadorRelacional.MENORQUE:
            if opi < opd:
                return True
            else:
                return False
        if self.operador == OperadorRelacional.MAYORIGUAL:
            if opi >= opd:
                return True
            else:
                return False
        if self.operador == OperadorRelacional.MENORIGUAL:
            if opi <= opd:
                return True
            else:
                return False
        if self.operador == OperadorRelacional.IGUALIGUAL:
            if opi == opd:
                return True
            else:
                return False
        if self.operador == OperadorRelacional.DIFERENTE:
            if opi != opd:
                return True
            else:
                return False
        return "Error de tipos"

    def traducir(self, traductor, entorno):
        return "relacional"
        