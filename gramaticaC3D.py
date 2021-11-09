import re
import sys
from Optimizacion.BloqueDeclaracion import BloqueDeclaracion
from Optimizacion.BloqueMetodo import BloqueMetodo
from Optimizacion.BloqueNormal import BloqueNormal
from Optimizacion.Optimizar import Optimizar
#-----------------------IMPORTACION CLASES DE OPTIMIZACION------------
from Optimizacion.TipoCodigo import TipoBloque
from Optimizacion.TipoCodigo import TipoInstruccion
from Optimizacion.AsignacionOperacion import AsignacionOperacion
from Optimizacion.ArregloAsignacion import ArregloAsignacion
from Optimizacion.AsignacionArreglo import AsignacionArreglo
from Optimizacion.AsignacionSimple import AsignacionSimple
from Optimizacion.Etiqueta import Etiqueta
from Optimizacion.Goto import Goto
from Optimizacion.If import If
from Optimizacion.LlamadaFuncion import LlamadaFuncion
from Optimizacion.Print import Print
from Optimizacion.Return import Return

sys.setrecursionlimit(3000)

reservadas = {
    'fmt'       : 'rfmt',
    'printf'    : 'rprintf',
    'float64'   : 'rfloat',
    'import'    : 'rimport',
    'var'       : 'rvar',
    'package'   : 'rpackage',
    'int'       : 'rint',
    'main'      : 'rmain',
    'func'      : 'rfunc',
    'return'    : 'rreturn',
    'goto'      : 'rgoto',
    'if'        : 'rif'
}

tokens = [
    'int', 'float', 'cadena', 'mas', 'menos', 'por', 'div', 'mayor', 'menor', 'mayori', 'menori', 'igualigual', 
    'diferente',  'igual', 'apar', 'cpar', 'acor', 'ccor', 'alla', 'clla', 'dosp', 'pcoma', 'coma', 'id', 'dot'
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

#--------------------GRAMATICA--------------------------------------------------
def p_init(t) :
    'init            : BLOQUES'
    t[0]= t[1]

def p_bloques_lista(t):
    'BLOQUES : BLOQUES BLOQUE'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]
    
def p_bloques_final(t):
    'BLOQUES : BLOQUE' 
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]
#-------------------------BLOQUES-------------------------------------------------
def p_instruccion_package(t):#package main;
    '''BLOQUE : rpackage rmain pcoma'''
    t[0] = BloqueNormal(t.lineno(1), t.lexpos(1), "package main;", TipoBloque.PACKAGE)

def p_instruccion_import(t):#import ("fmt");
    '''BLOQUE : rimport apar cadena cpar pcoma'''
    codigo = "import (\""+t[3]+"\");"
    t[0] = BloqueNormal(t.lineno(1), t.lexpos(1), codigo, TipoBloque.IMPORT)


def p_declaraheapstack(t):#var stack [19121997]float64;
    '''BLOQUE : rvar id acor int ccor rfloat pcoma'''
    codigo = "var "+t[2]+"[19121997]float64;"
    t[0] = BloqueNormal(t.lineno(1), t.lexpos(1), codigo, TipoBloque.ARREGLO)

def p_declaraciontemporales(t):#var S, H float64;
    '''BLOQUE : rvar IDS rfloat pcoma'''
    t[0] = BloqueDeclaracion(t[2], t.lineno(1), t.lexpos(1), "", TipoBloque.DECLARA)

def p_voids(t):#func suma() { ins .. }
    '''BLOQUE : rfunc id apar cpar alla INSTRUCCIONES clla'''
    codigo = "func "+str(t[2])+"() { "
    t[0] = BloqueMetodo(t[2], t[6], t.lineno(1), t.lexpos(1), codigo, TipoBloque.VOID)

def p_main(t):#func main() { ins .. }
    '''BLOQUE : rfunc rmain apar cpar alla INSTRUCCIONES clla'''
    codigo = "func main() { "
    t[0] = BloqueMetodo(t[2], t[6], t.lineno(1), t.lexpos(1), codigo, TipoBloque.MAIN)

def p_lista_ids(t):
    '''IDS : IDS coma id'''
    if t[2] != "":
        t[1].append(t[3])
    t[0] = t[1]

def p_lista_ids2(t):
    '''IDS : id'''
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

#-------------------------INSTRUCCIONES-------------------------------
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

def p_asignacion1(t):#t0 = S + 0;
    '''INSTRUCCION : id igual OPERANDO OPERACION OPERANDO pcoma'''
    codigo = str(t[1]) + " = "+str(t[3])+" "+str(t[4])+" "+str(t[5])+";"
    t[0] = AsignacionOperacion(t[1], t[3], t[5], t[4], t.lineno(1), t.lexpos(1), codigo, TipoInstruccion.ASIGNACIONOPERACION)

def p_asignacion2(t):#H = 0; 
    '''INSTRUCCION : id igual OPERANDO pcoma'''
    codigo = str(t[1])+" = "+ str(t[3]) + ";"
    t[0] = AsignacionSimple(t[1], t[3], t.lineno(1), t.lexpos(1), codigo, TipoInstruccion.ASIGNACIONSIMPLE)

def p_asignacion3(t):#t10 = stack[int(t9)];
    '''INSTRUCCION : id igual id acor rint apar id cpar ccor pcoma'''
    codigo = str(t[1]) + " = "+str(t[3])+"[ int("+str(t[7])+")];"
    t[0] = AsignacionArreglo(t[1], t.lineno(1), t.lexpos(1), codigo, TipoInstruccion.ASIGNACIONARREGLO)

