from Expresiones.Constante import Constante
from Expresiones.Identificador import Identificador
from Expresiones.Logica import Logica
from Expresiones.Nativas import Nativas
from Expresiones.Parse import Parse
from Expresiones.Relacional import Relacional
from Expresiones.Struct import Struct
from Expresiones.Arreglo3D import Arreglo3D
from Expresiones.Arreglo2D import Arreglo2D
from Expresiones.Arreglo import Arreglo
from Abstract.Objeto import TipoObjeto
from Abstract.NodoAST import NodoAST
from Expresiones.Aritmetica import Aritmetica
from TablaSimbolo.Traductor import Traductor

class Imprimir(NodoAST):
    def __init__(self, expresion, esln, fila, columna):
        self.expresion = expresion
        self.essalto = esln
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        if self.expresion != None:
            for exp in self.expresion:
                x = exp.interpretar(arbol, entorno)
                if x != None:
                    if isinstance(x, Arreglo):
                        y = x.retornarArray(arbol, entorno)
                        arbol.AgregaraConsola(y)
                        return
                    if isinstance(x, Arreglo2D):
                        y = x.retornarArray(arbol, entorno)
                        arbol.AgregaraConsola(y)
                        return
                    if isinstance(x, Arreglo3D):
                        y = x.retornarArray(arbol, entorno)
                        arbol.AgregaraConsola(y)
                        return
                    if isinstance(x, Struct):
                        y = x.imprimirStruct(arbol, entorno)
                        arbol.AgregaraConsola(y)
                    else:
                        arbol.AgregaraConsola(str(x))
        if(self.essalto!='F'):
            arbol.AgregaraConsola("\n")
        return

    def traducir(self, traductor, entorno):
        traductor.addCodigo("//**************************IMPRIMIR**************************\n")
        for ins in self.expresion:
            print(type(ins))
            if isinstance(ins, Constante):
                constante = ins.traducir(traductor, entorno)
                if constante != "error":
                    tipo=constante[1]
                    if tipo == TipoObjeto.ENTERO:
                        self.ImprimirInt(traductor, constante[0])
                    elif tipo == TipoObjeto.DECIMAL:
                        self.ImprimirDoble(traductor, constante[0])
                    elif tipo == TipoObjeto.BOOLEANO:
                        valor = 0
                        if constante[0]: valor=1
                        self.ImprimirBooleano(traductor, valor)
                    else:#Es por que es string
                        self.ImprimirString(traductor, constante[0])
            if isinstance(ins, Identificador):
                tipo = ins.getTipo(traductor, entorno)
                if tipo != "error":
                    if tipo == TipoObjeto.ENTERO:
                        puntero = ins.traducir(traductor, entorno)#Nos da el puntero del Identificador
                        valor = traductor.ExtraerVariable(traductor, puntero)
                        self.ImprimirInt(traductor, valor)
                    elif tipo == TipoObjeto.DECIMAL:
                        puntero = ins.traducir(traductor, entorno)#Nos da el puntero del Identificador
                        valor = traductor.ExtraerVariable(traductor, puntero)
                        self.ImprimirDoble(traductor, valor)
                    elif tipo == TipoObjeto.BOOLEANO:
                        puntero = ins.traducir(traductor, entorno)
                        valor = traductor.ExtraerVariable(traductor, puntero)
                        self.ImprimirBooleano(traductor, valor)
                    else:
                        puntero = ins.traducir(traductor, entorno)
                        valor = traductor.ExtraerVariable(traductor, puntero)
                        self.ImprimirString(traductor, valor)
            if isinstance(ins, Aritmetica):
                resultado = ins.traducir(traductor, entorno)
                if resultado != "error":
                    if resultado[1] == TipoObjeto.ENTERO:
                        self.ImprimirInt(traductor, resultado[0])
                    elif resultado[1] == TipoObjeto.DECIMAL:
                        self.ImprimirDoble(traductor, resultado[0])
                    else:
                        self.ImprimirString(traductor, resultado[0])
            if isinstance(ins, Nativas):
                resultado = ins.traducir(traductor, entorno)
                if resultado[1] == TipoObjeto.CADENA:
                    self.ImprimirString(traductor, resultado[0])
                if resultado[1] == TipoObjeto.ENTERO:
                    self.ImprimirInt(traductor, resultado[0])
                if resultado[1] == TipoObjeto.DECIMAL:
                    self.ImprimirDoble(traductor, resultado[0])
            if isinstance(ins, Parse):
                resultado = ins.traducir(traductor, entorno)
                if resultado[1] == TipoObjeto.ENTERO:
                    self.ImprimirInt(traductor, resultado[0])
                elif resultado[1] == TipoObjeto.DECIMAL:
                    self.ImprimirDoble(traductor, resultado[0])
            if isinstance(ins, Relacional):
                res = ins.traducir(traductor, entorno)
                self.Condiciones(traductor, res[0], res[1])
            if isinstance(ins, Logica):
                res = ins.traducir(traductor, entorno)
                self.Condiciones(traductor, res[0], res[1])
        if self.essalto != 'F':
            traductor.addCodigo("fmt.Printf(\"%c\", 10);\n")
        return

    def AgregarMetodoImprimir(self, traductor):
        if not traductor.hayPrint():
            cadena = "func imprimir(){\n"
            cadena += "t"+str(traductor.getContador()) +" = S + 1;//Posicionamos en parametro\n"
            traductor.IncrementarContador()
            cadena += "t"+str(traductor.getContador()) + " = stack[int(t"+str(traductor.getContador()-1)+")];\n"
            traductor.IncrementarContador()
            cadena += "L1:\n"
            cadena += "t"+str(traductor.getContador())+" = heap[int(t"+str(traductor.getContador()-1)+")];\n" 
            cadena += "if t"+str(traductor.getContador())+" == -1 {goto L0;}\n"
            cadena += "fmt.Printf(\"%c\", int(t"+str(traductor.getContador())+"));\n"
            cadena += "t"+str(traductor.getContador()-1)+" = t"+str(traductor.getContador()-1)+" + 1;\n"
            cadena += "goto L1;\n"
            cadena += "L0:\nreturn;\n}\n\n"
            traductor.IncrementarContador()
            traductor.addFuncion(cadena)
            traductor.activarPrint()

    def ImprimirBooleano(self, traductor, valor):
        goto = traductor.getGotos()
        cadena = "if "+str(valor)+ " == 1 {goto L"+str(goto)+";}\n"
        cadena += "goto L"+str(goto + 1)+";\n"
        cadena += "L"+str(goto)+":\n"
        cadena += "fmt.Printf(\"%c\",116);\n" 
        cadena += "fmt.Printf(\"%c\",114);\n"
        cadena += "fmt.Printf(\"%c\",117);\n"
        cadena += "fmt.Printf(\"%c\",101);\n"
        cadena += "goto L"+str(goto + 2)+";\n"
        cadena += "L"+str(goto + 1)+": \n"
        cadena += "fmt.Printf(\"%c\",102);\n" 
        cadena += "fmt.Printf(\"%c\",97);\n"
        cadena += "fmt.Printf(\"%c\",108);\n"
        cadena += "fmt.Printf(\"%c\",115);\n"
        cadena += "fmt.Printf(\"%c\",101);\n"
        cadena += "L"+str(goto + 2)+": \n"
        traductor.addCodigo(cadena)
        traductor.IncrementarGotos(3)
        return

    def ImprimirInt(self, traductor, valor):
        cadena = "fmt.Printf(\"%d\", int("+str(valor)+"));\n"
        traductor.addCodigo(cadena)
        return

    def ImprimirDoble(self, traductor, valor):
        cadena = "fmt.Printf(\"%f\", "+str(valor)+");\n"
        traductor.addCodigo(cadena)
        return

    def Condiciones(self, traductor, acepta, rechaza):
        goto = traductor.getGotos()
        cadena =  str(acepta)+":\n"
        cadena += "fmt.Printf(\"%c\",116);\n" 
        cadena += "fmt.Printf(\"%c\",114);\n"
        cadena += "fmt.Printf(\"%c\",117);\n"
        cadena += "fmt.Printf(\"%c\",101);\n"
        cadena += "goto L"+str(goto)+";\n"
        cadena += str(rechaza)+": \n"
        cadena += "fmt.Printf(\"%c\",102);\n" 
        cadena += "fmt.Printf(\"%c\",97);\n"
        cadena += "fmt.Printf(\"%c\",108);\n"
        cadena += "fmt.Printf(\"%c\",115);\n"
        cadena += "fmt.Printf(\"%c\",101);\n"
        cadena += "L"+str(goto)+": \n"
        traductor.addCodigo(cadena)
        traductor.IncrementarGotos(1)

    def ImprimirString(self, traductor, valor):
        cadena = "t"+str(traductor.getContador())+" = S + "+str(traductor.getStack())+";//Ve un espacio libre en el stack\n"
        cadena += "t"+str(traductor.getContador())+" = t"+str(traductor.getContador()) +" + 1;//Para enviar el parametro\n"
        cadena += "stack[int(t"+str(traductor.getContador())+")] = "+str(valor)+";//Guarda el puntero del heap\n"
        cadena += "S = S + "+str(traductor.getStack())+";//Para llevar hasta ahí el puntero para que imprima\n"
        cadena += "imprimir();\n"
        cadena += "S = S - "+str(traductor.getStack())+";//Volvemos a posicionarnos en el stack donde se debe\n"
        traductor.IncrementarContador()
        traductor.addCodigo(cadena)
        self.AgregarMetodoImprimir(traductor)
