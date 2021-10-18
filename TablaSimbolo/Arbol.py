from Abstract.Objeto import TipoObjeto
from Expresiones.Arreglo import Arreglo
from Expresiones.Arreglo2D import Arreglo2D
from Expresiones.Arreglo3D import Arreglo3D

class Arbol:
    def __init__(self):
        self.excepciones = []
        self.simbolos = []
        self.consola = ""
        self.grafica = ""
        self.cadena = ""
        self.error = ""

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
#PARA GENERAR LA TABLA DE ERRORES
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