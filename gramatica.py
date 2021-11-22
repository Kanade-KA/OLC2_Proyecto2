
from Expresiones.Length import Length
from Expresiones.Parse import Parse
from Expresiones.Typeof import Typeof
from Instrucciones.AsignacionFuncion import AsignacionFuncion
from Instrucciones.AsignacionObjeto import AsignaObjeto
from Instrucciones.AsignacionStruct import AsignacionStruct
from Instrucciones.LlamaStruct import LlamaStruct
from Expresiones.Struct import Struct
from Instrucciones.AsignaMatriz3D import AsignaMatriz3D
from Instrucciones.LlamaMatriz3D import LlamaMatriz3D
from Expresiones.Arreglo3D import Arreglo3D
from Instrucciones.Pop import Pop
from Instrucciones.Push import Push
from Instrucciones.AsignaMatriz2D import AsignaMatriz2D
from Instrucciones.LlamaMatriz2D import LlamaMatriz2D
from Instrucciones.AsignaMatriz import AsignaMatriz
from Instrucciones.LlamaMatriz import LlamaMatriz
from Expresiones.Arreglo import Arreglo
from TablaSimbolo.AST import AST
from TablaSimbolo.Arbol import Arbol
from Instrucciones.Retonar import Retornar
from Instrucciones.Return import Return
from Instrucciones.LlamadaFuncion import LlamadaFuncion
from Instrucciones.Funciones import Funcion
from Instrucciones.For import For
from Instrucciones.Continue import Continue
from Instrucciones.If import If
from Instrucciones.Asignacion import Asignacion
from TablaSimbolo.Error import Error
import re
import sys

from TablaSimbolo.Traductor import Traductor
sys.setrecursionlimit(3000)

errores = []

reservadas = {
    'println'   : 'rprintln',
    'print'     : 'rprint',
    'global'    : 'rglobal',
    'local'     : 'rlocal',
    'function'  : 'rfunction',
    'end'       : 'rend',
    'parse'     : 'rparse',
    'trunc'     : 'rtrunc',
    'typeof'    : 'rtypeof',
    'push'      : 'rpush',
    'pop'       : 'rpop',
    'length'    : 'rlength',
    'if'        : 'rif',
    'elseif'    : 'relseif',
    'else'      : 'relse',
    'while'     : 'rwhile',
    'for'       : 'rfor',
    'in'        : 'rin',
    'break'     : 'rbreak',
    'continue'  : 'rcontinue',
    'return'    : 'rreturn',
    'lowercase' : 'rlc',
    'uppercase'  : 'ruc',
    'struct'    : 'rstruct',
    'mutable'   : 'rmutable',
    'log10'     : 'logd', 
    'log'       : 'logb', 
    'sin'       : 'seno', 
    'cos'       : 'coseno', 
    'tan'       : 'tang', 
    'sqrt'      : 'cuadrado',
    'string'    : 'rstring', 
    'int64'     : 'rint',
    'float64'   : 'rfloat', 
    'float'     : 'rrfloat',
    'true'      : 'rtrue',
    'false'     : 'rfalse'
}

tokens = [
    'int', 'float', 'cadena',
    'mas', 'menos', 'por', 'div', 'mod', 'pow', 
    'mayor', 'menor', 'mayori', 'menori', 'igualigual', 'diferente',
    'or', 'and', 'not',
    'igual', 'apar', 'cpar', 'acor', 'ccor', 'punto', 'dosp', 'pcoma', 'coma', 'id'
] + list(reservadas.values())

# Tokens
t_pcoma         = r';'
t_apar          = r'\('
t_cpar          = r'\)'
t_acor          = r'\['
t_ccor          = r'\]'
t_coma          = r','
t_mas           = r'\+' 
t_menos         = r'-'
t_por           = r'\*'
t_div           = r'\/'
t_mod           = r'%'
t_pow           = r'\^'
t_igual         = r'='
t_mayor         = r'>'
t_menor         = r'<'
t_mayori        = r'>='
t_menori        = r'<='
t_igualigual    = r'=='
t_diferente     = r'!='
t_and           = r'&&'
t_or            = r'\|\|'
t_not           = r'!'
t_dosp          = r'\:'
t_punto         = r'\.'

