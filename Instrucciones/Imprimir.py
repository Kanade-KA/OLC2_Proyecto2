from Expresiones.Constante import Constante
from Expresiones.Identificador import Identificador
from Expresiones.Struct import Struct
from Expresiones.Arreglo3D import Arreglo3D
from Expresiones.Arreglo2D import Arreglo2D
from Expresiones.Arreglo import Arreglo
from Abstract.Objeto import TipoObjeto
from Abstract.NodoAST import NodoAST

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
                traductor.putStringHeap(cad)
                traductor.addCodigo("imprimir();\n")
            if isinstance(ins, Identificador):
                puntero = ins.traducir(traductor, entorno)
                print("----------")
                print(puntero)
                contadortemp = traductor.getContador()
                cadena = "t"+ str(traductor.getContador())+" = S//Para guardar el puntero Stack en donde va\n"
                traductor.IncrementarContador()
                cadena += "S = "+str(puntero)+"\n"
                traductor.addCodigo(cadena)
                traductor.addCodigo("imprimir();\n")
                regreso = "S = t"+str(contadortemp)+";\n"
                traductor.addCodigo(regreso)
                
                
        #if self.essalto != 'F':
            #x+="\n"
        #-------------------METER EL X EN EL HEAP
        
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