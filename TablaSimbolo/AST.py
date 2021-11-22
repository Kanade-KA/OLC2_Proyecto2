class AST():
    def __init__(self):
        self.contador = 0
        self.cadena = ""

    def addRelacion(self, padre, hijo):
        self.cadena += str(padre) +'->'+ str(hijo) +";" + "\n";

    def newHijo(self, texto):
        self.cadena += str(self.contador) + ' [label="'+texto+'", fillcolor="LightBlue", style ="filled", shape="box"]; \n'
        self.contador += 1
    
    def getContador(self):
        return self.contador
    
    