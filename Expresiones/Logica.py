from Abstract.NodoAST import NodoAST
from Abstract.Objeto import TipoObjeto
from TablaSimbolo.Tipo import OperadorLogico, TipoFor
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
            if self.esBooleano(opi) == 2:
                traductor.addCodigo(str(opi[0])+":\n")
                traductor.CambiarEtiqueta(opi[1], 1)
                opd = self.OperacionDer.traducir(traductor, entorno)
                return [opd[0], opd[1]]
            elif self.esBooleano(opi) == 1:
                acepta ="L"+ str(traductor.getGotos())
                traductor.addCodigo("goto "+ acepta +";\n")
                traductor.addCodigo(acepta+":\n")
                traductor.IncrementarGotos(1)
                opd = self.OperacionDer.traducir(traductor, entorno)
                return [opd[0], opd[1]]
            else:
                acepta = "L"+str(traductor.getGotos())
                traductor.addCodigo("goto "+acepta+";\n")
                traductor.IncrementarGotos(2)
                traductor.CambiarEtiqueta(acepta, 1)
                opd = self.OperacionDer.traducir(traductor, entorno)
                return[opd[0], opd[1]]

        if self.operador == OperadorLogico.OR:
            if self.esBooleano(opi) == 2:
                traductor.addCodigo(str(opi[1])+":\n")
                traductor.CambiarEtiqueta(opi[0], 2)
                opd = self.OperacionDer.traducir(traductor, entorno)
                return [opd[0], opd[1]]
            elif self.esBooleano(opi) == 1 or self.esBooleano(opi) == 0:
                opd = self.OperacionDer.traducir(traductor, entorno)
                return [opd[0], opd[1]]
        if self.operador == OperadorLogico.NOT:
            if self.esBooleano(opi) ==2:
                return [opi[0], opi[1]]
            if self.esBooleano(opi)==1:
                acepta = "L"+str(traductor.getGotos())
                rechaza= "L"+str(traductor.getGotos()+1)
                traductor.addCodigo("goto "+ rechaza+";\n")
                traductor.addCodigo("goto "+ acepta+";\n")
                traductor.IncrementarGotos(2)
                return[acepta, rechaza]
            else:
                acepta = "L"+str(traductor.getGotos())
                rechaza= "L"+str(traductor.getGotos()+1)
                traductor.addCodigo("goto "+ acepta +";\n")
                traductor.addCodigo("goto "+ rechaza+";\n")
                traductor.IncrementarGotos(2)
                return[acepta, rechaza]
        return "error"

    def esBooleano(self, op):
        if op[1] == TipoObjeto.BOOLEANO:
            if op[0]:
                return 1
            return 0
        return 2