from Abstract.Objeto import TipoObjeto
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
        return arbol.addExcepcion(Error("Semantico", "Operador Nulo", self.fila, self.columna))
        

    def traducir(self, traductor, entorno):
        opi = self.OperacionIzq.traducir(traductor, entorno)
        opd = self.OperacionDer.traducir(traductor, entorno)
       #------------------------------TENGO QUE VER SI MIS OPERAOORES SON ID---------------------------------
       #Operador Izquierdo
        if isinstance(self.OperacionIzq, Identificador):
            tipo = self.OperacionIzq.getTipo(traductor, entorno)
            resultado = ""
            if tipo != "error":
                resultado = traductor.ExtraerVariable(opi)
                opi=[resultado, tipo]
            else:
                return "error"
        #Operador Derecho
        if isinstance(self.OperacionDer, Identificador):
            tipo = self.OperacionDer.getTipo(traductor, entorno)
            resultadod = ""
            if tipo != "error":
                resultadod = traductor.ExtraerVariable(opd)
                opd=[resultadod, tipo]
            else:
                return "error"
        #----------------------------------------------------------------------------------------------------
        if opi != None and opd != None:
            if (self.operador==OperadorAritmetico.MAS):
                if self.sinString(opi[1], opd[1]):
                    if  self.HayDoble(opi[1], opd[1]):
                        suma = "t"+ str(traductor.getContador()) + " = "+ str(opi[0]) + "+"+ str(opd[0])
                        traductor.addCodigo(suma+";\n")
                        traductor.IncrementarContador()
                        return  ["t"+str(traductor.getContador()-1), TipoObjeto.DECIMAL]
                    else:
                        suma = "t"+ str(traductor.getContador()) + " = "+ str(opi[0]) + "+"+ str(opd[0])
                        traductor.addCodigo(suma+";\n")
                        traductor.IncrementarContador()
                        return  ["t"+str(traductor.getContador()-1), TipoObjeto.ENTERO]
            if (self.operador==OperadorAritmetico.MENOS):
                if self.sinString(opi[1], opd[1]):
                    if  self.HayDoble(opi[1], opd[1]):
                        resta = "t"+ str(traductor.getContador()) + " = "+ str(opi[0]) + "-"+ str(opd[0])
                        traductor.addCodigo(resta+";\n")
                        traductor.IncrementarContador()
                        return  ["t"+str(traductor.getContador()-1), TipoObjeto.DECIMAL]
                    else:
                        resta = "t"+ str(traductor.getContador()) + " = "+ str(opi[0]) + "-"+ str(opd[0])
                        traductor.addCodigo(resta+";\n")
                        traductor.IncrementarContador()
                        return  ["t"+str(traductor.getContador()-1), TipoObjeto.ENTERO]
            if (self.operador == OperadorAritmetico.POR):
                if self.sinString(opi[1], opd[1]):
                    if  self.HayDoble(opi[1], opd[1]):
                        mult = "t"+ str(traductor.getContador()) + " = "+ str(opi[0]) + "*"+ str(opd[0])
                        traductor.addCodigo(mult+";\n")
                        traductor.IncrementarContador()
                        return  ["t"+str(traductor.getContador()-1), TipoObjeto.DECIMAL]
                    else:
                        mult = "t"+ str(traductor.getContador()) + " = "+ str(opi[0]) + "*"+ str(opd[0])
                        traductor.addCodigo(mult+";\n")
                        traductor.IncrementarContador()
                        return  ["t"+str(traductor.getContador()-1), TipoObjeto.ENTERO]
                if self.sonAmbasCadenas(opi[1], opd[1]):
                    cadena = "t"+str(traductor.getContador())+ " = S + "+str(traductor.getStack())+";//Guarda donde va el stack\n"
                    cadena += "t"+str(traductor.getContador())+ " = t"+str(traductor.getContador())+" + 1;// para meter el primer parametro\n"
                    cadena += "stack[int(t"+str(traductor.getContador())+")] = "+str(opi[0])+";\n"
                    cadena += "t"+str(traductor.getContador())+ " = t"+str(traductor.getContador())+" + 1;// para meter el segundo parametro\n"
                    cadena += "stack[int(t"+str(traductor.getContador())+")] = "+str(opd[0])+";\n"
                    cadena += "S = S + "+str(traductor.getStack())+";\n"
                    traductor.IncrementarContador()
                    cadena += "MultString();\n"
                    heap = "t"+str(traductor.getContador())
                    cadena += "t"+str(traductor.getContador())+" = stack[int(S)];//Sacamos el retorno\n"
                    cadena += "S = S - "+str(traductor.getStack())+";\n"
                    traductor.IncrementarContador()
                    traductor.addCodigo(cadena)
                    self.ConcatenaString(traductor)
                    return [heap, TipoObjeto.CADENA]
            if (self.operador == OperadorAritmetico.DIV):
                if self.sinString(opi[1], opd[1]):
                    div = "t"+ str(traductor.getContador()) + "= "+ str(opi[0]) + "/"+ str(opd[0])
                    traductor.addCodigo(div+";\n")
                    traductor.IncrementarContador()
                    return ["t"+str(traductor.getContador()-1), TipoObjeto.DECIMAL]
            if (self.operador == OperadorAritmetico.POW):
                if self.sinString(opi[1], opd[1]):
                    pow = "t"+str(traductor.getContador())+" = S + "+str(traductor.getStack())+";//Extraemos el stack \n"
                    pow += "t"+str(traductor.getContador())+ " = t"+str(traductor.getContador())+" + 1;// le agregamos 1 al Stack para guardar el primer parametro ya que en P vendrá el retorno\n"
                    pow += "stack[int(t"+ str(traductor.getContador())+")] = "+str(opi[0])+";//Agregamos el primer parametro al stack\n"
                    pow += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador())+" + 1;// para agregar el segundo\n"
                    pow += "stack[int(t"+ str(traductor.getContador())+")] = "+str(opd[0])+";//Agregamos el segundo parametro al stack\n"
                    pow += "S = S +"+str(traductor.getStack())+";\n"
                    traductor.IncrementarContador()
                    pow += "potencia();\n"
                    resultado = "t"+str(traductor.getContador())
                    pow += resultado + " = stack[int(S)];\n"
                    pow += "S = S - "+str(traductor.getStack())+";\n"
                    traductor.addCodigo(pow)
                    traductor.IncrementarContador()
                    if not traductor.hayPotencia():
                        self.Potencia(traductor)
                    return [resultado, TipoObjeto.ENTERO]
                if self.CadenaInt(opi[1], opd[1]):
                    cadena = "t"+str(traductor.getContador())+ " = S + "+str(traductor.getStack())+";//Guarda donde va el stack\n"
                    cadena += "t"+str(traductor.getContador())+ " = t"+str(traductor.getContador())+" + 1;// para meter el primer parametro\n"
                    cadena += "stack[int(t"+str(traductor.getContador())+")] = "+str(opi[0])+";\n"
                    cadena += "S = S + "+str(traductor.getStack())+";\n"
                    traductor.IncrementarContador()
                    cadena += "PotenciaString();\n"
                    heap = "t"+str(traductor.getContador())
                    cadena += "t"+str(traductor.getContador())+" = stack[int(S)];//Sacamos el retorno\n"
                    cadena += "S = S - "+str(traductor.getStack())+";\n"
                    traductor.IncrementarContador()
                    traductor.addCodigo(cadena)
                    self.PotenciaString(traductor, opd[0])
                    return [heap, TipoObjeto.CADENA]
            if (self.operador == OperadorAritmetico.MOD):
                if opd[0] != 0:
                    mod = "t" + str(traductor.getContador())+" = math.Mod("+str(opi[0]) +","+str(opd[0])+");"
                    traductor.addCodigo(mod+"\n")
                    traductor.IncrementarContador()
                    return ["t"+ str(traductor.getContador()-1), TipoObjeto.ENTERO]
            traductor.addExcepcion(Error("Semantico", "Los tipos no coinciden", self.fila, self.columna))
            return "error"
        traductor.addExcepcion(Error("Semantico", "Operador Nulo", self.fila, self.columna))
        return "error"

    def PotenciaString(self, traductor, num):
        if not traductor.hayPotString():
            reinicio = "L1"
            concatena = "L3"
            revision = "L4"
            fin = "L5"

            heap = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            palabra = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            temporal = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            cont = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            tmpheap = "t"+str(traductor.getContador())
            traductor.IncrementarContador()

            cadena = "func PotenciaString(){\n"
            cadena += heap +" = H;//Sacamos el puntero libre del heap\n"
            cadena += palabra +" = S + 1;//Sacamos la palabra\n"
            cadena += cont +" = 0;\n"
            cadena += reinicio +"://Reiniciamos la palabra\n"
            cadena += temporal +" = stack[int("+palabra+")];//Sacamos el puntero del heap\n"
            cadena += "if "+str(cont)+" >= "+str(num) +"{ goto "+fin+";}\n"
            cadena += concatena+"://Concatenación de palabra\n"
            cadena += tmpheap+" = heap[int("+temporal+")];\n"
            cadena += "if "+tmpheap+" == -1 { goto "+ revision+"; }\n"
            cadena += "heap[int(H)] = "+tmpheap+";\n"
            cadena += "H = H + 1;\n"
            cadena += temporal +" = "+temporal+" + 1;\n"
            cadena += "goto "+concatena+";\n"
            cadena += revision+":\n"
            cadena += cont +"= "+cont + " + 1;\n"
            cadena += "goto "+ reinicio +";\n"
            cadena += fin +":\n"
            cadena += "heap[int(H)] = -1;\n"
            cadena += "H = H + 1;\n"
            cadena += "stack[int(S)] = "+heap+";\n\n"
            cadena += "return;\n}\n"
            traductor.activarPotString()
            traductor.addFuncion(cadena)

    def sinString(self, opi, opd):
        if opi == TipoObjeto.CADENA or opd == TipoObjeto.CADENA:
            return False
        if opi == TipoObjeto.BOOLEANO or opd == TipoObjeto.BOOLEANO:
            return False
        return True

    def HayDoble(self, opi, opd):
        if opi == TipoObjeto.DECIMAL or opd == TipoObjeto.DECIMAL:
            return True
        return False

    def sonAmbasCadenas(self, opi, opd):
        if opi == TipoObjeto.CADENA and opd == TipoObjeto.CADENA:
            return True
        return False

    def CadenaInt(self, opi, opd):
        if opi == TipoObjeto.CADENA and opd == TipoObjeto.ENTERO:
            return True
        return False

    def ConcatenaString(self, traductor):
        if not traductor.hayMultString():
            etiquetainicio1 = "L1"
            etiquetair2 = "L2"
            etiquetainicio2 = "L3"
            etiquetafin="L4"

            heap = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            pal1 = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            pal2 = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            h1 = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            tmp1 = "t"+str(traductor.getContador())
            traductor.IncrementarContador()

            cadena = "func MultString(){\n"
            cadena += heap +" = H;//Sacamos el puntero libre del heap\n"
            cadena += pal1 +" = S + 1;//Sacamos el primer parámetro\n"
            cadena += pal2 +" = S + 2;//Sacamos el segundo parametro\n"
            cadena += h1 +"= stack[int("+pal1+")];//Sacamos el puntero del heap\n"
            cadena += etiquetainicio1 +"://Inicio de la primera palabra\n"
            cadena += tmp1+" = heap[int("+h1+")];\n"
            cadena += "if "+tmp1+" == -1 { goto "+ etiquetair2+"; }\n"
            cadena += "heap[int(H)] = "+tmp1+";\n"
            cadena += "H = H + 1;\n"
            cadena += h1 +" = "+h1+" + 1;\n"
            cadena += "goto "+etiquetainicio1+";\n"
            cadena += etiquetair2+":\n"
            cadena += h1 +"= stack[int("+pal2+")];//Sacamos el segundo puntero heap\n"
            cadena += etiquetainicio2+":\n"
            cadena += tmp1+" = heap[int("+h1+")];\n"
            cadena += "if "+tmp1 +" == -1 { goto "+etiquetafin+"; }\n"
            cadena += "heap[int(H)] ="+tmp1+";\n"
            cadena += "H = H + 1;\n"
            cadena += h1 +" = "+h1+" + 1;\n"
            cadena += "goto "+etiquetainicio2+";\n"
            cadena += etiquetafin+":\n"
            cadena += "heap[int(H)] = -1;\n"
            cadena += "H = H + 1;\n"
            cadena += "stack[int(S)] = "+heap+";\n\n"
            cadena += "return;\n}\n"
            traductor.activarMultString()
            traductor.addFuncion(cadena)

    def Potencia(self, traductor):
        #----------------------------POTENCIA--------------------------------
        potencia = "func potencia(){\n"
        potencia += "t"+str(traductor.getContador())+" = S + 1;//para sacar el primer parametro\n"
        traductor.IncrementarContador()
        potencia += "t"+str(traductor.getContador())+" = stack[int(t"+str(traductor.getContador()-1)+")];//Saco el primer parametro\n"
        traductor.IncrementarContador()
        numero = traductor.getContador()#base la que siempre va a estar cambiando
        potencia += "t"+str(numero)+" = t"+str(numero - 1)+";//en esta variable se guarda el numero\n"
        traductor.IncrementarContador()
        multip = traductor.getContador()#numero por el que se multiplicará nunca va a cambiar
        potencia += "t"+str(multip) + " = t"+str(numero -1)+";//esta se va a usar para el que se multiplica\n"
        traductor.IncrementarContador()
        potencia += "t"+str(traductor.getContador())+" = S + 2;//va a posicionarse en el segundo parametro (cuantas veces va a mult)\n"
        traductor.IncrementarContador()
        repeticion = traductor.getContador()#para el while que se va  ahacer
        potencia += "t"+str(repeticion)+" = stack[int(t"+str(traductor.getContador()-1)+")];//Saco el segundo parametro del stack\n"
        traductor.IncrementarContador()
        potencia += "if t"+str(repeticion)+" == 0 { goto L1; }//Si es 0 es por que un numero elevado a 0 es 1\n"
        potencia += "L2:\n"
        potencia += "if t"+str(repeticion)+" <= 1 { goto L0; }\n"
        potencia += "t"+str(numero) +" = t"+str(numero)+ " * t"+str(multip)+";//para multiplicar por la base\n"
        potencia += "t"+str(repeticion) + " = t"+str(repeticion)+ "- 1;// se resta uno \n"
        potencia += "goto L2;\n"
        potencia += "L0:\n"
        potencia += "stack[int(S)] = t"+str(numero) +";\n"
        potencia += "goto L3;\n"
        potencia += "L1:\n"
        potencia += "stack[int(S)] = 1;\n"
        potencia += "L3:\n"
        potencia += "return;\n"
        potencia += "}\n\n"
        traductor.addFuncion(potencia)
        traductor.activarPotencia()
        traductor.IncrementarStack()