
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'acor alla apar cadena ccor clla coma cpar diferente div dosp dot float id igual igualigual int mas mayor mayori menor menori menos pcoma por rfloat rfmt rfunc rgoto rif rimport rint rmain rpackage rprintf rreturn rvarinit            : BLOQUESBLOQUES : BLOQUES BLOQUEBLOQUES : BLOQUEBLOQUE : rpackage rmain pcomaBLOQUE : rimport apar cadena cpar pcomaBLOQUE : rvar id acor int ccor rfloat pcomaBLOQUE : rvar IDS rfloat pcomaBLOQUE : rfunc id apar cpar alla INSTRUCCIONES cllaBLOQUE : rfunc rmain apar cpar alla INSTRUCCIONES cllaIDS : IDS coma idIDS : idINSTRUCCIONES : INSTRUCCIONES INSTRUCCIONINSTRUCCIONES : INSTRUCCIONINSTRUCCION : id igual OPERANDO OPERACION OPERANDO pcomaINSTRUCCION : id igual OPERANDO pcomaINSTRUCCION : id igual id acor rint apar id cpar ccor pcomaINSTRUCCION : id acor rint apar id cpar ccor igual OPERANDO pcomaINSTRUCCION : id dospINSTRUCCION : rfmt dot rprintf apar cadena coma rint apar OPERANDO cpar cpar pcomaINSTRUCCION : rfmt dot rprintf apar cadena coma OPERANDO cpar pcomaINSTRUCCION : rfmt dot rprintf apar cadena coma cadena cpar pcomaINSTRUCCION : rif OPERANDO CONDICION OPERANDO alla rgoto id pcoma cllaINSTRUCCION : rgoto id pcomaINSTRUCCION : rreturn pcomaINSTRUCCION : id apar cpar pcomaCONDICION : mayor\n                 | mayori\n                 | menor\n                 | menori\n                 | igualigual\n                 | diferente\n    OPERACION :  mas\n                 |  menos\n                 |  por\n                 |  div\n    OPERANDO : idOPERANDO : intOPERANDO : floatOPERANDO : id dot id apar OPERANDO coma OPERANDO cpar'
    