def t_float(t):
    r'-?\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_int(t):
    r'-?\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_id(t):
     r'[a-zA-Z][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'id')
     return t

def t_cadena(t):
    r'(\".*?\")'
    t.value = t.value[1:-1] # remuevo las comillas
    return t

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_IGNORAR(t):
    r'\ |\t|\r'

def t_error(t):
    errores.append(Error("Lexico","Error léxico: " + t.value[0] , t.lexer.lineno, t.lexer.lexpos))
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()

precedence = (
    ('left', 'or'),
    ('left', 'and'),
    ('left', 'igualigual', 'diferente'),
    ('left', 'mayori', 'mayor', 'menori', 'menor'),
    ('left', 'mas','menos'),
    ('left', 'div', 'por', 'mod'),
    ('left',  'pow'),
    ('right', 'not')
)
#IMPORTACIONES
from Objeto.Primitivo import Primitivo
from Expresiones.Constante import Constante
from Abstract.Objeto import TipoObjeto
from Instrucciones.Imprimir import Imprimir
from Expresiones.Aritmetica import Aritmetica
from TablaSimbolo.Tipo import OperadorAritmetico, OperadorLogico, OperadorRelacional
from TablaSimbolo.Tipo import OperadorNativo
from Expresiones.Nativas import Nativas
from Expresiones.Relacional import Relacional
from Expresiones.Logica import Logica
from TablaSimbolo.Entorno import Entorno
from Instrucciones.Asignacion import Asignacion
from Expresiones.Identificador import Identificador
from Instrucciones.If import If
from Instrucciones.While import While
from Instrucciones.Break import Break
from Expresiones.Arreglo2D import Arreglo2D
from TablaSimbolo.Simbolo import Simbolo
from TablaSimbolo.Tipo import TIPO
from Instrucciones.AsignacionArreglos import AsignacionArreglo
#--------------------------------------------Definición de la Gramatica----------------------------------------------
def p_init(t) :
    'init            : INSTRUCCIONES'
    t[0]=t[1]

def p_instrucciones_lista(t):
    'INSTRUCCIONES : INSTRUCCIONES INSTRUCCION'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]
    
def p_instrucciones_final(t):
    'INSTRUCCIONES : INSTRUCCION' 
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_instruccion(t):
    '''INSTRUCCION : PRINT pcoma
                    | ASIGNACION 
                    | IF 
                    | WHILE
                    | FOR
                    | BREAK
                    | CONTINUE
                    | PUSH
                    | FUNCION
                    | LLAMAFN
                    | RETURN
                    | STRUCTS
    '''
    t[0] = t[1]

def p_instruccion_error(t):
    'INSTRUCCION       : error pcoma'
    errores.append(Error("Sintáctico","Error Sintáctico:" + str(t[1].value) , t.lineno(1), t.lexpos(1)))
    t[0] = ""
#-----------------------------------STRUCTS------------------------------------------
def p_struct_mutable(t):
    '''STRUCTS : rmutable rstruct id VARIABLES rend pcoma'''
    struct = Struct(t[3], t[4], False, t.lineno(1), t.lexpos(1))
    t[0] = AsignacionStruct(t[3], struct, "Struct Mutable", t.lineno(1), t.lexpos(1))
def p_struct(t):
    '''STRUCTS : rstruct id VARIABLES rend pcoma'''
    struct = Struct(t[2], t[3], True, t.lineno(1), t.lexpos(1))
    t[0] = AsignacionStruct(t[2], struct, "Struct Inmutable", t.lineno(1), t.lexpos(1))
def p_struct_variables(t):
    '''VARIABLES : VARIABLES DEC'''
    t[1].append(t[2])
    t[0] = t[1]

