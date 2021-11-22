from Abstract.Objeto import TipoObjeto
from Instrucciones.LlamaMatriz2D import LlamaMatriz2D
from Expresiones.Arreglo2D import Arreglo2D
from TablaSimbolo.Error import Error
from Expresiones.Arreglo import Arreglo
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Tipo import OperadorNativo
from Expresiones.Constante import Constante
from Instrucciones.LlamaMatriz import LlamaMatriz
import math

class Parse(NodoAST):
    def __init__(self, tipo, expresion, fila, columna):
        self.operador = tipo
        self.operando=expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, table):
        op = self.operando.interpretar(arbol, table)
        if isinstance(op, int):
            return "Int64"
        if isinstance(op, float):
            return "Float64"
        if isinstance(op, str):
            return "String"
        if isinstance(op, bool):
            return "Booleano"

    def graficar(self, graf, nodo):
        graf += "Asingacion\n"
        return

    def traducir(self, traductor, entorno):
        resultado = self.operando.traducir(traductor, entorno)
        if resultado[1] != TipoObjeto.CADENA:
            traductor.addExcepcion(Error("Semantico", "Parse, solo acepta tipo String", self.fila, self.columna))
            return "error"
        traductor.addCodigo("//**************************CASO PARSE**************************\n")
        if self.operador.lower() == "int64":
            cadena = "t"+str(traductor.getContador())+" = S + "+str(traductor.getStack())+";\n"
            cadena += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador())+" + 1;//Para ingresar el parametro\n"
            cadena += "stack[int(t"+str(traductor.getContador())+")] = "+str(resultado[0])+";\n"
            cadena += "S = S + "+str(traductor.getStack())+";\n"
            cadena += "parseint();\n"
            traductor.IncrementarContador()
            resultado = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            cadena += resultado +" = stack[int(S)];\n"
            cadena += "S = S - "+str(traductor.getStack())+";\n"
            traductor.addCodigo(cadena)
            self.parseint(traductor)
            return [resultado, TipoObjeto.ENTERO]
        if self.operador.lower() == "float64":
            cadena = "t"+str(traductor.getContador())+" = S + "+str(traductor.getStack())+";\n"
            cadena += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador())+" + 1;//Para ingresar el parametro\n"
            cadena += "stack[int(t"+str(traductor.getContador())+")] = "+str(resultado[0])+";\n"
            cadena += "S = S + "+str(traductor.getStack())+";\n"
            cadena += "parsedoble();\n"
            traductor.IncrementarContador()
            resultado = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            cadena += resultado +" = stack[int(S)];\n"
            cadena += "S = S - "+str(traductor.getStack())+";\n"
            traductor.addCodigo(cadena)
            self.parsedoble(traductor)
            return [resultado, TipoObjeto.DECIMAL]

    def parseint(self, traductor):
        if not traductor.hayParseInt():
            unidades = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            suma = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            heap = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            numero = "t"+str(traductor.getContador())
            traductor.IncrementarContador()

            inicio = "L0"
            posicionar = "L1"
            revision = "L2"
            retroceder = "L3"
            fin = "L4"
            ultimo = "L5" 
            cadena = "func parseint(){\n"
            cadena += suma +" = 0;\n"
            cadena += unidades +" = 1;\n"
            cadena += "t"+str(traductor.getContador())+" = S + 1;//Para posicionarnos en el heap donde está la cadena\n"
            cadena += heap + " = stack[int(t"+str(traductor.getContador())+")];\n"
            traductor.IncrementarContador()
            cadena += inicio+":\n"
            cadena += numero +" = heap[int("+str(heap)+")];\n"
            cadena += "if "+numero+" == -1 { goto "+posicionar+"; }//Esto es para ver si ya llegó al final de esa cadena\n"
            cadena += heap +" = "+heap +" + 1;\n"
            cadena += "goto "+inicio+";\n"
            cadena += posicionar+":\n"
            cadena += heap +" = "+heap +" - 1;\n"
            cadena += "goto "+revision+";\n"
            cadena += retroceder+":\n"
            cadena += "t"+str(traductor.getContador())+" = "+numero+";\n"
            cadena += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador()) +" - 48;\n"
            cadena += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador()) +" * "+ unidades+";\n"
            cadena += unidades +" = "+unidades +" * 10;\n"
            cadena += suma +" = "+suma+" + t"+str(traductor.getContador())+";\n"
            traductor.IncrementarContador()
            cadena += heap +" = "+heap +" - 1;\n"
            cadena += revision+":\n"
            cadena += numero +" = heap[int("+heap+")];\n"
            cadena += "if "+heap+" == 0 { goto "+ultimo+"; }\n"
            cadena += "if "+numero+" == -1 { goto "+fin+"; }\n"
            cadena += "goto "+retroceder+";\n"
            cadena += ultimo+":\n"
            cadena += "t"+str(traductor.getContador())+" = "+numero+";\n"
            cadena += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador()) +" - 48;\n"
            cadena += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador()) +" * "+ unidades+";\n"
            cadena += suma +" = "+suma+" + t"+str(traductor.getContador())+";\n"
            traductor.IncrementarContador()
            cadena += fin +":\n"
            cadena += "stack[int(S)] = "+suma+";\n"
            cadena += "return;\n}\n\n"
            traductor.addFuncion(cadena)
            traductor.activarParseInt()
        return

    def parsedoble(self, traductor):
        if not traductor.hayParseDoble():
            unidades = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            suma = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            heap = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            numero = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            posicion = "t"+str(traductor.getContador())
            traductor.IncrementarContador()

            inicio = "L1"
            revision = "L2"
            fin = "L3"
            ultimo = "L4" 
            punto = "L5"
            decimal = "L6"
            entero = "L7"

            cadena = "func parsedoble(){\n"
            cadena += suma +" = 0;\n"
            cadena += unidades +" = 10;\n"
            cadena += "t"+str(traductor.getContador())+" = S + 1;\n"
            cadena += heap + " = stack[int(t"+str(traductor.getContador())+")];\n"
            traductor.IncrementarContador()
            #PRIMERO HAY QUE LLEGAR HASTA EL PUNTO
            cadena += inicio+"://HACE QUE SE VAYA HASTA EL PUNTO\n"
            cadena += numero +" = heap[int("+heap+")];\n"
            cadena += "if "+numero+" == -1 { goto "+fin+"; }\n"
            cadena += "if "+numero+" == 46 { goto "+punto+"; }\n"
            cadena += heap +" = "+heap +" + 1;\n"
            cadena += "goto "+inicio+";\n"
            cadena += punto+"://ES POR QUE ENCONTRÓ EL PUNTO\n"
            cadena += posicion+" = "+heap+";\n"
            cadena += heap +" = "+heap +" + 1;\n"
            cadena += decimal+"://RECORRE EL DECIMAL HASTA QUE ENCUENTRA EL -1 EN EL HEAP\n"
            cadena += numero +" = heap[int("+heap+")];\n"
            cadena += "if "+numero+" == -1 { goto "+entero+"; }\n"
            cadena += "t"+str(traductor.getContador())+" = "+numero+";\n"
            cadena += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador()) +" - 48;\n"
            cadena += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador()) +" / "+ unidades+";\n"
            cadena += unidades +" = "+unidades +" * 10;\n"
            cadena += suma +" = "+suma+" + t"+str(traductor.getContador())+";\n"
            traductor.IncrementarContador()
            cadena += heap +" = "+heap +" + 1;\n"
            cadena += "goto "+decimal+";\n"
            cadena += entero+"://TERMINÓ LA PARTE DECIMAL Y REGRESA A LA PARTE ENTERA\n"
            cadena += heap +" = "+posicion +";\n"
            cadena += unidades + " = 1;\n"
            cadena += heap +" = "+heap +" - 1;\n"
            cadena += revision+"://RECORRE LA PARTE ENTERA HASTA QUE ENCUENTRE EL -1 O EL CERO\n"
            cadena += numero +" = heap[int("+heap+")];\n"
            cadena += "if "+heap+" == 0 { goto "+ultimo+"; }\n"
            cadena += "if "+numero+" == -1 { goto "+fin+"; }\n"
            cadena += "t"+str(traductor.getContador())+" = "+numero+";\n"
            cadena += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador()) +" - 48;\n"
            cadena += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador()) +" * "+ unidades+";\n"
            cadena += unidades +" = "+unidades +" * 10;\n"
            cadena += suma +" = "+suma+" + t"+str(traductor.getContador())+";\n"
            traductor.IncrementarContador()
            cadena += heap +" = "+heap +" - 1;\n"
            cadena += "goto "+revision+";\n"
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
            traductor.activarParseDoble()
        return