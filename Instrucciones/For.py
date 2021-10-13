from Abstract.Objeto import TipoObjeto
from TablaSimbolo.Entorno import Entorno
from Expresiones.Identificador import Identificador
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Simbolo import Simbolo
from TablaSimbolo.Error import Error
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
from Instrucciones.Return import Return
class For(NodoAST):
    def __init__(self, indice, inicio, fin, instrucciones, fila, columna):
        self.indice = indice
        self.inicio = inicio
        self.fin = fin
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        #Hay que ver que el identificador sea identificador :v 
        if isinstance(self.indice, Identificador):
            ind = self.indice.getIdentificador()    
            simbolo = Simbolo(entorno.getNombre(), ind, "", "", "Variable", 0, self.fila, self.columna)
            entorno.addSimbolo(simbolo)
            if self.fin != None:#quiere decir que traía 2 puntos
                inicio = self.inicio.interpretar(arbol, entorno)
                fin = self.fin.interpretar(arbol, entorno)
                if not isinstance(inicio, str) or not isinstance(fin, str):
                    if not fin < inicio:
                        #NUEVO ENTORNO
                        if isinstance(inicio, int) and isinstance(fin, int):
                                nuevoentorno = Entorno("For", entorno)
                                for i in range(inicio, fin +1):
                                    #Hay que actualizar la variable
                                    simbolo = Simbolo(entorno.getNombre(), ind, i,"", "Variable", 0, self.fila, self.columna)
                                    
                                    entorno.tabla[ind] = simbolo
                                    for instrucciones in self.instrucciones:
                                        y = instrucciones.interpretar(arbol, nuevoentorno)
                                        if y != None and y!="":
                                            return y
                                        if isinstance(y, Return):
                                            return y
                                        if isinstance(y, Break):
                                            return None
                                        if isinstance(y, Continue):
                                            break
                            
                        else:
                            nuevoentorno = Entorno("For", entorno)
                            iniciofloat = 0
                            if isinstance(fin, float):
                                #Parsear el inicio
                                iniciofloat = float(inicio)
                            while(True):
                                if(iniciofloat > fin):
                                    break
                                #Hay que actualizar la variable
                                simbolo = Simbolo(entorno.getNombre(), ind, iniciofloat, "", "Variable", 0, self.fila, self.columna)
                                
                                entorno.tabla[ind] = simbolo
                                for instrucciones in self.instrucciones:
                                    y = instrucciones.interpretar(arbol, nuevoentorno)
                                    if y != None and y!="":
                                        return y
                                    if isinstance(y, Return):
                                        arbol.addExcepcion(Error("Semántico", "No se puede usar el Return con un Loop", self.fila, self.columna))
                                    if isinstance(y, Break):
                                        return None
                                    if isinstance(y, Continue):
                                        break
                                iniciofloat = iniciofloat + 1.0
                            return None
                    else:
                            arbol.addExcepcion(Error("Semantico", "No se puede iterar, el numero final es menor al inicial", self.fila, self.columna))
                else:
                        arbol.addExcepcion(Error("Semantico", "No se puede iterar Con cadenas en un intervalo", self.fila, self.columna))
            else:#Quiere decir que solo viene una cadena
                iterador = self.inicio.interpretar(arbol, entorno)
                if isinstance(iterador, str):
                    nuevoentorno = Entorno("For",entorno)
                    for i in iterador:
                        #Hay que actualizar la variable
                        simbolo = Simbolo(entorno.getNombre(), ind, i, "", "Variable", 0, self.fila, self.columna)
                        
                        entorno.tabla[ind] = simbolo
                        for instrucciones in self.instrucciones:
                            y = instrucciones.interpretar(arbol, nuevoentorno)
                            if y != None and y!="":
                                return y
                            if isinstance(y, Return):
                                arbol.addExcepcion(Error("Semántico", "No se puede usar el Return con un Loop", self.fila, self.columna))
                            if isinstance(y, Break):
                                return None
                            if isinstance(y, Continue):
                                break
                else:#o un numero
                    nuevoentorno = Entorno("For", entorno)
                    simbolo = Simbolo(entorno.getNombre(), ind, iterador, "", "Variable", 0, self.fila, self.columna)
                    
                    entorno.tabla[ind] = simbolo#no estoy segura de si es entorno o tabla normal
                    for instrucciones in self.instrucciones:
                            y = instrucciones.interpretar(arbol, nuevoentorno)
                            if y != None and y!="":
                                return y
                            if isinstance(y, Return):
                                arbol.addExcepcion(Error("Semántico", "No se puede usar el Return con un Loop", self.fila, self.columna))
                            if isinstance(y, Break):
                                return ""
                            if isinstance(y, Continue):
                                break

        return None

    def traducir(self, traductor, entorno):
        return "For"