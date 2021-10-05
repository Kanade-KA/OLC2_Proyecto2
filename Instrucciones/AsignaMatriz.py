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

    def interpretar(self, arbol, table):
        #PRIMERO DEBO DE TRAER EL SIMBOLO DE ESE COSITO 
        #Buscar en la tabla
        simbolo = table.retornarSimbolo(self.id)
        #Traer el arreglo
        arreglo = simbolo.getValor()
        #Verificar si este simbolo si es un arreglo
        if isinstance(arreglo, Arreglo):
            #Traer la lista...
            datos = arreglo.getDatos()
            #Traer el indice
            ind = self.indice.interpretar(arbol, table)
            if ind <= len(datos) and ind > 0:
                if isinstance(self.expresion, Identificador):
                    simbolo =  table.retornarSimbolo(self.expresion.getIdentificador())
                    valor = simbolo.getValor()
                    exp = Constante(valor, self.fila, self.columna)
                    arreglo.setearDato(ind-1, exp)
                else:
                    valor =  self.expresion.interpretar(arbol, table)
                    exp = Constante(valor, self.fila, self.columna)
                    arreglo.setearDato(ind-1, exp)
            else:
                arbol.addExcepcion(Error("Semántico", "Error el indice se pasa del limite del arreglo", self.fila, self.columna))
        else:
            arbol.addExcepcion(Error("Semántico", "Error variable no es de tipo Matriz", self.fila, self.columna))
        
        return