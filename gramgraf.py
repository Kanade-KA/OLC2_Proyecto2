from TablaSimbolo.GraficarNodos import GraficarNodos
from TablaSimbolo.NodoArbol import NodoArbol
import sys
sys.setrecursionlimit(3000)

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
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()

precedence = (
    ('left', 'or'),
    ('left', 'and'),
    ('left', 'igualigual', 'diferente'),
    ('left', 'mayori', 'mayor', 'menori', 'menor'),
    ('left', 'mas','menos'),
    ('left', 'por','div', 'mod'),
    ('left', 'pow'),
    ('right', 'not')
)
#IMPORTACIONES

#--------------------------------------------Definición de la Gramatica----------------------------------------------
def p_init(t) :
    'init            : INSTRUCCIONES'
    nodo = NodoArbol("S")
    nodo.addHijos(t[1])
    t[0] = nodo
def p_instrucciones_lista(t):
    'INSTRUCCIONES : INSTRUCCIONES INSTRUCCION'
    nodo = NodoArbol("LINSTRUCCIONES")
    nodo.addHijos(t[1])
    nodo.addHijos(t[2])
    t[0] = nodo
    
def p_instrucciones_final(t):
    'INSTRUCCIONES : INSTRUCCION' 
    t[0]=t[1]

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
    nodoinst = NodoArbol("INSTRUCCION")
    nodoinst.addHijos(t[1])
    t[0] = nodoinst

def p_instruccion_error(t):
    'INSTRUCCION       : error pcoma'
    t[0] = ""
#-----------------------------------STRUCTS------------------------------------------
def p_struct_mutable(t):
    '''STRUCTS : rmutable rstruct id VARIABLES rend pcoma'''
    nodo = NodoArbol("STRUCT")
    nodo.addHijos(NodoArbol("mutable"))
    nodo.addHijos(NodoArbol("struct"))
    nodo.addHijos(NodoArbol(t[3]))
    nodo.addHijos(t[4])
    nodo.addHijos(NodoArbol("end"))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo
def p_struct(t):
    '''STRUCTS : rstruct id VARIABLES rend pcoma'''
    nodo = NodoArbol("STRUCT")
    nodo.addHijos(NodoArbol("struct"))
    nodo.addHijos(NodoArbol(t[2]))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol("end"))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo
def p_struct_variables(t):
    '''VARIABLES : VARIABLES DEC'''
    nodo = NodoArbol("VARIABLES")
    nodo.addHijos(t[1])
    nodo.addHijos(t[2])
    t[0] = nodo

def p_struct_variables2(t):
    '''VARIABLES : DEC'''
    nodo = NodoArbol("VARIABLE")
    nodo.addHijos(t[1])
    t[0] = nodo

def p_declaracionesstructs(t):
    '''DEC : id pcoma'''
    nodo = NodoArbol("DECLARACION")
    nodo.addHijos(NodoArbol(t[1]))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo
def p_declaracionesstructs2(t):
    '''DEC : id dosp dosp TIPO pcoma''' 
    nodo = NodoArbol("DECLARACION")
    nodo.addHijos(NodoArbol(t[1]))
    nodo.addHijos(NodoArbol("::"))
    nodo.addHijos(t[4])
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo
#-----------------------------------------------------------------------------
def p_pushh(t):
    '''PUSH : rpush not apar id coma DATOPUSH cpar'''
    nodo = NodoArbol("PUSH")
    nodo.addHijos(NodoArbol("push!"))
    nodo.addHijos(NodoArbol("("))
    nodo.addHijos(NodoArbol(t[4]))
    nodo.addHijos(NodoArbol(","))
    nodo.addHijos(t[6])
    nodo.addHijos(NodoArbol(")"))
    t[0] = nodo

def p_datopush(t):
    '''DATOPUSH : EXP
                | MATRIZ'''
    t[0] = t[1]
#----------------------------------------------- FUNCIONES -----------------------------------------------
def p_funciones(t):
    '''FUNCION : rfunction id apar cpar INSTRUCCIONES rend pcoma'''
    nodo = NodoArbol("Funcion")
    nodo.addHijos(NodoArbol("function"))
    nodo.addHijos(NodoArbol(t[2]))
    nodo.addHijos(NodoArbol("("))
    nodo.addHijos(NodoArbol(")"))
    nodo.addHijos(t[5])
    nodo.addHijos(NodoArbol("end"))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo
