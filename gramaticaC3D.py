import re
import sys

sys.setrecursionlimit(3000)

reservadas = {
    
}

tokens = [
    'int', 'float', 'cadena',
    'mas', 'menos', 'por', 'div',
    'mayor', 'menor', 'mayori', 'menori', 'igualigual', 'diferente',
    'igual', 'apar', 'cpar', 'acor', 'ccor', 'alla', 'clla', 'punto', 'dosp', 'pcoma', 'coma', 'id', 'dot'
] + list(reservadas.values())

# Tokens
t_pcoma         = r';'
t_apar          = r'\('
t_cpar          = r'\)'
t_acor          = r'\['
t_ccor          = r'\]'
t_alla          = r'\{'
t_clla          = r'\}'
t_coma          = r','
t_mas           = r'\+' 
t_menos         = r'-'
t_por           = r'\*'
t_div           = r'\/'
t_igual         = r'='
t_mayor         = r'>'
t_menor         = r'<'
t_mayori        = r'>='
t_menori        = r'<='
t_igualigual    = r'=='
t_dosp          = r'\:'
t_dot           = r'\.'

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
    r'\//.*\n'
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

#IMPORTACIONES
def p_init(t) :
    'init            : id id pcoma INSTRUCCIONES'
    t[0]= "OK marce"#t[1]

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
    '''INSTRUCCION :  ASIGNACIONOPERACION
                    | ASIGNACIONUNICA
                    | ASIGNACIONARREGLO
                    | ASIGNACIONFUNCION
                    | ARREGLOASIGNACION
                    | ETIQUETA
                    | LLAMADAFUNCION
                    | FMT
                    | IF
                    | GOTO
                    | RETURN
                    | IMPORTS
                    | STACK
                    | DECLARACION
                    
    '''
    t[0] = t[1]

def p_imports(t):
    '''IMPORTS : id apar cadena cpar pcoma'''

def p_decstack(t):
    '''STACK : id id acor int ccor id pcoma'''

def p_declara(t):
    '''DECLARACION : id LDEC id pcoma'''

def p_lista_dec(t):
    '''LDEC : LDEC coma id'''

def p_lista_dec2(t):
    '''LDEC : id'''

def p_asignacion1(t):#t0 = S + 0;
    '''ASIGNACIONOPERACION : id igual OPERACION pcoma'''

def p_asignacion2(t):#H = 0; 
    '''ASIGNACIONUNICA : id igual OPERANDO pcoma'''

def p_asignacion3(t):#t10 = stack[int(t9)];
    '''ASIGNACIONARREGLO : id igual id acor id apar id cpar ccor pcoma'''

def p_asignacion4(t):#stack[int(t1)] = 10;
    '''ARREGLOASIGNACION : id acor id apar id cpar ccor igual OPERANDO pcoma'''

def p_etiqueta(t):#L0:
    '''ETIQUETA : id dosp'''

def p_fmt(t):#fmt.Printf("%.2f", t20);
    '''FMT : id dot id apar cadena coma OPERANDO cpar pcoma'''

def p_fmt2(t):#fmt.Printf("%s", "No se puede dividir en cero");
    '''FMT : id dot id apar cadena coma cadena cpar pcoma'''

def p_fmt(t):#fmt.Printf("%.2f", int(bla));
    '''FMT : id dot id apar cadena coma id apar OPERANDO cpar cpar pcoma'''

def p_if(t):#if 5 == 0 { goto L6; }
    '''IF : id CONDICION alla GOTO clla'''

def p_condicion(t):#5 == 0 
    '''CONDICION : OPERANDO mayor OPERANDO
                 | OPERANDO mayori OPERANDO
                 | OPERANDO menor OPERANDO
                 | OPERANDO menori OPERANDO
                 | OPERANDO igualigual OPERANDO
                 | OPERANDO diferente OPERANDO
    '''
def p_goto(t):#goto L6;
    '''GOTO : id id pcoma'''

def p_return(t):#return;
    '''RETURN : id pcoma'''

def p_llamadafn(t):#funcion()
    '''LLAMADAFUNCION : id apar cpar pcoma'''

def p_operacion(t):
    '''OPERACION : OPERANDO mas OPERANDO
                 | OPERANDO menos OPERANDO
                 | OPERANDO por OPERANDO
                 | OPERANDO div OPERANDO
    '''

def p_asingnacionfunc(t):
    '''ASIGNACIONFUNCION : id id apar cpar alla INSTRUCCIONES clla'''

def p_operando(t):#t0
    '''OPERANDO : id'''

def p_operando2(t):#2
    '''OPERANDO : int'''

def p_operando3(t):#2.5
    '''OPERANDO : float'''

def p_operando4(t):#math.Mod(125,5)
    '''OPERANDO : id dot id apar OPERANDO coma OPERANDO cpar'''



#-----------------------------------------------------FIN GRAMATICA--------------------------------------------------------------
import ply.yacc as yacc
parser = yacc.yacc()

def parseopt(imput):
    global errores
    global lexer
    global parser
    global salida
    global raiz
    errores = []
    lexer = lex.lex(reflags= re.IGNORECASE)
    parser = yacc.yacc()
    global input
    input = imput
    instrucciones=parser.parse(imput)
    return [instrucciones, "", ""]
