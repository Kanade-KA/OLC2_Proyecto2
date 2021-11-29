from Expresiones.Arreglo import Arreglo
from Instrucciones.LlamaMatriz import LlamaMatriz
from Instrucciones.Return import Return
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Simbolo import Simbolo
from TablaSimbolo.Error import Error
from Instrucciones.Retonar import Retornar
class AsignacionArreglo(NodoAST):
    def __init__(self, identificador, expresion, tipo, fila, columna):
        self.identificador = identificador
        self.expresion = expresion
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        simbolo = Simbolo(entorno.getNombre(), self.identificador, self.expresion, self.tipo, "Variable", 0, self.fila, self.columna)
        arbol.addSimbolo(simbolo)
        entorno.addSimbolo(simbolo)
        return

    def graficar(self, nodo):
        padre = nodo.getContador()
        nodo.newLabel("ASIGNACION")
        nodo.IncrementarContador()

        hijo = nodo.getContador()
        nodo.newLabel(self.identificador)
        nodo.IncrementarContador()
        nodo.newEdge(padre, hijo)

        hijo = nodo.getContador()
        nodo.newLabel("=")
        nodo.IncrementarContador()
        nodo.newEdge(padre, hijo)
        
        hijo = nodo.getContador()
        nodo.newLabel("[")
        nodo.IncrementarContador()
        nodo.newEdge(padre, hijo)
        
        for exp in self.expresion.getDatos():
            if type(exp) is list:
                hijo = nodo.getContador()
                nodo.newLabel("[")
                nodo.IncrementarContador()
                nodo.newEdge(padre, hijo)
                for exp2 in exp:
                    if type(exp2) is list:
                        hijo = nodo.getContador()
                        nodo.newLabel("[")
                        nodo.IncrementarContador()
                        nodo.newEdge(padre, hijo)
                        for exp3 in exp2:
                            hijo = exp3.graficar(nodo)
                            nodo.newEdge(padre, hijo)
                        hijo = nodo.getContador()
                        nodo.newLabel("\]")
                        nodo.IncrementarContador()
                        nodo.newEdge(padre, hijo)
                    else:
                        hijo = exp2.graficar(nodo)
                        nodo.newEdge(padre, hijo)
                hijo = nodo.getContador()
                nodo.newLabel("\]")
                nodo.IncrementarContador()
                nodo.newEdge(padre, hijo)
            else:
                hijo = exp.graficar(nodo)
                nodo.newEdge(padre, hijo)
        
        hijo = nodo.getContador()
        nodo.newLabel("\]")
        nodo.IncrementarContador()
        nodo.newEdge(padre, hijo)

        return padre

    def traducir(self, traductor, entorno):
        arreglo = self.expresion
        if isinstance(arreglo, Arreglo):
            traductor.addCodigo("//******************ASIGNACION MATRIZ*********************\n")
            datos = arreglo.getDatos()
            tam = len(datos)
            heap = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            
            simbolo = Simbolo(entorno.getNombre(), self.identificador, self.expresion, self.tipo, "Arreglo", traductor.getStack(), self.fila, self.columna)
            traductor.addSimbolo(simbolo)
            entorno.addSimbolo(simbolo)

            cadena = heap +" = H;\n"
            cadena += "heap[int(H)] = "+str(tam)+";\n"
            cadena += "H = H + 1;\n"
            traductor.IncrementarHeap()
            #Agregando datos al stack
            for dato in arreglo.getDatos():
                operado = dato.traducir(traductor, entorno)
                cadena += "heap[int(H)] = "+str(operado[0])+";\n"
                cadena += "H = H + 1;\n"
            
            cadena += "stack[int("+str(traductor.getStack())+")] = "+heap + ";\n"
            traductor.IncrementarStack()
            traductor.addCodigo(cadena)
        return