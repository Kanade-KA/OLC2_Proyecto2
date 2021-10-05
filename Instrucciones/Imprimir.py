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

    def interpretar(self, arbol, table):
        if self.expresion != None:
            for exp in self.expresion:
                x = exp.interpretar(arbol, table)
                if x != None:
                    if isinstance(x, Arreglo):
                        y = x.retornarArray(arbol, table)
                        arbol.AgregaraConsola(y)
                        return
                    if isinstance(x, Arreglo2D):
                        y = x.retornarArray(arbol,table)
                        arbol.AgregaraConsola(y)
                        return
                    if isinstance(x, Arreglo3D):
                        y = x.retornarArray(arbol, table)
                        arbol.AgregaraConsola(y)
                        return
                    if isinstance(x, Struct):
                        y = x.imprimirStruct(arbol, table)
                        arbol.AgregaraConsola(y)
                    else:
                        arbol.AgregaraConsola(str(x))
        if(self.essalto!='F'):
            arbol.AgregaraConsola("\n")
        return