def p_funciones_parametro(t):
    '''FUNCION : rfunction id apar PARAMETROS cpar INSTRUCCIONES rend pcoma'''
    nodo = NodoArbol("Funcion")
    nodo.addHijos(NodoArbol("function"))
    nodo.addHijos(NodoArbol(t[2]))
    nodo.addHijos(NodoArbol("("))
    nodo.addHijos(t[4])
    nodo.addHijos(NodoArbol(")"))
    nodo.addHijos(t[6])
    nodo.addHijos(NodoArbol("end"))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo

def p_llamadafn(t):
    '''LLAMAFN : id apar cpar pcoma'''
    nodo = NodoArbol("LLAMADA")
    nodo.addHijos(NodoArbol(t[1]))
    nodo.addHijos(NodoArbol("("))
    nodo.addHijos(NodoArbol(")"))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo
def p_llamadafn_param(t):
    '''LLAMAFN : id apar PARAMETROS cpar pcoma'''
    nodo = NodoArbol("LLAMADA")
    nodo.addHijos(NodoArbol(t[1]))
    nodo.addHijos(NodoArbol("("))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol(")"))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo

def p_parametros(t):
    '''PARAMETROS : PARAMETROS coma EXP '''
    nodo = NodoArbol("PARAMETROS")
    nodo.addHijos(t[1])
    nodo.addHijos(NodoArbol(","))
    nodo.addHijos(t[3])
    t[0] = nodo
def p_parametros4(t):
    '''PARAMETROS : PARAMETRO'''
    nodo = NodoArbol("PARAMETRO")
    nodo.addHijos(t[1])
    t[0] = nodo 

def p_parametros2(t):
    '''PARAMETRO : EXP '''
    nodoe = NodoArbol("EXP")
    nodoe.addHijos(t[1])
    t[0] = nodoe

def p_parametros3(t):
    '''PARAMETRO : EXP dosp dosp TIPO '''
    nodoe = NodoArbol("EXP")
    nodoe.addHijos(t[1])
    nodoe.addHijos(NodoArbol("::"))
    nodoe.addHijos(t[4])
    t[0] = nodoe

def p_return(t):
    '''RETURN : rreturn pcoma'''
    t[0] = NodoArbol("RETURN")

def p_return1(t):
    '''RETURN : rreturn EXP pcoma'''
    nodo = NodoArbol("RETURN")
    nodo.addHijos(NodoArbol("return"))
    nodoexp = NodoArbol("EXP")
    nodoexp.addHijos(t[2])
    nodo.addHijos(nodoexp)
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo

#------------------------------------------------ FOR --------------------------------------------------------
def p_for_dosp(t):
    '''FOR : rfor EXP rin EXP dosp EXP INSTRUCCIONES rend pcoma'''
    nodo = NodoArbol("FOR")
    nodo.addHijos(NodoArbol("for"))
    #AGREGANDO VARIABLES
    nodovar = NodoArbol("EXP")
    nodovar.addHijos(t[2])
    #AGREGANDO RANGO
    rango1 = NodoArbol("EXP")
    rango1.addHijos(t[4])
    rango2 = NodoArbol("EXP")
    rango2.addHijos(t[6])
    nodorango = NodoArbol(":")
    nodorango.addHijos(rango1)
    nodorango.addHijos(rango2)
    #INSTRUCCIONES
    nodo.addHijos(nodovar)
    nodo.addHijos("in")
    nodo.addHijos(nodorango)
    nodo.addHijos(t[7])
    nodo.addHijos(NodoArbol("end"))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo
def p_for_sindos(t):
    '''FOR : rfor EXP rin EXP INSTRUCCIONES rend pcoma'''
    nodo = NodoArbol("FOR")
    nodo.addHijos(NodoArbol("for"))
    nodoexp = NodoArbol("EXP")
    nodoexp.addHijos(t[2])
    nodo.addHijos(NodoArbol("in"))
    nodoexp2 = NodoArbol("EXP")
    nodoexp2.addHijos(t[4])
    nodo.addHijos(nodoexp)
    nodo.addHijos(nodoexp2)
    nodo.addHijos(t[5])
    nodo.addHijos(NodoArbol("end"))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo
