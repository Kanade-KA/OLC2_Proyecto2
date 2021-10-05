from Expresiones.Arreglo3D import Arreglo3D
from Expresiones.Arreglo2D import Arreglo2D
from Expresiones.Constante import Constante
from Expresiones.Identificador import Identificador
from TablaSimbolo.Simbolo import Simbolo
from Expresiones.Arreglo import Arreglo
from TablaSimbolo.Error import Error

from Abstract.NodoAST import NodoAST

class LlamaMatriz3D(NodoAST):
    def __init__(self, identificador, indice, subindice, subsubindice, fila, columna):
        self.id = identificador
        self.indice = indice
        self.subindice = subindice
        self.subsubind = subsubindice
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, table):
        print("-------ESTOY EN LLAMAMATRIZ3D----------")
        simbolo = table.retornarSimbolo(self.id)
        arreglo3d = simbolo.getValor()
        if isinstance(arreglo3d, Arreglo3D):
            primerosdatos = arreglo3d.getDatos()
            segundosdatos = primerosdatos[self.indice.interpretar(arbol, table)-1]
            tercerdato = segundosdatos[self.subindice.interpretar(arbol, table)-1]
            dato = tercerdato[self.subsubind.interpretar(arbol, table) -1]
            return dato.interpretar(arbol, table)
        else:
            arbol.addExcepcion(Error("Semántico", "No es de tipo multidimensional"), t.lineno(1), t.lexpos(1))
            return
