from Expresiones.Struct import Struct
from Expresiones.Identificador import Identificador
from TablaSimbolo.Simbolo import Simbolo
from Instrucciones.Funciones import Funcion
from Abstract.NodoAST import NodoAST
from TablaSimbolo.Error import Error
from TablaSimbolo.Entorno import Entorno
from Instrucciones.Break import Break


class Retornar(NodoAST):
    def __init__(self, nombre, parametros, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.fila = fila
        self.columna = columna
    
    def interpretar(self, arbol, entorno):
        x = entorno.retornarSimbolo(self.nombre.lower())#Retorna el simbolo
        if isinstance(x.getValor(), Funcion):
            funcion = x.getValor()#Extraigo el objeto de tipo funcion
            if funcion.getParametros() == None:
                nuevoentorno = Entorno(self.nombre, entorno)
                return funcion.interpretar(arbol, nuevoentorno)
            else:
                listaparametros = funcion.getParametros()
                if self.parametros == None:#self parametros son los valores
                    arbol.addExcepcion(Error("Semantico", "Error, faltan parametros", self.fila, self.columna))
                else:
                    nuevoentorno = Entorno(self.nombre, entorno)
                    listavalores = self.parametros
                    if len(listaparametros) == len (listavalores):
                        for i in range(0,len(listaparametros)):
                            identificador = listaparametros[i].getIdentificador()
                            valor = listavalores[i].interpretar(arbol, entorno)
                            simbolo = Simbolo(entorno.getNombre(), identificador, valor, arbol.getTipo(valor), "Variable", 0, self.fila, self.columna)
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
                    simbolo = Simbolo(entorno.getNombre(), cte, self.parametros[contador], "", "Variable", 0, self.fila, self.columna)
                    listatmp.append(simbolo)
                    contador = contador + 1
                newstruct = Struct(self.nombre, listatmp, ism, self.fila, self.columna)
                return newstruct
            else:
                arbol.addExcepcion(Error("Semantico", "Faltan propiedades en el struct", self.fila, self.columna))
            return

    def traducir(self, traductor, entorno):
        cont = 1
        cadena = ""
        contador = "t"+str(traductor.getContador())
        traductor.IncrementarContador()
        simbolo = entorno.retornarSimbolo(self.nombre.lower())
        if isinstance(simbolo, Simbolo):
            func = simbolo.getValor()
            if isinstance(func, Funcion):
                tamfunc = len(func.getParametros())
                if self.parametros!=None:
                    tampar = len(self.parametros)
                else:
                    tampar = 0
            if tamfunc != tampar:
                traductor.addExcepcion(Error("Semantico", "Los parametros añadidos no coinciden con los de la funcion", self.fila, self.columna))
            else:
                if tamfunc!=0:
                    cadena = "S = S + "+str(traductor.getStack())+";\n"
                    for param in self.parametros:
                        p = param.traducir(traductor, entorno)
                        cadena +=  contador +" = S + " +str(cont)+";\n"
                        cadena += "stack[int("+str(contador)+")] = "+str(p[0])+";\n"
                        traductor.IncrementarContador()   
                        cont = cont +1
                traductor.addCodigo(cadena)
                func.traducir(traductor, entorno)
                retorna = traductor.getReturn()
                traductor.resetReturn()
                valorRetornado = "t"+str(traductor.getContador())
                traductor.IncrementarContador()
                cadena = valorRetornado +" = stack[int(S)];\n"
                cadena += "S = S - "+str(traductor.getStack())+";\n"
                traductor.addCodigo(cadena)
                #return ["h", "p"]
                return [valorRetornado, retorna[1]]
        return "Retornar"