def p_asignacion4(t):#stack[int(t1)] = 10;
    '''INSTRUCCION : id acor rint apar id cpar ccor igual OPERANDO pcoma'''
    codigo = str(t[1])+"[int("+str(t[5])+")] = "+ str(t[9])+";"
    t[0] = ArregloAsignacion(t[1], t[5], t.lineno(1), t.lexpos(1), codigo, TipoInstruccion.ARREGLOASIGNACION)

def p_etiqueta(t):#L0:
    '''INSTRUCCION : id dosp'''
    codigo = str(t[1])+":"
    t[0] = Etiqueta(t[1], t.lineno(1), t.lexpos(1), codigo, TipoInstruccion.ETIQUETA)

def p_fmt(t):#fmt.Printf("%.2f", int(bla));
    '''INSTRUCCION : rfmt dot rprintf apar cadena coma rint apar OPERANDO cpar cpar pcoma'''
    codigo = "fmt.Printf(\""+str(t[5])+"\", int("+str(t[9])+"));"
    t[0] = Print(t.lineno(1), t.lexpos(1), codigo, TipoInstruccion.FMT)

def p_fmt2(t):#fmt.Printf("%.2f", t20);
    '''INSTRUCCION : rfmt dot rprintf apar cadena coma OPERANDO cpar pcoma'''
    codigo = "fmt.Printf(\""+str(t[5])+"\", "+str(t[7])+");"
    t[0] = Print(t.lineno(1), t.lexpos(1), codigo, TipoInstruccion.FMT)

def p_fmt3(t):#fmt.Printf("%s", "No se puede dividir en cero");
    '''INSTRUCCION : rfmt dot rprintf apar cadena coma cadena cpar pcoma'''
    codigo = "fmt.Printf(\""+str(t[5])+"\", "+str(t[7])+");"
    t[0] = Print(t.lineno(1), t.lexpos(1), codigo, TipoInstruccion.FMT)

def p_if(t):#if 5 == 0 { goto L6; }
    '''INSTRUCCION : rif OPERANDO CONDICION OPERANDO alla rgoto id pcoma clla'''
    codigo = "if "+str(t[2])+" "+ str(t[3])+" "+ str(t[4]) + "{ goto "+ str(t[7])+ "; };"
    t[0] = If(t[2], t[4], t[3], t[7], t.lineno(1), t.lexpos(1), codigo, TipoInstruccion.IF)

def p_goto(t):#goto L6;
    '''INSTRUCCION : rgoto id pcoma'''
    codigo = "goto "+str(t[2])+";"
    t[0] = Goto(t[2], t.lineno(1), t.lexpos(1), codigo, TipoInstruccion.GOTO)

def p_return(t):#return;
    '''INSTRUCCION : rreturn pcoma'''
    codigo = "return;"
    t[0] = Return(t.lineno(1), t.lexpos(1), codigo, TipoInstruccion.RETURN)

def p_llamadafn(t):#funcion()
    '''INSTRUCCION : id apar cpar pcoma'''
    codigo = str(t[1])+"();"
    t[0] = LlamadaFuncion(t[1], t.lineno(1), t.lexpos(1), codigo, TipoInstruccion.METODO)

#-----------------------CONDICIONES----------------------------
def p_condicion(t):#5 == 0 
    '''CONDICION : mayor
                 | mayori
                 | menor
                 | menori
                 | igualigual
                 | diferente
    '''
    t[0] = t[1]
#-----------------------------OPERACIÓN-------------------------
def p_operacion(t):
    '''OPERACION :  mas
                 |  menos
                 |  por
                 |  div
    '''
    t[0] = t[1]
#-------------------------OPERANDOS FINALES-----------------------------
def p_operando(t):#t0
    '''OPERANDO : id'''
    t[0] = t[1]

def p_operando2(t):#2
    '''OPERANDO : int'''
    t[0] = t[1]

def p_operando3(t):#2.5
    '''OPERANDO : float'''
    t[0] = t[1]

def p_operando4(t):#math.Mod(125,5)
    '''OPERANDO : id dot id apar OPERANDO coma OPERANDO cpar'''
    t[0] = "math.Mod("+str(t[5])+", "+str(t[7])+")"

#-----------------------------------------------------FIN GRAMATICA--------------------------------------------------------------
#---IMPORTACIONES-----
import ply.yacc as yacc
parser = yacc.yacc()

import ply.lex as lex
lexer = lex.lex()

def parseopt(imput):
    global errores
    global lexer
    global parser
    global salida
    global raiz
    reglas = []
    lexer = lex.lex()
    parser = yacc.yacc()
    global input
    input = imput
    
    instrucciones=parser.parse(imput)
    c3d = ""
    reporte = ""
    optimizador = Optimizar(instrucciones, reglas)
    optimizador.Ejecutar()
    reporte = optimizador.ReporteOptimizacion(reglas)

    for ins in instrucciones:
        print("INSTRUCCIONES: ", ins)
        c3d += ins.getC3D()+"\n"
        if ins.getTipo() == TipoBloque.MAIN or ins.getTipo()== TipoBloque.VOID:
            for bloque in ins.getInstrucciones():
                c3d += bloque.getC3D()+"\n"
            c3d+="}\n"

    return [c3d, "", reporte]

 