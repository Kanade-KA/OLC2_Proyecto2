from Expresiones.Arreglo3D import Arreglo3D
from Expresiones.Arreglo2D import Arreglo2D
from Expresiones.Constante import Constante
from Expresiones.Identificador import Identificador
from TablaSimbolo.Simbolo import Simbolo
from Expresiones.Arreglo import Arreglo
from TablaSimbolo.Error import Error

from Abstract.NodoAST import NodoAST

class AsignaMatriz3D(NodoAST):
    def __init__(self, identificador, indice, subindice, subsub, expresion, fila, columna):
        self.id = identificador
        self.indice = indice
        self.subindice = subindice
        self.subsub = subsub
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
        if isinstance(arreglo, Arreglo3D):
            #Traer el indice
            ind = self.indice.interpretar(arbol, entorno)
            sub = self.subindice.interpretar(arbol, entorno)
            subsub = self.subsub.interpretar(arbol, entorno)
            if isinstance(self.expresion, Identificador):
                simbolo =  entorno.retornarSimbolo(self.expresion.getIdentificador())
                valor = simbolo.getValor()
                exp = Constante(valor, self.fila, self.columna)
                arreglo.setearDato(ind-1, sub-1, subsub-1, exp)
            else:
                valor =  self.expresion.interpretar(arbol, entorno)
                exp = Constante(valor, self.fila, self.columna)
                arreglo.setearDato(ind-1, sub-1, subsub-1, exp)
        else:
            arbol.addExcepcion(Error("Semántico", "Error variable no es de tipo Matriz Multidimensional", self.fila, self.columna))
        
        return

    def graficar(self, graf, nodo):
        graf += "Asingacion\n"
        return
    
    def traducir(self, traductor, entorno):
        return "Asignacion Matriz 3D"