#------------------------------------------ WHILE ---------------------------------------------------
def p_while(t):
    '''WHILE : rwhile EXP INSTRUCCIONES rend pcoma'''
    nodo = NodoArbol("WHILE")
    nodo.addHijos(NodoArbol("while"))
    nodocondicion = NodoArbol("CONDICION")
    nodocondicion.addHijos(t[2])
    nodo.addHijos(nodocondicion)
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol("end"))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo
def p_break(t):
    '''BREAK : rbreak pcoma'''
    t[0] = NodoArbol("BREAK")
def p_continue(t):
    '''CONTINUE : rcontinue pcoma'''
    t[0] = NodoArbol("CONTINUE")
#---------------------------------------------IF------------------------------------------------------------
def p_if0(t):
    '''IF : rif EXP INSTRUCCIONES ELSEIF'''
    nodo = NodoArbol("IF")
    nodo.addHijos(NodoArbol("if"))
    nodoexp = NodoArbol("EXP")
    nodoexp.addHijos(t[2])
    nodo.addHijos(nodoexp)
    nodo.addHijos(t[3])
    nodo.addHijos(t[4])
    t[0] = nodo
def p_if(t):
    '''IF : rif EXP INSTRUCCIONES rend pcoma'''
    nodo = NodoArbol("IF")
    nodo.addHijos(NodoArbol("if"))
    nodoexp = NodoArbol("EXP")
    nodoexp.addHijos(t[2])
    nodo.addHijos(nodoexp)
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol("end"))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo

def p_if2(t):
    '''IF : rif EXP INSTRUCCIONES relse INSTRUCCIONES rend pcoma'''
    nodo = NodoArbol("IF")
    nodo.addHijos(NodoArbol("if"))
    nodoexp = NodoArbol("EXP")
    nodoexp.addHijos(t[2])
    nodo.addHijos(nodoexp)
    nodo.addHijos(t[3])
    nodoelse = NodoArbol("ELSE")
    nodoelse.addHijos(t[5])
    nodo.addHijos(nodoelse)
    nodo.addHijos(NodoArbol("end"))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo
#------------------------------------------------IF VACIO------------------------------------------------------
def p_if4(t):
    '''IF : rif EXP rend pcoma'''
    nodo = NodoArbol("IF")
    nodo.addHijos(NodoArbol("if"))
    nodoexp = NodoArbol("EXP")
    nodoexp.addHijos(t[2])
    nodo.addHijos(nodoexp)
    nodo.addHijos(NodoArbol("end"))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo

def p_if5(t):
    '''IF : rif EXP INSTRUCCIONES relse rend pcoma'''
    nodo = NodoArbol("IF")
    nodo.addHijos(NodoArbol("if"))
    nodoexp = NodoArbol("EXP")
    nodoexp.addHijos(t[2])
    nodo.addHijos(nodoexp)
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol("ELSE"))
    nodo.addHijos(NodoArbol("end"))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo

def p_if6(t):
    '''IF : rif EXP relse rend pcoma'''
    nodo = NodoArbol("IF")
    nodo.addHijos(NodoArbol("if"))
    nodoexp = NodoArbol("EXP")
    nodoexp.addHijos(t[2])
    nodo.addHijos(nodoexp)
    nodoelse = NodoArbol("ELSE")
    nodo.addHijos(nodoelse)
    nodo.addHijos(NodoArbol("end"))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo
def p_if7(t):
    '''IF : rif EXP ELSEIF'''
    nodo = NodoArbol("IF")
    nodo.addHijos(NodoArbol("if"))
    nodoexp = NodoArbol("EXP")
    nodoexp.addHijos(t[2])
    nodo.addHijos(nodoexp)
    nodo.addHijos(t[3])
    t[0] = nodo
