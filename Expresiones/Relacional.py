from Expresiones.Constante import Constante
from Expresiones.Identificador import Identificador
from Objeto.Primitivo import Primitivo
from Abstract.Objeto import TipoObjeto
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Error import Error
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
        #------------------------------TENGO QUE VER SI MIS OPERAOORES SON ID---------------------------------
        #Operador Izquierdo
        if isinstance(self.OperacionIzq, Identificador):
            tipo = self.OperacionIzq.getTipo(traductor, entorno)
            resultado = ""
            if tipo != "error":
                if tipo != TipoObjeto.CADENA:
                    traer = "t"+str(traductor.getContador())+" = stack[int("+str(opi)+")];//Traemos la variable\n"
                    resultado = "t"+str(traductor.getContador())
                    traductor.addCodigo(traer)
                    traductor.IncrementarContador()
                else:
                    resultado = self.OperacionIzq.getValor(traductor, entorno)
                opi=[resultado, tipo]
            else:
                return "error"
        #Operador Derecho
        if isinstance(self.OperacionDer, Identificador):
            tipo = self.OperacionDer.getTipo(traductor, entorno)
            resultadod = ""
            if tipo != "error":
                if tipo != TipoObjeto.CADENA:
                    traer = "t"+str(traductor.getContador())+" = stack[int("+str(opd)+")];//Traemos la variable\n"
                    resultadod = "t"+str(traductor.getContador())
                    traductor.addCodigo(traer)
                    traductor.IncrementarContador()
                else:
                    resultadod = self.OperacionDer.getValor(entorno)
                opd = [resultadod, tipo]
            else:
                return "error"
        #print(self.operador)
        if self.operador == OperadorRelacional.MAYORQUE:

            if self.VerificarTipo(opi[1], opd[1]):
                valor = self.getEtiqueta(traductor)
                acepta = valor[0]
                rechaza= valor[1]

                #traductor.IncrementarGotos(2)
                cadena = "if "+str(opi[0])+" > "+ str(opd[0])+" { goto "+acepta+ ";}\n"
                cadena += "goto "+rechaza+";\n"
                traductor.addCodigo(cadena)
                return [acepta, rechaza]
        if self.operador == OperadorRelacional.MENORQUE:
            if self.VerificarTipo(opi[1], opd[1]):
                valor = self.getEtiqueta(traductor)
                acepta = valor[0]
                rechaza= valor[1]

                #traductor.IncrementarGotos(2)
                cadena = "if "+str(opi[0])+" < "+ str(opd[0])+" { goto "+acepta+ ";}\n"
                cadena += "goto "+rechaza+";\n"
                traductor.addCodigo(cadena)
                return [acepta, rechaza]
        if self.operador == OperadorRelacional.MAYORIGUAL:
            if self.VerificarTipo(opi[1], opd[1]):
                valor = self.getEtiqueta(traductor)
                acepta = valor[0]
                rechaza= valor[1]

                #traductor.IncrementarGotos(2)
                cadena = "if "+str(opi[0])+" >= "+ str(opd[0])+" { goto "+acepta+ ";}\n"
                cadena += "goto "+rechaza+";\n"
                traductor.addCodigo(cadena)
                return [acepta, rechaza]
        if self.operador == OperadorRelacional.MENORIGUAL:
            if self.VerificarTipo(opi[1], opd[1]):
                valor = self.getEtiqueta(traductor)
                acepta = valor[0]
                rechaza= valor[1]

                #traductor.IncrementarGotos(2)
                cadena = "if "+str(opi[0])+" <= "+ str(opd[0])+" { goto "+acepta+ ";}\n"
                cadena += "goto "+rechaza+";\n"
                traductor.addCodigo(cadena)
                return [acepta, rechaza]
        if self.operador == OperadorRelacional.IGUALIGUAL:
            if self.VerificarTipo(opi[1], opd[1]):
                valor = self.getEtiqueta(traductor)
                acepta = valor[0]
                rechaza= valor[1]

                #traductor.IncrementarGotos(2)
                cadena = "if "+str(opi[0])+" == "+ str(opd[0])+" { goto "+acepta+ ";}\n"
                cadena += "goto "+rechaza+";\n"
                traductor.addCodigo(cadena)
                return [acepta, rechaza]
        if self.operador == OperadorRelacional.DIFERENTE:
            if self.VerificarTipo(opi[1], opd[1]):
                valor = self.getEtiqueta(traductor)
                acepta = valor[0]
                rechaza= valor[1]
        
                #traductor.IncrementarGotos(2)
                cadena = "if "+str(opi[0])+" != "+ str(opd[0])+" { goto "+acepta+ ";}\n"
                cadena += "goto "+rechaza+";\n"
                traductor.addCodigo(cadena)
                return [acepta, rechaza]
        traductor.addExcepcion(Error("Semántico", "Los tipos de operandos no coinciden", self.fila, self.columna))
        return "error"
        
    def VerificarTipo(self, opi, opd):
        if opi == TipoObjeto.ENTERO or opi == TipoObjeto.DECIMAL:
            if opd == TipoObjeto.ENTERO or opd == TipoObjeto.DECIMAL:
                return True
            return False
        if opi == TipoObjeto.CADENA and opd == TipoObjeto.CADENA:
            return True
        if opi == TipoObjeto.BOOLEANO and opd == TipoObjeto.BOOLEANO:
            return True
        return False

    def getEtiqueta(self, traductor):
        rechaza=""
        acepta = ""
        if traductor.HayCambio():
            if traductor.getLogica() == 1:
                rechaza = traductor.getEtiquetaCambio()
                acepta = "L"+str(traductor.getGotos())
                traductor.SetearEtiqueta()
                traductor.IncrementarGotos(1)
            elif traductor.getLogica() == 2:
                acepta = traductor.getEtiquetaCambio()
                rechaza = "L"+str(traductor.getGotos())
                traductor.SetearEtiqueta()
                traductor.IncrementarGotos(1)
        else:
            acepta = "L"+str(traductor.getGotos())
            rechaza = "L"+str(traductor.getGotos()+1)
            traductor.IncrementarGotos(2)
        return [acepta, rechaza]