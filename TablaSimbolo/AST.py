from TablaSimbolo.Tipo import OperadorAritmetico


class AST():
    def __init__(self):
        self.contador = 0
        self.cadena = ""

    def newEdge(self, padre, hijo):
        self.cadena += str(padre) +'->'+ str(hijo) +";" + "\n";

    def newLabel(self, texto):
        self.cadena += str(self.contador) + ' [label="'+str(texto)+'", fillcolor="Purple", style ="filled", shape="box"]; \n'
    
    def getContador(self):
        return self.contador

    def IncrementarContador(self):
        self.contador += 1

    def generarDot(self):
        dot = "digraph lista{ rankdir=TB;node[shape = box, style = filled, color = white]; \n"
        dot += self.cadena +"}"
        return dot