#---------------------------------------------------ELSE IF----------------------------------------------------
def p_elseif(t):
    '''ELSEIF : relseif EXP INSTRUCCIONES rend pcoma'''
    nodo = NodoArbol("ELSEIF")
    nodo.addHijos(NodoArbol("elseif"))
    expresion = NodoArbol("EXP")
    expresion.addHijos(t[2])
    nodo.addHijos(expresion)
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol("end"))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo

def p_elseif1(t):
    '''ELSEIF : relseif EXP INSTRUCCIONES relse INSTRUCCIONES rend pcoma'''
    nodo = NodoArbol("ELSEIF")
    nodo.addHijos(NodoArbol("elseif"))
    expresion = NodoArbol("EXP")
    expresion.addHijos(t[2])
    nodo.addHijos(expresion)
    nodo.addHijos(t[3])
    nodoelse = NodoArbol("ELSE")
    nodoelse.addHijos(t[5])
    nodo.addHijos(nodoelse)
    nodo.addHijos(NodoArbol("end"))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo

def p_elseif2(t):
    '''ELSEIF : relseif EXP INSTRUCCIONES ELSEIF'''
    nodo = NodoArbol("ELSEIF")
    nodo.addHijos(NodoArbol("elseif"))
    expresion = NodoArbol("EXP")
    expresion.addHijos(t[2])
    nodo.addHijos(expresion)
    nodo.addHijos(t[3])
    nodo.addHijos(t[4])
    t[0] = nodo
#---------------------------------------------------ELSE IF VACÍOS--------------------------------------------
def p_elseif3(t):
    '''ELSEIF : relseif EXP rend pcoma'''
    nodo = NodoArbol("ELSEIF")
    nodo.addHijos(NodoArbol("elseif"))
    expresion = NodoArbol("EXP")
    expresion.addHijos(t[2])
    nodo.addHijos(expresion)
    nodo.addHijos(NodoArbol("end"))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo

def p_elseif4(t):
    '''ELSEIF : relseif EXP relse INSTRUCCIONES rend pcoma'''
    nodo = NodoArbol("ELSEIF")
    nodo.addHijos(NodoArbol("elseif"))
    expresion = NodoArbol("EXP")
    expresion.addHijos(t[2])
    nodo.addHijos(expresion)
    nodoelse = NodoArbol("ELSE")
    nodoelse.addHijos(t[4])
    nodo.addHijos(nodoelse)
    nodo.addHijos(NodoArbol("end"))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo

def p_elseif5(t):
    '''ELSEIF : relseif EXP INSTRUCCIONES relse rend pcoma'''
    nodo = NodoArbol("ELSEIF")
    nodo.addHijos(NodoArbol("elseif"))
    expresion = NodoArbol("EXP")
    expresion.addHijos(t[2])
    nodo.addHijos(expresion)
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol("else"))
    nodo.addHijos(NodoArbol("end"))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo
def p_elseif6(t):
    '''ELSEIF : relseif EXP relse rend pcoma'''
    nodo = NodoArbol("ELSEIF")
    nodo.addHijos(NodoArbol("elseif"))
    expresion = NodoArbol("EXP")
    expresion.addHijos(t[2])
    nodo.addHijos(expresion)
    nodo.addHijos(NodoArbol("else"))
    nodo.addHijos(NodoArbol("end"))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo
def p_elseif7(t):
    '''ELSEIF : relseif EXP ELSEIF'''
    nodo = NodoArbol("ELSEIF")
    nodo.addHijos(NodoArbol("elseif"))
    expresion = NodoArbol("EXP")
    expresion.addHijos(t[2])
    nodo.addHijos(expresion)
    nodo.addHijos(t[3])
    t[0] = nodo
#-------------------------------------------ASIGNACIONES-------------------------------------------------------------
def p_asignacion_objeto(t):
    '''ASIGNACION : id punto id igual EXP pcoma'''
    nodo = NodoArbol("ASIGNACION")
    nodo.addHijos(NodoArbol(t[1]))
    nodo.addHijos(NodoArbol("."))
    nodo.addHijos(NodoArbol(t[3]))
    nodo.addHijos(NodoArbol("="))
    nodo.addHijos(t[5])
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo
def p_asignacion_tipo(t):
    '''ASIGNACION : id igual EXP dosp dosp TIPO pcoma'''
    nodo = NodoArbol("ASIGNACION")
    nodo.addHijos(NodoArbol(t[1]))
    nodo.addHijos(NodoArbol("="))
    expresion = NodoArbol("EXP")
    expresion.addHijos(t[3])
    nodo.addHijos(expresion)
    nodo.addHijos(NodoArbol("::"))
    nodo.addHijos(t[6])
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo

