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
        self.encabezado = "//------------------------HEADER-----------------------------\npackage main\nimport \"fmt\" \nvar stack [19121997]float64\nvar heap [19121997]float64\nvar S, H float64\n"
        self.heap = 0
        self.stack= 0
        self.contador = 0
        self.c3d = ""
        self.main = "func main (){\n//-------------Inicializando Punteros------------\nH = 0 \nS = 0\n"
        self.print = False
#Banderas

    def hayPrint(self):
        return self.print

    def activarPrint(self):
        self.print = True

#Inicializar Temporales
    def temporales(self):
        temp = "var "
        for i in range(0, self.contador):
            if i + 1 == self.contador:
                temp += "t"+str(i)+ " float64\n"
            else:
                temp += "t"+str(i)+", "
        return temp
#Funciones
    def addFuncion(self, funcion):
        self.funciones += self.funciones + funcion

    def getFuncion(self):
        return self.funciones
#METODO PARA PRINT
    def Print(self):
        contadortemp = self.contador
        cadena = "func imprimir(){\n"
        cadena += "t"+str(contadortemp) +" = S + 1//Posicionamos en parametro\n"
        contadortemp += 1
        cadena += "t"+str(contadortemp) + "stack[int(t"+str(contadortemp-1)+")]\n"
        contadortemp += 1
        cadena += "L1:\n"
        cadena += "t"+str(contadortemp)+" = heap[int(t"+str(contadortemp-1)+")]\n" 
        cadena += "if t"+str(contadortemp)+" == -1 {goto L0}\n"
        cadena += "{ asciiValue := int(t"+str(contadortemp)+")\n"
        cadena += "character := rune(asciiValue)\n"
        cadena += "fmt.Printf(\"%c\",character)\n"
        cadena += "t"+str(contadortemp-1)+" = t"+str(contadortemp-1)+" + 1\n"
        cadena += "goto L1}\n"
        cadena += "L0:\nreturn\n}"
        return cadena
#Para encabezados  
    def getMain(self):
        return self.main
    
    def getCodigo(self):
        return self.c3d
    
    def addCodigo(self, cadena):
        self.c3d += cadena

    def getEncabezado(self):
        return self.encabezado
#CONTADORES, HEAP Y STACK
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
#PARA LA TABLA DE SIMBOLOS
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
#EXCEPCIONES
    def getExcepciones(self):
        return self.excepciones

    def addExcepcion(self, excepciones):
        self.excepciones.append(excepciones)
#CONSOLA
    def getConsola(self):
        return self.consola

    def AgregaraConsola(self,cadena):
        self.consola += str(cadena)
#GRAFICA AST
    def AgregarGrafica(self, grafo):
        self.grafica += str(grafo) + "\n"

    def getGrafica(self):
        self.grafica
#TIPO DE SIMBOLO
    def getTipo(self, tipo):
        if isinstance(tipo, int):
            return TipoObjeto.ENTERO
        if isinstance(tipo, float):
            return TipoObjeto.DECIMAL
        if isinstance(tipo, str):
            return TipoObjeto.CADENA
        if isinstance(tipo, bool):
            return TipoObjeto.BOOLEANO
        if isinstance(tipo, Arreglo):
            return TipoObjeto.ARREGLO
        if isinstance(tipo, Arreglo2D):
            return TipoObjeto.ARREGLO
        if isinstance(tipo, Arreglo3D):
            return TipoObjeto.ARREGLO
        return TipoObjeto.ANY
#PARA GENERAR EL STRING DEL TIPO
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
#PARA GENERAR LA TABLA DE SIMBOLOS
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
            self.cadena += str(self.tipoToString(sim.getTipo()))
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