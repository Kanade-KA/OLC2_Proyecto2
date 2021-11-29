from Expresiones.Constante import Constante
from Expresiones.Identificador import Identificador
from TablaSimbolo.Simbolo import Simbolo
from Expresiones.Arreglo import Arreglo
from TablaSimbolo.Error import Error

from Abstract.NodoAST import NodoAST

class AsignaMatriz(NodoAST):
    def __init__(self, identificador, indice, expresion, fila, columna):
        self.id = identificador
        self.indice = indice
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        #PRIMERO DEBO DE TRAER EL SIMBOLO DE ESE COSITO 
        #Buscar en la tabla
        simbolo = entorno.retornarSimbolo(self.id)
        #Traer el arreglo
        arreglo = simbolo.getValor()
        #Verificar si este simbolo si es un arreglo
        if isinstance(arreglo, Arreglo):
            #Traer la lista...
            datos = arreglo.getDatos()
            #Traer el indice
            ind = self.indice.interpretar(arbol, entorno)
            if ind <= len(datos) and ind > 0:
                if isinstance(self.expresion, Identificador):
                    simbolo =  entorno.retornarSimbolo(self.expresion.getIdentificador())
                    valor = simbolo.getValor()
                    exp = Constante(valor, self.fila, self.columna)
                    arreglo.setearDato(ind-1, exp)
                else:
                    valor =  self.expresion.interpretar(arbol, entorno)
                    exp = Constante(valor, self.fila, self.columna)
                    arreglo.setearDato(ind-1, exp)
            else:
                arbol.addExcepcion(Error("Semántico", "Error el indice se pasa del limite del arreglo", self.fila, self.columna))
        else:
            arbol.addExcepcion(Error("Semántico", "Error variable no es de tipo Matriz", self.fila, self.columna))
        
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
        nodo.newLabel("[")
        nodo.IncrementarContador()
        nodo.newEdge(padre, hijo)

        hijo = self.indice.graficar(nodo)
        nodo.newEdge(padre, hijo)

        hijo = nodo.getContador()
        nodo.newLabel("]")
        nodo.IncrementarContador()
        nodo.newEdge(padre, hijo)

        hijo = nodo.getContador()
        nodo.newLabel("=")
        nodo.IncrementarContador()
        nodo.newEdge(padre, hijo)

        hijo = self.expresion.graficar()
        nodo.newEdge(padre, hijo)

        return padre
    
    def traducir(self, traductor, entorno):
        traductor.addCodigo("//----LLAMANDO ELEMENTO DE MATRIZ-------\n")
        indice = self.indice.traducir(traductor, entorno)
        simbolo = entorno.retornarSimbolo(self.id.lower())
        valor = self.expresion.traducir(traductor, entorno)
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
                res = "t"+str(traductor.getContador())
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
                cadena += res +" = "+str(valor[0])+";\n"
                cadena += "heap[int("+pos+")] = "+res+";\n"
                cadena += "goto "+salida+";\n"
                cadena += rechaza+":\n"
                cadena += "fmt.Printf(\"%s\", \"Se ha excedido el limite de la matriz\");\n"
                cadena += val +"= -1;\n"
                cadena += salida+":\n"
                traductor.ActivarFMT()
                traductor.addCodigo(cadena)
                #return [val, TipoObjeto.ENTERO]                
            else:
                traductor.addExcepcion(Error("Semantico", "El identificador no es de tipo Matriz", self.fila, self.columna))
        return 