def p_asignacion(t):
    '''ASIGNACION : id igual EXP pcoma'''
    nodo = NodoArbol("ASIGNACION")
    nodo.addHijos(NodoArbol(t[1]))
    nodo.addHijos(NodoArbol("="))
    expresion = NodoArbol("EXP")
    expresion.addHijos(t[3])
    nodo.addHijos(expresion)
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo

def p_asignacion_local_valor(t):
    '''ASIGNACION : rlocal id igual EXP pcoma'''
    nodo = NodoArbol("ASIGNACION")
    nodo.addHijos(NodoArbol("local"))
    nodo.addHijos(NodoArbol(t[2]))
    nodo.addHijos(NodoArbol("="))
    expresion = NodoArbol("EXP")
    expresion.addHijos(t[4])
    nodo.addHijos(expresion)
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo

def p_asignacion_local_nulo(t):
    '''ASIGNACION : rlocal id pcoma'''
    nodo = NodoArbol("ASIGNACION")
    nodo.addHijos(NodoArbol("local"))
    nodo.addHijos(NodoArbol(t[2]))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo

def p_asignacion_global_valor(t):
    '''ASIGNACION : rglobal id igual EXP pcoma'''
    nodo = NodoArbol("ASIGNACION")
    nodo.addHijos("global")
    nodo.addHijos(NodoArbol(t[2]))
    nodo.addHijos(NodoArbol("="))
    expresion = NodoArbol("EXP")
    expresion.addHijos(t[4])
    nodo.addHijos(expresion)
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo

def p_asignacion_global_nulo(t):
    '''ASIGNACION : rglobal id pcoma'''
    nodo = NodoArbol("ASIGNACION")
    nodo.addHijos(NodoArbol("global"))
    nodo.addHijos(NodoArbol(t[2]))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo
#------------------------------------------------ASIGNACION MATRIZ-----------------------------------------
def p_asignacion_matriz(t):
    '''ASIGNACION : id igual MATRIZ pcoma'''
    nodo = NodoArbol("ASIGNACION")
    nodo.addHijos(NodoArbol(t[1]))
    nodo.addHijos(NodoArbol("="))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo
def p_reasignacion_matriz(t):
    '''ASIGNACION : id acor EXP ccor igual EXP pcoma'''
    nodo = NodoArbol("ASIGNACION")
    nodo.addHijos(NodoArbol(t[1]))
    nodo.addHijos(NodoArbol("["))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol("]"))
    nodo.addHijos(NodoArbol("="))
    nodo.addHijos(t[6])
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo
def p_reasignacion_matriz2(t):
    '''ASIGNACION : id acor EXP ccor acor EXP ccor igual EXP pcoma'''
    nodo = NodoArbol("ASGINACION")
    nodo.addHijos(NodoArbol(t[1]))
    nodo.addHijos(NodoArbol("["))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol("]"))
    nodo.addHijos(NodoArbol("["))
    nodo.addHijos(t[6])
    nodo.addHijos(NodoArbol("]"))
    nodo.addHijos(NodoArbol("="))
    nodo.addHijos(t[9])
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo

def p_reasignacion_matriz3(t):
    '''ASIGNACION : id acor EXP ccor acor EXP ccor acor EXP ccor igual EXP pcoma'''
    nodo = NodoArbol("ASGINACION")
    nodo.addHijos(NodoArbol(t[1]))
    nodo.addHijos(NodoArbol("["))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol("]"))
    nodo.addHijos(NodoArbol("["))
    nodo.addHijos(t[6])
    nodo.addHijos(NodoArbol("]"))
    nodo.addHijos(NodoArbol("["))
    nodo.addHijos(t[9])
    nodo.addHijos(NodoArbol("]"))
    nodo.addHijos(NodoArbol("="))
    nodo.addHijos(t[12])
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo
#--------------------------------------------DE TRES DIMENSIONES---------------------------------------------
def p_asignacion_matriz3(t):
    '''ASIGNACION : id igual  MULT pcoma'''
    nodo = NodoArbol("ASIGNACION")
    nodo.addHijos(NodoArbol(t[1]))
    nodo.addHijos(NodoArbol("="))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo
    
