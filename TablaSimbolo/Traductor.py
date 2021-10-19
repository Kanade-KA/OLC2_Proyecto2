from Abstract.Objeto import TipoObjeto
from Expresiones.Arreglo import Arreglo
from Expresiones.Arreglo2D import Arreglo2D
from Expresiones.Arreglo3D import Arreglo3D

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
        self.libfmt = "import (\"fmt\");\n"
        self.encabezado = "//------------------------HEADER-----------------------------\npackage main;\n"+self.libmath+self.libfmt+"var stack [19121997]float64;\nvar heap [19121997]float64;\nvar S, H float64;\n"
        self.heap = 0
        self.stack= 0
        self.contador = 0#Este me sirve para el contador de temporales
        self.c3d = ""
        self.main = "func main (){\n//-------------Inicializando Punteros------------\nH = 0; \nS = 0;\n"
        #Banderas para no repetir metodos
        self.print = False
        self.potencia = False
        self.haygotos = False
        self.goto = 0#Este contador me va a servir para contar los Estados que se creen en el main.
        self.cambio = "L"
        self.logica = 0

#---------------------BANDERAS PARA SABER SI HAY QUE AGREGAR ALGUNO DE ESTOS CÓDIGOS--------------------------------
    def hayPrint(self):
        return self.print

    def activarPrint(self):
        self.print = True
    
    def hayPotencia(self):
        return self.potencia

    def activarPotencia(self):
        self.potencia = True

    def getGotos(self):
        return self.goto
#--------------------PARA TRAER UNA ETIQUETA---------
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
#----------------------------------------------------
    def IncrementarGotos(self, numero):
        self.haygotos = True
        self.goto = self.goto + numero
#---------------------------------PARA METER UN BOOLEANO AL STACK-----------------------------------
    def putBooleanStack(self, valor):
        cadena = "//-------AGREGANDO VALOR BOOLEANO--------\n"
        if valor == True:
            cadena += "stack[int(S)] = 1;\n"
        else:
            cadena += "stack[int(S)] = 0;\n"
        cadena += "S = S + 1;\n"
        self.IncrementarStack()
        self.addCodigo(cadena)
        return self.getStack()-1

#------------------------------------PARA METER UN STRING AL HEAP-------------------------------------------
    def putStringHeap(self, valor):
        temporal = self.getHeap()
        cadena = "//-----Agregando String a Heap------\n"
        cadena += "t"+str(self.getContador()) + "= H;//Se extrae la posción libre del heap;\n"
        for letra in valor:
            cadena += "heap[int(H)] = "+ self.getAscii(letra) + ";//Se mete la letra "+letra+"\n"
            cadena += "H = H + 1;//Se suma uno al heap\n"
            self.IncrementarHeap()
        cadena += "heap[int(H)] = -1;//Se ingresa al heap el fin de la cadena\n"
        cadena += "H = H + 1;//Se suma uno para que se pueda volver a usar el heap\n"
        self.IncrementarHeap()
        self.IncrementarContador()
        self.addCodigo(cadena)
        return temporal
#---------------------------------AGREGAR UN NUMERO ENTERO AL STACK-------------------------------------
    def putIntStack(self, numero):
        cadena = "//AGREGANDO UN ENTERO "+str(numero) + "\n"
        temporal = self.getStack()
        cadena += "stack[int("+ str(temporal) + ")] = "+str(numero)+";\n"
        cadena += "S = S + 1;\n"
        self.addCodigo(cadena)
        self.IncrementarStack()
        return temporal
#------------------------------AGREGAR UN NUMERO DOBLE AL STACK---------------------------------------
    def putDoubleStack(self, numero):
        cadena = "//AGREGANDO UN DOBLE "+str(numero) + "\n"
        temporal = self.getStack()
        cadena += "stack["+ str(temporal) + "] = "+str(numero)+";\n"
        cadena += "S = S + 1;\n"
        self.addCodigo(cadena)
        self.IncrementarStack()
        return temporal
#--------------------------------------------CONVERTIR UNA LETRA A ASCII----------------------------------------
    def getAscii(self, cadena):
        return str(ord(cadena))
#-----------------------------------------AREA DE TEMPORALES PARA C3D------------------------------------
    def temporales(self):
        temp = "var "
        for i in range(0, self.contador):
            if i + 1 == self.contador:
                temp += "t"+str(i)+ " float64;\n"
            else:
                temp += "t"+str(i)+", "
        return temp
#------------------------------------------PARA AGREGAR CODIGO FUERA DEL MAIN------------------------------
    def addFuncion(self, funcion):
        self.funciones += self.funciones + funcion

    def getFuncion(self):
        return self.funciones
        
#-------------------------------------LOS ENCABEZADOS DEL C3D----------------------------------------------
    def getMain(self):
        return self.main
    
    def getCodigo(self):
        return self.c3d
    
    def addCodigo(self, cadena):
        self.c3d += cadena

    def getEncabezado(self):
        return self.encabezado
#----------------------------------CONTADORES, HEAP Y STACK-------------------------------
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
#-------------------------------PARA LA TABLA DE SIMBOLOS---------------------------------
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
#-----------------------------------------------EXCEPCIONES-----------------------------------
    def getExcepciones(self):
        return self.excepciones

    def addExcepcion(self, excepciones):
        self.excepciones.append(excepciones)
        return "Error"
#-----------------------------------CONSOLA--------------------------------------------
    def getConsola(self):
        return self.consola

    def AgregaraConsola(self,cadena):
        self.consola += str(cadena)
#--------------------------------GRAFICA AST---------------------------------------
    def AgregarGrafica(self, grafo):
        self.grafica += str(grafo) + "\n"

    def getGrafica(self):
        self.grafica
#--------------------------------TIPO DE SIMBOLO-----------------------------------
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
#-----------------------------------PARA GENERAR EL STRING DEL TIPO----------------------------
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
#---------------------------------PARA GENERAR LA TABLA DE SIMBOLOS---------------------------
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

#--------------------------------PARA GENERAR LA TABLA DE ERRORES----------------------
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