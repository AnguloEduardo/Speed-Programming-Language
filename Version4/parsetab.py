
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'SLR'

_lr_signature = 'AND ARRAY AS ASSIGN CLS COMMA CUBE DIM DIVIDE DO ELSE END ENDIF ENDO ENDSUB EQUAL FLOAT FLOATNUMBER FOR GOSUB GT GTE GTGT ID IF INPUT LBRACKET LET LOOPUNTIL LPARENT LT LTE MATRIX MINUS NE NEXT NOT NUMBER OR PLUS POINT PRINT PROGRAM RBRACKET RPARENT SEMMICOLON STRING SUBPROCEDURE THEN TIMES TO WHEND WHILE WORD\n\tprogram : PROGRAM1 ID VARIABLE SP SALTO STATUTES END SEMMICOLON\n\t\n\tPROGRAM1 : PROGRAM\n\t\n\tSALTO :\n\t\n\tVARIABLE : DIM IDLIST AS TIPO SEMMICOLON VARIABLE\n\t|\n\t\n\tSP : SUBPROCEDURE ID2 STATUTES ENDSUB SEMMICOLON RETURN SP\n\t\n\tRETURN :\n\t\n\tID2 : ID\n\t\n\tSP :\n\t\n\tSTATUTES : STATEMENTS SEMMICOLON STATUTES\n\t|\n\t\n\tSTATEMENTS : LET VAR ASSIGN E\n\t\n\tSTATEMENTS : PRINT VALUE\n\t\n\tSTATEMENTS : INPUT TEXT GTGT VAR\n\t\n\tSTATEMENTS : CLS\n\t\n\tSTATEMENTS : IF EL THEN1 STATUTES ELSE1 ENDIF\n\t\n\tSTATEMENTS : WHILE1 EL DO1 STATUTES WHEND\n\t\n\tSTATEMENTS : DO2 STATUTES LOOPUNTIL EL ENDO\n\t\n\tSTATEMENTS : FOR ID1 ASSIGN E TO1 E DO3 STATUTES NEXT\n\t\n\tSTATEMENTS : GOSUB POINT ID\n\t\n\tE : E PLUS T\n\t| E MINUS T\n\t\n\tE : T\n\t\n\tT : T TIMES F\n\t| T DIVIDE F\n\t\n\tT : F\n\t\n\tF : NUMBER\n\t\n\tF : FLOATNUMBER\n\t\n\tF : VAR\n\t\n\tF : LPARENT E RPARENT\n\t\n\tEL : EL OR TL\n\t\n\tEL : TL NOT\n\t| TL\n\t\n\tTL : TL AND FL\n\t\n\tTL : FL\n\t\n\tFL : OPERATOR OPREL OPERATOR\n\t\n\tFL : LPARENT EL RPARENT\n\t\n\tOPREL : LT\n\t| LTE\n\t| GT\n\t| GTE\n\t| NE\n\t| EQUAL\n\t\n\tOPERATOR : ID\n\t\n\tOPERATOR : NUMBER\n\t\n\tOPERATOR : FLOATNUMBER\n\t\n\tIDLIST : ID\n\t\n\tIDLIST : IDLIST COMMA ID\n\t\n\tTIPO : WORD\n\t| FLOAT\n\t| ARRAY DCLARRAY\n\t| MATRIX DCLMATRIX\n\t| CUBE DCLCUBE\n\t\n\tDCLARRAY : LBRACKET IDENTIFICATOR RBRACKET\n\t\n\tDCLMATRIX : LBRACKET IDENTIFICATOR RBRACKET LBRACKET IDENTIFICATOR RBRACKET\n\t\n\tDCLCUBE : LBRACKET IDENTIFICATOR RBRACKET LBRACKET IDENTIFICATOR RBRACKET LBRACKET IDENTIFICATOR RBRACKET\n\t\n\tIDENTIFICATOR : NUMBER\n\t| ID\n\t\n\tVAR : ID\n\t| ID DCLARRAY\n\t| ID DCLMATRIX\n\t| ID DCLCUBE\n\t\n\tELSE1 : ELSE STATUTES\n\t\n\tELSE1 :\n\t\n\tTHEN1 : THEN\n\t\n\tWHILE1 : WHILE\n\t\n\tDO1 : DO\n\t\n\tDO2 : DO\n\t\n\tID1 : ID\n\t\n\tTO1 : TO\n\t\n\tDO3 : DO\n\t\n\tVALUE : LPARENT VAR RPARENT\n\t\n\tVALUE : TEXT\n\t\n\tTEXT : LPARENT STRING RPARENT\n\t'
    