def p_multidimensional(t):
    '''MULT : acor LISTAM ccor'''
    nodo = NodoArbol("MULT")
    nodo.addHijos(NodoArbol("["))
    nodo.addHijos(t[2])
    nodo.addHijos(NodoArbol("["))
    t[0] = nodo
def p_listam(t):
    '''LISTAM : LISTAM coma LISTAM2'''
    nodo = NodoArbol("LISTAM")
    nodo.addHijos(t[1])
    nodo.addHijos(NodoArbol(","))
    nodo.addHijos(t[3])
    t[0] = nodo
def p_listamm(t):
    '''LISTAM : LISTAM2'''
    nodo = NodoArbol("LISTAM")
    nodo.addHijos(t[1])
    t[0] = nodo
def p_listalista(t):
    '''LISTAM2 : MULT'''
    t[0] = t[1]
def p_listalista2(t):
    '''LISTAM2 : EXP'''
    t[0] = t[1]
#------------------------------------------------DE DOS DIMENSIONES------------------------------------------
def p_asignacion_matriz2(t):
    '''ASIGNACION : id acor LMATRIZMATRIZ ccor pcoma'''
    nodo = NodoArbol("ASIGNACION")
    nodo.addHijos(NodoArbol(t[1]))
    nodo.addHijos(NodoArbol("["))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol("]"))
    nodo.addHijos(NodoArbol(";"))
    t[0] = nodo

def p_listamatrices(t):
    '''LMATRIZMATRIZ : LMATRIZMATRIZ coma MATRIZ'''
    nodo = NodoArbol("LMATRIZ")
    nodo.addHijos(t[1])
    nodo.addHijos(NodoArbol(","))
    nodo.addHijos(t[3])
    t[0] = nodo

def p_matrices(t):
    '''LMATRIZMATRIZ : MATRIZ'''
    t[0] = t[1]
#--------------------------------------------------MATRIZ----------------------------------------------------
def p_matriz(t):
    '''MATRIZ : acor LMATRIZ ccor'''
    nodo = NodoArbol("MATRIZ")
    nodo.addHijos(NodoArbol("["))
    nodo.addHijos(t[2])
    nodo.addHijos(NodoArbol("]"))
    t[0] = nodo

def p_l_matriz(t):
    '''LMATRIZ : LMATRIZ coma EXP'''
    nodo = NodoArbol("LMATRIZ")
    nodo.addHijos(t[1])
    nodo.addHijos(NodoArbol(","))
    nodo.addHijos(t[3])
    t[0] = nodo

def p_l_matriz2(t):
    '''LMATRIZ : EXP'''
    nodo = NodoArbol("EXP")
    nodo.addHijos(t[1])
    t[0] = nodo
#------------------------------------------------------TIPO-------------------------------------------------
def p_tipo(t):
    '''TIPO : rstring
            | rfloat
            | rint'''
    t[0]=NodoArbol(t[1].upper())
#------------------------------------------------------IMPRESIONES-------------------------------------------------
def p_print(t):
    '''PRINT :  rprint apar IMPRESIONES cpar'''
    nodo = NodoArbol("IMPRESIONES")
    nodo.addHijos(NodoArbol("print"))
    nodo.addHijos(NodoArbol("("))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol(")"))
    t[0] = nodo

def p_pritn_ln(t):
    ''' PRINT : rprintln apar IMPRESIONES cpar'''
    nodo = NodoArbol("IMPRESIONESLN")
    nodo.addHijos(NodoArbol("println"))
    nodo.addHijos(NodoArbol("("))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol(")"))
    t[0] = nodo

def p_print_vacio(t):
    '''PRINT :  rprint apar cpar'''
    nodo = NodoArbol("IMPRESIONES")
    nodo.addHijos(NodoArbol("print"))
    nodo.addHijos(NodoArbol("("))
    nodo.addHijos(NodoArbol(")"))
    t[0] = nodo

