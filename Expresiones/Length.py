from Abstract.Objeto import TipoObjeto
from Instrucciones.LlamaMatriz2D import LlamaMatriz2D
from Expresiones.Arreglo2D import Arreglo2D
from TablaSimbolo.Error import Error
from Expresiones.Arreglo import Arreglo
from Abstract.NodoAST import NodoAST
from Instrucciones.LlamaMatriz import LlamaMatriz

class Length(NodoAST):
    def __init__(self, matriz, fila, columna):
        self.operando=matriz
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        if isinstance(self.operando, LlamaMatriz):
            #Si entra aca es por que puede que sea una matriz que no sea de una dimension
            Matriz = self.operando
            iden = Matriz.identificador
            pos = Matriz.expresion.interpretar(arbol, entorno)
            simbolo = entorno.retornarSimbolo(iden)
            valorsimbolo = simbolo.getValor()
            if isinstance(valorsimbolo, Arreglo2D):
                sublista = valorsimbolo.getDatos()
                return int(len(sublista[pos -1]))
            else:
                arbol.addExcepcion(Error("SEMANTICO", "Error, no es de tipo matriz", self.fila, self.columna))
            return
        else:
            iden = self.operando.getIdentificador()
            simbolo = entorno.retornarSimbolo(iden)
            array = simbolo.getValor()
            if isinstance(array, Arreglo):
                datos = array.getDatos()
                return int(len(datos))
            if isinstance(array, Arreglo2D):
                datos = array.getDatos()
                return int(len(datos))
            else:
                arbol.addExcepcion(Error("SEMANTICO", "Error, no es de tipo matriz", self.fila, self.columna))
                return "nothing"

    def graficar(self, nodo):
        padre = nodo.getContador()
        nodo.newLabel("LENGTH")
        nodo.IncrementarContador()

        hijo = self.operando.graficar(nodo)
        nodo.newEdge(padre, hijo)
        
        return padre

    def traducir(self, traductor, entorno):
        iden = self.operando.getIdentificador()
        simbolo = entorno.retornarSimbolo(iden)
        array = simbolo.getValor()
        if isinstance(array, Arreglo):
            heap = traductor.ExtraerVariable(simbolo.getPosicion(), False)
            temporal = "t"+str(traductor.getContador())
            traductor.IncrementarContador()
            cadena = temporal +" = heap[int("+heap+")];\n"
            traductor.addCodigo(cadena)
            return [temporal, TipoObjeto.ENTERO]
        else:
            traductor.addExcepcion(Error("Semantico", "Error, no es de tipo matriz", self.fila, self.columna))
        
        