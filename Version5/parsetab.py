
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'SLR'

_lr_signature = 'AND ARRAY AS ASSIGN CLS COMMA CUBE DIM DIVIDE DO ELSE END ENDIF ENDO ENDSUB EQUAL FLOAT FLOATNUMBER FOR GOSUB GT GTE GTGT ID IF INPUT LBRACKET LET LOOPUNTIL LPARENT LT LTE MATRIX MINUS NE NEXT NOT NUMBER OR PLUS POINT PRINT PROGRAM RBRACKET RPARENT SEMMICOLON STRING SUBPROCEDURE THEN TIMES TO WHEND WHILE WORD\n\tprogram : PROGRAM1 ID VARIABLE SP SALTO STATUTES END SEMMICOLON\n\t\n\tPROGRAM1 : PROGRAM\n\t\n\tSALTO :\n\t\n\tVARIABLE : DIM IDLIST AS TIPO SEMMICOLON VARIABLE\n\t|\n\t\n\tSP : SUBPROCEDURE ID2 STATUTES ENDSUB SEMMICOLON RETURN SP\n\t\n\tRETURN :\n\t\n\tID2 : ID\n\t\n\tSP :\n\t\n\tSTATUTES : STATEMENTS SEMMICOLON STATUTES\n\t|\n\t\n\tSTATEMENTS : LET VAR ASSIGN E\n\t\n\tSTATEMENTS : PRINT VALUE\n\t\n\tSTATEMENTS : INPUT TEXT GTGT VAR\n\t\n\tSTATEMENTS : CLS\n\t\n\tSTATEMENTS : IF EL THEN1 STATUTES ELSE1 STATUTES ENDIF\n\t\n\tSTATEMENTS : WHILE1 EL DO1 STATUTES WHEND\n\t\n\tSTATEMENTS : DO2 STATUTES LOOPUNTIL EL ENDO\n\t\n\tSTATEMENTS : FOR ID1 ASSIGN E TO1 E DO3 STATUTES NEXT\n\t\n\tSTATEMENTS : GOSUB POINT ID\n\t\n\tE : E PLUS T\n\t| E MINUS T\n\t\n\tE : T\n\t\n\tT : T TIMES F\n\t| T DIVIDE F\n\t\n\tT : F\n\t\n\tF : NUMBER\n\t\n\tF : FLOATNUMBER\n\t\n\tF : VAR\n\t\n\tF : LPARENT E RPARENT\n\t\n\tEL : EL OR TL\n\t\n\tEL : TL NOT\n\t| TL\n\t\n\tTL : TL AND FL\n\t\n\tTL : FL\n\t\n\tFL : OPERATOR OPREL OPERATOR\n\t\n\tFL : LPARENT EL RPARENT\n\t\n\tOPREL : LT\n\t| LTE\n\t| GT\n\t| GTE\n\t| NE\n\t| EQUAL\n\t\n\tOPERATOR : ID\n\t\n\tOPERATOR : NUMBER\n\t\n\tOPERATOR : FLOATNUMBER\n\t\n\tIDLIST : ID\n\t\n\tIDLIST : IDLIST COMMA ID\n\t\n\tTIPO : WORD\n\t| FLOAT\n\t\n\tTIPO : ARRAY DCLARRAY\n\t\n\tTIPO : MATRIX DCLMATRIX\n\t\n\tTIPO : CUBE DCLCUBE\n\t\n\tDCLARRAY : LBRACKET IDENTIFICATOR RBRACKET\n\t\n\tDCLMATRIX : LBRACKET IDENTIFICATOR RBRACKET LBRACKET IDENTIFICATOR RBRACKET\n\t\n\tDCLCUBE : LBRACKET IDENTIFICATOR RBRACKET LBRACKET IDENTIFICATOR RBRACKET LBRACKET IDENTIFICATOR RBRACKET\n\t\n\tIDENTIFICATOR : NUMBER\n\t\n\tIDENTIFICATOR : ID\n\t\n\tDCLARRAY1 : LBRACKET IDENTIFICATOR1 RBRACKET\n\t\n\tDCLMATRIX1 : LBRACKET IDENTIFICATOR1 RBRACKET LBRACKET IDENTIFICATOR1 RBRACKET\n\t\n\tDCLCUBE1 : LBRACKET IDENTIFICATOR1 RBRACKET LBRACKET IDENTIFICATOR1 RBRACKET LBRACKET IDENTIFICATOR1 RBRACKET\n\t\n\tIDENTIFICATOR1 : NUMBER\n\t\n\tIDENTIFICATOR1 : ID\n\t\n\tVAR : ID\n\t\n\tVAR : ID PUSH DCLARRAY1\n\t| ID  PUSH DCLMATRIX1\n\t| ID PUSH DCLCUBE1\n\t\n\tPUSH :\n\t\n\tELSE1 : ELSE\n\t\n\tELSE1 :\n\t\n\tTHEN1 : THEN\n\t\n\tWHILE1 : WHILE\n\t\n\tDO1 : DO\n\t\n\tDO2 : DO\n\t\n\tID1 : ID\n\t\n\tTO1 : TO\n\t\n\tDO3 : DO\n\t\n\tVALUE : LPARENT VAR RPARENT\n\t\n\tVALUE : TEXT\n\t\n\tTEXT : LPARENT STRING RPARENT\n\t\n\tTEXT :\n\t'
    
