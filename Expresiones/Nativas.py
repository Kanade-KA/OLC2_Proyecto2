from Abstract.NodoAST import NodoAST
from Abstract.Objeto import TipoObjeto
from Expresiones.Identificador import Identificador
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

    def traducir(self, traductor, entorno):
        op = self.operando.traducir(traductor, entorno)
        if isinstance(self.operando, Identificador):
            tipo = self.operando.getTipo(traductor, entorno)
            resultado = ""
            if tipo != "error":
                traer = "t"+str(traductor.getContador())+" = stack[int("+str(op)+")];//Traemos la variable\n"
                resultado = "t"+str(traductor.getContador())
                traductor.addCodigo(traer)
                traductor.IncrementarContador()
                op=[resultado, tipo]
            else:
                return "error"
        if self.operador == OperadorNativo.LOWERCASE:
            if op[1] != TipoObjeto.CADENA:
                return "error"
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
            return resultado
        if self.operador == OperadorNativo.UPPERCASE:
            if op[1] != TipoObjeto.CADENA:
                return "error"
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
            return resultado

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