def p_struct_variables2(t):
    '''VARIABLES : DEC'''
    t[0] = [t[1]]

def p_declaracionesstructs(t):
    '''DEC : id pcoma'''
    t[0] = t[1]

def p_declaracionesstructs2(t):
    '''DEC : id dosp dosp TIPO pcoma''' 
    t[0] = t[1]
#-----------------------------------------------------------------------------
def p_pushh(t):
    '''PUSH : rpush not apar id coma DATOPUSH cpar pcoma'''
    t[0] = Push(t[4], t[6], t.lineno(1), t.lexpos(1))

def p_datopush(t):
    '''DATOPUSH : EXP
                | MATRIZ'''
    t[0] = t[1]
#----------------------------------------------- FUNCIONES -----------------------------------------------
def p_funciones(t):
    '''FUNCION : rfunction id apar cpar INSTRUCCIONES rend pcoma'''
    func = Funcion(t[2], None, t[5], t.lineno(1), t.lexpos(1))
    t[0] = AsignacionFuncion(t[2], func, "Funcion", t.lineno(1), t.lexpos(1))
def p_funciones_parametro(t):
    '''FUNCION : rfunction id apar PARAMETROS cpar INSTRUCCIONES rend pcoma'''
    func = Funcion(t[2], t[4], t[6], t.lineno(1), t.lexpos(1))
    t[0] = AsignacionFuncion(t[2], func, "Funcion", t.lineno(1), t.lexpos(1))

def p_llamadafn(t):
    '''LLAMAFN : id apar cpar pcoma'''
    t[0] = LlamadaFuncion(t[1], None, t.lineno(1), t.lexpos(1))
def p_llamadafn_param(t):
    '''LLAMAFN : id apar PARAMETROS cpar pcoma'''
    t[0] = LlamadaFuncion(t[1], t[3], t.lineno(1), t.lexpos(1))

def p_parametros(t):
    '''PARAMETROS : PARAMETROS coma PARAMETRO '''
    t[1].append(t[3])
    t[0] = t[1]

def p_parametros2(t):
    '''PARAMETROS : PARAMETRO '''
    t[0] = [t[1]]

def p_parametros3(t):
    '''PARAMETRO : EXP dosp dosp TIPO '''
    t[0] = t[1]

def p_parametros4(t):
    '''PARAMETRO : EXP '''
    t[0] = t[1]



def p_return(t):
    '''RETURN : rreturn pcoma'''
    t[0] = Return(None, t.lineno(1), t.lexpos(1))

def p_return1(t):
    '''RETURN : rreturn EXP pcoma'''
    t[0] = Return(t[2], t.lineno(1), t.lexpos(1))

#------------------------------------------------ FOR --------------------------------------------------------
def p_for_dosp(t):
    '''FOR : rfor EXP rin EXP dosp EXP INSTRUCCIONES rend pcoma'''
    t[0] = For(t[2], t[4], t[6], t[7], t.lineno(1), t.lexpos(1))
def p_for_sindos(t):
    '''FOR : rfor EXP rin EXP INSTRUCCIONES rend pcoma'''
    t[0] = For(t[2], t[4], None, t[5], t.lineno(1), t.lexpos(1))
#------------------------------------------ WHILE ---------------------------------------------------
def p_while(t):
    '''WHILE : rwhile EXP INSTRUCCIONES rend pcoma'''
    t[0] = While(t[2], t[3], t.lineno(1), t.lexpos(1))
def p_break(t):
    '''BREAK : rbreak pcoma'''
    t[0] = Break(t.lineno(1), t.lexpos(1))
def p_continue(t):
    '''CONTINUE : rcontinue pcoma'''
    t[0] = Continue(t.lineno(1), t.lexpos(1))
#---------------------------------------------IF------------------------------------------------------------
def p_if0(t):
    '''IF : rif EXP INSTRUCCIONES ELSEIF'''
    t[0] = If(t[2], t[3], None, t[4], t.lineno(1), t.lexpos(1))
