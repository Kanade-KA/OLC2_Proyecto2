from Abstract.Objeto import TipoObjeto
from Expresiones.Arreglo import Arreglo
from Expresiones.Arreglo2D import Arreglo2D
from Expresiones.Arreglo3D import Arreglo3D
from Expresiones.Identificador import Identificador
from Instrucciones.Return import Return
from TablaSimbolo.Error import Error

class Traductor:
    def __init__(self):
        self.excepciones = []
        self.simbolos = []
        self.consola = ""
        self.funciones = "\n"
        self.grafica = ""
        self.cadena = ""
        self.error = ""
        self.libmath = ""
        self.functmp = ""
        self.libfmt = "import (\"fmt\");\n"
        self.encabezado = "//------------------------HEADER-----------------------------\npackage main;\n"+self.libmath+self.libfmt+"var stack [19121997]float64;\nvar heap [19121997]float64;\nvar S, H float64;\n"
        self.heap = 0
        self.stack= 0
        self.contador = 0#Este me sirve para el contador de temporales
        self.c3d = ""
        self.main = "func main (){\n//-------------Inicializando Punteros------------\nH = 0; \nS = 0;\n"
        self.print = False
        self.potencia = False
        self.haygotos = False
        self.haylower = False
        self.hayupper = False
        self.parseint = False
        self.parsedoble = False
        self.multstring = False
        self.trunc = False
        self.potstring = False
        self.compstring = False
        self.goto = 0#Este contador me va a servir para contar los Estados que se creen en el main.
        self.cambio = "L"
        self.logica = 0
        self.isbreak = ""
        self.iscontinue = ""
        self.hayreturn = False
        self.simboloretornado = ""
        self.esFuncion = False
        self.tamaniofuncion = 0

#---------------------------------BANDERAS--------------------------------------------------
    def hayPrint(self):
        return self.print

    def activarPrint(self):
        self.print = True
    
    def hayPotencia(self):
        return self.potencia

    def activarPotencia(self):
        self.potencia = True
    
    def hayMultString(self):
        return self.multstring

    def activarMultString(self):
        self.multstring = True

    def getGotos(self):
        return self.goto

    def activarPotString(self):
        self.potstring = True

    def hayPotString(self):
        return self.potstring
    
    def activarCompString(self):
        self.compstring = True

    def hayCompString(self):
        return self.compstring

    def activarLower(self):
        self.haylower = True

    def hayLower(self):
        return self.haylower
    
    def activarUpper(self):
        self.hayupper = True

    def hayUpper(self):
        return self.hayupper

    def activarParseInt(self):
        self.parseint = True

    def hayParseInt(self):
        return self.parseint

    def activarParseDoble(self):
        self.parsedoble = True

    def hayParseDoble(self):
        return self.parsedoble

    def activarTrunc(self):
        self.trunc = True

    def hayTrunc(self):
        return self.trunc

    def ActivarFuncion(self):
        self.esFuncion = True

    def DesactivarFuncion(self):
        self.esFuncion = False
    
    def EsFuncion(self):
        return self.esFuncion

    def LimpiarFuncion(self):
        self.functmp = ""

    def getTmpFuncion(self):
        return self.functmp
    
    def getBreak(self):
        return self.isbreak

    def setBreak(self,  goto):
        self.isbreak = "L"+str(goto)
    
    def resetBreak(self):
        self.isbreak = ""
    
    def setContinue(self, goto):
        self.iscontinue = str(goto)

    def getContinue(self):
        return self.iscontinue

    def getReturn(self):
        return self.simboloretornado
    
    def setReturn(self, simbolo):
        self.simboloretornado = simbolo

    def resetReturn(self):
        self.simboloretornado = ""

    def getTamanioFunc(self):
        return self.tamaniofuncion

    def setTamanioFunc(self, tam):
        self.tamaniofuncion = tam

    def resetTamanioFunc(self):
        self.tamaniofuncion = 0
