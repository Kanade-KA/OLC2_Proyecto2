from TablaSimbolo.Simbolo import Simbolo
from TablaSimbolo.Error import Error
from Expresiones.Constante import Constante
from Objeto.Primitivo import Primitivo
from Abstract.Objeto import TipoObjeto
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Tipo import OperadorAritmetico
from Expresiones.Constante import Constante

class Aritmetica(NodoAST):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        self.operador = operador
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperacionDer
        self.fila = fila
        self.columna = columna


    def interpretar(self, arbol, table):
        opi = self.OperacionIzq.interpretar(arbol, table)
        opd = self.OperacionDer.interpretar(arbol, table)
        if opi != None and opd != None:
            if (self.operador==OperadorAritmetico.MAS):
                if  isinstance(opi, float) or isinstance(opd, float) :
                    return  float(opi + opd)
                else:
                    return int(opi + opd)
            if (self.operador==OperadorAritmetico.MENOS):
                if isinstance(opi, float) or isinstance(opd, float):
                    return  float(opi - opd)
                else:
                    return  int(opi - opd)
            if (self.operador == OperadorAritmetico.POR):
                if isinstance(opi, str) and isinstance(opd, str):
                    return str(opi + opd)
                if isinstance(opi, float) or isinstance(opd, float):
                    return  float(opi * opd)
                else:
                    return int(opi * opd)
            if (self.operador == OperadorAritmetico.DIV):
                    return  float(opi / opd)
            if (self.operador == OperadorAritmetico.POW):
                if isinstance(opi, str) and isinstance(opd, int):
                    palabra=""
                    for x in range (opd):
                        palabra+=opi
                    return str(palabra)
                if isinstance(opi, float) or isinstance(opd, float):
                    return  float(pow(opi,opd))
                else:
                    return int(pow(opi,opd))
            if (self.operador == OperadorAritmetico.MOD):
                if opd != 0:
                    if isinstance(opi, float) or isinstance(opd, float):
                        return  float(opi % opd)
                    else:
                        return int(opi % opd)
            return arbol.addExcepcion(Error("Semantico", "Los tipos no coinciden", self.fila, self.columna))
        arbol.addExcepcion(Error("Semantico", "Operador Nulo", self.fila, self.columna))
        return
