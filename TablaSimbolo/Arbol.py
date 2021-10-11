class Arbol:
    def __init__(self):
        self.excepciones = []
        self.simbolos = []
        self.consola = ""
        self.grafica = ""
        self.cadena = ""
        self.error = ""

    def getExcepciones(self):
        return self.excepciones

    def getSimbolos(self):
        return self.simbolos

    def addSimbolo(self, simbolo):
        return self.simbolos.append(simbolo)
    
    def addExcepcion(self, excepciones):
        self.excepciones.append(excepciones)

    def getConsola(self):
        return self.consola

    def AgregaraConsola(self,cadena):
        self.consola += str(cadena)

    def AgregarGrafica(self, grafo):
        self.grafica += str(grafo) + "\n"

    def getGrafica(self):
        self.grafica

    def generateTable(self):
        self.cadena +="<table class=\"table\">"
        self.cadena +="<tr>"
        self.cadena +="<th scope=\"col\">Entorno</th>"
        self.cadena +="<th scope=\"col\">Simbolo</th>"
        self.cadena +="<th scope=\"col\">Valor</th>"
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
            self.cadena += str(sim.getValor())
            self.cadena += "</td>"
            self.cadena += "<td>"
            self.cadena += str(sim.getTipo())
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