#---------------------------------PARA TRAER UNA ETIQUETA-----------------------------------
    def HayCambio(self):
        if self.cambio == "L":
            return False
        else:
            return True

    def CambiarEtiqueta(self, et, logica):
        self.cambio = et
        self.logica = logica

    def SetearEtiqueta(self):
        self.cambio = "L"
        self.logica = 0

    def getEtiquetaCambio(self):
        return self.cambio
        
    def getLogica(self):
        return self.logica

    def IncrementarGotos(self, numero):
        self.haygotos = True
        self.goto = self.goto + numero
#---------------------------------CAMBIO DE ENTORNO-----------------------------------------
    def cambioEntorno(self, parametros, entorno):
        self.addCodigo("//******************CAMBIO DE ENTORNO********************\n")
        if parametros != None and parametros != 0:
            stack = "t"+str(self.getContador())
            self.IncrementarContador()

            contador = "t"+str(self.getContador())
            self.IncrementarContador()

            cadena = stack + " = S + "+str(self.getStack() + self.tamaniofuncion)+";\n"
            cont = 1
            for param in parametros:
                p = param.traducir(self, entorno)
                iden = self.EsIdentificador(param, p, entorno, 0, 0)
                if iden[0]:
                    p = [iden[1], iden[2]]
                cadena +=  contador +" = "+stack+" + " +str(cont)+";\n"
                cadena += "stack[int("+str(contador)+")] = "+str(p[0])+";\n"  
                cont = cont + 1
            self.addCodigo(cadena)
#---------------------------------REVISAR IDENTIFICADOR-------------------------------------
    def EsIdentificador(self, operador, resultado, entorno, fila, columna):
        if isinstance(operador, Identificador):
            parametro = False
            busqueda = entorno.retornarSimbolo(operador.getIdentificador().lower())
            if busqueda != None:
                if busqueda.getRol() == "Parametro":
                    parametro = True
                tipo = busqueda.getTipo()
                result = self.ExtraerVariable(resultado, parametro)
                return [True, result, tipo]
            else:
                self.addExcepcion(Error("Semantico", "No existe la variable", fila, columna))
        return [False, "", ""]
#---------------------------------PARA METER UN BOOLEANO AL STACK---------------------------
    def putBooleanStack(self, valor):
        self.addCodigo("//*************AGREGANDO BOOLEANO***************\n")
        cadena = "t"+str(self.getContador()) +" = S + "+str(self.getStack())+ ";\n"
        temporal = self.getStack()
        if valor == True:
            cadena += "stack[int(t"+str(self.getContador())+")] = 1;\n"
        else:   
            cadena += "stack[int(t"+str(self.getContador())+")] = 0;\n"
        self.IncrementarStack()
        self.addCodigo(cadena)
        return temporal
#---------------------------------PARA METER UN STRING AL HEAP------------------------------
    def putStringHeap(self, valor):
        self.addCodigo("//*************AGREGANDO STRING EN HEAP***************\n")
        temporal = "t"+str(self.getContador())
        cadena = temporal + " = H;\n"
        for letra in valor:
            cadena += "heap[int(H)] = "+self.getAscii(letra)+";\n"
            cadena += "H = H + 1;\n"
            self.IncrementarHeap()
        cadena += "heap[int(H)] = -1;\n"
        cadena += "H = H + 1;\n"
        self.IncrementarHeap()
        self.IncrementarContador()
        self.addCodigo(cadena)
        return temporal
#---------------------------------AGREGAR UN NUMERO ENTERO AL STACK-------------------------
    def putIntStack(self, numero):
        self.addCodigo("//*************AGREGANDO ENTERO***************\n")
        cadena = "t"+str(self.getContador()) +" = S + "+str(self.getStack())+ ";\n"
        temporal = self.getStack()
        cadena += "stack[int(t"+ str(self.getContador()) + ")] = "+str(numero)+";\n"
        self.addCodigo(cadena)
        self.IncrementarStack()
        self.IncrementarContador()
        return temporal
#---------------------------------AGREGAR UN NUMERO DOBLE AL STACK--------------------------
    def putDoubleStack(self, numero):
        self.addCodigo("//*************AGREGANDO DOBLE***************\n")
        cadena = "t"+str(self.getContador()) +" = S + "+str(self.getStack())+ ";\n"
        temporal = self.getStack()
        cadena += "stack[int("+ str(temporal) + ")] = "+str(numero)+";\n"
        self.addCodigo(cadena)
        self.IncrementarStack()
        self.IncrementarContador()
        return temporal
