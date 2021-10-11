class Entorno:
    def __init__(self, nombre, anterior = None):
        self.tabla = {} # Diccionario Vacio
        self.anterior = anterior
        self.nombre = nombre

    def addSimbolo(self, simbolo):
        entorno = self
        while entorno != None:
            if simbolo.id.lower() in entorno.tabla:
                entorno.tabla[simbolo.id.lower()] = simbolo
                return None
            else:
                entorno = entorno.anterior
        self.tabla[simbolo.id.lower()] = simbolo
        return None
                
    def retornarSimbolo(self, id):
        entorno = self
        while entorno != None:
            if id in  entorno.tabla:
                return entorno.tabla[id.lower()]
            else:
                entorno = entorno.anterior
        return None
            

    def AgregarGlobal(self, simbolo):
        entorno = self
        while entorno.anterior != None:#Así sabe que es el último
            entorno= entorno.anterior
        #tablaActual.addSimbolo(Simbolo)
        entorno.tabla[simbolo.id.lower()] = simbolo
        return None

    def getNombre(self):
        return self.nombre