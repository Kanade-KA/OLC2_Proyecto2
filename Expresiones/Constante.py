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
        if isinstance(self.valor, Primitivo):
            if self.valor.tipo == TipoObjeto.CADENA:
                heap = traductor.putStringHeap(self.valor.toString())
                return [heap, TipoObjeto.CADENA]
            if self.valor.tipo == TipoObjeto.BOOLEANO:
                return [self.valor.toBoolean(), TipoObjeto.BOOLEANO]
            if self.valor.tipo == TipoObjeto.DECIMAL:
                return [self.valor.toDouble(), TipoObjeto.DECIMAL]
            if self.valor.tipo == TipoObjeto.ENTERO:
                return [self.valor.toInt(), TipoObjeto.ENTERO]
        return 