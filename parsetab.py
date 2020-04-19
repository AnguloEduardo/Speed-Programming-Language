
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'SLR'

_lr_signature = 'AND ARRAY AS ASSIGN CLS COMMA CUBE DIM DIVIDE DO ELSE END ENDIF ENDO ENDSUB EQUAL FLOAT FOR GOSUB GT GTE GTGT ID IF INPUT LBRACKET LET LOOPUNTIL LPARENT LT LTE MATRIX MINUS NE NEXT NOT NUMBER OR PLUS PRINT PROGRAM RBRACKET RPARENT SEMMICOLON STRING SUBPROCEDURE THEN TIMES TO WHEND WHILE WORD\n\tprogram : PROGRAM ID V SP X END\n\t\n\tV : DIM IDLIST AS TIPO SEMMICOLON V\n\t|\n\t\n\tIDLIST : ID\n\t| IDLIST COMMA ID\n\t|\n\t\n\tTIPO : WORD\n\t| FLOAT\n\t| ARRAY LBRACKET E RBRACKET\n\t| MATRIX LBRACKET E RBRACKET LBRACKET E RBRACKET\n\t| CUBE LBRACKET E RBRACKET LBRACKET E RBRACKET LBRACKET E RBRACKET\n\t\n\tSP : SUBPROCEDURE ID V X ENDSUB SEMMICOLON SP\n\t|\n\t\n\tX : S SEMMICOLON X\n\t|\n\t\n\tS : LET E ASSIGN E\n\t| PRINT Q\n\t| INPUT TEXT GTGT U\n\t| CLS\n\t| IF EL THEN X ELSE1 ENDIF\n\t| WHILE EL X WHEND\n\t| DO X LOOPUNTIL EL ENDO\n\t| FOR O TO E X NEXT\n\t| GOSUB ID\n\t\n\tO : E\n\t| E ASSIGN E\n\t\n\tU : ID\n\t| ID LBRACKET E RBRACKET\n\t| ID LBRACKET E RBRACKET LBRACKET E RBRACKET\n\t| ID LBRACKET E RBRACKET LBRACKET E RBRACKET LBRACKET E RBRACKET\n\t\n\tQ : LPARENT U RPARENT\n\t| TEXT\n\t\n    TEXT : LPARENT STRING H RPARENT\n    |\n    \n\tH : PLUS STRING H\n\t| PLUS U H\n\t|\n\t\n\tELSE1 : ELSE X\n\t|\n\t\n\tE : E PLUS T\n\t| E MINUS T\n\t| T\n\t\n\tT : T TIMES F\n\t| T DIVIDE F\n\t| F\n\t\n\tF : NUMBER\n\t| U\n\t| LPARENT E RPARENT\n\t\n\tEL : EL OR TL\n\t| NOT TL\n\t| TL\n\t\n\tTL : TL AND FL\n\t| FL\n\t\n\tFL : K OPREL K\n\t| LPARENT EL RPARENT\n\t\n\tOPREL : LT\n\t| LTE\n\t| GT\n\t| GTE\n\t| NE\n\t| EQUAL\n\t\n\tK : ID\n\t| NUMBER\n\t'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,24,],[0,-1,]),'ID':([2,5,7,12,16,17,19,20,23,31,34,40,43,60,61,62,63,64,66,69,71,72,74,75,76,77,78,79,80,83,84,85,88,89,90,100,128,135,136,143,144,],[3,9,21,32,44,44,32,50,58,32,32,44,44,32,32,32,32,32,32,32,44,44,44,-56,-57,-58,-59,-60,-61,44,32,32,32,32,32,32,32,32,32,32,32,]),'DIM':([3,21,87,],[5,5,5,]),'SUBPROCEDURE':([3,4,21,87,112,124,],[-3,7,-3,-3,-2,7,]),'LET':([3,4,6,18,21,25,27,28,29,30,32,39,41,44,45,46,51,70,73,87,92,93,94,95,96,103,104,105,106,109,112,116,121,124,134,140,147,],[-3,-13,12,12,-3,12,-42,-45,-46,-47,-27,-51,-53,-62,-63,12,12,12,-50,-3,-40,-41,-43,-44,-48,-49,-52,-54,-55,12,-2,-28,12,-13,-12,-29,-30,]),'PRINT':([3,4,6,18,21,25,27,28,29,30,32,39,41,44,45,46,51,70,73,87,92,93,94,95,96,103,104,105,106,109,112,116,121,124,134,140,147,],[-3,-13,13,13,-3,13,-42,-45,-46,-47,-27,-51,-53,-62,-63,13,13,13,-50,-3,-40,-41,-43,-44,-48,-49,-52,-54,-55,13,-2,-28,13,-13,-12,-29,-30,]),'INPUT':([3,4,6,18,21,25,27,28,29,30,32,39,41,44,45,46,51,70,73,87,92,93,94,95,96,103,104,105,106,109,112,116,121,124,134,140,147,],[-3,-13,14,14,-3,14,-42,-45,-46,-47,-27,-51,-53,-62,-63,14,14,14,-50,-3,-40,-41,-43,-44,-48,-49,-52,-54,-55,14,-2,-28,14,-13,-12,-29,-30,]),'CLS':([3,4,6,18,21,25,27,28,29,30,32,39,41,44,45,46,51,70,73,87,92,93,94,95,96,103,104,105,106,109,112,116,121,124,134,140,147,],[-3,-13,15,15,-3,15,-42,-45,-46,-47,-27,-51,-53,-62,-63,15,15,15,-50,-3,-40,-41,-43,-44,-48,-49,-52,-54,-55,15,-2,-28,15,-13,-12,-29,-30,]),'IF':([3,4,6,18,21,25,27,28,29,30,32,39,41,44,45,46,51,70,73,87,92,93,94,95,96,103,104,105,106,109,112,116,121,124,134,140,147,],[-3,-13,16,16,-3,16,-42,-45,-46,-47,-27,-51,-53,-62,-63,16,16,16,-50,-3,-40,-41,-43,-44,-48,-49,-52,-54,-55,16,-2,-28,16,-13,-12,-29,-30,]),'WHILE':([3,4,6,18,21,25,27,28,29,30,32,39,41,44,45,46,51,70,73,87,92,93,94,95,96,103,104,105,106,109,112,116,121,124,134,140,147,],[-3,-13,17,17,-3,17,-42,-45,-46,-47,-27,-51,-53,-62,-63,17,17,17,-50,-3,-40,-41,-43,-44,-48,-49,-52,-54,-55,17,-2,-28,17,-13,-12,-29,-30,]),'DO':([3,4,6,18,21,25,27,28,29,30,32,39,41,44,45,46,51,70,73,87,92,93,94,95,96,103,104,105,106,109,112,116,121,124,134,140,147,],[-3,-13,18,18,-3,18,-42,-45,-46,-47,-27,-51,-53,-62,-63,18,18,18,-50,-3,-40,-41,-43,-44,-48,-49,-52,-54,-55,18,-2,-28,18,-13,-12,-29,-30,]),'FOR':([3,4,6,18,21,25,27,28,29,30,32,39,41,44,45,46,51,70,73,87,92,93,94,95,96,103,104,105,106,109,112,116,121,124,134,140,147,],[-3,-13,19,19,-3,19,-42,-45,-46,-47,-27,-51,-53,-62,-63,19,19,19,-50,-3,-40,-41,-43,-44,-48,-49,-52,-54,-55,19,-2,-28,19,-13,-12,-29,-30,]),'GOSUB':([3,4,6,18,21,25,27,28,29,30,32,39,41,44,45,46,51,70,73,87,92,93,94,95,96,103,104,105,106,109,112,116,121,124,134,140,147,],[-3,-13,20,20,-3,20,-42,-45,-46,-47,-27,-51,-53,-62,-63,20,20,20,-50,-3,-40,-41,-43,-44,-48,-49,-52,-54,-55,20,-2,-28,20,-13,-12,-29,-30,]),'END':([3,4,6,10,18,21,25,46,51,59,70,87,109,112,121,124,134,],[-3,-13,-15,24,-15,-3,-15,-15,-15,-14,-15,-3,-15,-2,-15,-13,-12,]),'ENDSUB':([3,6,18,21,25,46,51,59,70,86,87,109,112,121,],[-3,-15,-15,-3,-15,-15,-15,-14,-15,111,-3,-15,-2,-15,]),'AS':([5,8,9,58,],[-6,22,-4,-5,]),'COMMA':([5,8,9,58,],[-6,23,-4,-5,]),'ELSE':([6,18,25,46,51,59,70,102,109,121,],[-15,-15,-15,-15,-15,-14,-15,121,-15,-15,]),'ENDIF':([6,18,25,46,51,59,70,102,109,120,121,132,],[-15,-15,-15,-15,-15,-14,-15,-39,-15,131,-15,-38,]),'WHEND':([6,18,25,39,41,44,45,46,51,59,70,73,82,103,104,105,106,109,121,],[-15,-15,-15,-51,-53,-62,-63,-15,-15,-14,-15,-50,107,-49,-52,-54,-55,-15,-15,]),'LOOPUNTIL':([6,18,25,46,47,51,59,70,109,121,],[-15,-15,-15,-15,83,-15,-14,-15,-15,-15,]),'NEXT':([6,18,25,27,28,29,30,32,46,51,59,70,92,93,94,95,96,109,116,121,123,140,147,],[-15,-15,-15,-42,-45,-46,-47,-27,-15,-15,-14,-15,-40,-41,-43,-44,-48,-15,-28,-15,133,-29,-30,]),'SEMMICOLON':([11,13,14,15,27,28,29,30,32,33,35,50,52,53,54,91,92,93,94,95,96,98,101,107,111,116,117,122,125,131,133,140,141,147,148,],[25,-34,-34,-19,-42,-45,-46,-47,-27,-17,-32,-24,87,-7,-8,-16,-40,-41,-43,-44,-48,-31,-18,-21,124,-28,-33,-22,-9,-20,-23,-29,-10,-30,-11,]),'NUMBER':([12,16,17,19,31,40,43,60,61,62,63,64,66,71,72,74,75,76,77,78,79,80,83,84,85,88,89,90,128,135,136,143,144,],[29,45,45,29,29,45,45,29,29,29,29,29,29,45,45,45,-56,-57,-58,-59,-60,-61,45,29,29,29,29,29,29,29,29,29,29,]),'LPARENT':([12,13,14,16,17,19,31,40,43,60,61,62,63,64,66,71,72,83,84,85,88,89,90,128,135,136,143,144,],[31,34,37,43,43,31,31,43,43,31,31,31,31,31,31,43,43,43,31,31,31,31,31,31,31,31,31,31,]),'GTGT':([13,14,36,117,],[-34,-34,69,-33,]),'NOT':([16,17,43,83,],[40,40,40,40,]),'WORD':([22,],[53,]),'FLOAT':([22,],[54,]),'ARRAY':([22,],[55,]),'MATRIX':([22,],[56,]),'CUBE':([22,],[57,]),'ASSIGN':([26,27,28,29,30,32,49,92,93,94,95,96,116,140,147,],[60,-42,-45,-46,-47,-27,85,-40,-41,-43,-44,-48,-28,-29,-30,]),'PLUS':([26,27,28,29,30,32,49,65,68,91,92,93,94,95,96,97,109,110,113,114,115,116,118,119,137,138,139,140,145,146,147,],[61,-42,-45,-46,-47,-27,61,61,100,61,-40,-41,-43,-44,-48,61,61,61,61,61,61,-28,100,100,61,61,61,-29,61,61,-30,]),'MINUS':([26,27,28,29,30,32,49,65,91,92,93,94,95,96,97,109,110,113,114,115,116,137,138,139,140,145,146,147,],[62,-42,-45,-46,-47,-27,62,62,62,-40,-41,-43,-44,-48,62,62,62,62,62,62,-28,62,62,62,-29,62,62,-30,]),'RBRACKET':([27,28,29,30,32,92,93,94,95,96,97,113,114,115,116,137,138,139,140,145,146,147,],[-42,-45,-46,-47,-27,-40,-41,-43,-44,-48,116,125,126,127,-28,140,141,142,-29,147,148,-30,]),'TO':([27,28,29,30,32,48,49,92,93,94,95,96,110,116,140,147,],[-42,-45,-46,-47,-27,84,-25,-40,-41,-43,-44,-48,-26,-28,-29,-30,]),'RPARENT':([27,28,29,30,32,39,41,44,45,65,67,68,73,81,92,93,94,95,96,99,103,104,105,106,116,118,119,129,130,140,147,],[-42,-45,-46,-47,-27,-51,-53,-62,-63,96,98,-37,-50,106,-40,-41,-43,-44,-48,117,-49,-52,-54,-55,-28,-37,-37,-35,-36,-29,-30,]),'TIMES':([27,28,29,30,32,92,93,94,95,96,116,140,147,],[63,-45,-46,-47,-27,63,63,-43,-44,-48,-28,-29,-30,]),'DIVIDE':([27,28,29,30,32,92,93,94,95,96,116,140,147,],[64,-45,-46,-47,-27,64,64,-43,-44,-48,-28,-29,-30,]),'LBRACKET':([32,55,56,57,116,126,127,140,142,],[66,88,89,90,128,135,136,143,144,]),'STRING':([34,37,100,],[68,68,118,]),'THEN':([38,39,41,44,45,73,103,104,105,106,],[70,-51,-53,-62,-63,-50,-49,-52,-54,-55,]),'OR':([38,39,41,44,45,46,73,81,103,104,105,106,108,],[71,-51,-53,-62,-63,71,-50,71,-49,-52,-54,-55,71,]),'ENDO':([39,41,44,45,73,103,104,105,106,108,],[-51,-53,-62,-63,-50,-49,-52,-54,-55,122,]),'AND':([39,41,44,45,73,103,104,105,106,],[72,-53,-62,-63,72,72,-52,-54,-55,]),'LT':([42,44,45,],[75,-62,-63,]),'LTE':([42,44,45,],[76,-62,-63,]),'GT':([42,44,45,],[77,-62,-63,]),'GTE':([42,44,45,],[78,-62,-63,]),'NE':([42,44,45,],[79,-62,-63,]),'EQUAL':([42,44,45,],[80,-62,-63,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'V':([3,21,87,],[4,51,112,]),'SP':([4,124,],[6,134,]),'IDLIST':([5,],[8,]),'X':([6,18,25,46,51,70,109,121,],[10,47,59,82,86,102,123,132,]),'S':([6,18,25,46,51,70,109,121,],[11,11,11,11,11,11,11,11,]),'E':([12,19,31,60,66,84,85,88,89,90,128,135,136,143,144,],[26,49,65,91,97,109,110,113,114,115,137,138,139,145,146,]),'T':([12,19,31,60,61,62,66,84,85,88,89,90,128,135,136,143,144,],[27,27,27,27,92,93,27,27,27,27,27,27,27,27,27,27,27,]),'F':([12,19,31,60,61,62,63,64,66,84,85,88,89,90,128,135,136,143,144,],[28,28,28,28,28,28,94,95,28,28,28,28,28,28,28,28,28,28,28,]),'U':([12,19,31,34,60,61,62,63,64,66,69,84,85,88,89,90,100,128,135,136,143,144,],[30,30,30,67,30,30,30,30,30,30,101,30,30,30,30,30,119,30,30,30,30,30,]),'Q':([13,],[33,]),'TEXT':([13,14,],[35,36,]),'EL':([16,17,43,83,],[38,46,81,108,]),'TL':([16,17,40,43,71,83,],[39,39,73,39,103,39,]),'FL':([16,17,40,43,71,72,83,],[41,41,41,41,41,104,41,]),'K':([16,17,40,43,71,72,74,83,],[42,42,42,42,42,42,105,42,]),'O':([19,],[48,]),'TIPO':([22,],[52,]),'OPREL':([42,],[74,]),'H':([68,118,119,],[99,129,130,]),'ELSE1':([102,],[120,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID V SP X END','program',6,'p_PROGRAM','semantic_analyser.py',20),
  ('V -> DIM IDLIST AS TIPO SEMMICOLON V','V',6,'p_V','semantic_analyser.py',25),
  ('V -> <empty>','V',0,'p_V','semantic_analyser.py',26),
  ('IDLIST -> ID','IDLIST',1,'p_IDLIST','semantic_analyser.py',31),
  ('IDLIST -> IDLIST COMMA ID','IDLIST',3,'p_IDLIST','semantic_analyser.py',32),
  ('IDLIST -> <empty>','IDLIST',0,'p_IDLIST','semantic_analyser.py',33),
  ('TIPO -> WORD','TIPO',1,'p_TIPO','semantic_analyser.py',38),
  ('TIPO -> FLOAT','TIPO',1,'p_TIPO','semantic_analyser.py',39),
  ('TIPO -> ARRAY LBRACKET E RBRACKET','TIPO',4,'p_TIPO','semantic_analyser.py',40),
  ('TIPO -> MATRIX LBRACKET E RBRACKET LBRACKET E RBRACKET','TIPO',7,'p_TIPO','semantic_analyser.py',41),
  ('TIPO -> CUBE LBRACKET E RBRACKET LBRACKET E RBRACKET LBRACKET E RBRACKET','TIPO',10,'p_TIPO','semantic_analyser.py',42),
  ('SP -> SUBPROCEDURE ID V X ENDSUB SEMMICOLON SP','SP',7,'p_SP','semantic_analyser.py',47),
  ('SP -> <empty>','SP',0,'p_SP','semantic_analyser.py',48),
  ('X -> S SEMMICOLON X','X',3,'p_X','semantic_analyser.py',52),
  ('X -> <empty>','X',0,'p_X','semantic_analyser.py',53),
  ('S -> LET E ASSIGN E','S',4,'p_S','semantic_analyser.py',58),
  ('S -> PRINT Q','S',2,'p_S','semantic_analyser.py',59),
  ('S -> INPUT TEXT GTGT U','S',4,'p_S','semantic_analyser.py',60),
  ('S -> CLS','S',1,'p_S','semantic_analyser.py',61),
  ('S -> IF EL THEN X ELSE1 ENDIF','S',6,'p_S','semantic_analyser.py',62),
  ('S -> WHILE EL X WHEND','S',4,'p_S','semantic_analyser.py',63),
  ('S -> DO X LOOPUNTIL EL ENDO','S',5,'p_S','semantic_analyser.py',64),
  ('S -> FOR O TO E X NEXT','S',6,'p_S','semantic_analyser.py',65),
  ('S -> GOSUB ID','S',2,'p_S','semantic_analyser.py',66),
  ('O -> E','O',1,'p_O','semantic_analyser.py',71),
  ('O -> E ASSIGN E','O',3,'p_O','semantic_analyser.py',72),
  ('U -> ID','U',1,'p_U','semantic_analyser.py',77),
  ('U -> ID LBRACKET E RBRACKET','U',4,'p_U','semantic_analyser.py',78),
  ('U -> ID LBRACKET E RBRACKET LBRACKET E RBRACKET','U',7,'p_U','semantic_analyser.py',79),
  ('U -> ID LBRACKET E RBRACKET LBRACKET E RBRACKET LBRACKET E RBRACKET','U',10,'p_U','semantic_analyser.py',80),
  ('Q -> LPARENT U RPARENT','Q',3,'p_Q','semantic_analyser.py',85),
  ('Q -> TEXT','Q',1,'p_Q','semantic_analyser.py',86),
  ('TEXT -> LPARENT STRING H RPARENT','TEXT',4,'p_TEXT','semantic_analyser.py',91),
  ('TEXT -> <empty>','TEXT',0,'p_TEXT','semantic_analyser.py',92),
  ('H -> PLUS STRING H','H',3,'p_H','semantic_analyser.py',97),
  ('H -> PLUS U H','H',3,'p_H','semantic_analyser.py',98),
  ('H -> <empty>','H',0,'p_H','semantic_analyser.py',99),
  ('ELSE1 -> ELSE X','ELSE1',2,'p_ELSE1','semantic_analyser.py',104),
  ('ELSE1 -> <empty>','ELSE1',0,'p_ELSE1','semantic_analyser.py',105),
  ('E -> E PLUS T','E',3,'p_E','semantic_analyser.py',110),
  ('E -> E MINUS T','E',3,'p_E','semantic_analyser.py',111),
  ('E -> T','E',1,'p_E','semantic_analyser.py',112),
  ('T -> T TIMES F','T',3,'p_T','semantic_analyser.py',117),
  ('T -> T DIVIDE F','T',3,'p_T','semantic_analyser.py',118),
  ('T -> F','T',1,'p_T','semantic_analyser.py',119),
  ('F -> NUMBER','F',1,'p_F','semantic_analyser.py',124),
  ('F -> U','F',1,'p_F','semantic_analyser.py',125),
  ('F -> LPARENT E RPARENT','F',3,'p_F','semantic_analyser.py',126),
  ('EL -> EL OR TL','EL',3,'p_EL','semantic_analyser.py',131),
  ('EL -> NOT TL','EL',2,'p_EL','semantic_analyser.py',132),
  ('EL -> TL','EL',1,'p_EL','semantic_analyser.py',133),
  ('TL -> TL AND FL','TL',3,'p_TL','semantic_analyser.py',138),
  ('TL -> FL','TL',1,'p_TL','semantic_analyser.py',139),
  ('FL -> K OPREL K','FL',3,'p_FL','semantic_analyser.py',144),
  ('FL -> LPARENT EL RPARENT','FL',3,'p_FL','semantic_analyser.py',145),
  ('OPREL -> LT','OPREL',1,'p_OPREL','semantic_analyser.py',150),
  ('OPREL -> LTE','OPREL',1,'p_OPREL','semantic_analyser.py',151),
  ('OPREL -> GT','OPREL',1,'p_OPREL','semantic_analyser.py',152),
  ('OPREL -> GTE','OPREL',1,'p_OPREL','semantic_analyser.py',153),
  ('OPREL -> NE','OPREL',1,'p_OPREL','semantic_analyser.py',154),
  ('OPREL -> EQUAL','OPREL',1,'p_OPREL','semantic_analyser.py',155),
  ('K -> ID','K',1,'p_K','semantic_analyser.py',160),
  ('K -> NUMBER','K',1,'p_K','semantic_analyser.py',161),
]
