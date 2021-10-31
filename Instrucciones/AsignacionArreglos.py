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

    def traducir(self, traductor, entorno):
        arreglo = self.expresion
        if isinstance(arreglo, Arreglo):
            traductor.addCodigo("//******************ASIGNACION MATRIZ*********************\n")
            datos = arreglo.getDatos()
            tam = len(datos)
            stacklibre = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            heap = "t"+str(traductor.getContador())
            traductor.IncrementarContador()

            cadena = heap +" = H;\n"
            cadena += "heap[int(H)] = "+str(tam)+";\n"
            cadena += "H = H + 1;\n"
            traductor.IncrementarHeap()
            #Agregando datos al stack
            
        return "Asignacion Arreglos"