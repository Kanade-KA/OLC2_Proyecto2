class NodoArbol():
    def __init__(self, valor):
        self.id = 0
        self.valor = valor  ## instancia de clase OBJETO
        self.hijos = []
        self.graf = "digraph lista{ rankdir=TB;node[shape = box, style = filled, color = white]; \n"

    def addHijos(self, hijo):
        self.hijos.append(hijo)

    def getHijos(self):
        return self.hijos
    
    def getValor(self):
        return self.valor
    def getGraf(self):
        return self.graf