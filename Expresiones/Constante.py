from Abstract.Objeto import TipoObjeto
from Objeto.Primitivo import Primitivo
from Abstract.NodoAST import NodoAST


class Constante(NodoAST):
    def __init__(self, valor, fila, columna):
        self.valor = valor      # Esta será una instancia de la clase OBJETO
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, entorno):
        if isinstance(self.valor, Primitivo):
            if self.valor.tipo == TipoObjeto.CADENA:
                return self.valor.toString()
            if self.valor.tipo == TipoObjeto.BOOLEANO:
                return self.valor.toBoolean()
            if self.valor.tipo == TipoObjeto.DECIMAL:
                return self.valor.toDouble()
            if self.valor.tipo == TipoObjeto.ENTERO:
                return self.valor.toInt()
        else:
            if isinstance(self.valor, int):
                x = Primitivo(TipoObjeto.CADENA, self.valor)
                return x.toInt()
            if isinstance(self.valor, float):
                x = Primitivo(TipoObjeto.FLOAT, self.valor)
                return x.toDouble()
            if isinstance(self.valor, str):
                x = Primitivo(TipoObjeto.CADENA, self.valor)
                return x.toString()
            if isinstance(self.valor, bool):
                x = Primitivo(TipoObjeto.BOOLEANO, self.valor)
                return x.toBoolean()

        return "F"

    def getTipo(self):
        return type(self.valor)

    def traducir(self, traductor, entorno):
        cadena = ""
        if isinstance(self.valor, Primitivo):
            if self.valor.tipo == TipoObjeto.CADENA:
                valor = self.valor.toString()
                cadena += "//-----Agregando "+ valor + " a Heap------\n"
                cadena += "t"+str(traductor.getContador()) + "= H\n"
                #traductor.IncrementarContador()
                for letra in valor:
                    cadena += "heap[int(H)] = "+ self.getAscii(letra) + ";\n"
                    cadena += "H = H + 1\n"
                    traductor.IncrementarHeap()
                cadena += "heap[int(H)] = -1;\n"
                cadena += "H = H + 1\n"
                #Meter en el stack la posición del heap
                cadena += "stack[int(S)] = t"+str(traductor.getContador()) + ";\n"
                traductor.IncrementarContador()
                cadena += "t"+str(traductor.getContador())+" = stack[int(S)];\n"
                traductor.IncrementarContador()
                cadena += "t"+str(traductor.getContador())+"= S + 1;\n"
                cadena += "t"+str(traductor.getContador())+"= t"+str(traductor.getContador())+" + 1;\n"
                cadena += "stack[int(t"+str(traductor.getContador())+")] = t"+str(traductor.getContador()-1)+";\n"
                cadena += "S = S + 1;\n"
                
                traductor.IncrementarContador()
                traductor.addCodigo(cadena)
                return #self.valor.toString()#No se si retornarlo o Nel
            if self.valor.tipo == TipoObjeto.BOOLEANO:
                return self.valor.toBoolean()
            if self.valor.tipo == TipoObjeto.DECIMAL:
                return self.valor.toDouble()
            if self.valor.tipo == TipoObjeto.ENTERO:
                return self.valor.toInt()
        return "Constante"

    def getAscii(self, cadena):
        return str(ord(cadena))
    