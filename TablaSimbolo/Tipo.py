from enum import Enum

class TIPO(Enum):
    ENTERO = 1
    DECIMAL = 2
    BOOLEANO = 3
    CHARACTER = 4
    CADENA = 5
    NULO = 6
    ARREGLO = 7

class OperadorAritmetico(Enum):
    MAS = 1
    MENOS = 2
    POR = 3
    DIV = 4
    POW = 5
    MOD = 6

class OperadorRelacional(Enum):
    MENORQUE = 1
    MAYORQUE = 2
    MENORIGUAL = 3
    MAYORIGUAL = 4
    IGUALIGUAL = 5
    DIFERENTE = 6

class OperadorNativo(Enum):
    LOGARITMO = 1
    UPPERCASE = 2
    LOWERCASE = 3
    SENO = 4
    COSENO = 5
    TANGENTE = 6
    CUADRADA = 7
    PARSE = 8
    TRUNC = 9
    FLOAT = 10
    STRING = 11
    TYPEOF = 12
    LENGTH = 13
    PUSH = 14
    POP = 15

class OperadorLogico(Enum):
    NOT = 1
    AND = 2
    OR = 3

class TipoFor(Enum):
    INTERVALO = 1
    EXPRESION = 2
    ARRAY = 3