_lr_action_items = {'rpackage':([0,2,3,8,15,24,28,41,46,55,],[4,4,-3,-2,-4,-7,-5,-6,-8,-9,]),'rimport':([0,2,3,8,15,24,28,41,46,55,],[5,5,-3,-2,-4,-7,-5,-6,-8,-9,]),'rvar':([0,2,3,8,15,24,28,41,46,55,],[6,6,-3,-2,-4,-7,-5,-6,-8,-9,]),'rfunc':([0,2,3,8,15,24,28,41,46,55,],[7,7,-3,-2,-4,-7,-5,-6,-8,-9,]),'$end':([1,2,3,8,15,24,28,41,46,55,],[0,-1,-3,-2,-4,-7,-5,-6,-8,-9,]),'rmain':([4,7,],[9,14,]),'apar':([5,13,14,33,58,60,81,82,97,],[10,20,21,44,77,79,87,88,104,]),'id':([6,7,19,30,31,34,35,37,38,40,42,45,47,54,61,62,63,64,65,66,67,68,69,71,72,73,74,75,76,77,78,87,88,89,91,92,100,102,104,110,112,113,115,116,119,],[11,13,25,33,33,33,-13,50,53,33,56,-18,-12,-24,50,-26,-27,-28,-29,-30,-31,81,-23,50,-15,-32,-33,-34,-35,84,-25,50,94,-14,50,99,50,50,50,-21,-20,-22,-16,-17,-19,]),'pcoma':([9,18,22,32,39,50,51,52,53,56,57,59,83,99,103,105,108,109,114,118,],[15,24,28,41,54,-36,-37,-38,69,-36,72,78,89,106,110,112,115,116,-39,119,]),'cadena':([10,79,91,],[16,85,96,]),'acor':([11,33,56,],[17,43,70,]),'rfloat':([11,12,25,29,],[-11,18,-10,32,]),'coma':([11,12,25,50,51,52,85,93,114,],[-11,19,-10,-36,-37,-38,91,100,-39,]),'cpar':([16,20,21,44,50,51,52,84,94,96,98,107,111,114,117,],[22,26,27,59,-36,-37,-38,90,101,103,105,114,117,-39,118,]),'int':([17,37,42,61,62,63,64,65,66,67,71,73,74,75,76,87,91,100,102,104,],[23,51,51,51,-26,-27,-28,-29,-30,-31,51,-32,-33,-34,-35,51,51,51,51,51,]),'ccor':([23,90,101,],[29,95,108,]),'alla':([26,27,50,51,52,80,114,],[30,31,-36,-37,-38,86,-39,]),'rfmt':([30,31,34,35,40,45,47,54,69,72,78,89,110,112,113,115,116,119,],[36,36,36,-13,36,-18,-12,-24,-23,-15,-25,-14,-21,-20,-22,-16,-17,-19,]),'rif':([30,31,34,35,40,45,47,54,69,72,78,89,110,112,113,115,116,119,],[37,37,37,-13,37,-18,-12,-24,-23,-15,-25,-14,-21,-20,-22,-16,-17,-19,]),'rgoto':([30,31,34,35,40,45,47,54,69,72,78,86,89,110,112,113,115,116,119,],[38,38,38,-13,38,-18,-12,-24,-23,-15,-25,92,-14,-21,-20,-22,-16,-17,-19,]),'rreturn':([30,31,34,35,40,45,47,54,69,72,78,89,110,112,113,115,116,119,],[39,39,39,-13,39,-18,-12,-24,-23,-15,-25,-14,-21,-20,-22,-16,-17,-19,]),'igual':([33,95,],[42,102,]),'dosp':([33,],[45,]),'clla':([34,35,40,45,47,54,69,72,78,89,106,110,112,113,115,116,119,],[46,-13,55,-18,-12,-24,-23,-15,-25,-14,113,-21,-20,-22,-16,-17,-19,]),'dot':([36,50,56,],[48,68,68,]),'float':([37,42,61,62,63,64,65,66,67,71,73,74,75,76,87,91,100,102,104,],[52,52,52,-26,-27,-28,-29,-30,-31,52,-32,-33,-34,-35,52,52,52,52,52,]),'rint':([43,70,91,],[58,82,97,]),'rprintf':([48,],[60,]),'mayor':([49,50,51,52,114,],[62,-36,-37,-38,-39,]),'mayori':([49,50,51,52,114,],[63,-36,-37,-38,-39,]),'menor':([49,50,51,52,114,],[64,-36,-37,-38,-39,]),'menori':([49,50,51,52,114,],[65,-36,-37,-38,-39,]),'igualigual':([49,50,51,52,114,],[66,-36,-37,-38,-39,]),'diferente':([49,50,51,52,114,],[67,-36,-37,-38,-39,]),'mas':([51,52,56,57,114,],[-37,-38,-36,73,-39,]),'menos':([51,52,56,57,114,],[-37,-38,-36,74,-39,]),'por':([51,52,56,57,114,],[-37,-38,-36,75,-39,]),'div':([51,52,56,57,114,],[-37,-38,-36,76,-39,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'BLOQUES':([0,],[2,]),'BLOQUE':([0,2,],[3,8,]),'IDS':([6,],[12,]),'INSTRUCCIONES':([30,31,],[34,40,]),'INSTRUCCION':([30,31,34,40,],[35,35,47,47,]),'OPERANDO':([37,42,61,71,87,91,100,102,104,],[49,57,80,83,93,98,107,109,111,]),'CONDICION':([49,],[61,]),'OPERACION':([57,],[71,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> BLOQUES','init',1,'p_init','gramaticaC3D.py',109),
  ('BLOQUES -> BLOQUES BLOQUE','BLOQUES',2,'p_bloques_lista','gramaticaC3D.py',113),
  ('BLOQUES -> BLOQUE','BLOQUES',1,'p_bloques_final','gramaticaC3D.py',119),
  ('BLOQUE -> rpackage rmain pcoma','BLOQUE',3,'p_instruccion_package','gramaticaC3D.py',126),
  ('BLOQUE -> rimport apar cadena cpar pcoma','BLOQUE',5,'p_instruccion_import','gramaticaC3D.py',130),
  ('BLOQUE -> rvar id acor int ccor rfloat pcoma','BLOQUE',7,'p_declaraheapstack','gramaticaC3D.py',136),
  ('BLOQUE -> rvar IDS rfloat pcoma','BLOQUE',4,'p_declaraciontemporales','gramaticaC3D.py',141),
  ('BLOQUE -> rfunc id apar cpar alla INSTRUCCIONES clla','BLOQUE',7,'p_voids','gramaticaC3D.py',145),
  ('BLOQUE -> rfunc rmain apar cpar alla INSTRUCCIONES clla','BLOQUE',7,'p_main','gramaticaC3D.py',150),
  ('IDS -> IDS coma id','IDS',3,'p_lista_ids','gramaticaC3D.py',155),
  ('IDS -> id','IDS',1,'p_lista_ids2','gramaticaC3D.py',161),
  ('INSTRUCCIONES -> INSTRUCCIONES INSTRUCCION','INSTRUCCIONES',2,'p_instrucciones_lista','gramaticaC3D.py',169),
  ('INSTRUCCIONES -> INSTRUCCION','INSTRUCCIONES',1,'p_instrucciones_final','gramaticaC3D.py',175),
  ('INSTRUCCION -> id igual OPERANDO OPERACION OPERANDO pcoma','INSTRUCCION',6,'p_asignacion1','gramaticaC3D.py',182),
  ('INSTRUCCION -> id igual OPERANDO pcoma','INSTRUCCION',4,'p_asignacion2','gramaticaC3D.py',187),
  ('INSTRUCCION -> id igual id acor rint apar id cpar ccor pcoma','INSTRUCCION',10,'p_asignacion3','gramaticaC3D.py',192),
  ('INSTRUCCION -> id acor rint apar id cpar ccor igual OPERANDO pcoma','INSTRUCCION',10,'p_asignacion4','gramaticaC3D.py',197),
  ('INSTRUCCION -> id dosp','INSTRUCCION',2,'p_etiqueta','gramaticaC3D.py',202),
  ('INSTRUCCION -> rfmt dot rprintf apar cadena coma rint apar OPERANDO cpar cpar pcoma','INSTRUCCION',12,'p_fmt','gramaticaC3D.py',207),
  ('INSTRUCCION -> rfmt dot rprintf apar cadena coma OPERANDO cpar pcoma','INSTRUCCION',9,'p_fmt2','gramaticaC3D.py',212),
  ('INSTRUCCION -> rfmt dot rprintf apar cadena coma cadena cpar pcoma','INSTRUCCION',9,'p_fmt3','gramaticaC3D.py',217),
  ('INSTRUCCION -> rif OPERANDO CONDICION OPERANDO alla rgoto id pcoma clla','INSTRUCCION',9,'p_if','gramaticaC3D.py',222),
  ('INSTRUCCION -> rgoto id pcoma','INSTRUCCION',3,'p_goto','gramaticaC3D.py',227),
  ('INSTRUCCION -> rreturn pcoma','INSTRUCCION',2,'p_return','gramaticaC3D.py',232),
  ('INSTRUCCION -> id apar cpar pcoma','INSTRUCCION',4,'p_llamadafn','gramaticaC3D.py',237),
  ('CONDICION -> mayor','CONDICION',1,'p_condicion','gramaticaC3D.py',243),
  ('CONDICION -> mayori','CONDICION',1,'p_condicion','gramaticaC3D.py',244),
  ('CONDICION -> menor','CONDICION',1,'p_condicion','gramaticaC3D.py',245),
  ('CONDICION -> menori','CONDICION',1,'p_condicion','gramaticaC3D.py',246),
  ('CONDICION -> igualigual','CONDICION',1,'p_condicion','gramaticaC3D.py',247),
  ('CONDICION -> diferente','CONDICION',1,'p_condicion','gramaticaC3D.py',248),
  ('OPERACION -> mas','OPERACION',1,'p_operacion','gramaticaC3D.py',253),
  ('OPERACION -> menos','OPERACION',1,'p_operacion','gramaticaC3D.py',254),
  ('OPERACION -> por','OPERACION',1,'p_operacion','gramaticaC3D.py',255),
  ('OPERACION -> div','OPERACION',1,'p_operacion','gramaticaC3D.py',256),
  ('OPERANDO -> id','OPERANDO',1,'p_operando','gramaticaC3D.py',261),
  ('OPERANDO -> int','OPERANDO',1,'p_operando2','gramaticaC3D.py',265),
  ('OPERANDO -> float','OPERANDO',1,'p_operando3','gramaticaC3D.py',269),
  ('OPERANDO -> id dot id apar OPERANDO coma OPERANDO cpar','OPERANDO',8,'p_operando4','gramaticaC3D.py',273),
]