def p_if(t):
    '''IF : rif EXP INSTRUCCIONES rend pcoma'''
    t[0] = If(t[2], t[3], None, None, t.lineno(1), t.lexpos(1))

def p_if2(t):
    '''IF : rif EXP INSTRUCCIONES relse INSTRUCCIONES rend pcoma'''
    t[0] = If(t[2], t[3], t[5], None, t.lineno(1), t.lexpos(1))
#------------------------------------------------IF VACIO------------------------------------------------------
def p_if4(t):
    '''IF : rif EXP rend pcoma'''
    t[0] = If(t[2], None, None, None, t.lineno(1), t.lexpos(1))

def p_if5(t):
    '''IF : rif EXP INSTRUCCIONES relse rend pcoma'''
    t[0] = If(t[2], t[3], None, None, t.lineno(1), t.lexpos(1))

def p_if6(t):
    '''IF : rif EXP relse rend pcoma'''
    t[0] = If(t[2], None, None, None, t.lineno(1), t.lexpos(1))
def p_if7(t):
    '''IF : rif EXP ELSEIF'''
    t[0] = If(t[2], None, None, t[3], t.lineno(1), t.lexpos(1))
#---------------------------------------------------ELSE IF----------------------------------------------------
def p_elseif(t):
    '''ELSEIF : relseif EXP INSTRUCCIONES rend pcoma'''
    t[0] = If(t[2], t[3], None, None, t.lineno(1), t.lexpos(1))

def p_elseif1(t):
    '''ELSEIF : relseif EXP INSTRUCCIONES relse INSTRUCCIONES rend pcoma'''
    t[0] = If(t[2], t[3], t[5], None, t.lineno(1), t.lexpos(1))

def p_elseif2(t):
    '''ELSEIF : relseif EXP INSTRUCCIONES ELSEIF'''
    t[0] = If(t[2], t[3], None, t[4], t.lineno(1), t.lexpos(1))
#---------------------------------------------------ELSE IF VACÍOS--------------------------------------------
def p_elseif3(t):
    '''ELSEIF : relseif EXP rend pcoma'''
    t[0] = If(t[2], None, None, None, t.lineno(1), t.lexpos(1))

def p_elseif4(t):
    '''ELSEIF : relseif EXP relse INSTRUCCIONES rend pcoma'''
    t[0] = If(t[2], None, t[4], None, t.lineno(1), t.lexpos(1))

def p_elseif5(t):
    '''ELSEIF : relseif EXP INSTRUCCIONES relse rend pcoma'''
    t[0] = If(t[2], t[3], None, None, t.lineno(1), t.lexpos(1))
def p_elseif6(t):
    '''ELSEIF : relseif EXP relse rend pcoma'''
    t[0] = If(t[2], None, None, None, t.lineno(1), t.lexpos(1))
def p_elseif7(t):
    '''ELSEIF : relseif EXP ELSEIF'''
    t[0] = If(t[2], None, None, t[3], t.lineno(1), t.lexpos(1))
#-------------------------------------------ASIGNACIONES-------------------------------------------------------------
def p_asignacion_objeto(t):
    '''ASIGNACION : id punto id igual EXP pcoma'''
    t[0] = AsignaObjeto(t[1], t[3], t[5], t.lineno(1), t.lexpos(1))
def p_asignacion_tipo(t):
    '''ASIGNACION : id igual EXP dosp dosp TIPO pcoma'''
    t[0] = Asignacion(t[1], t[3],t[6], t.lineno(1), t.lexpos(1))

def p_asignacion(t):
    '''ASIGNACION : id igual EXP pcoma'''
    t[0] = Asignacion(t[1], t[3], "any", t.lineno(1), t.lexpos(1))

def p_asignacion_local_valor(t):
    '''ASIGNACION : rlocal id igual EXP pcoma'''
    t[0] = Asignacion(t[2], t[4], "local", t.lineno(1), t.lexpos(1))

