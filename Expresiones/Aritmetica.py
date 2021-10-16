from TablaSimbolo.Error import Error
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Tipo import OperadorAritmetico

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
        if opi != None and opd != None:
            if (self.operador==OperadorAritmetico.MAS):
                if  isinstance(opi, float) or isinstance(opd, float) :
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
                if  isinstance(opi, float) or isinstance(opd, float) :
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
                if isinstance(opi, str) and isinstance(opd, str):
                    cad = opi + opd
                    traductor.cambiarTipo("string")
                    return cad
                elif isinstance(opi, float) or isinstance(opd, float):
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
            if (self.operador == OperadorAritmetico.DIV):
                    div = "t"+ str(traductor.getContador()) + "= "+ str(opi) + "/"+ str(opd)
                    traductor.addCodigo(div+"\n")
                    traductor.IncrementarContador()
                    traductor.cambiarTipo("doble")
                    return  "t"+str(traductor.getContador()-1)
            if (self.operador == OperadorAritmetico.POW):
                if isinstance(opi, str) and isinstance(opd, int):
                    palabra=""
                    for x in range (opd):
                        palabra+=opi
                    traductor.cambiarTipo("string")
                    return str(palabra)
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