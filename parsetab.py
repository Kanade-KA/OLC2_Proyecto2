
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'acor alla apar cadena ccor clla coma cpar diferente div dosp dot float id igual igualigual int mas mayor mayori menor menori menos pcoma por rfloat rfmt rfunc rgoto rif rimport rint rmain rpackage rprintf rreturn rvarinit            : BLOQUESBLOQUES : BLOQUES BLOQUEBLOQUES : BLOQUEBLOQUE : rpackage rmain pcomaBLOQUE : rimport apar cadena cpar pcomaBLOQUE : rvar id acor int ccor rfloat pcomaBLOQUE : rvar IDS rfloat pcomaBLOQUE : rfunc id apar cpar alla INSTRUCCIONES cllaBLOQUE : rfunc rmain apar cpar alla INSTRUCCIONES cllaIDS : IDS coma idIDS : idINSTRUCCIONES : INSTRUCCIONES INSTRUCCIONINSTRUCCIONES : INSTRUCCIONINSTRUCCION : id igual OPERANDO OPERACION OPERANDO pcomaINSTRUCCION : id igual OPERANDO pcomaINSTRUCCION : id igual id acor rint apar id cpar ccor pcomaINSTRUCCION : id acor rint apar id cpar ccor igual OPERANDO pcomaINSTRUCCION : id acor rint apar int cpar ccor igual OPERANDO pcomaINSTRUCCION : id dospINSTRUCCION : rfmt dot rprintf apar cadena coma rint apar OPERANDO cpar cpar pcomaINSTRUCCION : rfmt dot rprintf apar cadena coma OPERANDO cpar pcomaINSTRUCCION : rfmt dot rprintf apar cadena coma cadena cpar pcomaINSTRUCCION : rif OPERANDO CONDICION OPERANDO alla rgoto id pcoma cllaINSTRUCCION : rgoto id pcomaINSTRUCCION : rreturn pcomaINSTRUCCION : id apar cpar pcomaCONDICION : mayor\n                 | mayori\n                 | menor\n                 | menori\n                 | igualigual\n                 | diferente\n    OPERACION :  mas\n                 |  menos\n                 |  por\n                 |  div\n    OPERANDO : idOPERANDO : intOPERANDO : floatOPERANDO : id dot id apar OPERANDO coma OPERANDO cpar'
    