def p_asignacion_local_nulo(t):
    '''ASIGNACION : rlocal id pcoma'''
    t[0] = Asignacion(t[2], None, "local", t.lineno(1), t.lexpos(1))

def p_asignacion_global_valor(t):
    '''ASIGNACION : rglobal id igual EXP pcoma'''
    t[0] = Asignacion(t[2], t[4], "global", t.lineno(1), t.lexpos(1))

def p_asignacion_global_nulo(t):
    '''ASIGNACION : rglobal id pcoma'''
    t[0] = Asignacion(t[2], None, "global", t.lineno(1), t.lexpos(1))
#------------------------------------------------ASIGNACION MATRIZ-----------------------------------------
def p_asignacion_matriz(t):
    '''ASIGNACION : id igual MATRIZ pcoma'''
    arreglo = Arreglo(t[1], t[3])
    t[0] = AsignacionArreglo(t[1], arreglo, "1D", t.lineno(1), t.lexpos(1))

def p_reasignacion_matriz(t):
    '''ASIGNACION : id acor EXP ccor igual EXP pcoma'''
    t[0] = AsignaMatriz(t[1], t[3], t[6], t.lineno(1), t.lexpos(1))
def p_reasignacion_matriz2(t):
    '''ASIGNACION : id acor EXP ccor acor EXP ccor igual EXP pcoma'''
    t[0] = AsignaMatriz2D(t[1], t[3], t[6], t[9], t.lineno(1), t.lexpos(1))

def p_reasignacion_matriz3(t):
    '''ASIGNACION : id acor EXP ccor acor EXP ccor acor EXP ccor igual EXP pcoma'''
    t[0] = AsignaMatriz3D(t[1], t[3], t[6], t[9], t[12], t.lineno(1), t.lexpos(1))
#--------------------------------------------------MATRIZ----------------------------------------------------
def p_matriz(t):
    '''MATRIZ : acor LMATRIZ ccor'''
    t[0]=t[2]

def p_l_matriz(t):
    '''LMATRIZ : LMATRIZ coma EXP'''
    if t[2] != "":
        t[1].append(t[3])
    t[0] = t[1]

def p_l_matriz2(t):
    '''LMATRIZ : EXP'''
    t[0] = [t[1]]

def p_tipo(t):
    '''TIPO : rstring
            | rfloat
            | rint'''
    t[0]=t[1]
#------------------------------------------------DE DOS DIMENSIONES------------------------------------------
def p_asignacion_matriz2(t):
    '''ASIGNACION : id igual acor LMATRIZMATRIZ ccor pcoma'''
    arreglo = Arreglo2D(t[1], t[4])
    t[0] = AsignacionArreglo(t[1], arreglo, "2D", t.lineno(1), t.lexpos(1))

def p_listamatrices(t):
    '''LMATRIZMATRIZ : LMATRIZMATRIZ coma MATRIZ'''
    t[1].append(t[3])
    t[0]=t[1]

def p_matrices(t):
    '''LMATRIZMATRIZ : MATRIZ'''
    t[0] = [t[1]]
#--------------------------------------------DE TRES DIMENSIONES---------------------------------------------
def p_asignacion_matriz3(t):
    '''ASIGNACION : id igual  MULT pcoma'''
    arreglo = Arreglo3D(t[1], t[3])
    t[0] = AsignacionArreglo(t[1], arreglo, "3D", t.lineno(1), t.lexpos(1))
    
def p_multidimensional(t):
    '''MULT : acor LISTAM ccor'''
    t[0] = t[2]

def p_listam(t):
    '''LISTAM : LISTAM coma LISTAM2'''
    t[1].append(t[3])
    t[0] = t[1]

def p_listamm(t):
    '''LISTAM : LISTAM2'''
    t[0] = [t[1]]

def p_listalista(t):
    '''LISTAM2 : MULT'''
    t[0] = t[1]
def p_listalista2(t):
    '''LISTAM2 : EXP'''
    t[0] = t[1]

