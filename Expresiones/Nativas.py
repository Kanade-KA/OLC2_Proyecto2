from Abstract.NodoAST import NodoAST
from Abstract.Objeto import TipoObjeto
from Expresiones.Identificador import Identificador
from TablaSimbolo.Error import Error
from TablaSimbolo.Tipo import OperadorNativo
import math

class Nativas(NodoAST):
    def __init__(self, operador, operando, base, fila, columna):
        self.operador = operador
        self.operando=operando
        self.base = base
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        op = self.operando.interpretar(arbol, entorno)
        if self.operador == OperadorNativo.LOGARITMO:
            base = self.base.interpretar(arbol, entorno)
            if isinstance(op, int) or isinstance(op, float):
                if isinstance(base, int) or isinstance(base, float):
                    return float(math.log(op, base))
        if self.operador == OperadorNativo.LOWERCASE:
            if isinstance(op, str):
                return str.lower(op)
        if self.operador == OperadorNativo.UPPERCASE:
            if isinstance(op, str):
                return str.upper(op)
        if self.operador == OperadorNativo.SENO:
            if isinstance(op, float) or isinstance(op, int):
                return float(math.sin(op))
        if self.operador == OperadorNativo.COSENO:
            if isinstance(op, float) or isinstance(op, int):
                return float(math.cos(op))
        if self.operador == OperadorNativo.TANGENTE:
            if isinstance(op, float) or isinstance(op, int):
                return float(math.tan(op))
        if self.operador == OperadorNativo.CUADRADA:
            if isinstance(op, float) or isinstance(op, int):
                return float(math.sqrt(op))
        if self.operador == OperadorNativo.TRUNC:
            return int(float(op))
        if self.operador == OperadorNativo.FLOAT:
            return float(int(op))
        if self.operador == OperadorNativo.STRING:
            return str(op)
        return

    def graficar(self, nodo):
        nodo += "Asingacion\n"
        return

    def traducir(self, traductor, entorno):
        op = self.operando.traducir(traductor, entorno)
        #VIENDO SI NO ES UN IDENTIFICADOR
        idder = traductor.EsIdentificador(self.operando, op, entorno, self.fila, self.columna)
        if idder[0]:
            op = [idder[1], idder[2]]

        if self.operador == OperadorNativo.LOWERCASE:
            if op[1] != TipoObjeto.CADENA:
                traductor.addExcepcion(Error("Semantico", "Lowercase acepta solo Cadenas", self.fila, self.columna))
                return "error"
            traductor.addCodigo("//**************************KOWER CASE**************************\n")
            cadena = "t"+str(traductor.getContador())+" = S + "+str(traductor.getStack())+";\n"
            cadena += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador())+" + 1;//Para ingresar el parametro\n"
            cadena += "stack[int(t"+str(traductor.getContador())+")] = "+str(op[0])+";\n"
            cadena += "S = S + "+str(traductor.getStack())+";\n"
            cadena += "lowercase();\n"
            traductor.IncrementarContador()
            resultado = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            cadena += resultado +" = stack[int(S)];\n"
            cadena += "S = S - "+str(traductor.getStack())+";\n"
            traductor.addCodigo(cadena)
            self.getLower(traductor)
            return [resultado, TipoObjeto.CADENA]
        if self.operador == OperadorNativo.UPPERCASE:
            if op[1] != TipoObjeto.CADENA:
                traductor.addExcepcion(Error("Semantico", "Uppercase acepta solo Cadenas", self.fila, self.columna))
                return "error"
            traductor.addCodigo("//**************************UPPER CASE**************************\n")
            cadena = "t"+str(traductor.getContador())+" = S + "+str(traductor.getStack())+";\n"
            cadena += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador())+" + 1;//Para ingresar el parametro\n"
            cadena += "stack[int(t"+str(traductor.getContador())+")] = "+str(op[0])+";\n"
            cadena += "S = S + "+str(traductor.getStack())+";\n"
            cadena += "uppercase();\n"
            traductor.IncrementarContador()
            resultado = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            cadena += resultado +" = stack[int(S)];\n"
            cadena += "S = S - "+str(traductor.getStack())+";\n"
            traductor.addCodigo(cadena)
            self.getUpper(traductor)
            return [resultado, TipoObjeto.CADENA]
        if self.operador == OperadorNativo.TRUNC:
            if op[1] != TipoObjeto.DECIMAL:
                traductor.addExcepcion(Error("Semantico", "Trunc acepta solo float64", self.fila, self.columna))
                return "error"
            traductor.addCodigo("//**************************TRUNC CASE**************************\n")
            cadena = "t"+str(traductor.getContador())+" = S + "+str(traductor.getStack())+";\n"
            cadena += "stack[int(t"+str(traductor.getContador())+")] = "+str(op[0])+";\n"
            traductor.IncrementarContador()
            resultado = "t"+str(traductor.getContador())
            cadena += resultado +" = stack[int(t"+str(traductor.getContador()-1)+")];\n"
            traductor.IncrementarContador()
            traductor.addCodigo(cadena)
            return [resultado, TipoObjeto.ENTERO]
        if self.operador == OperadorNativo.FLOAT:
            if op[1] != TipoObjeto.ENTERO:
                traductor.addExcepcion(Error("Semantico", "Trunc acepta solo float64", self.fila, self.columna))
                return "error"
            traductor.addCodigo("//**************************FLOAT CASE**************************\n")
            cadena = "t"+str(traductor.getContador())+" = S + "+str(traductor.getStack())+";\n"
            cadena += "stack[int(t"+str(traductor.getContador())+")] = "+str(op[0])+";\n"
            traductor.IncrementarContador()
            resultado = "t"+str(traductor.getContador())
            cadena += resultado +" = stack[int(t"+str(traductor.getContador()-1)+")];\n"
            traductor.IncrementarContador()
            traductor.addCodigo(cadena)
            return [resultado, TipoObjeto.DECIMAL]
        if self.operador == OperadorNativo.STRING:
            traductor.addCodigo("//**************************STRING CASE**************************\n")
            valor = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            heap = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            cadena = valor+" = "+str(op[0])+";\n"
            cadena += heap +" = heap[int("+valor+")];\n"
            cadena += "if "+heap+" == 0 { goto L0; }\n"
            cadena += valor +" = "+valor+" - 1;\n"
            cadena += "if "+valor+" == -1 { goto L1; }\n"
            cadena += heap +" = heap[int("+valor+")];"
            cadena += "if "+heap+" == -1 { goto L1; }\n"
            cadena += "L0:\n"
            traductor.addCodigo(cadena)
            newheap = traductor.putStringHeap(str(op[0]))
            cadena = valor +" = "+newheap+";\n"
            cadena += "goto L2;\n"
            cadena += "L1:\n"
            cadena += valor +" = "+str(op[0])+";\n"
            cadena += "L2:\n"
            traductor.addCodigo(cadena)
            return[valor, TipoObjeto.CADENA]


    def getLower(self, traductor):
        if not traductor.hayLower():
            heap = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            stack = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            letra = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            resultado = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            #Etiquetas
            revision = "L0"
            esmayor = "L2"
            esletra = "L3"
            incrementar = "L4"
            fin = "L5"
            #Funcion
            cadena="func lowercase(){\n"
            cadena += resultado +" = H;\n"
            cadena += stack +" = S + 1;\n"
            cadena += heap +" = stack[int("+stack+")];\n"
            cadena += revision+":\n"
            cadena += letra +" = heap[int("+heap+")];\n"
            cadena += "if "+letra+" == -1 { goto "+fin+"; }\n"
            cadena += "if "+letra+" >= 65 { goto "+ esletra+"; }\n"
            cadena += "goto "+incrementar+";\n"
            cadena += esletra+":\n"
            cadena += "if "+letra+" <= 90 { goto "+esmayor+"; }\n"
            cadena += "goto "+incrementar+";\n"
            cadena += esmayor+":\n"
            cadena += "t"+str(traductor.getContador())+" = "+letra+";\n"
            cadena += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador())+" + 32;\n"
            cadena += "heap[int(H)] = t"+str(traductor.getContador())+";\n"
            cadena += "H = H + 1;\n"
            cadena += heap +" = "+heap+" + 1;\n"
            cadena += "goto "+revision+";\n"
            cadena += incrementar + ":\n"
            cadena += "heap[int(H)] = "+letra+";\n"
            cadena += "H = H + 1;\n"
            cadena += heap +" = "+heap+" + 1;\n"
            cadena += "goto "+revision+";\n"
            cadena += fin + ":\n"
            cadena += "heap[int(H)] = -1;\n"
            cadena += "H = H + 1;\n"
            cadena += "stack[int(S)] = "+resultado+";\n"
            cadena += "return;\n}\n\n"
            traductor.addFuncion(cadena)
            traductor.activarLower()
        return

    def getUpper(self, traductor):
        if not traductor.hayUpper():
            heap = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            stack = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            letra = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            resultado = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            #Etiquetas
            revision = "L0"
            esmenor = "L2"
            esletra = "L3"
            incrementar = "L4"
            fin = "L5"
            #Funcion
            cadena="func uppercase(){\n"
            cadena += resultado +" = H;\n"
            cadena += stack +" = S + 1;\n"
            cadena += heap +" = stack[int("+stack+")];\n"
            cadena += revision+":\n"
            cadena += letra +" = heap[int("+heap+")];\n"
            cadena += "if "+letra+" == -1 { goto "+fin+"; }\n"
            cadena += "if "+letra+" >= 97 { goto "+ esletra+"; }\n"
            cadena += "goto "+incrementar+";\n"
            cadena += esletra+":\n"
            cadena += "if "+letra+" <= 122 { goto "+esmenor+"; }\n"
            cadena += "goto "+incrementar+";\n"
            cadena += esmenor+":\n"
            cadena += "t"+str(traductor.getContador())+" = "+letra+";\n"
            cadena += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador())+" - 32;\n"
            cadena += "heap[int(H)] = t"+str(traductor.getContador())+";\n"
            cadena += "H = H + 1;\n"
            cadena += heap +" = "+heap+" + 1;\n"
            cadena += "goto "+revision+";\n"
            cadena += incrementar + ":\n"
            cadena += "heap[int(H)] = "+letra+";\n"
            cadena += "H = H + 1;\n"
            cadena += heap +" = "+heap+" + 1;\n"
            cadena += "goto "+revision+";\n"
            cadena += fin + ":\n"
            cadena += "heap[int(H)] = -1;\n"
            cadena += "H = H + 1;\n"
            cadena += "stack[int(S)] = "+resultado+";\n"
            cadena += "return;\n}\n\n"
            traductor.addFuncion(cadena)
            traductor.activarUpper()
        return

    def getTrunc(self, traductor):
        if not traductor.hayTrunc():
            inicio = "L0"
            fin = "L1"
            punto = "L2"
            entero = "L3"
            ultimo = "L4"

            heap = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            numero = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            unidades = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            suma = "t"+str(traductor.getContador())
            traductor.IncrementarContador()

            cadena = "func trunc(){\n"
            cadena += heap +" = S + 1;\n"
            cadena += unidades +" = 1;\n"
            cadena += inicio+":\n"
            cadena += numero +" = heap[int("+heap+")];\n"
            cadena += "if "+numero+" == 46 { goto "+punto +"; }\n"
            cadena += heap +" = "+heap +" + 1;\n"
            cadena += "goto "+inicio+";\n"
            cadena += punto +":\n"
            cadena += heap +" = "+heap +" - 1;\n"
            cadena += entero+":\n"
            cadena += numero +" = heap[int("+heap+")];\n"
            cadena += "if "+heap+" == 0 { goto "+ultimo+"; }\n"
            cadena += "if "+numero+" == -1 { goto "+fin+"; }\n"
            cadena += "t"+str(traductor.getContador())+" = "+numero+";\n"
            cadena += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador()) +" - 48;\n"
            cadena += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador()) +" / "+ unidades+";\n"
            cadena += unidades +" = "+unidades +" * 10;\n"
            cadena += suma +" = "+suma+" + t"+str(traductor.getContador())+";\n"
            traductor.IncrementarContador()
            cadena += heap +" = "+heap +" - 1;\n"
            cadena += "goto "+entero+";\n"
            cadena += ultimo+"://SI ENCUENTRA UN 0 ES POR QUE NO PUDO GUARDAR ESE LO HACE DE ULTIMO\n"
            cadena += "t"+str(traductor.getContador())+" = "+numero+";\n"
            cadena += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador()) +" - 48;\n"
            cadena += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador()) +" * "+ unidades+";\n"
            cadena += suma +" = "+suma+" + t"+str(traductor.getContador())+";\n"
            traductor.IncrementarContador()
            cadena += fin +"://FIN SOLO GUARDA LA SUMA QUE DIÓ EN TODO\n"
            cadena += "stack[int(S)] = "+suma+";\n"
            cadena += "return;\n}\n\n"
            traductor.addFuncion(cadena)
            traductor.activarTrunc()