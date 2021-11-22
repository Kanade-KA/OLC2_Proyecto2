from Expresiones.Arreglo2D import Arreglo2D
from Expresiones.Constante import Constante
from Expresiones.Identificador import Identificador
from TablaSimbolo.Simbolo import Simbolo
from Expresiones.Arreglo import Arreglo
from TablaSimbolo.Error import Error

from Abstract.NodoAST import NodoAST

class AsignaMatriz2D(NodoAST):
    def __init__(self, identificador, indice, subindice, expresion, fila, columna):
        self.id = identificador
        self.indice = indice
        self.subindice = subindice
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
        if isinstance(arreglo, Arreglo2D):
            #Traer el indice
            ind = self.indice.interpretar(arbol, entorno)
            sub = self.subindice.interpretar(arbol, entorno)
            if isinstance(self.expresion, Identificador):
                simbolo =  entorno.retornarSimbolo(self.expresion.getIdentificador())
                valor = simbolo.getValor()
                exp = Constante(valor, self.fila, self.columna)
                arreglo.setearDato(ind-1, sub-1, exp)
            else:
                valor =  self.expresion.interpretar(arbol, entorno)
                exp = Constante(valor, self.fila, self.columna)
                arreglo.setearDato(ind-1, sub-1, exp)
        else:
            arbol.addExcepcion(Error("Semántico", "Error variable no es de tipo Matriz", self.fila, self.columna))
        return

    def graficar(self, nodo):
        nodo += "Asingacion\n"
        return
    
    def traducir(self, traductor, entorno):
        return "Asignacion Matriz 2D"