_lr_action_items = {'rpackage':([0,2,3,8,15,24,28,41,46,55,],[4,4,-3,-2,-4,-7,-5,-6,-8,-9,]),'rimport':([0,2,3,8,15,24,28,41,46,55,],[5,5,-3,-2,-4,-7,-5,-6,-8,-9,]),'rvar':([0,2,3,8,15,24,28,41,46,55,],[6,6,-3,-2,-4,-7,-5,-6,-8,-9,]),'rfunc':([0,2,3,8,15,24,28,41,46,55,],[7,7,-3,-2,-4,-7,-5,-6,-8,-9,]),'$end':([1,2,3,8,15,24,28,41,46,55,],[0,-1,-3,-2,-4,-7,-5,-6,-8,-9,]),'rmain':([4,7,],[9,14,]),'apar':([5,13,14,33,58,60,81,82,100,],[10,20,21,44,77,79,88,89,108,]),'id':([6,7,19,30,31,34,35,37,38,40,42,45,47,54,61,62,63,64,65,66,67,68,69,71,72,73,74,75,76,77,78,88,89,90,93,94,103,105,106,108,115,117,118,120,121,122,125,],[11,13,25,33,33,33,-13,50,53,33,56,-19,-12,-25,50,-27,-28,-29,-30,-31,-32,81,-24,50,-15,-33,-34,-35,-36,84,-26,50,96,-14,50,102,50,50,50,50,-22,-21,-23,-16,-17,-18,-20,]),'pcoma':([9,18,22,32,39,50,51,52,53,56,57,59,83,102,107,109,112,113,114,119,124,],[15,24,28,41,54,-37,-38,-39,69,-37,72,78,90,110,115,117,120,121,122,-40,125,]),'cadena':([10,79,93,],[16,86,99,]),'acor':([11,33,56,],[17,43,70,]),'rfloat':([11,12,25,29,],[-11,18,-10,32,]),'coma':([11,12,25,50,51,52,86,95,119,],[-11,19,-10,-37,-38,-39,93,103,-40,]),'cpar':([16,20,21,44,50,51,52,84,85,96,99,101,111,116,119,123,],[22,26,27,59,-37,-38,-39,91,92,104,107,109,119,123,-40,124,]),'int':([17,37,42,61,62,63,64,65,66,67,71,73,74,75,76,77,88,93,103,105,106,108,],[23,51,51,51,-27,-28,-29,-30,-31,-32,51,-33,-34,-35,-36,85,51,51,51,51,51,51,]),'ccor':([23,91,92,104,],[29,97,98,112,]),'alla':([26,27,50,51,52,80,119,],[30,31,-37,-38,-39,87,-40,]),'rfmt':([30,31,34,35,40,45,47,54,69,72,78,90,115,117,118,120,121,122,125,],[36,36,36,-13,36,-19,-12,-25,-24,-15,-26,-14,-22,-21,-23,-16,-17,-18,-20,]),'rif':([30,31,34,35,40,45,47,54,69,72,78,90,115,117,118,120,121,122,125,],[37,37,37,-13,37,-19,-12,-25,-24,-15,-26,-14,-22,-21,-23,-16,-17,-18,-20,]),'rgoto':([30,31,34,35,40,45,47,54,69,72,78,87,90,115,117,118,120,121,122,125,],[38,38,38,-13,38,-19,-12,-25,-24,-15,-26,94,-14,-22,-21,-23,-16,-17,-18,-20,]),'rreturn':([30,31,34,35,40,45,47,54,69,72,78,90,115,117,118,120,121,122,125,],[39,39,39,-13,39,-19,-12,-25,-24,-15,-26,-14,-22,-21,-23,-16,-17,-18,-20,]),'igual':([33,97,98,],[42,105,106,]),'dosp':([33,],[45,]),'clla':([34,35,40,45,47,54,69,72,78,90,110,115,117,118,120,121,122,125,],[46,-13,55,-19,-12,-25,-24,-15,-26,-14,118,-22,-21,-23,-16,-17,-18,-20,]),'dot':([36,50,56,],[48,68,68,]),'float':([37,42,61,62,63,64,65,66,67,71,73,74,75,76,88,93,103,105,106,108,],[52,52,52,-27,-28,-29,-30,-31,-32,52,-33,-34,-35,-36,52,52,52,52,52,52,]),'rint':([43,70,93,],[58,82,100,]),'rprintf':([48,],[60,]),'mayor':([49,50,51,52,119,],[62,-37,-38,-39,-40,]),'mayori':([49,50,51,52,119,],[63,-37,-38,-39,-40,]),'menor':([49,50,51,52,119,],[64,-37,-38,-39,-40,]),'menori':([49,50,51,52,119,],[65,-37,-38,-39,-40,]),'igualigual':([49,50,51,52,119,],[66,-37,-38,-39,-40,]),'diferente':([49,50,51,52,119,],[67,-37,-38,-39,-40,]),'mas':([51,52,56,57,119,],[-38,-39,-37,73,-40,]),'menos':([51,52,56,57,119,],[-38,-39,-37,74,-40,]),'por':([51,52,56,57,119,],[-38,-39,-37,75,-40,]),'div':([51,52,56,57,119,],[-38,-39,-37,76,-40,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'BLOQUES':([0,],[2,]),'BLOQUE':([0,2,],[3,8,]),'IDS':([6,],[12,]),'INSTRUCCIONES':([30,31,],[34,40,]),'INSTRUCCION':([30,31,34,40,],[35,35,47,47,]),'OPERANDO':([37,42,61,71,88,93,103,105,106,108,],[49,57,80,83,95,101,111,113,114,116,]),'CONDICION':([49,],[61,]),'OPERACION':([57,],[71,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> BLOQUES','init',1,'p_init','gramaticaC3D.py',111),
  ('BLOQUES -> BLOQUES BLOQUE','BLOQUES',2,'p_bloques_lista','gramaticaC3D.py',115),
  ('BLOQUES -> BLOQUE','BLOQUES',1,'p_bloques_final','gramaticaC3D.py',121),
  ('BLOQUE -> rpackage rmain pcoma','BLOQUE',3,'p_instruccion_package','gramaticaC3D.py',128),
  ('BLOQUE -> rimport apar cadena cpar pcoma','BLOQUE',5,'p_instruccion_import','gramaticaC3D.py',132),
  ('BLOQUE -> rvar id acor int ccor rfloat pcoma','BLOQUE',7,'p_declaraheapstack','gramaticaC3D.py',138),
  ('BLOQUE -> rvar IDS rfloat pcoma','BLOQUE',4,'p_declaraciontemporales','gramaticaC3D.py',143),
  ('BLOQUE -> rfunc id apar cpar alla INSTRUCCIONES clla','BLOQUE',7,'p_voids','gramaticaC3D.py',147),
  ('BLOQUE -> rfunc rmain apar cpar alla INSTRUCCIONES clla','BLOQUE',7,'p_main','gramaticaC3D.py',152),
  ('IDS -> IDS coma id','IDS',3,'p_lista_ids','gramaticaC3D.py',157),
  ('IDS -> id','IDS',1,'p_lista_ids2','gramaticaC3D.py',163),
  ('INSTRUCCIONES -> INSTRUCCIONES INSTRUCCION','INSTRUCCIONES',2,'p_instrucciones_lista','gramaticaC3D.py',171),
  ('INSTRUCCIONES -> INSTRUCCION','INSTRUCCIONES',1,'p_instrucciones_final','gramaticaC3D.py',177),
  ('INSTRUCCION -> id igual OPERANDO OPERACION OPERANDO pcoma','INSTRUCCION',6,'p_asignacion1','gramaticaC3D.py',184),
  ('INSTRUCCION -> id igual OPERANDO pcoma','INSTRUCCION',4,'p_asignacion2','gramaticaC3D.py',189),
  ('INSTRUCCION -> id igual id acor rint apar id cpar ccor pcoma','INSTRUCCION',10,'p_asignacion3','gramaticaC3D.py',194),
  ('INSTRUCCION -> id acor rint apar id cpar ccor igual OPERANDO pcoma','INSTRUCCION',10,'p_asignacion4','gramaticaC3D.py',199),
  ('INSTRUCCION -> id acor rint apar int cpar ccor igual OPERANDO pcoma','INSTRUCCION',10,'p_asignacion5','gramaticaC3D.py',204),
  ('INSTRUCCION -> id dosp','INSTRUCCION',2,'p_etiqueta','gramaticaC3D.py',209),
  ('INSTRUCCION -> rfmt dot rprintf apar cadena coma rint apar OPERANDO cpar cpar pcoma','INSTRUCCION',12,'p_fmt','gramaticaC3D.py',214),
  ('INSTRUCCION -> rfmt dot rprintf apar cadena coma OPERANDO cpar pcoma','INSTRUCCION',9,'p_fmt2','gramaticaC3D.py',219),
  ('INSTRUCCION -> rfmt dot rprintf apar cadena coma cadena cpar pcoma','INSTRUCCION',9,'p_fmt3','gramaticaC3D.py',224),
  ('INSTRUCCION -> rif OPERANDO CONDICION OPERANDO alla rgoto id pcoma clla','INSTRUCCION',9,'p_if','gramaticaC3D.py',229),
  ('INSTRUCCION -> rgoto id pcoma','INSTRUCCION',3,'p_goto','gramaticaC3D.py',234),
  ('INSTRUCCION -> rreturn pcoma','INSTRUCCION',2,'p_return','gramaticaC3D.py',239),
  ('INSTRUCCION -> id apar cpar pcoma','INSTRUCCION',4,'p_llamadafn','gramaticaC3D.py',244),
  ('CONDICION -> mayor','CONDICION',1,'p_condicion','gramaticaC3D.py',250),
  ('CONDICION -> mayori','CONDICION',1,'p_condicion','gramaticaC3D.py',251),
  ('CONDICION -> menor','CONDICION',1,'p_condicion','gramaticaC3D.py',252),
  ('CONDICION -> menori','CONDICION',1,'p_condicion','gramaticaC3D.py',253),
  ('CONDICION -> igualigual','CONDICION',1,'p_condicion','gramaticaC3D.py',254),
  ('CONDICION -> diferente','CONDICION',1,'p_condicion','gramaticaC3D.py',255),
  ('OPERACION -> mas','OPERACION',1,'p_operacion','gramaticaC3D.py',260),
  ('OPERACION -> menos','OPERACION',1,'p_operacion','gramaticaC3D.py',261),
  ('OPERACION -> por','OPERACION',1,'p_operacion','gramaticaC3D.py',262),
  ('OPERACION -> div','OPERACION',1,'p_operacion','gramaticaC3D.py',263),
  ('OPERANDO -> id','OPERANDO',1,'p_operando','gramaticaC3D.py',268),
  ('OPERANDO -> int','OPERANDO',1,'p_operando2','gramaticaC3D.py',272),
  ('OPERANDO -> float','OPERANDO',1,'p_operando3','gramaticaC3D.py',276),
  ('OPERANDO -> id dot id apar OPERANDO coma OPERANDO cpar','OPERANDO',8,'p_operando4','gramaticaC3D.py',280),
]
