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

    def traducir(self, traductor, entorno):
        opi = self.OperacionIzq.traducir(traductor, entorno)
        if self.operador == OperadorLogico.AND:
            traductor.addCodigo(str(opi[0])+":\n")
            traductor.CambiarEtiqueta(opi[1], 1)
            opd = self.OperacionDer.traducir(traductor, entorno)
            return [opd[0], opd[1]]
        if self.operador == OperadorLogico.OR:
            traductor.addCodigo(str(opi[1])+":\n")
            traductor.CambiarEtiqueta(opi[0], 2)
            opd = self.OperacionDer.traducir(traductor, entorno)
            return [opd[0], opd[1]]
        if self.operador == OperadorLogico.NOT:
            print("and")
        return "error"