#------------------------------------------------------IMPRESIONES-------------------------------------------------
def p_print(t):
    '''PRINT :  rprint apar IMPRESIONES cpar'''
    t[0] = Imprimir(t[3], 'F', t.lineno(1), t.lexpos(3))

def p_pritn_ln(t):
    ''' PRINT : rprintln apar IMPRESIONES cpar'''
    t[0] = Imprimir(t[3], 'V', t.lineno(1), t.lexpos(3))

def p_print_vacio(t):
    '''PRINT :  rprint apar cpar'''
    t[0] = Imprimir(None, 'F', t.lineno(1), t.lexpos(3))

def p_pritn_ln_vacio(t):
    ''' PRINT : rprintln apar cpar'''
    t[0] = Imprimir(None, 'V', t.lineno(1), t.lexpos(3))

def p_lista_impresiones(t):
    '''IMPRESIONES : IMPRESIONES coma IMPRESION'''
    if t[3] != "":
        t[1].append(t[3])
    t[0] = t[1]

def p_impresiones(t):
    '''IMPRESIONES : IMPRESION'''
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_impresion(t):
    '''IMPRESION : EXP
    '''
    t[0] = t[1]
#------------------------------------------- EXPRESIONES -------------------------------------------
def p_expresion(t):
    '''
    EXP : EXP mas EXP
        | EXP menos EXP
        | EXP por EXP
        | EXP div EXP
        | EXP mod EXP
        | EXP pow EXP
        | EXP mayor EXP
        | EXP menor EXP
        | EXP mayori EXP
        | EXP menori EXP
        | EXP igualigual EXP
        | EXP diferente EXP
        | EXP punto EXP
    '''
    if t[2] =='+':
        t[0] = Aritmetica(OperadorAritmetico.MAS, t[1],t[3], t.lineno(2), t.lexpos(2))
    if t[2] == '-':
        t[0] = Aritmetica(OperadorAritmetico.MENOS, t[1],t[3], t.lineno(2), t.lexpos(2))
    if t[2] == '*':
        t[0] = Aritmetica(OperadorAritmetico.POR, t[1],t[3], t.lineno(2), t.lexpos(2))
    if t[2] == '/':
        t[0] = Aritmetica(OperadorAritmetico.DIV, t[1],t[3], t.lineno(2), t.lexpos(2))
    if t[2] == '^':
        t[0] = Aritmetica(OperadorAritmetico.POW, t[1],t[3], t.lineno(2), t.lexpos(2))
    if t[2] == '%':
        t[0] = Aritmetica(OperadorAritmetico.MOD, t[1],t[3], t.lineno(2), t.lexpos(2))
    if t[2] == '>':
        t[0] = Relacional(OperadorRelacional.MAYORQUE, t[1],t[3], t.lineno(2), t.lexpos(2))
    if t[2] == '<': 
        t[0] = Relacional(OperadorRelacional.MENORQUE, t[1],t[3], t.lineno(2), t.lexpos(2))
    if t[2] == '>=':
        t[0] = Relacional(OperadorRelacional.MAYORIGUAL, t[1],t[3], t.lineno(2), t.lexpos(2))
    if t[2] == '<=': 
        t[0] = Relacional(OperadorRelacional.MENORIGUAL, t[1],t[3], t.lineno(2), t.lexpos(2))
    if t[2] == '==':
        t[0] = Relacional(OperadorRelacional.IGUALIGUAL, t[1],t[3], t.lineno(2), t.lexpos(2))
    if t[2] == '!=': 
        t[0] = Relacional(OperadorRelacional.DIFERENTE, t[1],t[3], t.lineno(2), t.lexpos(2))
    if t[2] == '.':
        t[0] = LlamaStruct(t[1], t[3], t.lineno(1), t.lexpos(1))
#-------------------------------------------------VARIOS--------------------------------------------
def p_expresion_agrupacion(t):
    '''
    EXP : apar EXP cpar
    '''
    t[0] = t[2]