def p_pritn_ln_vacio(t):
    ''' PRINT : rprintln apar cpar'''
    nodo = NodoArbol("IMPRESIONESLN")
    nodo.addHijos(NodoArbol("println"))
    nodo.addHijos(NodoArbol("("))
    nodo.addHijos(NodoArbol(")"))
    t[0] = nodo

def p_lista_impresiones(t):
    '''IMPRESIONES : IMPRESIONES coma IMPRESION'''
    nodo = NodoArbol("IMPRESIONES")
    nodo.addHijos(t[1])
    nodo.addHijos(NodoArbol(","))
    nodo.addHijos(t[3])
    t[0] = nodo

def p_impresiones(t):
    '''IMPRESIONES : IMPRESION'''
    t[0] = t[1]

def p_impresion(t):
    '''IMPRESION : EXP'''
    nodo = NodoArbol("IMPRESION")
    nodo.addHijos(t[1])
    t[0] = nodo
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
    nodo = NodoArbol(NodoArbol(t[2]))
    nodo.addHijos(t[1])
    nodo.addHijos(t[3])
    t[0] = nodo
#-------------------------------------------------VARIOS--------------------------------------------
def p_expresion_agrupacion(t):
    '''EXP : apar EXP cpar'''
    nodo = NodoArbol("EXP")
    nodo.addHijos(NodoArbol("("))
    nodo.addHijos(t[2])
    nodo.addHijos(NodoArbol(")"))
    t[0] = nodo
    
def p_expresion_func(t):
    '''EXP : id apar cpar'''
    nodo = NodoArbol("FUNCION")
    nodo.addHijos(NodoArbol(t[1]))
    nodo.addHijos(NodoArbol("("))
    nodo.addHijos(NodoArbol(")"))
    t[0] = nodo

def p_expresion_func_par(t):
    '''EXP : id apar PARAMETROS cpar'''
    nodo = NodoArbol("FUNCION")
    nodo.addHijos(NodoArbol(t[1]))
    nodo.addHijos(NodoArbol("("))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol(")"))
    t[0] = nodo
#----------------------------------------------------FINALES-----------------------------------------
def p_expresion_identificador(t):
    '''EXP : id'''
    t[0] = NodoArbol(t[1])

def p_expresion_entero(t):
    '''EXP : int'''
    t[0] = NodoArbol(str(t[1]))

def p_expresion_decimal(t):
    '''EXP : float'''
    t[0] = NodoArbol(str(t[1]))
def p_expresion_cadena(t):
    '''EXP : cadena'''
    t[0] = NodoArbol(t[1])

def p_expresion_true(t):
    '''EXP : rtrue'''
    t[0] = NodoArbol("TRUE")

def p_expresion_false(t):
    '''EXP : rfalse'''
    t[0] = NodoArbol("FALSE")

def p_expresion_para_nativas(t):
    '''EXP : ENATIVAS'''
    t[0] = t[1]

def p_expresion_matriz(t):
    '''EXP : id acor EXP ccor'''
    nodo = NodoArbol("EXP")
    nodo.addHijos(NodoArbol(t[1]))
    nodo.addHijos(NodoArbol("["))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol("]"))
    t[0] = nodo

def p_expresion_matriz2(t):
    '''EXP : id acor EXP ccor acor EXP ccor'''
    nodo = NodoArbol("EXP")
    nodo.addHijos(NodoArbol(t[1]))
    nodo.addHijos(NodoArbol("["))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol("]"))
    nodo.addHijos(NodoArbol("["))
    nodo.addHijos(t[6])
    nodo.addHijos(NodoArbol("]"))
    t[0] = nodo

def p_expresion_matriz3(t):
    '''EXP : id acor EXP ccor acor EXP ccor acor EXP ccor'''
    nodo = NodoArbol("EXP")
    nodo.addHijos(NodoArbol(t[1]))
    nodo.addHijos(NodoArbol("["))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol("]"))
    nodo.addHijos(NodoArbol("["))
    nodo.addHijos(t[6])
    nodo.addHijos(NodoArbol("]"))
    nodo.addHijos(NodoArbol("["))
    nodo.addHijos(t[9])
    nodo.addHijos(NodoArbol("]"))
    t[0] = nodo
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
    nodo = NodoArbol("EXP")
    nodo.addHijos(NodoArbol(t[1].upper()))
    nodo.addHijos(NodoArbol("("))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol(")"))
    t[0] = nodo

