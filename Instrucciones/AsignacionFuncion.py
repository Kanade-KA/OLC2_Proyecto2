from Abstract.NodoAST import NodoAST
from Abstract.Objeto import TipoObjeto
from Instrucciones.Funciones import Funcion
from TablaSimbolo.Entorno import Entorno
from TablaSimbolo.Simbolo import Simbolo
class AsignacionFuncion(NodoAST):
    def __init__(self, identificador, expresion, tipo, fila, columna):
        self.identificador = identificador
        self.expresion = expresion
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        simbolo = Simbolo(entorno.getNombre(), self.identificador.lower(), self.expresion, "", self.tipo, 0, self.fila, self.columna)
        arbol.addSimbolo(simbolo)
        entorno.addSimbolo(simbolo)
        return
    
    def traducir(self, traductor, entorno):#Debo cambiar entorno
        funcion = self.expresion
        tam = 0
        if isinstance(funcion, Funcion):
            tam = funcion.getParametros()
            if tam != None:
                tam = len(tam)
        simbolo = Simbolo(entorno.getNombre(), self.identificador.lower(), funcion, "", "Void", tam+1, self.fila, self.columna)
        traductor.addSimbolo(simbolo)
        entorno.addSimbolo(simbolo)

        traductor.ActivarFuncion()

        traductor.setTamanioFunc(tam + 1)
        newentorno = Entorno(str(self.identificador), entorno)
        lista = funcion.getInstrucciones()
        cont = 1;
        cadena = "func "+self.identificador.lower()+"(){\n"
        if tam>0:#quiere decir que si hay funcioens
            for parametro in funcion.getParametros():
                simbolo = Simbolo(newentorno.getNombre(), parametro.getIdentificador(), None, TipoObjeto.ENTERO, "Parametro", "S + "+str(cont), self.fila, self.columna)
                traductor.addSimbolo(simbolo)
                newentorno.addSimbolo(simbolo)
                cont = cont +1
        for ins in lista:
            ins.traducir(traductor, newentorno)
        cadena += traductor.getTmpFuncion()
        cadena += "\n}\n\n"
        traductor.addFuncion(cadena)
        traductor.DesactivarFuncion()
        traductor.LimpiarFuncion()
        traductor.resetTamanioFunc()
        return