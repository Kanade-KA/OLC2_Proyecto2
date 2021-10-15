from Expresiones.Constante import Constante
from Expresiones.Identificador import Identificador
from Expresiones.Struct import Struct
from Expresiones.Arreglo3D import Arreglo3D
from Expresiones.Arreglo2D import Arreglo2D
from Expresiones.Arreglo import Arreglo
from Abstract.Objeto import TipoObjeto
from Abstract.NodoAST import NodoAST
from Expresiones.Aritmetica import Aritmetica

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
        for ins in self.expresion:
            if isinstance(ins, Constante):
                cad = str(ins.traducir(traductor, entorno))
                heap = traductor.putStringHeap(cad)
                #TENGO QUE TENER UN TEMPORAL QUE ME LLEVE UNA POSICIÓN MAS DEL STACK
                cadena = "t"+str(traductor.getContador())+" = S + 1;//Se envía en S + 1 donde se guardará el parametro\n"
                #TENGO QUE EXTRAER EL PUNTERO DEL HEAP Y METERLO AL STACK
                cadena += "stack[int(t"+str(traductor.getContador())+")] = "+str(heap)+";//Se extrae el puntero del Heap\n"
                traductor.IncrementarContador()
                cadena += "imprimir();\n"
                traductor.addCodigo(cadena)
            if isinstance(ins, Identificador):
                tipo = ins.getTipo(entorno)
                if tipo == "int":
                    puntero = ins.traducir(traductor, entorno)#Nos da el puntero del Identificador
                    cadena = "t"+str(traductor.getContador())+" = stack[int("+str(puntero)+")]//Extraigo el valor y ese lo imprimo\n"
                    cadena += "fmt.Printf(\"%d\", int(t"+str(traductor.getContador())+"))\n"
                    traductor.IncrementarContador()
                    traductor.addCodigo(cadena)
                elif tipo == "doble":
                    puntero = ins.traducir(traductor, entorno)#Nos da el puntero del Identificador
                    cadena = "t"+str(traductor.getContador())+" = stack[int("+str(puntero)+")]//Extraigo el valor y ese lo imprimo\n"
                    cadena += "fmt.Printf(\"%f\", t"+str(traductor.getContador())+")\n"
                    traductor.IncrementarContador()
                    traductor.addCodigo(cadena)
                else:
                    puntero = ins.traducir(traductor, entorno)#Nos da el puntero del Identificador
                    contadortemp = traductor.getContador()#Contador que guarda la posición del stack para volver despues de ir a buscar la variable
                    cadena = "t"+ str(contadortemp)+" = S//Para guardar el puntero Stack en donde va\n"
                    traductor.IncrementarContador()
                    cadena += "S = "+str(puntero - 1 ) +"//Nos posicionamos en la posición donde está el identificador\n"
                    traductor.addCodigo(cadena)#Agregamos esto antes del imprimir
                    traductor.addCodigo("imprimir();\n")
                    regreso = "S = t"+str(contadortemp)+";//aquí devolvemos el puntero a su posición inicial\n"
                    traductor.addCodigo(regreso)
                    traductor.IncrementarContador()
            #Aquí si viene una operacion aritmetica
            if isinstance(ins, Aritmetica):
                traductor.addCodigo("hay aritmetica")
        if self.essalto != 'F':
            traductor.addCodigo("fmt.Printf(\"%c\", 10);\n")
        #traductor.addCodigo("imprimir();\n")
        if not traductor.hayPrint():
            cadena = "func imprimir(){\n"
            cadena += "t"+str(traductor.getContador()) +" = S + 1//Posicionamos en parametro\n"
            traductor.IncrementarContador()
            cadena += "t"+str(traductor.getContador()) + " = stack[int(t"+str(traductor.getContador()-1)+")]\n"
            traductor.IncrementarContador()
            cadena += "L1:\n"
            cadena += "t"+str(traductor.getContador())+" = heap[int(t"+str(traductor.getContador()-1)+")]\n" 
            cadena += "if t"+str(traductor.getContador())+" == -1 {goto L0}\n"
            cadena += "{ asciiValue := int(t"+str(traductor.getContador())+")\n"
            cadena += "character := rune(asciiValue)\n"
            cadena += "fmt.Printf(\"%c\",character)\n"
            cadena += "t"+str(traductor.getContador()-1)+" = t"+str(traductor.getContador()-1)+" + 1\n"
            cadena += "goto L1}\n"
            cadena += "L0:\nreturn\n}"
            traductor.IncrementarContador()
            traductor.addFuncion(cadena)
            traductor.activarPrint()
        return