_lr_action_items = {'PROGRAM':([0,],[3,]),'$end':([1,67,],[0,-1,]),'ID':([2,3,6,8,15,18,22,23,25,27,42,50,58,62,64,66,69,73,76,78,81,82,83,84,85,86,87,88,92,93,108,125,126,127,128,135,136,138,139,145,158,],[4,-2,10,13,36,40,51,51,57,-66,40,51,94,99,99,99,40,99,40,51,51,51,-38,-39,-40,-41,-42,-43,51,40,40,40,40,40,40,40,-70,99,99,99,99,]),'DIM':([4,60,],[6,6,]),'SUBPROCEDURE':([4,5,60,95,96,121,],[-5,8,-5,-7,-4,8,]),'LET':([4,5,7,11,12,13,24,28,38,60,77,79,90,91,95,96,121,132,137,152,153,],[-5,-9,-3,18,18,-8,18,-68,18,-5,18,-65,18,-67,-7,-4,-9,18,-6,18,-71,]),'PRINT':([4,5,7,11,12,13,24,28,38,60,77,79,90,91,95,96,121,132,137,152,153,],[-5,-9,-3,19,19,-8,19,-68,19,-5,19,-65,19,-67,-7,-4,-9,19,-6,19,-71,]),'INPUT':([4,5,7,11,12,13,24,28,38,60,77,79,90,91,95,96,121,132,137,152,153,],[-5,-9,-3,20,20,-8,20,-68,20,-5,20,-65,20,-67,-7,-4,-9,20,-6,20,-71,]),'CLS':([4,5,7,11,12,13,24,28,38,60,77,79,90,91,95,96,121,132,137,152,153,],[-5,-9,-3,21,21,-8,21,-68,21,-5,21,-65,21,-67,-7,-4,-9,21,-6,21,-71,]),'IF':([4,5,7,11,12,13,24,28,38,60,77,79,90,91,95,96,121,132,137,152,153,],[-5,-9,-3,22,22,-8,22,-68,22,-5,22,-65,22,-67,-7,-4,-9,22,-6,22,-71,]),'FOR':([4,5,7,11,12,13,24,28,38,60,77,79,90,91,95,96,121,132,137,152,153,],[-5,-9,-3,25,25,-8,25,-68,25,-5,25,-65,25,-67,-7,-4,-9,25,-6,25,-71,]),'GOSUB':([4,5,7,11,12,13,24,28,38,60,77,79,90,91,95,96,121,132,137,152,153,],[-5,-9,-3,26,26,-8,26,-68,26,-5,26,-65,26,-67,-7,-4,-9,26,-6,26,-71,]),'WHILE':([4,5,7,11,12,13,24,28,38,60,77,79,90,91,95,96,121,132,137,152,153,],[-5,-9,-3,27,27,-8,27,-68,27,-5,27,-65,27,-67,-7,-4,-9,27,-6,27,-71,]),'DO':([4,5,7,11,12,13,24,28,38,40,47,48,51,52,53,54,60,70,71,72,77,79,80,90,91,95,96,102,104,105,106,107,114,115,116,117,121,122,130,132,137,140,141,142,143,144,148,152,153,154,156,161,],[-5,-9,-3,28,28,-8,28,-68,28,-59,-33,-35,-44,-45,-46,91,-5,-60,-61,-62,28,-65,-32,28,-67,-7,-4,-29,-23,-26,-27,-28,-31,-34,-36,-37,-9,-54,-54,28,-6,-21,-22,-24,-25,-30,153,28,-71,-55,-55,-56,]),'END':([4,5,7,11,12,16,24,38,60,68,77,90,95,96,121,132,137,152,],[-5,-9,-3,-11,-11,37,-11,-11,-5,-10,-11,-11,-7,-4,-9,-11,-6,-11,]),'AS':([9,10,36,],[14,-47,-48,]),'COMMA':([9,10,36,],[15,-47,-48,]),'ENDSUB':([11,12,13,24,29,38,68,77,90,132,152,],[-11,-11,-8,-11,59,-11,-10,-11,-11,-11,-11,]),'ELSE':([11,12,24,38,68,77,79,90,113,132,152,],[-11,-11,-11,-11,-10,-11,-65,-11,132,-11,-11,]),'ENDIF':([11,12,24,38,68,77,79,90,113,131,132,147,152,],[-11,-11,-11,-11,-10,-11,-65,-11,-64,146,-11,-63,-11,]),'WHEND':([11,12,24,38,68,77,90,91,118,132,152,],[-11,-11,-11,-11,-10,-11,-11,-67,133,-11,-11,]),'LOOPUNTIL':([11,12,24,28,38,55,68,77,90,132,152,],[-11,-11,-11,-68,-11,92,-10,-11,-11,-11,-11,]),'NEXT':([11,12,24,38,68,77,90,132,152,153,157,],[-11,-11,-11,-11,-10,-11,-11,-11,-11,-71,159,]),'WORD':([14,],[31,]),'FLOAT':([14,],[32,]),'ARRAY':([14,],[33,]),'MATRIX':([14,],[34,]),'CUBE':([14,],[35,]),'SEMMICOLON':([17,21,30,31,32,37,40,41,43,59,61,63,65,70,71,72,94,102,103,104,105,106,107,110,111,112,122,130,133,134,140,141,142,143,144,146,154,156,159,161,],[38,-15,60,-49,-50,67,-59,-13,-73,95,-51,-52,-53,-60,-61,-62,-20,-29,-12,-23,-26,-27,-28,-72,-74,-14,-54,-54,-17,-18,-21,-22,-24,-25,-30,-16,-55,-55,-19,-56,]),'LPARENT':([19,20,22,23,27,50,69,78,81,92,93,108,125,126,127,128,135,136,],[42,45,50,50,-66,50,108,50,50,50,108,108,108,108,108,108,108,-70,]),'NUMBER':([22,23,27,50,62,64,66,69,73,78,81,82,83,84,85,86,87,88,92,93,108,125,126,127,128,135,136,138,139,145,158,],[52,52,-66,52,98,98,98,106,98,52,52,52,-38,-39,-40,-41,-42,-43,52,106,106,106,106,106,106,106,-70,98,98,98,98,]),'FLOATNUMBER':([22,23,27,50,69,78,81,82,83,84,85,86,87,88,92,93,108,125,126,127,128,135,136,],[53,53,-66,53,107,53,53,53,-38,-39,-40,-41,-42,-43,53,107,107,107,107,107,107,107,-70,]),'POINT':([26,],[58,]),'LBRACKET':([33,34,35,40,123,124,130,155,156,],[62,64,66,73,138,139,145,158,158,]),'ASSIGN':([39,40,56,57,70,71,72,122,130,154,156,161,],[69,-59,93,-69,-60,-61,-62,-54,-54,-55,-55,-56,]),'TO':([40,70,71,72,102,104,105,106,107,120,122,130,140,141,142,143,144,154,156,161,],[-59,-60,-61,-62,-29,-23,-26,-27,-28,136,-54,-54,-21,-22,-24,-25,-30,-55,-55,-56,]),'PLUS':([40,70,71,72,102,103,104,105,106,107,120,122,129,130,140,141,142,143,144,148,154,156,161,],[-59,-60,-61,-62,-29,125,-23,-26,-27,-28,125,-54,125,-54,-21,-22,-24,-25,-30,125,-55,-55,-56,]),'MINUS':([40,70,71,72,102,103,104,105,106,107,120,122,129,130,140,141,142,143,144,148,154,156,161,],[-59,-60,-61,-62,-29,126,-23,-26,-27,-28,126,-54,126,-54,-21,-22,-24,-25,-30,126,-55,-55,-56,]),'TIMES':([40,70,71,72,102,104,105,106,107,122,130,140,141,142,143,144,154,156,161,],[-59,-60,-61,-62,-29,127,-26,-27,-28,-54,-54,127,127,-24,-25,-30,-55,-55,-56,]),'DIVIDE':([40,70,71,72,102,104,105,106,107,122,130,140,141,142,143,144,154,156,161,],[-59,-60,-61,-62,-29,128,-26,-27,-28,-54,-54,128,128,-24,-25,-30,-55,-55,-56,]),'RPARENT':([40,47,48,51,52,53,70,71,72,74,75,80,89,102,104,105,106,107,114,115,116,117,122,129,130,140,141,142,143,144,154,156,161,],[-59,-33,-35,-44,-45,-46,-60,-61,-62,110,111,-32,117,-29,-23,-26,-27,-28,-31,-34,-36,-37,-54,144,-54,-21,-22,-24,-25,-30,-55,-55,-56,]),'STRING':([42,45,],[75,75,]),'GTGT':([44,111,],[76,-74,]),'OR':([46,47,48,51,52,53,54,80,89,114,115,116,117,119,],[78,-33,-35,-44,-45,-46,78,-32,78,-31,-34,-36,-37,78,]),'THEN':([46,47,48,51,52,53,80,114,115,116,117,],[79,-33,-35,-44,-45,-46,-32,-31,-34,-36,-37,]),'NOT':([47,48,51,52,53,115,116,117,],[80,-35,-44,-45,-46,-34,-36,-37,]),'ENDO':([47,48,51,52,53,80,114,115,116,117,119,],[-33,-35,-44,-45,-46,-32,-31,-34,-36,-37,134,]),'AND':([47,48,51,52,53,114,115,116,117,],[81,-35,-44,-45,-46,81,-34,-36,-37,]),'LT':([49,51,52,53,],[83,-44,-45,-46,]),'LTE':([49,51,52,53,],[84,-44,-45,-46,]),'GT':([49,51,52,53,],[85,-44,-45,-46,]),'GTE':([49,51,52,53,],[86,-44,-45,-46,]),'NE':([49,51,52,53,],[87,-44,-45,-46,]),'EQUAL':([49,51,52,53,],[88,-44,-45,-46,]),'RBRACKET':([97,98,99,100,101,109,149,150,151,160,],[122,-57,-58,123,124,130,154,155,156,161,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'PROGRAM1':([0,],[2,]),'VARIABLE':([4,60,],[5,96,]),'SP':([5,121,],[7,137,]),'IDLIST':([6,],[9,]),'SALTO':([7,],[11,]),'ID2':([8,],[12,]),'STATUTES':([11,12,24,38,77,90,132,152,],[16,29,55,68,113,118,147,157,]),'STATEMENTS':([11,12,24,38,77,90,132,152,],[17,17,17,17,17,17,17,17,]),'WHILE1':([11,12,24,38,77,90,132,152,],[23,23,23,23,23,23,23,23,]),'DO2':([11,12,24,38,77,90,132,152,],[24,24,24,24,24,24,24,24,]),'TIPO':([14,],[30,]),'VAR':([18,42,69,76,93,108,125,126,127,128,135,],[39,74,102,112,102,102,102,102,102,102,102,]),'VALUE':([19,],[41,]),'TEXT':([19,20,],[43,44,]),'EL':([22,23,50,92,],[46,54,89,119,]),'TL':([22,23,50,78,92,],[47,47,47,114,47,]),'FL':([22,23,50,78,81,92,],[48,48,48,48,115,48,]),'OPERATOR':([22,23,50,78,81,82,92,],[49,49,49,49,49,116,49,]),'ID1':([25,],[56,]),'DCLARRAY':([33,40,],[61,70,]),'DCLMATRIX':([34,40,],[63,71,]),'DCLCUBE':([35,40,],[65,72,]),'THEN1':([46,],[77,]),'OPREL':([49,],[82,]),'DO1':([54,],[90,]),'IDENTIFICATOR':([62,64,66,73,138,139,145,158,],[97,100,101,109,149,150,151,160,]),'E':([69,93,108,135,],[103,120,129,148,]),'T':([69,93,108,125,126,135,],[104,104,104,140,141,104,]),'F':([69,93,108,125,126,127,128,135,],[105,105,105,105,105,142,143,105,]),'RETURN':([95,],[121,]),'ELSE1':([113,],[131,]),'TO1':([120,],[135,]),'DO3':([148,],[152,]),}

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
  ('STATEMENTS -> IF EL THEN1 STATUTES ELSE1 ENDIF','STATEMENTS',6,'p_STATEMENTS_IF','syntactic_analyser.py',99),
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
  ('TIPO -> WORD','TIPO',1,'p_TIPO_WORD','syntactic_analyser.py',250),
  ('TIPO -> FLOAT','TIPO',1,'p_TIPO_WORD','syntactic_analyser.py',251),
  ('TIPO -> ARRAY DCLARRAY','TIPO',2,'p_TIPO_WORD','syntactic_analyser.py',252),
  ('TIPO -> MATRIX DCLMATRIX','TIPO',2,'p_TIPO_WORD','syntactic_analyser.py',253),
  ('TIPO -> CUBE DCLCUBE','TIPO',2,'p_TIPO_WORD','syntactic_analyser.py',254),
  ('DCLARRAY -> LBRACKET IDENTIFICATOR RBRACKET','DCLARRAY',3,'p_DCLARRAY','syntactic_analyser.py',260),
  ('DCLMATRIX -> LBRACKET IDENTIFICATOR RBRACKET LBRACKET IDENTIFICATOR RBRACKET','DCLMATRIX',6,'p_DCLMATRIX','syntactic_analyser.py',265),
  ('DCLCUBE -> LBRACKET IDENTIFICATOR RBRACKET LBRACKET IDENTIFICATOR RBRACKET LBRACKET IDENTIFICATOR RBRACKET','DCLCUBE',9,'p_DCLCUBE','syntactic_analyser.py',270),
  ('IDENTIFICATOR -> NUMBER','IDENTIFICATOR',1,'p_IDENTIFICATOR','syntactic_analyser.py',275),
  ('IDENTIFICATOR -> ID','IDENTIFICATOR',1,'p_IDENTIFICATOR','syntactic_analyser.py',276),
  ('VAR -> ID','VAR',1,'p_STATEMENTS_INPUT_VAR','syntactic_analyser.py',281),
  ('VAR -> ID DCLARRAY','VAR',2,'p_STATEMENTS_INPUT_VAR','syntactic_analyser.py',282),
  ('VAR -> ID DCLMATRIX','VAR',2,'p_STATEMENTS_INPUT_VAR','syntactic_analyser.py',283),
  ('VAR -> ID DCLCUBE','VAR',2,'p_STATEMENTS_INPUT_VAR','syntactic_analyser.py',284),
  ('ELSE1 -> ELSE STATUTES','ELSE1',2,'p_STATEMENTS_IF_ELSE1','syntactic_analyser.py',290),
  ('ELSE1 -> <empty>','ELSE1',0,'p_STATEMENTS_IF_ELSE1_EMPTY','syntactic_analyser.py',296),
  ('THEN1 -> THEN','THEN1',1,'p_STATEMENTS_IF_THEN1','syntactic_analyser.py',301),
  ('WHILE1 -> WHILE','WHILE1',1,'p_STATEMENTS_WHILE_WHILE1','syntactic_analyser.py',307),
  ('DO1 -> DO','DO1',1,'p_STATEMENTS_WHILE_DO1','syntactic_analyser.py',313),
  ('DO2 -> DO','DO2',1,'p_STATEMENTS_DO_DO2','syntactic_analyser.py',319),
  ('ID1 -> ID','ID1',1,'p_STATEMENTS_FOR_ID','syntactic_analyser.py',325),
  ('TO1 -> TO','TO1',1,'p_STATEMENTS_FOR_TO','syntactic_analyser.py',331),
  ('DO3 -> DO','DO3',1,'p_STATEMENTS_FOR_DO','syntactic_analyser.py',337),
  ('VALUE -> LPARENT VAR RPARENT','VALUE',3,'p_VALUE','syntactic_analyser.py',343),
  ('VALUE -> TEXT','VALUE',1,'p_VALUE1','syntactic_analyser.py',349),
  ('TEXT -> LPARENT STRING RPARENT','TEXT',3,'p_TEXT','syntactic_analyser.py',355),
]