def p_nativas2(t):
    '''ENATIVAS : rparse apar TIPO coma EXP cpar'''
    nodo = NodoArbol("PARSE")
    nodo.addHijos(NodoArbol("parse"))
    nodo.addHijos(NodoArbol("("))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol(","))
    nodo.addHijos(t[5])
    nodo.addHijos(NodoArbol(")"))
    t[0] = nodo

def p_nativas3(t):
    '''ENATIVAS : rtrunc apar EXP cpar'''
    nodo = NodoArbol("TRUNC")
    nodo.addHijos(NodoArbol("trunc"))
    nodo.addHijos(NodoArbol("("))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol(")"))
    t[0] = nodo
def p_nativas4(t):
    '''ENATIVAS : rrfloat apar EXP cpar'''
    nodo = NodoArbol("FLOAT")
    nodo.addHijos(NodoArbol("float"))
    nodo.addHijos(NodoArbol("("))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol(")"))
    t[0] = nodo
def p_nativas5(t):
    '''ENATIVAS : rstring apar EXP cpar'''
    nodo = NodoArbol("STRING")
    nodo = NodoArbol(NodoArbol("string"))
    nodo.addHijos(NodoArbol("("))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol(")"))
    t[0] = nodo
def p_nativas6(t):
    '''ENATIVAS : rtypeof apar EXP cpar'''
    nodo = NodoArbol("TYPEOF")
    nodo.addHijos(NodoArbol("typeof"))
    nodo.addHijos(NodoArbol("("))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol(")"))
    t[0] = nodo

def p_nativas7(t):
    '''ENATIVAS : rlength apar EXP cpar'''
    nodo = NodoArbol("LENGTH")
    nodo.addHijos(NodoArbol("length"))
    nodo.addHijos(NodoArbol("("))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol(")"))
    t[0] = nodo

def p_nativas9(t):
    '''ENATIVAS : rpop not apar id cpar'''
    nodo = NodoArbol("POP")
    nodo.addHijos(NodoArbol("pop"))
    nodo.addHijos(NodoArbol("!"))
    nodo.addHijos(NodoArbol("("))
    nodo.addHijos(NodoArbol(t[4]))
    nodo.addHijos(NodoArbol(")"))
    t[0] = nodo

def p_exp_logb(t):
    '''EXP : logb apar EXP coma EXP cpar'''
    nodo = NodoArbol("LOG")
    nodo.addHijos(NodoArbol("log"))
    nodo.addHijos(NodoArbol("("))
    nodo.addHijos(t[3])
    nodo.addHijos(NodoArbol(","))
    nodo.addHijos(t[5])
    nodo.addHijos(NodoArbol(")"))
    t[0] = nodo
#-----------------------------------------EXPRESIONES LOGICAS----------------------------------------------
def p_logicas(t):
    '''EXP : EXP and EXP
            | EXP or EXP
    '''
    if t[2] == '&&':
        nodo = NodoArbol("AND")
        nodo.addHijos(t[1])
        nodo.addHijos(NodoArbol("&&"))
        nodo.addHijos(t[3])
        t[0] = nodo
    if t[2] == '||':
        nodo = NodoArbol("OR")
        nodo.addHijos(t[1])
        nodo.addHijos(NodoArbol("||"))
        nodo.addHijos(t[3])
        t[0] = nodo

def p_logica_not(t):
    '''EXP : not EXP'''
    nodo = NodoArbol("NOT")
    nodo.addHijos(NodoArbol("!"))
    nodo.addHijos(t[1])
    t[0] = nodo

#-----------------------------------------------------FIN GRAMATICA--------------------------------------------------------------
import ply.yacc as yacc
parser = yacc.yacc()
graf = GraficarNodos()

def parse(imput) :
    global raiz
    global input
    input = imput
    instrucciones=parser.parse(imput)
    x =graf.GenerarDotG(instrucciones)
    return x