from Expresiones.Struct import Struct
from Expresiones.Identificador import Identificador
from TablaSimbolo.Simbolo import Simbolo
from Instrucciones.Funciones import Funcion
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Error import Error
from TablaSimbolo.TS import TablaSimbolos
from Instrucciones.Break import Break


class Retornar(NodoAST):
    def __init__(self, nombre, parametros, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.fila = fila
        self.columna = columna
    
    def interpretar(self, arbol, table):
        x = table.retornarSimbolo(self.nombre.lower())#Retorna el simbolo
        if isinstance(x.getValor(), Funcion):
            funcion = x.getValor()#Extraigo el objeto de tipo funcion
            if funcion.getParametros() == None:
                nuevoentorno = TablaSimbolos(table)
                return funcion.interpretar(arbol, nuevoentorno)
            else:
                listaparametros = funcion.getParametros()
                if self.parametros == None:#self parametros son los valores
                    arbol.addExcepcion(Error("Semantico", "Error, faltan parametros", self.fila, self.columna))
                else:
                    nuevoentorno = TablaSimbolos(table)
                    listavalores = self.parametros
                    if len(listaparametros) == len (listavalores):
                        for i in range(0,len(listaparametros)):
                            identificador = listaparametros[i].getIdentificador()
                            valor = listavalores[i].interpretar(arbol, table)
                            simbolo = Simbolo(identificador, valor, "id", self.fila, self.columna)
                            nuevoentorno.tabla[identificador.lower()] = simbolo
                        return funcion.interpretar(arbol,nuevoentorno)   
                    else: 
                        arbol.addExcepcion(Error("Semantico", "Error, faltan parametros", self.fila, self.columna))
        if isinstance(x.getValor(), Struct):
            #SACO EL STRUCT PARA VER LA ESTRUCTURA 
            struct = x.getValor()
            datos = struct.getDatos()
            ism = struct.getMutable()
            listatmp = []
            contador = 0
            #Se crea un nuevo struct
            if len(datos) == len(self.parametros):
                for cte in datos:
                    simbolo = Simbolo(cte, self.parametros[contador], "any", self.fila, self.columna)
                    listatmp.append(simbolo)
                    contador = contador + 1
                newstruct = Struct(self.nombre, listatmp, ism, self.fila, self.columna)
                return newstruct
            else:
                arbol.addExcepcion(Error("Semantico", "Faltan propiedades en el struct", self.fila, self.columna))
            return