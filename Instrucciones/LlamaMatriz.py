from Abstract.Objeto import TipoObjeto
from Expresiones.Arreglo import Arreglo
from Expresiones.Identificador import Identificador
from TablaSimbolo.Error import Error

from Abstract.NodoAST import NodoAST
from TablaSimbolo.Simbolo import Simbolo

class LlamaMatriz(NodoAST):
    def __init__(self, identificador, expresion, fila, columna):
        self.identificador = identificador
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        posicion = self.expresion.interpretar(arbol, entorno)
        x = entorno.retornarSimbolo(self.identificador.lower())
        simbolo = x.getValor()
        if isinstance(simbolo, Arreglo):
            arreglo = simbolo.getDatos()
            if posicion > len(arreglo):
                arbol.addExcepcion(Error("Semantico", "Error el indice pasa los limites de la matriz", self.fila, self.columna))
            else:
                elemento = arreglo[posicion-1]
                resultado = elemento.interpretar(arbol, entorno)
                return resultado
        else:
            arbol.addExcepcion(Error("Semantico", "La variable no es de tipo arreglo", self.fila, self.columna))
        return
    
    def graficar(self, nodo):
        padre = nodo.getContador()
        nodo.newLabel("LLAMADA MATRIZ")
        nodo.IncrementarContador()

        hijo = nodo.getContador()
        nodo.newLabel(self.identificador)
        nodo.IncrementarContador()
        nodo.newEdge(padre, hijo)

        hijo = nodo.getContador()
        nodo.newLabel("[")
        nodo.IncrementarContador()
        nodo.newEdge(padre, hijo)

        hijo = self.expresion.graficar(nodo)
        nodo.newEdge(padre, hijo)

        hijo = nodo.getContador()
        nodo.newLabel("]")
        nodo.IncrementarContador()
        nodo.newEdge(padre, hijo)

        return padre

    def traducir(self, traductor, entorno):
        traductor.addCodigo("//----LLAMANDO ELEMENTO DE MATRIZ-------\n")
        indice = self.expresion.traducir(traductor, entorno)
        simbolo = entorno.retornarSimbolo(self.identificador.lower())
        if isinstance(simbolo, Simbolo):
            arreglo = simbolo.getValor()
            if isinstance(arreglo, Arreglo):
                tamanio = "t"+str(traductor.getContador())
                traductor.IncrementarContador()
                stack = "t"+str(traductor.getContador())
                traductor.IncrementarContador()
                ind = "t"+str(traductor.getContador())
                traductor.IncrementarContador()
                val = "t"+str(traductor.getContador())
                traductor.IncrementarContador()
                pos = "t"+str(traductor.getContador())
                traductor.IncrementarContador()
                tmp = "t"+str(traductor.getContador())
                traductor.IncrementarContador()
                rechaza = "L"+str(traductor.getGotos())
                salida = "L"+str(traductor.getGotos()+1)
                traductor.IncrementarGotos(2)

                cadena = tmp +" = S + "+str(simbolo.getPosicion())+";\n"
                cadena += stack + " = stack[int("+tmp+")];\n"
                cadena += tamanio + " = heap[int("+stack+")];\n"
                cadena += ind + " = "+str(indice[0])+";\n"
                cadena += "if "+ind+" > "+tamanio+" { goto "+rechaza+"; }\n"
                cadena += pos +" = "+ stack + " + "+ ind+ ";\n"
                cadena += val + " = heap[int("+pos+")];\n"
                cadena += "goto "+salida+";\n"
                cadena += rechaza+":\n"
                cadena += "fmt.Printf(\"%s\", \"Se ha excedido el limite de la matriz\");\n"
                cadena += val +"= -1;\n"
                cadena += salida+":\n"
                traductor.ActivarFMT()
                traductor.addCodigo(cadena)
                return [val, TipoObjeto.ENTERO]                
            else:
                traductor.addExcepcion(Error("Semantico", "El identificador no es de tipo Matriz", self.fila, self.columna))
        return 