
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'SLR'

_lr_signature = 'AND ARRAY AS ASSIGN CLS COMMA CUBE DIM DIVIDE DO ELSE END ENDIF ENDO ENDSUB EQUAL FLOAT FOR GOSUB GT GTE GTGT ID IF INPUT LBRACKET LET LOOPUNTIL LPARENT LT LTE MATRIX MINUS NE NEXT NOT NUMBER OR PLUS PRINT PROGRAM RBRACKET RPARENT SEMMICOLON STRING SUBPROCEDURE THEN TIMES TO WHEND WHILE WORD\n\tprogram : PROGRAM ID VARIABLE SP X END SEMMICOLON\n\t\n\tVARIABLE : DIM IDLIST AS TIPO SEMMICOLON VARIABLE\n\t\n\tVARIABLE :\n\t\n\tIDLIST : ID\n\t\n\tIDLIST : IDLIST COMMA ID\n\t\n\tIDLIST :\n\t\n\tTIPO : WORD\n\t\n\tTIPO : FLOAT\n\t\n\tTIPO : ARRAY DCLARRAY\n\t\n\tTIPO : MATRIX DCLMATRIX\n\t\n\tTIPO : CUBE DCLCUBE\n\t\n\tDCLARRAY : LBRACKET Z RBRACKET\n\t\n\tDCLMATRIX : LBRACKET Z RBRACKET LBRACKET Z RBRACKET\n\t\n\tDCLCUBE : LBRACKET Z RBRACKET LBRACKET Z RBRACKET LBRACKET Z RBRACKET\n\t\n\tZ : NUMBER\n\t| ID\n\t\n\tSP : SUBPROCEDURE ID X ENDSUB SEMMICOLON SP\n\t\n\tSP :\n\t\n\tX : STATEMENTS SEMMICOLON X\n\t\n\tX :\n\t\n\tSTATEMENTS : LET U ASSIGN E\n\t\n\tSTATEMENTS : PRINT Q\n\t\n\tSTATEMENTS : INPUT TEXT GTGT VAR\n\t\n\tVAR : ID\n\t| ID DCLARRAY\n\t| ID DCLMATRIX\n\t| ID DCLCUBE\n\t\n\tSTATEMENTS : CLS\n\t\n\tSTATEMENTS : IF EL THEN1 X ELSE1 ENDIF\n\t\n\tSTATEMENTS : WHILE EL X WHEND\n\t\n\tSTATEMENTS : DO X LOOPUNTIL EL ENDO\n\t\n\tSTATEMENTS : FOR ID TO E X NEXT\n\t\n\tSTATEMENTS : GOSUB ID\n\t\n\tU : ID\n\t\n\tU : ID DCLARRAY\n\t\n\tU : ID DCLMATRIX\n\t\n\tU : ID DCLCUBE\n\t\n\tQ : LPARENT VAR RPARENT\n\t\n\tQ : TEXT\n\t\n    TEXT : LPARENT STRING H RPARENT\n    \n\tTEXT :\n\t\n\tH : PLUS STRING H\n\t\n\tH : PLUS U H\n\t\n\tH :\n\t\n\tELSE1 : ELSE X\n\t\n\tTHEN1 : THEN\n\t\n\tELSE1 :\n\t\n\tE : E PLUS T\n\t| E MINUS T\n\t\n\tE : T\n\t\n\tT : T TIMES F\n\t| T DIVIDE F\n\t\n\tT : F\n\t\n\tF : NUMBER\n\t\n\tF : U\n\t\n\tF : LPARENT E RPARENT\n\t\n\tEL : EL OR TL\n\t\n\tEL : TL NOT\n\t| TL\n\t\n\tTL : TL AND FL\n\t\n\tTL : FL\n\t\n\tFL : K OPREL K\n\t\n\tFL : LPARENT EL RPARENT\n\t\n\tOPREL : LT\n\t| LTE\n\t| GT\n\t| GTE\n\t| NE\n\t| EQUAL\n\t\n\tK : ID\n\t\n\tK : NUMBER\n\t'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,52,],[0,-1,]),'ID':([2,5,7,12,16,17,19,20,23,29,37,54,58,62,64,67,68,69,70,71,72,73,74,77,78,82,84,86,92,98,116,117,118,119,138,144,145,152,],[3,9,21,27,38,38,42,43,51,61,38,27,95,61,38,38,38,-64,-65,-66,-67,-68,-69,38,27,95,95,95,27,27,27,27,27,27,95,95,95,95,]),'DIM':([3,80,],[5,5,]),'SUBPROCEDURE':([3,4,80,111,112,],[-3,7,-3,7,-2,]),'LET':([3,4,6,18,21,25,27,34,35,38,39,40,55,56,57,63,65,66,80,87,89,90,91,104,105,106,107,110,111,112,121,126,129,130,133,134,135,136,137,149,150,154,],[-3,-18,12,12,12,12,-34,-59,-61,-70,-71,12,-35,-36,-37,12,-46,-58,-3,-55,-50,-53,-54,-57,-60,-62,-63,12,-18,-2,-12,12,-17,-12,-48,-49,-51,-52,-56,-13,-13,-14,]),'PRINT':([3,4,6,18,21,25,27,34,35,38,39,40,55,56,57,63,65,66,80,87,89,90,91,104,105,106,107,110,111,112,121,126,129,130,133,134,135,136,137,149,150,154,],[-3,-18,13,13,13,13,-34,-59,-61,-70,-71,13,-35,-36,-37,13,-46,-58,-3,-55,-50,-53,-54,-57,-60,-62,-63,13,-18,-2,-12,13,-17,-12,-48,-49,-51,-52,-56,-13,-13,-14,]),'INPUT':([3,4,6,18,21,25,27,34,35,38,39,40,55,56,57,63,65,66,80,87,89,90,91,104,105,106,107,110,111,112,121,126,129,130,133,134,135,136,137,149,150,154,],[-3,-18,14,14,14,14,-34,-59,-61,-70,-71,14,-35,-36,-37,14,-46,-58,-3,-55,-50,-53,-54,-57,-60,-62,-63,14,-18,-2,-12,14,-17,-12,-48,-49,-51,-52,-56,-13,-13,-14,]),'CLS':([3,4,6,18,21,25,27,34,35,38,39,40,55,56,57,63,65,66,80,87,89,90,91,104,105,106,107,110,111,112,121,126,129,130,133,134,135,136,137,149,150,154,],[-3,-18,15,15,15,15,-34,-59,-61,-70,-71,15,-35,-36,-37,15,-46,-58,-3,-55,-50,-53,-54,-57,-60,-62,-63,15,-18,-2,-12,15,-17,-12,-48,-49,-51,-52,-56,-13,-13,-14,]),'IF':([3,4,6,18,21,25,27,34,35,38,39,40,55,56,57,63,65,66,80,87,89,90,91,104,105,106,107,110,111,112,121,126,129,130,133,134,135,136,137,149,150,154,],[-3,-18,16,16,16,16,-34,-59,-61,-70,-71,16,-35,-36,-37,16,-46,-58,-3,-55,-50,-53,-54,-57,-60,-62,-63,16,-18,-2,-12,16,-17,-12,-48,-49,-51,-52,-56,-13,-13,-14,]),'WHILE':([3,4,6,18,21,25,27,34,35,38,39,40,55,56,57,63,65,66,80,87,89,90,91,104,105,106,107,110,111,112,121,126,129,130,133,134,135,136,137,149,150,154,],[-3,-18,17,17,17,17,-34,-59,-61,-70,-71,17,-35,-36,-37,17,-46,-58,-3,-55,-50,-53,-54,-57,-60,-62,-63,17,-18,-2,-12,17,-17,-12,-48,-49,-51,-52,-56,-13,-13,-14,]),'DO':([3,4,6,18,21,25,27,34,35,38,39,40,55,56,57,63,65,66,80,87,89,90,91,104,105,106,107,110,111,112,121,126,129,130,133,134,135,136,137,149,150,154,],[-3,-18,18,18,18,18,-34,-59,-61,-70,-71,18,-35,-36,-37,18,-46,-58,-3,-55,-50,-53,-54,-57,-60,-62,-63,18,-18,-2,-12,18,-17,-12,-48,-49,-51,-52,-56,-13,-13,-14,]),'FOR':([3,4,6,18,21,25,27,34,35,38,39,40,55,56,57,63,65,66,80,87,89,90,91,104,105,106,107,110,111,112,121,126,129,130,133,134,135,136,137,149,150,154,],[-3,-18,19,19,19,19,-34,-59,-61,-70,-71,19,-35,-36,-37,19,-46,-58,-3,-55,-50,-53,-54,-57,-60,-62,-63,19,-18,-2,-12,19,-17,-12,-48,-49,-51,-52,-56,-13,-13,-14,]),'GOSUB':([3,4,6,18,21,25,27,34,35,38,39,40,55,56,57,63,65,66,80,87,89,90,91,104,105,106,107,110,111,112,121,126,129,130,133,134,135,136,137,149,150,154,],[-3,-18,20,20,20,20,-34,-59,-61,-70,-71,20,-35,-36,-37,20,-46,-58,-3,-55,-50,-53,-54,-57,-60,-62,-63,20,-18,-2,-12,20,-17,-12,-48,-49,-51,-52,-56,-13,-13,-14,]),'END':([3,4,6,10,18,21,25,40,53,63,80,110,111,112,126,129,],[-3,-18,-20,24,-20,-20,-20,-20,-19,-20,-3,-20,-18,-2,-20,-17,]),'AS':([5,8,9,51,],[-6,22,-4,-5,]),'COMMA':([5,8,9,51,],[-6,23,-4,-5,]),'ENDSUB':([6,18,21,25,40,44,53,63,110,126,],[-20,-20,-20,-20,-20,79,-19,-20,-20,-20,]),'ELSE':([6,18,21,25,40,53,63,65,103,110,126,],[-20,-20,-20,-20,-20,-19,-20,-46,126,-20,-20,]),'ENDIF':([6,18,21,25,40,53,63,65,103,110,125,126,142,],[-20,-20,-20,-20,-20,-19,-20,-46,-47,-20,141,-20,-45,]),'WHEND':([6,18,21,25,34,35,38,39,40,53,63,66,76,104,105,106,107,110,126,],[-20,-20,-20,-20,-59,-61,-70,-71,-20,-19,-20,-58,108,-57,-60,-62,-63,-20,-20,]),'LOOPUNTIL':([6,18,21,25,40,41,53,63,110,126,],[-20,-20,-20,-20,-20,77,-19,-20,-20,-20,]),'NEXT':([6,18,21,25,27,40,53,55,56,57,63,87,89,90,91,110,121,126,128,130,133,134,135,136,137,149,150,154,],[-20,-20,-20,-20,-34,-20,-19,-35,-36,-37,-20,-55,-50,-53,-54,-20,-12,-20,143,-12,-48,-49,-51,-52,-56,-13,-13,-14,]),'SEMMICOLON':([11,13,14,15,24,27,28,30,43,45,46,47,55,56,57,61,79,81,83,85,87,88,89,90,91,96,99,100,101,102,108,121,122,127,130,133,134,135,136,137,141,143,149,150,154,],[25,-41,-41,-28,52,-34,-22,-39,-33,80,-7,-8,-35,-36,-37,-24,111,-9,-10,-11,-55,-21,-50,-53,-54,-38,-25,-26,-27,-23,-30,-12,-40,-31,-12,-48,-49,-51,-52,-56,-29,-32,-13,-13,-14,]),'LPARENT':([13,14,16,17,37,54,64,67,77,78,92,116,117,118,119,],[29,32,37,37,37,92,37,37,37,92,92,92,92,92,92,]),'GTGT':([13,14,31,122,],[-41,-41,62,-40,]),'NUMBER':([16,17,37,54,58,64,67,68,69,70,71,72,73,74,77,78,82,84,86,92,116,117,118,119,138,144,145,152,],[39,39,39,91,94,39,39,39,-64,-65,-66,-67,-68,-69,39,91,94,94,94,91,91,91,91,91,94,94,94,94,]),'WORD':([22,],[46,]),'FLOAT':([22,],[47,]),'ARRAY':([22,],[48,]),'MATRIX':([22,],[49,]),'CUBE':([22,],[50,]),'ASSIGN':([26,27,55,56,57,121,130,149,150,154,],[54,-34,-35,-36,-37,-12,-12,-13,-13,-14,]),'PLUS':([27,55,56,57,60,87,88,89,90,91,110,120,121,123,124,130,133,134,135,136,137,149,150,154,],[-34,-35,-36,-37,98,-55,116,-50,-53,-54,116,116,-12,98,98,-12,-48,-49,-51,-52,-56,-13,-13,-14,]),'RPARENT':([27,34,35,38,39,55,56,57,59,60,61,66,75,87,89,90,91,97,99,100,101,104,105,106,107,120,121,123,124,130,133,134,135,136,137,139,140,149,150,154,],[-34,-59,-61,-70,-71,-35,-36,-37,96,-44,-24,-58,107,-55,-50,-53,-54,122,-25,-26,-27,-57,-60,-62,-63,137,-12,-44,-44,-12,-48,-49,-51,-52,-56,-42,-43,-13,-13,-14,]),'MINUS':([27,55,56,57,87,88,89,90,91,110,120,121,130,133,134,135,136,137,149,150,154,],[-34,-35,-36,-37,-55,117,-50,-53,-54,117,117,-12,-12,-48,-49,-51,-52,-56,-13,-13,-14,]),'TIMES':([27,55,56,57,87,89,90,91,121,130,133,134,135,136,137,149,150,154,],[-34,-35,-36,-37,-55,118,-53,-54,-12,-12,118,118,-51,-52,-56,-13,-13,-14,]),'DIVIDE':([27,55,56,57,87,89,90,91,121,130,133,134,135,136,137,149,150,154,],[-34,-35,-36,-37,-55,119,-53,-54,-12,-12,119,119,-51,-52,-56,-13,-13,-14,]),'LBRACKET':([27,48,49,50,61,121,131,132,149,151,],[58,82,84,86,58,138,144,145,152,152,]),'STRING':([29,32,98,],[60,60,123,]),'OR':([33,34,35,38,39,40,66,75,104,105,106,107,109,],[64,-59,-61,-70,-71,64,-58,64,-57,-60,-62,-63,64,]),'THEN':([33,34,35,38,39,66,104,105,106,107,],[65,-59,-61,-70,-71,-58,-57,-60,-62,-63,]),'NOT':([34,35,38,39,105,106,107,],[66,-61,-70,-71,-60,-62,-63,]),'ENDO':([34,35,38,39,66,104,105,106,107,109,],[-59,-61,-70,-71,-58,-57,-60,-62,-63,127,]),'AND':([34,35,38,39,104,105,106,107,],[67,-61,-70,-71,67,-60,-62,-63,]),'LT':([36,38,39,],[69,-70,-71,]),'LTE':([36,38,39,],[70,-70,-71,]),'GT':([36,38,39,],[71,-70,-71,]),'GTE':([36,38,39,],[72,-70,-71,]),'NE':([36,38,39,],[73,-70,-71,]),'EQUAL':([36,38,39,],[74,-70,-71,]),'TO':([42,],[78,]),'RBRACKET':([93,94,95,113,114,115,146,147,148,153,],[121,-15,-16,130,131,132,149,150,151,154,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'VARIABLE':([3,80,],[4,112,]),'SP':([4,111,],[6,129,]),'IDLIST':([5,],[8,]),'X':([6,18,21,25,40,63,110,126,],[10,41,44,53,76,103,128,142,]),'STATEMENTS':([6,18,21,25,40,63,110,126,],[11,11,11,11,11,11,11,11,]),'U':([12,54,78,92,98,116,117,118,119,],[26,87,87,87,124,87,87,87,87,]),'Q':([13,],[28,]),'TEXT':([13,14,],[30,31,]),'EL':([16,17,37,77,],[33,40,75,109,]),'TL':([16,17,37,64,77,],[34,34,34,104,34,]),'FL':([16,17,37,64,67,77,],[35,35,35,35,105,35,]),'K':([16,17,37,64,67,68,77,],[36,36,36,36,36,106,36,]),'TIPO':([22,],[45,]),'DCLARRAY':([27,48,61,],[55,81,99,]),'DCLMATRIX':([27,49,61,],[56,83,100,]),'DCLCUBE':([27,50,61,],[57,85,101,]),'VAR':([29,62,],[59,102,]),'THEN1':([33,],[63,]),'OPREL':([36,],[68,]),'E':([54,78,92,],[88,110,120,]),'T':([54,78,92,116,117,],[89,89,89,133,134,]),'F':([54,78,92,116,117,118,119,],[90,90,90,90,90,135,136,]),'Z':([58,82,84,86,138,144,145,152,],[93,113,114,115,146,147,148,153,]),'H':([60,123,124,],[97,139,140,]),'ELSE1':([103,],[125,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID VARIABLE SP X END SEMMICOLON','program',7,'p_PROGRAM','syntactic_analyser.py',25),
  ('VARIABLE -> DIM IDLIST AS TIPO SEMMICOLON VARIABLE','VARIABLE',6,'p_VARIABLE','syntactic_analyser.py',31),
  ('VARIABLE -> <empty>','VARIABLE',0,'p_VARIABLE_EMPTY','syntactic_analyser.py',37),
  ('IDLIST -> ID','IDLIST',1,'p_IDLIST','syntactic_analyser.py',42),
  ('IDLIST -> IDLIST COMMA ID','IDLIST',3,'p_IDLIST2','syntactic_analyser.py',48),
  ('IDLIST -> <empty>','IDLIST',0,'p_IDLIST_EMPTY','syntactic_analyser.py',55),
  ('TIPO -> WORD','TIPO',1,'p_TIPO_WORD','syntactic_analyser.py',60),
  ('TIPO -> FLOAT','TIPO',1,'p_TIPO_FLOAT','syntactic_analyser.py',66),
  ('TIPO -> ARRAY DCLARRAY','TIPO',2,'p_TIPO_ARRAY','syntactic_analyser.py',72),
  ('TIPO -> MATRIX DCLMATRIX','TIPO',2,'p_TIPO_MATRIX','syntactic_analyser.py',79),
  ('TIPO -> CUBE DCLCUBE','TIPO',2,'p_TIPO_CUBE','syntactic_analyser.py',86),
  ('DCLARRAY -> LBRACKET Z RBRACKET','DCLARRAY',3,'p_DCLARRAY','syntactic_analyser.py',93),
  ('DCLMATRIX -> LBRACKET Z RBRACKET LBRACKET Z RBRACKET','DCLMATRIX',6,'p_DCLMATRIX','syntactic_analyser.py',99),
  ('DCLCUBE -> LBRACKET Z RBRACKET LBRACKET Z RBRACKET LBRACKET Z RBRACKET','DCLCUBE',9,'p_DCLCUBE','syntactic_analyser.py',105),
  ('Z -> NUMBER','Z',1,'p_Z','syntactic_analyser.py',111),
  ('Z -> ID','Z',1,'p_Z','syntactic_analyser.py',112),
  ('SP -> SUBPROCEDURE ID X ENDSUB SEMMICOLON SP','SP',6,'p_SP','syntactic_analyser.py',117),
  ('SP -> <empty>','SP',0,'p_SP_EMPTY','syntactic_analyser.py',123),
  ('X -> STATEMENTS SEMMICOLON X','X',3,'p_X','syntactic_analyser.py',128),
  ('X -> <empty>','X',0,'p_X1','syntactic_analyser.py',134),
  ('STATEMENTS -> LET U ASSIGN E','STATEMENTS',4,'p_STATEMENTS_LET','syntactic_analyser.py',139),
  ('STATEMENTS -> PRINT Q','STATEMENTS',2,'p_STATEMENTS_PRINT','syntactic_analyser.py',146),
  ('STATEMENTS -> INPUT TEXT GTGT VAR','STATEMENTS',4,'p_STATEMENTS_INPUT','syntactic_analyser.py',152),
  ('VAR -> ID','VAR',1,'p_STATEMENTS_INPUT_VAR','syntactic_analyser.py',158),
  ('VAR -> ID DCLARRAY','VAR',2,'p_STATEMENTS_INPUT_VAR','syntactic_analyser.py',159),
  ('VAR -> ID DCLMATRIX','VAR',2,'p_STATEMENTS_INPUT_VAR','syntactic_analyser.py',160),
  ('VAR -> ID DCLCUBE','VAR',2,'p_STATEMENTS_INPUT_VAR','syntactic_analyser.py',161),
  ('STATEMENTS -> CLS','STATEMENTS',1,'p_STATEMENTS_CLS','syntactic_analyser.py',165),
  ('STATEMENTS -> IF EL THEN1 X ELSE1 ENDIF','STATEMENTS',6,'p_STATEMENTS_IF','syntactic_analyser.py',170),
  ('STATEMENTS -> WHILE EL X WHEND','STATEMENTS',4,'p_STATEMENTS_WHILE','syntactic_analyser.py',176),
  ('STATEMENTS -> DO X LOOPUNTIL EL ENDO','STATEMENTS',5,'p_STATEMENTS_DO','syntactic_analyser.py',182),
  ('STATEMENTS -> FOR ID TO E X NEXT','STATEMENTS',6,'p_STATEMENTS_FOR','syntactic_analyser.py',188),
  ('STATEMENTS -> GOSUB ID','STATEMENTS',2,'p_STATEMENTS_GOSUB','syntactic_analyser.py',194),
  ('U -> ID','U',1,'p_U','syntactic_analyser.py',199),
  ('U -> ID DCLARRAY','U',2,'p_U1','syntactic_analyser.py',206),
  ('U -> ID DCLMATRIX','U',2,'p_U2','syntactic_analyser.py',213),
  ('U -> ID DCLCUBE','U',2,'p_U3','syntactic_analyser.py',220),
  ('Q -> LPARENT VAR RPARENT','Q',3,'p_Q','syntactic_analyser.py',227),
  ('Q -> TEXT','Q',1,'p_Q1','syntactic_analyser.py',233),
  ('TEXT -> LPARENT STRING H RPARENT','TEXT',4,'p_TEXT','syntactic_analyser.py',239),
  ('TEXT -> <empty>','TEXT',0,'p_TEXT_EMPTY','syntactic_analyser.py',245),
  ('H -> PLUS STRING H','H',3,'p_H','syntactic_analyser.py',249),
  ('H -> PLUS U H','H',3,'p_H1','syntactic_analyser.py',255),
  ('H -> <empty>','H',0,'p_H_EMPTY','syntactic_analyser.py',261),
  ('ELSE1 -> ELSE X','ELSE1',2,'p_ELSE1','syntactic_analyser.py',266),
  ('THEN1 -> THEN','THEN1',1,'p_THEN1','syntactic_analyser.py',272),
  ('ELSE1 -> <empty>','ELSE1',0,'p_ELSE1_EMPTY','syntactic_analyser.py',278),
  ('E -> E PLUS T','E',3,'p_E','syntactic_analyser.py',283),
  ('E -> E MINUS T','E',3,'p_E','syntactic_analyser.py',284),
  ('E -> T','E',1,'p_E1','syntactic_analyser.py',291),
  ('T -> T TIMES F','T',3,'p_T','syntactic_analyser.py',297),
  ('T -> T DIVIDE F','T',3,'p_T','syntactic_analyser.py',298),
  ('T -> F','T',1,'p_T1','syntactic_analyser.py',305),
  ('F -> NUMBER','F',1,'p_F','syntactic_analyser.py',311),
  ('F -> U','F',1,'p_F1','syntactic_analyser.py',317),
  ('F -> LPARENT E RPARENT','F',3,'p_F2','syntactic_analyser.py',323),
  ('EL -> EL OR TL','EL',3,'p_EL','syntactic_analyser.py',329),
  ('EL -> TL NOT','EL',2,'p_EL1','syntactic_analyser.py',336),
  ('EL -> TL','EL',1,'p_EL1','syntactic_analyser.py',337),
  ('TL -> TL AND FL','TL',3,'p_TL','syntactic_analyser.py',343),
  ('TL -> FL','TL',1,'p_TL1','syntactic_analyser.py',350),
  ('FL -> K OPREL K','FL',3,'p_FL','syntactic_analyser.py',356),
  ('FL -> LPARENT EL RPARENT','FL',3,'p_FL1','syntactic_analyser.py',363),
  ('OPREL -> LT','OPREL',1,'p_OPREL','syntactic_analyser.py',369),
  ('OPREL -> LTE','OPREL',1,'p_OPREL','syntactic_analyser.py',370),
  ('OPREL -> GT','OPREL',1,'p_OPREL','syntactic_analyser.py',371),
  ('OPREL -> GTE','OPREL',1,'p_OPREL','syntactic_analyser.py',372),
  ('OPREL -> NE','OPREL',1,'p_OPREL','syntactic_analyser.py',373),
  ('OPREL -> EQUAL','OPREL',1,'p_OPREL','syntactic_analyser.py',374),
  ('K -> ID','K',1,'p_K','syntactic_analyser.py',380),
  ('K -> NUMBER','K',1,'p_K1','syntactic_analyser.py',386),
]
