from Expresiones.Constante import Constante
from Objeto.Primitivo import Primitivo
from Abstract.Objeto import TipoObjeto
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Tipo import OperadorRelacional
from Expresiones.Constante import Constante
from TablaSimbolo.Traductor import Traductor

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
        opi = self.OperacionIzq.traducir(traductor, entorno)
        opd = self.OperacionDer.traducir(traductor, entorno)
        #print(self.operador)
        if self.operador == OperadorRelacional.MAYORQUE:
            if self.VerificarTipo(traductor, opi, opd):
                cadena = "if "+str(opi)+" >= "+ str(opd)+" { goto L"+str(traductor.getGotos()) + "}\n"
                cadena += "goto L"+str(traductor.getGotos() +1)+"\n"
                traductor.addCodigo(cadena)
            else:
                print("Error")
        '''if self.operador == OperadorRelacional.MENORQUE:
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
                return False'''
        return "relacional"
        
    def VerificarTipo(self, traductor, opi, opd):
        tipoizq = traductor.getTipo(opi)
        tipoder = traductor.getTipo(opd)
        if tipoder == TipoObjeto.DECIMAL or tipoder == TipoObjeto.ENTERO :
            if tipoizq == TipoObjeto.CADENA or tipoizq == TipoObjeto.BOOLEANO :
                return False
            return True
        if tipoizq == TipoObjeto.CADENA and tipoder == TipoObjeto.CADENA:
            return True
        if tipoizq == TipoObjeto.BOOLEANO and tipoizq == TipoObjeto.BOOLEANO:
            return True
        return False