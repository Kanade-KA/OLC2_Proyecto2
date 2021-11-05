from enum import Enum

class TipoInstruccion(Enum):
    ASIGNACIONOPERACION = 1
    ASIGNACIONSIMPLE = 2
    ASIGNACIONARREGLO = 3
    ARREGLOASIGNACION = 4
    ETIQUETA = 5
    RETURN = 6
    METODO = 7
    GOTO = 8
    FMT = 9
    IF = 10
    
class TipoBloque(Enum):
    VOID = 1
    MAIN = 2
    IMPORT = 3
    DECLARA = 4
    ARREGLO = 5
    PACKAGE = 6