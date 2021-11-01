from TablaSimbolo.Error import Error


class Struct():
    def __init__(self, id, datos, isMutable, fila, columna):
        self.id = id
        self.datos = datos
        self.mutable = isMutable
        self.fila = fila
        self.columna = columna

    def getDatos(self):
        return self.datos

    def getMutable(self):
        return self.mutable

    def setSimbolo(self, id, valor, arbol, entorno):
        for dato in self.datos:
            if dato.getID() == id.lower():
                if self.mutable:
                    datooriginal = dato.getValor().interpretar(arbol, entorno)
                    datox = valor.interpretar(arbol, entorno)

                    if type(datooriginal) == type(datox):
                        dato.setValor(valor)
                        return
                    else:
                        arbol.addExcepcion(Error("Semantico", "El struct es inmutable, no cumple con el tipo", self.fila, self.columna))
                        return
                dato.setValor(valor)
                return
        return

    def getSimbolo(self, id):
        for sim in self.datos:
            if sim.getID() == id.lower():
                return sim

    def imprimirStruct(self, arbol, entorno):
        x = self.id
        x += "("
        cont = 0;
        for sim in self.datos:
            x += str(sim.getValor().interpretar(arbol, entorno))
            if cont + 1 < len(self.datos):
                x += ","
            cont = cont +1
        x += ")"
        return x