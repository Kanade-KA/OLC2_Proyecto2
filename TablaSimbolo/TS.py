class TablaSimbolos:
    def __init__(self, anterior = None):
        self.tabla = {} # Diccionario Vacio
        self.anterior = anterior

    def addSimbolo(self, simbolo):
        tablaActual = self
        while tablaActual != None:
            if simbolo.id.lower() in tablaActual.tabla:
                tablaActual.tabla[simbolo.id.lower()] = simbolo
                return None
            else:
                tablaActual = tablaActual.anterior
        self.tabla[simbolo.id.lower()] = simbolo
        return None
                
    def retornarSimbolo(self, id):
        tablaactual = self
        while tablaactual != None:
            if id in  tablaactual.tabla:
                return tablaactual.tabla[id.lower()]
            else:
                tablaactual = tablaactual.anterior
        return None
            

    def AgregarGlobal(self, simbolo):
        tablaActual = self
        while tablaActual.anterior != None:#Así sabe que es el último
            tablaActual = tablaActual.anterior
        #tablaActual.addSimbolo(Simbolo)
        tablaActual.tabla[simbolo.id.lower()] = simbolo
        return None

    def Imprimir(self):
        print("===========================TABLA=============================")
        for simbolo in self.tabla:
            print(simbolo)
            #print("ID:" + str(simbolo.getID()) + " - VALOR: "+ str(simbolo.getValor()))
            print("________________________________________________________")
        return