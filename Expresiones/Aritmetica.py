from TablaSimbolo.Error import Error
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Tipo import OperadorAritmetico
from Expresiones.Identificador import Identificador


class Aritmetica(NodoAST):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        self.operador = operador
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperacionDer
        self.fila = fila
        self.columna = columna


    def interpretar(self, arbol, entorno):
        opi = self.OperacionIzq.interpretar(arbol, entorno)
        opd = self.OperacionDer.interpretar(arbol, entorno)
        
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

    def traducir(self, traductor, entorno):
        opi = self.OperacionIzq.traducir(traductor, entorno)
        opd = self.OperacionDer.traducir(traductor, entorno)
       #------------------------------TENGO QUE VER SI MIS OPERAOORES SON ID---------------------------------
       #Operador Izquierdo
        if isinstance(self.OperacionIzq, Identificador):
            traductor.setTmpIzq(self.OperacionIzq.getTipo(entorno))
            if traductor.getTmpIzq() != "string":
                traer = "t"+str(traductor.getContador())+" = stack[int("+str(opi)+")]//Traemos la variable\n"
                opi = "t"+str(traductor.getContador())
                traductor.addCodigo(traer)
                traductor.IncrementarContador()
            else:
                opi = self.OperacionIzq.getValor(entorno)
        #Operador Derecho
        if isinstance(self.OperacionDer, Identificador):
            traductor.setTmpDer(self.OperacionDer.getTipo(entorno))
            if traductor.getTmpIzq() != "string":
                traer = "t"+str(traductor.getContador())+" = stack[int("+str(opd)+")]//Traemos la variable\n"
                opd = "t"+str(traductor.getContador())
                traductor.addCodigo(traer)
                traductor.IncrementarContador()
            else:
                opd = self.OperacionDer.getValor(entorno)
        #----------------------------------------------------------------------------------------------------
        if opi != None and opd != None:
            if (self.operador==OperadorAritmetico.MAS):
                if self.sinString(traductor, opi, opd):
                    if  self.HayDoble(traductor, opi, opd):
                        suma = "t"+ str(traductor.getContador()) + "= "+ str(opi) + "+"+ str(opd)
                        traductor.addCodigo(suma+"\n")
                        traductor.IncrementarContador()
                        traductor.cambiarTipo("doble")
                        return  "t"+str(traductor.getContador()-1)
                    else:
                        suma = "t"+ str(traductor.getContador()) + "= "+ str(opi) + "+"+ str(opd)
                        traductor.addCodigo(suma+"\n")
                        traductor.IncrementarContador()
                        traductor.cambiarTipo("int")
                        return  "t"+str(traductor.getContador()-1)
            if (self.operador==OperadorAritmetico.MENOS):
                if self.sinString(traductor, opi, opd):
                    if  self.HayDoble(traductor, opi, opd):
                        resta = "t"+ str(traductor.getContador()) + "= "+ str(opi) + "-"+ str(opd)
                        traductor.addCodigo(resta+"\n")
                        traductor.IncrementarContador()
                        traductor.cambiarTipo("doble")
                        return  "t"+str(traductor.getContador()-1)
                    else:
                        resta = "t"+ str(traductor.getContador()) + "= "+ str(opi) + "-"+ str(opd)
                        traductor.addCodigo(resta+"\n")
                        traductor.IncrementarContador()
                        traductor.cambiarTipo("int")
                        return  "t"+str(traductor.getContador()-1)
            if (self.operador == OperadorAritmetico.POR):
                if self.sinString(traductor, opi, opd):
                    if self.HayDoble(traductor, opi, opd):
                        mult = "t"+ str(traductor.getContador()) + "= "+ str(opi) + "*"+ str(opd)
                        traductor.addCodigo(mult+"\n")
                        traductor.IncrementarContador()
                        traductor.cambiarTipo("doble")
                        return  "t"+str(traductor.getContador()-1)
                    else:
                        mult = "t"+ str(traductor.getContador()) + "= "+ str(opi) + "*"+ str(opd)
                        traductor.addCodigo(mult+"\n")
                        traductor.IncrementarContador()
                        traductor.cambiarTipo("int")
                        return  "t"+str(traductor.getContador()-1)
                if self.sonAmbasCadenas(traductor, opi, opd):
                    cad = opi + opd
                    traductor.cambiarTipo("string")
                    return cad
            if (self.operador == OperadorAritmetico.DIV):
                if self.sinString(traductor, opi, opd):
                    div = "t"+ str(traductor.getContador()) + "= "+ str(opi) + "/"+ str(opd)
                    traductor.addCodigo(div+"\n")
                    traductor.IncrementarContador()
                    traductor.cambiarTipo("doble")
                    return  "t"+str(traductor.getContador()-1)
            if (self.operador == OperadorAritmetico.POW):
                if self.sinString(traductor, opi, opd):
                    pow = "t"+str(traductor.getContador())+" = S + 0//Extraemos el stack \n"
                    pow += "t"+str(traductor.getContador())+ " = t"+str(traductor.getContador())+" + 1 // le agregamos 1 al Stack para guardar el primer parametro ya que en P vendrá el retorno\n"
                    pow += "stack[int(t"+ str(traductor.getContador())+")] = "+str(opi)+"//Agregamos el primer parametro al stack\n"
                    pow += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador())+" + 1 // para agregar el segundo\n"
                    pow += "stack[int(t"+ str(traductor.getContador())+")] = "+str(opd)+"//Agregamos el segundo parametro al stack\n"
                    pow += "potencia()\n"
                    traductor.addCodigo(pow)
                    traductor.IncrementarContador()
                    contres = traductor.getContador()
                    res = "t"+str(contres)+ " = stack[int(S)]\n"
                    traductor.IncrementarContador()
                    traductor.cambiarTipo("int")
                    traductor.addCodigo(res)

                    if not traductor.hayPotencia():
                        #----------------------------POTENCIA--------------------------------
                        potencia = "func potencia(){\n"
                        potencia += "t"+str(traductor.getContador())+" = S + 1//para sacar el primer parametro\n"
                        traductor.IncrementarContador()
                        potencia += "t"+str(traductor.getContador())+" = stack[int(t"+str(traductor.getContador()-1)+")]//Saco el primer parametro\n"
                        traductor.IncrementarContador()
                        numero = traductor.getContador()#base la que siempre va a estar cambiando
                        potencia += "t"+str(numero)+" = t"+str(numero - 1)+"//en esta variable se guarda el numero\n"
                        traductor.IncrementarContador()
                        multip = traductor.getContador()#numero por el que se multiplicará nunca va a cambiar
                        potencia += "t"+str(multip) + " = t"+str(numero -1)+"//esta se va a usar para el que se multiplica\n"
                        traductor.IncrementarContador()
                        potencia += "t"+str(traductor.getContador())+" = S + 2// va a posicionarse en el segundo parametro (cuantas veces va a mult)\n"
                        traductor.IncrementarContador()
                        repeticion = traductor.getContador()#para el while que se va  ahacer
                        potencia += "t"+str(repeticion)+" = stack[int(t"+str(traductor.getContador()-1)+")]//Saco el segundo parametro del stack\n"
                        traductor.IncrementarContador()
                        potencia += "if t"+str(repeticion)+" == 0 { goto L1 }//Si es 0 es por que un numero elevado a 0 es 1\n"
                        potencia += "L2:\n"
                        potencia += "if t"+str(repeticion)+" <= 1 { goto L0 }\n"
                        potencia += "t"+str(numero) +" = t"+str(numero)+ " * t"+str(multip)+"//para multiplicar por la base\n"
                        potencia += "t"+str(repeticion) + " = t"+str(repeticion)+ "- 1 // se resta uno \n"
                        potencia += "goto L2\n"
                        potencia += "L0:\n"
                        potencia += "stack[int(S)] = t"+str(numero) +"\n"
                        potencia += "goto L3\n"
                        potencia += "L1:\n"
                        potencia += "stack[int(S)] = 1;\n"
                        potencia += "L3:\n"
                        potencia += "return\n"
                        potencia += "}\n\n"
                        traductor.addFuncion(potencia)
                        traductor.activarPotencia()
                    return "t"+str(contres)
                if self.CadenaInt(traductor, opi, opd):
                    palabra=""
                    for x in range (opd):
                        palabra+=opi
                    traductor.cambiarTipo("string")
                    return str(palabra)
            if (self.operador == OperadorAritmetico.MOD):
                if opd != 0:
                    mod = "t" + str(traductor.getContador())+" = math.Mod("+str(opi) +","+str(opd)+")"
                    traductor.addCodigo(mod+"\n")
                    traductor.IncrementarContador()
                    traductor.cambiarTipo("int")
                    return "t"+ str(traductor.getContador()-1)
            return traductor.addExcepcion(Error("Semantico", "Los tipos no coinciden", self.fila, self.columna))
        traductor.addExcepcion(Error("Semantico", "Operador Nulo", self.fila, self.columna))
        return

    def sinString(self, traductor, opi, opd):
        operadorizq = False
        operadorder = False
        if isinstance(opi, int) or isinstance(opi, float):
            operadorizq = True
        if traductor.getTmpIzq() == "int" or traductor.getTmpIzq() == "doble":
            operadorizq = True
        if traductor.getTmpDer() == "int" or traductor.getTmpDer() == "doble":
            operadorder = True
        if isinstance(opd, int) or isinstance(opd, float):
            operadorder = True
        if operadorizq and operadorder:
            return True
        else:
            return False

    def HayDoble(self, traductor, opi, opd):
        if isinstance(opi, float):
            return True
        if isinstance(opd, float):
            return True
        if traductor.getTmpIzq() == "doble":
            return True
        if traductor.getTmpDer() == "doble":
            return True
        return False

    def sonAmbasCadenas(self, traductor, opi, opd):
        izquierdo = False
        derecho = False
        if traductor.getTmpIzq() == "string" and isinstance(opi, str):
            izquierdo = True
        if traductor.getTmpDer() == "string" and isinstance(opd, str):
            derecho = True
        if traductor.getTmpIzq() == "" and isinstance(opi, str):
            izquierdo = True
        if traductor.getTmpDer() == "" and isinstance(opd, str):
            derecho = True
        if izquierdo and derecho:
            return True
        else:
            return False

    def CadenaInt(self, traductor, opi, opd):
        izquierdo = False
        derecho = False
        if traductor.getTmpIzq() == "string" and isinstance(opi, str):
            izquierdo = True
        if traductor.getTmpIzq() == "" and isinstance(opi, str):
            izquierdo = True
        if isinstance(opd, int):
            derecho = True
        if traductor.getTmpDer() == "int":
            derecho =  True
        
        if izquierdo and derecho:
            return True
        return False