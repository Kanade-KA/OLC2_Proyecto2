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
        sonRelacionales=False;
        valortmp = ""
        valortmp2 = ""
        opi = self.OperacionIzq.traducir(traductor, entorno)
        if isinstance(self.OperacionIzq, Relacional):
            cadena = opi[0]+":\n"
            valortmp = "t"+str(traductor.getContador())
            cadena += valortmp +" = 1;\n"
            nuevaetiqueta = "L"+str(traductor.getGotos())
            cadena += "goto "+nuevaetiqueta+";\n"
            cadena += opi[1]+":\n"
            cadena += valortmp +" = 0;\n"
            cadena += nuevaetiqueta+":\n"
            traductor.IncrementarGotos(1)
            traductor.IncrementarContador()
            traductor.addCodigo(cadena)

        opd = self.OperacionDer.traducir(traductor, entorno)
        if isinstance(self.OperacionDer, Relacional):
            cadena = opd[0]+":\n"
            valortmp2 = "t"+str(traductor.getContador())
            cadena += valortmp2 +" = 1;\n"
            nuevaetiqueta = "L"+str(traductor.getGotos())
            cadena += "goto "+nuevaetiqueta+";\n"
            cadena += opd[1]+":\n"
            cadena += valortmp2 +" = 0;\n"
            cadena += nuevaetiqueta+":\n"
            traductor.IncrementarGotos(1)
            traductor.IncrementarContador()
            traductor.addCodigo(cadena)
            sonRelacionales = True
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
            if sonRelacionales:
                valor = self.getEtiqueta(traductor)
                acepta = valor[0]
                rechaza= valor[1]
                cadena = "if "+str(valortmp)+" == "+ str(valortmp2)+" { goto "+acepta+ ";}\n"
                cadena += "goto "+rechaza+";\n"
                traductor.addCodigo(cadena)
                return [acepta, rechaza]
            if self.VerificarTipo(opi[1], opd[1]):
                if opi[1] == TipoObjeto.CADENA:
                    tmp = "t"+str(traductor.getContador())
                    traductor.IncrementarContador()
                    cadena = tmp+" = S + "+str(traductor.getStack())+";\n"
                    cadena +=  tmp +" = "+tmp+" + 1;\n"
                    cadena += "stack[int("+tmp+")] = "+opi[0]+";\n"
                    cadena +=  tmp +" = "+tmp+" + 1;\n"
                    cadena += "stack[int("+tmp+")] = "+opd[0]+";\n"
                    cadena += "S = S + "+str(traductor.getStack())+";\n"
                    self.CompararStrings(traductor)
                    cadena += "compararString();\n"
                    resultado = "t"+str(traductor.getContador())
                    traductor.IncrementarContador()
                    cadena += resultado + " = stack[int(S)];\n"
                    cadena += "S = S - "+str(traductor.getStack())+";\n"
                    traductor.addCodigo(cadena)
                    valor = self.getEtiqueta(traductor)
                    acepta = valor[0]
                    rechaza= valor[1]
                    cadena = "if "+str(resultado)+" == 1 { goto "+acepta+ ";}\n"
                    cadena += "goto "+rechaza+";\n"
                    traductor.addCodigo(cadena)
                    return [acepta, rechaza]
                else:
                    if opi[1] == TipoObjeto.BOOLEANO:
                        opizq = self.EtiquetaBooleana(traductor, opi[0])
                        opder = self.EtiquetaBooleana(traductor, opd[0])
                        opi[0]=opizq
                        opd[0]=opder
                    valor = self.getEtiqueta(traductor)
                    acepta = valor[0]
                    rechaza= valor[1]
                    cadena = "if "+str(opi[0])+" == "+ str(opd[0])+" { goto "+acepta+ ";}\n"
                    cadena += "goto "+rechaza+";\n"
                    traductor.addCodigo(cadena)
                    return [acepta, rechaza]
        if self.operador == OperadorRelacional.DIFERENTE:
            if sonRelacionales:
                valor = self.getEtiqueta(traductor)
                acepta = valor[0]
                rechaza= valor[1]
                cadena = "if "+str(valortmp)+" != "+ str(valortmp2)+" { goto "+acepta+ ";}\n"
                cadena += "goto "+rechaza+";\n"
                traductor.addCodigo(cadena)
                return [acepta, rechaza]
            if self.VerificarTipo(opi[1], opd[1]):
                if opi[1] == TipoObjeto.CADENA:
                    tmp = "t"+str(traductor.getContador())
                    traductor.IncrementarContador()
                    cadena = tmp+" = S + "+str(traductor.getStack())+";\n"
                    cadena +=  tmp +" = "+tmp+" + 1;\n"
                    cadena += "stack[int("+tmp+")] = "+opi[0]+";\n"
                    cadena +=  tmp +" = "+tmp+" + 1;\n"
                    cadena += "stack[int("+tmp+")] = "+opd[0]+";\n"
                    cadena += "S = S + "+str(traductor.getStack())+";\n"
                    self.CompararStrings(traductor)
                    cadena += "compararString();\n"
                    resultado = "t"+str(traductor.getContador())
                    traductor.IncrementarContador()
                    cadena += resultado + " = stack[int(S)];\n"
                    cadena += "S = S - "+str(traductor.getStack())+";\n"
                    traductor.addCodigo(cadena)
                    valor = self.getEtiqueta(traductor)
                    acepta = valor[0]
                    rechaza= valor[1]
                    cadena = "if "+str(resultado)+" == 0 { goto "+acepta+ ";}\n"
                    cadena += "goto "+rechaza+";\n"
                    traductor.addCodigo(cadena)
                    return [acepta, rechaza]
                else:
                    if opi[1] == TipoObjeto.BOOLEANO:
                        opizq = self.EtiquetaBooleana(traductor, opi[0])
                        opder = self.EtiquetaBooleana(traductor, opd[0])
                        opi[0]=opizq
                        opd[0]=opder
                    valor = self.getEtiqueta(traductor)
                    acepta = valor[0]
                    rechaza= valor[1]
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
        if type(opi) is str and type(opd) is str:
            return None
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

    def EtiquetaBooleana(self, traductor, operador):
        etiqueta = "t"+str(traductor.getContador())
        traductor.IncrementarContador()
        cadena = ""
        if operador == True:
            cadena += etiqueta + " = 1;\n"
        elif operador == False:
            cadena += etiqueta + " = 0; \n"
        else:
            return operador[0]
        traductor.addCodigo(cadena)
        return etiqueta

    def CompararStrings(self, traductor):
        if not traductor.hayCompString():
            revision = "L0"
            rechazo = "L1"
            acepta = "L2"
            fin = "L3"
            cadena = "func compararString(){\n"
            cadena += "t"+str(traductor.getContador()) +" = S + 1;//PrimerParametro\n"
            traductor.IncrementarContador()
            tmp1 = "t"+str(traductor.getContador())
            cadena += tmp1+" = stack[int(t"+str(traductor.getContador()-1)+")];\n"
            cadena += "t"+str(traductor.getContador()-1)+" = "+"t"+str(traductor.getContador()-1)+" + 1;\n"
            traductor.IncrementarContador()
            tmp2 = "t"+str(traductor.getContador()) 
            cadena += tmp2+" = stack[int(t"+str(traductor.getContador()-2)+")];\n"
            traductor.IncrementarContador()
            cadena += revision+":\n"
            pal1 = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            pal2 = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            cadena += pal1 + " = heap[int("+tmp1+")];\n"
            cadena += pal2 + " = heap[int("+tmp2+")];\n"
            cadena += "if "+pal1+" != "+pal2+" { goto "+ rechazo + "; }\n"
            cadena += "if "+pal1+" == -1 { goto "+acepta+"; }\n"
            cadena += tmp1 +" = "+tmp1+" + 1;\n"
            cadena += tmp2 +" = "+tmp2+" + 1;\n"
            cadena += "goto "+revision+"; \n"
            cadena += acepta+":\n"
            cadena += "stack[int(S)] = 1;\n"
            cadena += "goto "+fin+";\n"
            cadena += rechazo+":\n"
            cadena += "stack[int(S)] = 0;\n"
            cadena += fin+":\n"
            cadena += "return;\n}\n\n"
            traductor.addFuncion(cadena)
            traductor.activarCompString()