_lr_action_items = {'PROGRAM':([0,],[3,]),'$end':([1,67,],[0,-1,]),'ID':([2,3,6,8,15,18,22,23,25,27,42,50,58,62,64,66,69,73,75,78,79,80,81,82,83,84,85,89,90,105,109,125,126,127,128,137,138,140,141,152,160,164,],[4,-2,10,13,36,40,51,51,57,-72,40,51,91,96,96,96,40,40,51,51,51,-38,-39,-40,-41,-42,-43,51,40,40,132,40,40,40,40,40,-76,96,96,132,96,132,]),'DIM':([4,60,],[6,6,]),'SUBPROCEDURE':([4,5,60,92,93,121,],[-5,8,-5,-7,-4,8,]),'LET':([4,5,7,11,12,13,24,28,38,60,68,74,76,87,88,92,93,113,121,133,134,139,154,155,],[-5,-9,-3,18,18,-8,18,-74,18,-5,-10,18,-71,18,-73,-7,-4,-70,-9,18,-69,-6,18,-77,]),'PRINT':([4,5,7,11,12,13,24,28,38,60,68,74,76,87,88,92,93,113,121,133,134,139,154,155,],[-5,-9,-3,19,19,-8,19,-74,19,-5,-10,19,-71,19,-73,-7,-4,-70,-9,19,-69,-6,19,-77,]),'INPUT':([4,5,7,11,12,13,24,28,38,60,68,74,76,87,88,92,93,113,121,133,134,139,154,155,],[-5,-9,-3,20,20,-8,20,-74,20,-5,-10,20,-71,20,-73,-7,-4,-70,-9,20,-69,-6,20,-77,]),'CLS':([4,5,7,11,12,13,24,28,38,60,68,74,76,87,88,92,93,113,121,133,134,139,154,155,],[-5,-9,-3,21,21,-8,21,-74,21,-5,-10,21,-71,21,-73,-7,-4,-70,-9,21,-69,-6,21,-77,]),'IF':([4,5,7,11,12,13,24,28,38,60,68,74,76,87,88,92,93,113,121,133,134,139,154,155,],[-5,-9,-3,22,22,-8,22,-74,22,-5,-10,22,-71,22,-73,-7,-4,-70,-9,22,-69,-6,22,-77,]),'FOR':([4,5,7,11,12,13,24,28,38,60,68,74,76,87,88,92,93,113,121,133,134,139,154,155,],[-5,-9,-3,25,25,-8,25,-74,25,-5,-10,25,-71,25,-73,-7,-4,-70,-9,25,-69,-6,25,-77,]),'GOSUB':([4,5,7,11,12,13,24,28,38,60,68,74,76,87,88,92,93,113,121,133,134,139,154,155,],[-5,-9,-3,26,26,-8,26,-74,26,-5,-10,26,-71,26,-73,-7,-4,-70,-9,26,-69,-6,26,-77,]),'WHILE':([4,5,7,11,12,13,24,28,38,60,68,74,76,87,88,92,93,113,121,133,134,139,154,155,],[-5,-9,-3,27,27,-8,27,-74,27,-5,-10,27,-71,27,-73,-7,-4,-70,-9,27,-69,-6,27,-77,]),'DO':([4,5,7,11,12,13,24,28,38,40,47,48,51,52,53,54,60,68,74,76,77,87,88,92,93,99,101,102,103,104,106,107,108,113,114,115,116,117,121,133,134,139,142,143,144,145,146,147,149,154,155,161,167,],[-5,-9,-3,28,28,-8,28,-74,28,-64,-33,-35,-44,-45,-46,88,-5,-10,28,-71,-32,28,-73,-7,-4,-29,-23,-26,-27,-28,-65,-66,-67,-70,-31,-34,-36,-37,-9,28,-69,-6,-21,-22,-24,-25,-30,-59,155,28,-77,-60,-61,]),'END':([4,5,7,11,12,16,24,38,60,68,74,87,92,93,121,133,139,154,],[-5,-9,-3,-11,-11,37,-11,-11,-5,-10,-11,-11,-7,-4,-9,-11,-6,-11,]),'AS':([9,10,36,],[14,-47,-48,]),'COMMA':([9,10,36,],[15,-47,-48,]),'ENDSUB':([11,12,13,24,29,38,68,74,87,133,154,],[-11,-11,-8,-11,59,-11,-10,-11,-11,-11,-11,]),'ELSE':([11,12,24,38,68,74,76,87,113,133,154,],[-11,-11,-11,-11,-10,-11,-71,-11,134,-11,-11,]),'ENDIF':([11,12,24,38,68,74,76,87,113,133,134,148,154,],[-11,-11,-11,-11,-10,-11,-71,-11,-70,-11,-69,153,-11,]),'WHEND':([11,12,24,38,68,74,87,88,118,133,154,],[-11,-11,-11,-11,-10,-11,-11,-73,135,-11,-11,]),'LOOPUNTIL':([11,12,24,28,38,55,68,74,87,133,154,],[-11,-11,-11,-74,-11,89,-10,-11,-11,-11,-11,]),'NEXT':([11,12,24,38,68,74,87,133,154,155,159,],[-11,-11,-11,-11,-10,-11,-11,-11,-11,-77,162,]),'WORD':([14,],[31,]),'FLOAT':([14,],[32,]),'ARRAY':([14,],[33,]),'MATRIX':([14,],[34,]),'CUBE':([14,],[35,]),'SEMMICOLON':([17,19,20,21,30,31,32,37,40,41,43,59,61,63,65,91,99,100,101,102,103,104,106,107,108,110,111,112,122,135,136,142,143,144,145,146,147,153,156,161,162,165,167,],[38,-81,-81,-15,60,-49,-50,67,-64,-13,-79,92,-51,-52,-53,-20,-29,-12,-23,-26,-27,-28,-65,-66,-67,-78,-80,-14,-54,-17,-18,-21,-22,-24,-25,-30,-59,-16,-55,-60,-19,-56,-61,]),'LPARENT':([19,20,22,23,27,50,69,75,78,89,90,105,125,126,127,128,137,138,],[42,45,50,50,-72,50,105,50,50,50,105,105,105,105,105,105,105,-76,]),'GTGT':([19,20,44,111,],[-81,-81,73,-80,]),'NUMBER':([22,23,27,50,62,64,66,69,75,78,79,80,81,82,83,84,85,89,90,105,109,125,126,127,128,137,138,140,141,152,160,164,],[52,52,-72,52,95,95,95,103,52,52,52,-38,-39,-40,-41,-42,-43,52,103,103,131,103,103,103,103,103,-76,95,95,131,95,131,]),'FLOATNUMBER':([22,23,27,50,69,75,78,79,80,81,82,83,84,85,89,90,105,125,126,127,128,137,138,],[53,53,-72,53,104,53,53,53,-38,-39,-40,-41,-42,-43,53,104,104,104,104,104,104,104,-76,]),'POINT':([26,],[58,]),'LBRACKET':([33,34,35,40,70,123,124,147,157,161,],[62,64,66,-68,109,140,141,152,160,164,]),'ASSIGN':([39,40,56,57,106,107,108,147,161,167,],[69,-64,90,-75,-65,-66,-67,-59,-60,-61,]),'TO':([40,99,101,102,103,104,106,107,108,120,142,143,144,145,146,147,161,167,],[-64,-29,-23,-26,-27,-28,-65,-66,-67,138,-21,-22,-24,-25,-30,-59,-60,-61,]),'PLUS':([40,99,100,101,102,103,104,106,107,108,120,129,142,143,144,145,146,147,149,161,167,],[-64,-29,125,-23,-26,-27,-28,-65,-66,-67,125,125,-21,-22,-24,-25,-30,-59,125,-60,-61,]),'MINUS':([40,99,100,101,102,103,104,106,107,108,120,129,142,143,144,145,146,147,149,161,167,],[-64,-29,126,-23,-26,-27,-28,-65,-66,-67,126,126,-21,-22,-24,-25,-30,-59,126,-60,-61,]),'TIMES':([40,99,101,102,103,104,106,107,108,142,143,144,145,146,147,161,167,],[-64,-29,127,-26,-27,-28,-65,-66,-67,127,127,-24,-25,-30,-59,-60,-61,]),'DIVIDE':([40,99,101,102,103,104,106,107,108,142,143,144,145,146,147,161,167,],[-64,-29,128,-26,-27,-28,-65,-66,-67,128,128,-24,-25,-30,-59,-60,-61,]),'RPARENT':([40,47,48,51,52,53,71,72,77,86,99,101,102,103,104,106,107,108,114,115,116,117,129,142,143,144,145,146,147,161,167,],[-64,-33,-35,-44,-45,-46,110,111,-32,117,-29,-23,-26,-27,-28,-65,-66,-67,-31,-34,-36,-37,146,-21,-22,-24,-25,-30,-59,-60,-61,]),'STRING':([42,45,],[72,72,]),'OR':([46,47,48,51,52,53,54,77,86,114,115,116,117,119,],[75,-33,-35,-44,-45,-46,75,-32,75,-31,-34,-36,-37,75,]),'THEN':([46,47,48,51,52,53,77,114,115,116,117,],[76,-33,-35,-44,-45,-46,-32,-31,-34,-36,-37,]),'NOT':([47,48,51,52,53,115,116,117,],[77,-35,-44,-45,-46,-34,-36,-37,]),'ENDO':([47,48,51,52,53,77,114,115,116,117,119,],[-33,-35,-44,-45,-46,-32,-31,-34,-36,-37,136,]),'AND':([47,48,51,52,53,114,115,116,117,],[78,-35,-44,-45,-46,78,-34,-36,-37,]),'LT':([49,51,52,53,],[80,-44,-45,-46,]),'LTE':([49,51,52,53,],[81,-44,-45,-46,]),'GT':([49,51,52,53,],[82,-44,-45,-46,]),'GTE':([49,51,52,53,],[83,-44,-45,-46,]),'NE':([49,51,52,53,],[84,-44,-45,-46,]),'EQUAL':([49,51,52,53,],[85,-44,-45,-46,]),'RBRACKET':([94,95,96,97,98,130,131,132,150,151,158,163,166,],[122,-57,-58,123,124,147,-62,-63,156,157,161,165,167,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'PROGRAM1':([0,],[2,]),'VARIABLE':([4,60,],[5,93,]),'SP':([5,121,],[7,139,]),'IDLIST':([6,],[9,]),'SALTO':([7,],[11,]),'ID2':([8,],[12,]),'STATUTES':([11,12,24,38,74,87,133,154,],[16,29,55,68,113,118,148,159,]),'STATEMENTS':([11,12,24,38,74,87,133,154,],[17,17,17,17,17,17,17,17,]),'WHILE1':([11,12,24,38,74,87,133,154,],[23,23,23,23,23,23,23,23,]),'DO2':([11,12,24,38,74,87,133,154,],[24,24,24,24,24,24,24,24,]),'TIPO':([14,],[30,]),'VAR':([18,42,69,73,90,105,125,126,127,128,137,],[39,71,99,112,99,99,99,99,99,99,99,]),'VALUE':([19,],[41,]),'TEXT':([19,20,],[43,44,]),'EL':([22,23,50,89,],[46,54,86,119,]),'TL':([22,23,50,75,89,],[47,47,47,114,47,]),'FL':([22,23,50,75,78,89,],[48,48,48,48,115,48,]),'OPERATOR':([22,23,50,75,78,79,89,],[49,49,49,49,49,116,49,]),'ID1':([25,],[56,]),'DCLARRAY':([33,],[61,]),'DCLMATRIX':([34,],[63,]),'DCLCUBE':([35,],[65,]),'PUSH':([40,],[70,]),'THEN1':([46,],[74,]),'OPREL':([49,],[79,]),'DO1':([54,],[87,]),'IDENTIFICATOR':([62,64,66,140,141,160,],[94,97,98,150,151,163,]),'E':([69,90,105,137,],[100,120,129,149,]),'T':([69,90,105,125,126,137,],[101,101,101,142,143,101,]),'F':([69,90,105,125,126,127,128,137,],[102,102,102,102,102,144,145,102,]),'DCLARRAY1':([70,],[106,]),'DCLMATRIX1':([70,],[107,]),'DCLCUBE1':([70,],[108,]),'RETURN':([92,],[121,]),'IDENTIFICATOR1':([109,152,164,],[130,158,166,]),'ELSE1':([113,],[133,]),'TO1':([120,],[137,]),'DO3':([149,],[154,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM1 ID VARIABLE SP SALTO STATUTES END SEMMICOLON','program',8,'p_PROGRAM','syntactic_analyser.py',23),
  ('PROGRAM1 -> PROGRAM','PROGRAM1',1,'p_PROGRAM_PROGRAM1','syntactic_analyser.py',29),
  ('SALTO -> <empty>','SALTO',0,'p_PROGRAM_SALTO','syntactic_analyser.py',35),
  ('VARIABLE -> DIM IDLIST AS TIPO SEMMICOLON VARIABLE','VARIABLE',6,'p_VARIABLE','syntactic_analyser.py',41),
  ('VARIABLE -> <empty>','VARIABLE',0,'p_VARIABLE','syntactic_analyser.py',42),
  ('SP -> SUBPROCEDURE ID2 STATUTES ENDSUB SEMMICOLON RETURN SP','SP',7,'p_SP','syntactic_analyser.py',47),
  ('RETURN -> <empty>','RETURN',0,'p_RETURN','syntactic_analyser.py',52),
  ('ID2 -> ID','ID2',1,'p_SP_ID2','syntactic_analyser.py',58),
  ('SP -> <empty>','SP',0,'p_SP_EMPTY','syntactic_analyser.py',64),
  ('STATUTES -> STATEMENTS SEMMICOLON STATUTES','STATUTES',3,'p_STATUTES','syntactic_analyser.py',69),
  ('STATUTES -> <empty>','STATUTES',0,'p_STATUTES','syntactic_analyser.py',70),
  ('STATEMENTS -> LET VAR ASSIGN E','STATEMENTS',4,'p_STATEMENTS_LET','syntactic_analyser.py',75),
  ('STATEMENTS -> PRINT VALUE','STATEMENTS',2,'p_STATEMENTS_PRINT','syntactic_analyser.py',81),
  ('STATEMENTS -> INPUT TEXT GTGT VAR','STATEMENTS',4,'p_STATEMENTS_INPUT','syntactic_analyser.py',87),
  ('STATEMENTS -> CLS','STATEMENTS',1,'p_STATEMENTS_CLS','syntactic_analyser.py',93),
  ('STATEMENTS -> IF EL THEN1 STATUTES ELSE1 STATUTES ENDIF','STATEMENTS',7,'p_STATEMENTS_IF','syntactic_analyser.py',99),
  ('STATEMENTS -> WHILE1 EL DO1 STATUTES WHEND','STATEMENTS',5,'p_STATEMENTS_WHILE','syntactic_analyser.py',105),
  ('STATEMENTS -> DO2 STATUTES LOOPUNTIL EL ENDO','STATEMENTS',5,'p_STATEMENTS_DO','syntactic_analyser.py',111),
  ('STATEMENTS -> FOR ID1 ASSIGN E TO1 E DO3 STATUTES NEXT','STATEMENTS',9,'p_STATEMENTS_FOR','syntactic_analyser.py',117),
  ('STATEMENTS -> GOSUB POINT ID','STATEMENTS',3,'p_STATEMENTS_GOSUB','syntactic_analyser.py',123),
  ('E -> E PLUS T','E',3,'p_E','syntactic_analyser.py',129),
  ('E -> E MINUS T','E',3,'p_E','syntactic_analyser.py',130),
  ('E -> T','E',1,'p_E1','syntactic_analyser.py',136),
  ('T -> T TIMES F','T',3,'p_T','syntactic_analyser.py',141),
  ('T -> T DIVIDE F','T',3,'p_T','syntactic_analyser.py',142),
  ('T -> F','T',1,'p_T1','syntactic_analyser.py',148),
  ('F -> NUMBER','F',1,'p_F','syntactic_analyser.py',153),
  ('F -> FLOATNUMBER','F',1,'p_F1','syntactic_analyser.py',159),
  ('F -> VAR','F',1,'p_F2','syntactic_analyser.py',165),
  ('F -> LPARENT E RPARENT','F',3,'p_F3','syntactic_analyser.py',170),
  ('EL -> EL OR TL','EL',3,'p_EL','syntactic_analyser.py',175),
  ('EL -> TL NOT','EL',2,'p_EL1','syntactic_analyser.py',181),
  ('EL -> TL','EL',1,'p_EL1','syntactic_analyser.py',182),
  ('TL -> TL AND FL','TL',3,'p_TL','syntactic_analyser.py',187),
  ('TL -> FL','TL',1,'p_TL1','syntactic_analyser.py',193),
  ('FL -> OPERATOR OPREL OPERATOR','FL',3,'p_FL','syntactic_analyser.py',198),
  ('FL -> LPARENT EL RPARENT','FL',3,'p_FL1','syntactic_analyser.py',204),
  ('OPREL -> LT','OPREL',1,'p_OPREL','syntactic_analyser.py',209),
  ('OPREL -> LTE','OPREL',1,'p_OPREL','syntactic_analyser.py',210),
  ('OPREL -> GT','OPREL',1,'p_OPREL','syntactic_analyser.py',211),
  ('OPREL -> GTE','OPREL',1,'p_OPREL','syntactic_analyser.py',212),
  ('OPREL -> NE','OPREL',1,'p_OPREL','syntactic_analyser.py',213),
  ('OPREL -> EQUAL','OPREL',1,'p_OPREL','syntactic_analyser.py',214),
  ('OPERATOR -> ID','OPERATOR',1,'p_OPERATOR','syntactic_analyser.py',220),
  ('OPERATOR -> NUMBER','OPERATOR',1,'p_OPERATOR1','syntactic_analyser.py',226),
  ('OPERATOR -> FLOATNUMBER','OPERATOR',1,'p_OPERATOR2','syntactic_analyser.py',232),
  ('IDLIST -> ID','IDLIST',1,'p_IDLIST','syntactic_analyser.py',238),
  ('IDLIST -> IDLIST COMMA ID','IDLIST',3,'p_IDLIST2','syntactic_analyser.py',244),
  ('TIPO -> WORD','TIPO',1,'p_TIPO_SIMPLES','syntactic_analyser.py',250),
  ('TIPO -> FLOAT','TIPO',1,'p_TIPO_SIMPLES','syntactic_analyser.py',251),
  ('TIPO -> ARRAY DCLARRAY','TIPO',2,'p_TIPO_DIM_ARRAY','syntactic_analyser.py',257),
  ('TIPO -> MATRIX DCLMATRIX','TIPO',2,'p_TIPO_DIM_MATRIX','syntactic_analyser.py',263),
  ('TIPO -> CUBE DCLCUBE','TIPO',2,'p_TIPO_DIM_CUBE','syntactic_analyser.py',269),
  ('DCLARRAY -> LBRACKET IDENTIFICATOR RBRACKET','DCLARRAY',3,'p_DCLARRAY','syntactic_analyser.py',275),
  ('DCLMATRIX -> LBRACKET IDENTIFICATOR RBRACKET LBRACKET IDENTIFICATOR RBRACKET','DCLMATRIX',6,'p_DCLMATRIX','syntactic_analyser.py',280),
  ('DCLCUBE -> LBRACKET IDENTIFICATOR RBRACKET LBRACKET IDENTIFICATOR RBRACKET LBRACKET IDENTIFICATOR RBRACKET','DCLCUBE',9,'p_DCLCUBE','syntactic_analyser.py',285),
  ('IDENTIFICATOR -> NUMBER','IDENTIFICATOR',1,'p_IDENTIFICATOR','syntactic_analyser.py',290),
  ('IDENTIFICATOR -> ID','IDENTIFICATOR',1,'p_IDENTIFICATOR_1','syntactic_analyser.py',296),
  ('DCLARRAY1 -> LBRACKET IDENTIFICATOR1 RBRACKET','DCLARRAY1',3,'p_DCLARRAY_EJECUCION','syntactic_analyser.py',302),
  ('DCLMATRIX1 -> LBRACKET IDENTIFICATOR1 RBRACKET LBRACKET IDENTIFICATOR1 RBRACKET','DCLMATRIX1',6,'p_DCLMATRIX_EJECUCION','syntactic_analyser.py',308),
  ('DCLCUBE1 -> LBRACKET IDENTIFICATOR1 RBRACKET LBRACKET IDENTIFICATOR1 RBRACKET LBRACKET IDENTIFICATOR1 RBRACKET','DCLCUBE1',9,'p_DCLCUBE_EJECUCION','syntactic_analyser.py',313),
  ('IDENTIFICATOR1 -> NUMBER','IDENTIFICATOR1',1,'p_IDENTIFICATOR_EJECUCION','syntactic_analyser.py',318),
  ('IDENTIFICATOR1 -> ID','IDENTIFICATOR1',1,'p_IDENTIFICATOR_1_EJECUCION','syntactic_analyser.py',324),
  ('VAR -> ID','VAR',1,'p_STATEMENTS_VAR','syntactic_analyser.py',330),
  ('VAR -> ID PUSH DCLARRAY1','VAR',3,'p_STATEMENTS_VAR1','syntactic_analyser.py',336),
  ('VAR -> ID PUSH DCLMATRIX1','VAR',3,'p_STATEMENTS_VAR1','syntactic_analyser.py',337),
  ('VAR -> ID PUSH DCLCUBE1','VAR',3,'p_STATEMENTS_VAR1','syntactic_analyser.py',338),
  ('PUSH -> <empty>','PUSH',0,'p_PUSH','syntactic_analyser.py',343),
  ('ELSE1 -> ELSE','ELSE1',1,'p_STATEMENTS_IF_ELSE1','syntactic_analyser.py',349),
  ('ELSE1 -> <empty>','ELSE1',0,'p_STATEMENTS_IF_ELSE1_EMPTY','syntactic_analyser.py',355),
  ('THEN1 -> THEN','THEN1',1,'p_STATEMENTS_IF_THEN1','syntactic_analyser.py',360),
  ('WHILE1 -> WHILE','WHILE1',1,'p_STATEMENTS_WHILE_WHILE1','syntactic_analyser.py',366),
  ('DO1 -> DO','DO1',1,'p_STATEMENTS_WHILE_DO1','syntactic_analyser.py',372),
  ('DO2 -> DO','DO2',1,'p_STATEMENTS_DO_DO2','syntactic_analyser.py',378),
  ('ID1 -> ID','ID1',1,'p_STATEMENTS_FOR_ID','syntactic_analyser.py',384),
  ('TO1 -> TO','TO1',1,'p_STATEMENTS_FOR_TO','syntactic_analyser.py',390),
  ('DO3 -> DO','DO3',1,'p_STATEMENTS_FOR_DO','syntactic_analyser.py',396),
  ('VALUE -> LPARENT VAR RPARENT','VALUE',3,'p_VALUE','syntactic_analyser.py',402),
  ('VALUE -> TEXT','VALUE',1,'p_VALUE1','syntactic_analyser.py',408),
  ('TEXT -> LPARENT STRING RPARENT','TEXT',3,'p_TEXT','syntactic_analyser.py',414),
  ('TEXT -> <empty>','TEXT',0,'p_TEXT1','syntactic_analyser.py',420),
]
