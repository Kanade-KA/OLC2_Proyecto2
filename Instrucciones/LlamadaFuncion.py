from Expresiones.Arreglo import Arreglo
from Expresiones.Identificador import Identificador
from TablaSimbolo.Simbolo import Simbolo
from Instrucciones.Funciones import Funcion
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Error import Error
from TablaSimbolo.Entorno import Entorno
from Instrucciones.Break import Break


class LlamadaFuncion(NodoAST):
    def __init__(self, nombre, parametros, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.fila = fila
        self.columna = columna
    
    def interpretar(self, arbol, entorno):
        x = entorno.retornarSimbolo(self.nombre.lower())#Retorna el simbolo donde guardo el objeto Funcion
        if isinstance(x, Simbolo):#PARA VER SI ES UN SIMBOLO CREO QUE NO ES NECESARIO
            if isinstance(x.getValor(), Funcion):#VER SI EL GETVALOR ES UNA FUNCION 
                funcion = x.getValor()#solo para tener mejor el objeto función
                if funcion.getParametros() == None:
                    nuevoentorno = Entorno(self.nombre, entorno)
                    funcion.interpretar(arbol,nuevoentorno)#en esta clase no me importa si trae return pues no se debe mostrar
                else:#Si entra acá quiere decir que si tenía parametros
                    listaparametros = funcion.getParametros() #Extraigo la lista de parametros de la funcion
                    if self.parametros == None:#si entra aca es por que no trae parametros y eso no lo acepta
                        arbol.addExcepcion(Error("Semantico", "Error, faltan parametros", self.fila, self.columna))
                    else:
                        nuevoentorno = Entorno(self.nombre, entorno)#creamos un nuevo entorno, aquí se guardaran las variables 
                        listavalores = self.parametros#los valores de la funcion (no ids)
                        if len(listaparametros) == len (listavalores):
                            for i in range(0,len(listaparametros)):
                                #AQUÍ SOLO SE ASIGNAN Y SE CREAN VALORES, SE METEN EN EL NUEVO ENTORNO Y SE TRABAJA DE ESTO
                                identificador = listaparametros[i].getIdentificador()
                                valor = listavalores[i].interpretar(arbol, entorno)
                                simbolo = Simbolo(entorno.getNombre(), identificador, valor, "id", self.fila, self.columna)
                                nuevoentorno.tabla[identificador.lower()] = simbolo
                                #nuevoentorno.Imprimir()
                            funcion.interpretar(arbol, nuevoentorno)
                            #AHORA TENGO QUE ACTUALIZAR DONDE LO LLAMARON ENTONCES :/ 
                            for i in listaparametros:
                                simbolo = nuevoentorno.retornarSimbolo(i.getIdentificador())
                                matriz = simbolo.getValor()
                                if isinstance(matriz, Arreglo):
                                    nuevosimbolo = Simbolo(entorno.getNombre(), i.getIdentificador(), matriz, "arreglo", self.fila, self.columna)
                                    entorno.addSimbolo(nuevosimbolo)
                            
                        else:
                            arbol.addExcepcion(Error("Semantico", "Error, faltan parametros", self.fila, self.columna))
            else:
                arbol.addExcepcion(Error("Semantico", "No es una función", self.fila, self.columna))
        return