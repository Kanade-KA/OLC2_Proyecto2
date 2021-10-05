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
    LOGARITMOD = 1
    LOGARITMOB = 2
    UPPERCASE = 3
    LOWERCASE = 4
    SENO = 5
    COSENO = 6
    TANGENTE = 7
    CUADRADA = 8
    PARSE = 9
    TRUNC = 10
    FLOAT = 11
    STRING = 12
    TYPEOF = 13
    LENGTH = 14
    PUSH = 15
    POP = 16

class OperadorLogico(Enum):
    NOT = 1
    AND = 2
    OR = 3

class TipoFor(Enum):
    INTERVALO = 1
    EXPRESION = 2
    ARRAY = 3