#---------------------------------AGREGAR EL PUNTERO DEL HEAP AL STACK----------------------
    def putStringHStack(self, heap):
        self.addCodigo("//*************AGREGANDO HEAP A STACK***************\n")
        cadena = "t"+ str(self.getContador())+ " = S + "+str(self.getStack())+";\n"
        self.IncrementarContador()
        cadena += "t"+str(self.getContador())+" = "+str(heap) + ";\n"
        cadena += "stack[int(t"+str(self.getContador()-1)+")] = t"+str(self.getContador())+";\n"
        self.addCodigo(cadena)
        apuntastack = self.getStack()
        self.IncrementarStack()#Incrementamos el stack para que agarre el nuevo
        self.IncrementarContador()
        return apuntastack
#---------------------------------JALAR VARIABLE DEL STACK----------------------------------
    def ExtraerVariable(self, stack, parametro):
        self.addCodigo("//*************EXTRAYENDO DEL STACK***************\n")
        if parametro:
            cadena = "t"+str(self.getContador()) +" = "+str(stack)+";\n"
        else:
            cadena = "t"+str(self.getContador()) +" = S + "+str(stack)+";\n"
        self.IncrementarContador()
        valor = "t"+str(self.getContador())
        cadena += valor +" = stack[int(t"+str(self.getContador()-1)+")];\n"
        self.addCodigo(cadena)
        self.IncrementarContador()
        return valor
#---------------------------------CONVERTIR UNA LETRA A ASCII-------------------------------
    def getAscii(self, cadena):
        return str(ord(cadena))
#---------------------------------AREA DE TEMPORALES PARA C3D-------------------------------
    def temporales(self):
        if self.contador==0:
            return ""
        temp = "var "
        for i in range(0, self.contador):
            if i + 1 == self.contador:
                temp += "t"+str(i)+ " float64;\n"
            else:
                temp += "t"+str(i)+", "
        return temp
#---------------------------------PARA AGREGAR CODIGO FUERA DEL MAIN------------------------
    def addFuncion(self, funcion):
        self.funciones +=  funcion

    def getFuncion(self):
        return self.funciones     
#---------------------------------ENCABEZADOS DEL C3D---------------------------------------
    def getMain(self):
        return self.main
    
    def getCodigo(self):
        return self.c3d
    
    def addCodigo(self, cadena):
        if self.EsFuncion():
            self.functmp += cadena
        else:    
            self.c3d += cadena

    def getEncabezado(self):
        return self.encabezado
#---------------------------------CONTADORES, HEAP Y STACK----------------------------------
    def IncrementarHeap(self):
        self.heap = self.heap + 1
    
    def IncrementarStack(self):
        self.stack = self.stack + 1

    def IncrementarContador(self):
        self.contador = self.contador + 1
        return

    def getHeap(self):
        return self.heap
    
    def getStack(self):
        return self.stack
    
    def getContador(self):
        return self.contador
#---------------------------------PARA LA TABLA DE SIMBOLOS---------------------------------
    def getSimbolos(self):
        return self.simbolos

    def addSimbolo(self, simbolo):
        if not self.buscarSimbolo(simbolo.getID(), simbolo.getFila()):
            self.simbolos.append(simbolo)
        return

    def buscarSimbolo(self, simbolo, fila):
        for s in self.simbolos:
            if s.getID() == simbolo and s.getFila() == fila:
                    return True
        return False
#---------------------------------EXCEPCIONES-----------------------------------------------
    def getExcepciones(self):
        return self.excepciones

    def addExcepcion(self, excepciones):
        self.excepciones.append(excepciones)
        return "Error"
#---------------------------------CONSOLA---------------------------------------------------
    def getConsola(self):
        return self.consola

    def AgregaraConsola(self,cadena):
        self.consola += str(cadena)