def p_expresion_func(t):
    '''EXP : id apar cpar'''
    t[0] = Retornar(t[1], None, t.lineno(1), t.lexpos(1))

def p_expresion_func_par(t):
    '''EXP : id apar PARAMETROS cpar'''
    t[0] = Retornar(t[1], t[3], t.lineno(1), t.lexpos(1))
#----------------------------------------------------FINALES-----------------------------------------
def p_expresion_identificador(t):
    '''EXP : id'''
    t[0] = Identificador(t[1], t.lineno(1), t.lexpos(1))

def p_expresion_entero(t):
    '''EXP : int'''
    t[0] = Constante(Primitivo(TipoObjeto.ENTERO, t[1]), t.lineno(1), t.lexpos(1))

def p_expresion_decimal(t):
    '''EXP : float'''
    t[0] = Constante(Primitivo(TipoObjeto.DECIMAL, t[1]), t.lineno(1), t.lexpos(1))

def p_expresion_cadena(t):
    '''EXP : cadena'''
    t[0] = Constante(Primitivo(TipoObjeto.CADENA, t[1]), t.lineno(1), t.lexpos(1))

def p_expresion_true(t):
    '''EXP : rtrue'''
    t[0] = Constante(Primitivo(TipoObjeto.BOOLEANO, t[1]), t.lineno(1), t.lexpos(1))

def p_expresion_false(t):
    '''EXP : rfalse'''
    t[0] = Constante(Primitivo(TipoObjeto.BOOLEANO, t[1]), t.lineno(1), t.lexpos(1))

def p_expresion_para_nativas(t):
    '''EXP : ENATIVAS'''
    t[0] = t[1]

def p_expresion_matriz(t):
    '''EXP : id acor EXP ccor'''
    t[0] = LlamaMatriz(t[1], t[3], t.lineno(1), t.lexpos(1))

def p_expresion_matriz2(t):
    '''EXP : id acor EXP ccor acor EXP ccor'''
    t[0] = LlamaMatriz2D(t[1], t[3], t[6], t.lineno(1), t.lexpos(1))

def p_expresion_matriz3(t):
    '''EXP : id acor EXP ccor acor EXP ccor acor EXP ccor'''
    t[0] = LlamaMatriz3D(t[1], t[3], t[6], t[9], t.lineno(1), t.lexpos(1))

#----------------------------------------------------EXPRESIONES NATIVAS-------------------------------------------
def p_exp_nativas(t):
    '''
    ENATIVAS :
            | logd apar EXP cpar
            | ruc apar EXP cpar
            | rlc apar EXP cpar
            | seno apar EXP cpar
            | coseno apar EXP cpar
            | tang apar EXP cpar
            | cuadrado apar EXP cpar
    '''
    if t[1] == 'log10':
        base = Constante(Primitivo(TipoObjeto.ENTERO, 10), t.lineno(1), t.lexpos(1))
        t[0] = Nativas(OperadorNativo.LOGARITMO, t[3], base, t.lineno(1), t.lexpos(1))
    if t[1] == 'uppercase':
        t[0] = Nativas(OperadorNativo.UPPERCASE, t[3], 10, t.lineno(1), t.lexpos(1))
    if t[1] == 'lowercase':
        t[0] = Nativas(OperadorNativo.LOWERCASE, t[3], 10, t.lineno(1), t.lexpos(1))
    if t[1] == 'sin':
        t[0] = Nativas(OperadorNativo.SENO, t[3], 10, t.lineno(1), t.lexpos(1))
    if t[1] == 'cos':
        t[0] = Nativas(OperadorNativo.COSENO, t[3], 10, t.lineno(1), t.lexpos(1))
    if t[1] == 'tan':
        t[0] = Nativas(OperadorNativo.TANGENTE, t[3], 10, t.lineno(1), t.lexpos(1))
    if t[1] == 'sqrt':
        t[0] = Nativas(OperadorNativo.CUADRADA, t[3], 10, t.lineno(1), t.lexpos(1))
        
def p_nativas2(t):
    '''ENATIVAS : rparse apar TIPO coma EXP cpar'''
    t[0] = Parse(t[3], t[5], t.lineno(1), t.lexpos(1))

def p_nativas3(t):
    '''ENATIVAS : rtrunc apar EXP cpar'''
    t[0] = Nativas(OperadorNativo.TRUNC, t[3], None, t.lineno(1), t.lexpos(1))
def p_nativas4(t):
    '''ENATIVAS : rrfloat apar EXP cpar'''
    t[0] = Nativas(OperadorNativo.FLOAT, t[3], None, t.lineno(1), t.lexpos(1))
def p_nativas5(t):
    '''ENATIVAS : rstring apar EXP cpar'''
    t[0] = Nativas(OperadorNativo.STRING, t[3], None, t.lineno(1), t.lexpos(1))
def p_nativas6(t):
    '''ENATIVAS : rtypeof apar EXP cpar'''
    t[0] = Typeof(t[3], t.lineno(1), t.lexpos(1))
def p_nativas7(t):
    '''ENATIVAS : rlength apar EXP cpar'''
    t[0] = Length(t[3], t.lineno(1), t.lexpos(1))

def p_nativas9(t):
    '''ENATIVAS : rpop not apar id cpar'''
    t[0] = Pop(t[4], t.lineno(1), t.lexpos(1))

def p_exp_logb(t):
    '''EXP : logb apar EXP coma EXP cpar'''
    t[0] = Nativas(OperadorNativo.LOGARITMO, t[3], t[5], t.lineno(1), t.lexpos(1))
#-----------------------------------------EXPRESIONES LOGICAS----------------------------------------------
def p_logicas(t):
    '''EXP : EXP and EXP
            | EXP or EXP
    '''
    if t[2] == '&&':
        t[0] = Logica(OperadorLogico.AND, t[1],t[3], t.lineno(2), t.lexpos(2))
    if t[2] == '||':
        t[0] = Logica(OperadorLogico.OR, t[1],t[3], t.lineno(2), t.lexpos(2))

def p_logica_not(t):
    '''EXP : not EXP'''
    t[0] = Logica(OperadorLogico.NOT, t[2], True, t.lineno(2), t.lexpos(2))

#-----------------------------------------------------FIN GRAMATICA--------------------------------------------------------------
import ply.yacc as yacc
parser = yacc.yacc()

def parse(imput, tipo):
    global lexer
    global parser
    lexer = lex.lex(reflags= re.IGNORECASE)
    parser = yacc.yacc()

    instrucciones=parser.parse(imput)
    if tipo == 1:
        entorno = Entorno("global")
        arbol = Arbol()
        for instruccion in instrucciones:
            instruccion.interpretar(arbol, entorno)
        if len(arbol.getExcepciones())> 0:
            f = ""
            for err in arbol.getExcepciones():
                f += err.toString()
            return [f, "<h1>Existen Errores, no se puede mostrar la Tabla de Simbolos</h1>", arbol.generateErrors()]
        return [arbol.getConsola(), arbol.generateTable(), "No hay Errores :D"]     
    elif tipo == 2:
        entorno = Entorno("global")
        arbol = Traductor()
        for instruccion in instrucciones:
            instruccion.traducir(arbol, entorno)
        error = "No hay Errores :D"
        ts = arbol.generateTable()
        codigo =arbol.getImport() + arbol.getEncabezado() + arbol.temporales() + arbol.getMain() + arbol.getCodigo() +"}\n" + arbol.getFuncion() 
        if len(arbol.excepciones) >0:
            error = arbol.generateErrors()
            ts = "Hay Errores No se puede mostrar la tabla de simbolos D:"
        return [codigo, ts, error]
    else:
        grafica = AST()
        ast = ""
        for instruccion in instrucciones:
            ast = instruccion.graficar(grafica)

        return ast