#---------------------------------GRAFICA AST-----------------------------------------------
    def AgregarGrafica(self, grafo):
        self.grafica += str(grafo) + "\n"

    def getGrafica(self):
        self.grafica
#---------------------------------TIPO DE SIMBOLO-------------------------------------------
    def getTipo(self, tipo):
        if isinstance(tipo, bool):
            return TipoObjeto.BOOLEANO
        if isinstance(tipo, int):
            return TipoObjeto.ENTERO
        if isinstance(tipo, float):
            return TipoObjeto.DECIMAL
        if isinstance(tipo, str):
            return TipoObjeto.CADENA
        if isinstance(tipo, Arreglo):
            return TipoObjeto.ARREGLO
        if isinstance(tipo, Arreglo2D):
            return TipoObjeto.ARREGLO
        if isinstance(tipo, Arreglo3D):
            return TipoObjeto.ARREGLO
        return TipoObjeto.ANY
#---------------------------------PARA GENERAR EL STRING DEL TIPO---------------------------
    def tipoToString(self, tipo):
        if tipo == TipoObjeto.ENTERO:
            return "int"
        if tipo == TipoObjeto.DECIMAL:
            return "doble"
        if tipo == TipoObjeto.CADENA:
            return "string"
        if tipo == TipoObjeto.BOOLEANO:
            return "bool"
        if tipo == TipoObjeto.ARREGLO:
            return "arreglo"
        return "nothing"
#---------------------------------PARA GENERAR LA TABLA DE SIMBOLOS-------------------------
    def generateTable(self):
        self.cadena +="<table class=\"table\">"
        self.cadena +="<tr>"
        self.cadena +="<th scope=\"col\">Entorno</th>"
        self.cadena +="<th scope=\"col\">Simbolo</th>"
        self.cadena +="<th scope=\"col\">Tipo</th>"
        self.cadena +="<th scope=\"col\">Rol</th>"
        self.cadena +="<th scope=\"col\">Posicion</th>"
        self.cadena +="<th scope=\"col\">Fila</th>"
        self.cadena +="<th scope=\"col\">Columna</th>"
        self.cadena +="</tr>"
        self.RecorrerSimbolos()
        self.cadena +="</table>"
        return self.cadena

    def RecorrerSimbolos(self):
        for sim in self.simbolos:
            self.cadena += "<tr>"
            self.cadena += "<td>"
            self.cadena += str(sim.getEntorno())
            self.cadena += "</td>"
            self.cadena += "<td>"
            self.cadena += str(sim.getID())
            self.cadena += "</td>"
            self.cadena += "<td>"
            self.cadena += str(sim.getTipo())
            self.cadena += "</td>"
            self.cadena += "<td>"
            self.cadena += str(sim.getRol())
            self.cadena += "</td>"
            self.cadena += "<td>"
            self.cadena += str(sim.getPosicion())
            self.cadena += "</td>"
            self.cadena += "<td>"
            self.cadena += str(sim.getFila())
            self.cadena += "</td>"
            self.cadena += "<td>"
            self.cadena += str(sim.getColumna())
            self.cadena += "</td>"
            self.cadena += "</tr>"
#---------------------------------PARA GENERAR LA TABLA DE ERRORES--------------------------
    def generateErrors(self):
        self.error +="<table class=\"table\">"
        self.error +="<tr>"
        self.error +="<th scope=\"col\">Tipo Error</th>"
        self.error +="<th scope=\"col\">Descripción</th>"
        self.error +="<th scope=\"col\">Fila</th>"
        self.error +="<th scope=\"col\">Columna</th>"
        self.error +="</tr>"
        self.RecorrerError()
        self.error +="</table>"
        return self.error
    
    def RecorrerError(self):
        for err in self.excepciones:
            self.error += "<tr>"
            self.error += "<td>"
            self.error += str(err.getTipo())
            self.error += "</td>"
            self.error += "<td>"
            self.error += str(err.getDescripcion())
            self.error += "</td>"
            self.error += "<td>"
            self.error += str(err.getFila())
            self.error += "</td>"
            self.error += "<td>"
            self.error += str(err.getColumna())
            self.error += "</td>"
            self.error += "</tr>"