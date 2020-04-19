import ply.yacc as yacc
import os
import codecs
import re
from semantic_analyser import *
from syntax_analyser import tokens
from sys import stdin

tableID = []
tableType = []
repetido = False

precendence = (
	('right','ASSING'),
	('left','NE'),
	('left','AND','OR','NOT'),
	('left','LT','LTE','GT','GTE'),
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE'),
	('left','LPARENT','RPARENT')
)

def variabletable(p):
	global repetido
	while len(tableID) > len(tableType) and not (repetido):
		tableType.append(p)

def idTable(p):
	global repetido
	repetido = False
	for x in tableID:
		if x == p:
			repetido = True
			break
	if repetido == False:
		tableID.append(p)



def p_PROGRAM(p):
	'''
	program : PROGRAM ID V SP X END
	'''
	#p[0] = PROGRAM(p[3],p[4],p[5],"program")

def p_V(p):
	'''
	V : DIM IDLIST AS TIPO SEMMICOLON V
	|
	'''
	#p[0] = V(p[2],p[4],p[6],"V")

def p_IDLIST(p):
	'''
	IDLIST : ID
	'''
	idTable(p[1])
	#p[0] = IDLIST(p[1],"IDLIST")

def p_IDLIST2(p):
	'''
	IDLIST : IDLIST COMMA ID
	|
	'''
	idTable(p[3])

def p_TIPO(p):
	'''
	TIPO : WORD
	| FLOAT
	| ARRAY LBRACKET E RBRACKET
	| MATRIX LBRACKET E RBRACKET LBRACKET E RBRACKET
	| CUBE LBRACKET E RBRACKET LBRACKET E RBRACKET LBRACKET E RBRACKET
	'''
	#p[0] = TIPO(p[5],p[9],p[12],p[16],p[19],p[22],"TIPO")
	variabletable(p[1])

def p_SP(p):
	'''
	SP : SUBPROCEDURE ID X ENDSUB SEMMICOLON SP
	|
	'''
	#p[0] = SP(p[3],p[4],p[7],"SP")

def p_X(p):
	'''
	X : S SEMMICOLON X
	|
	'''
	#p[0] = X(p[1],p[3],"X")

def p_S(p):
	'''
	S : LET E ASSIGN E
	| PRINT Q
	| INPUT TEXT GTGT U
	| CLS
	| IF EL THEN X ELSE1 ENDIF
	| WHILE EL X WHEND
	| DO X LOOPUNTIL EL ENDO
	| FOR O TO E X NEXT
	| GOSUB ID
	'''
	#p[0] = S(p[2],p[4],p[6],p[8],p[10],p[13],p[15],p[16],p[19],p[20],p[23],p[25],p[28],p[30],p[31],"S")

def p_O(p):
	'''
	O : E
	| E ASSIGN E
	'''
	#p[0] = O(p[1],p[2],p[4],"O")

def p_U(p):
	'''
	U : ID
	| ID LBRACKET E RBRACKET
	| ID LBRACKET E RBRACKET LBRACKET E RBRACKET
	| ID LBRACKET E RBRACKET LBRACKET E RBRACKET LBRACKET E RBRACKET
	'''
	#p[0] = U(p[4],p[8],p[11],p[15],p[18],p[21],"U")

def p_Q(p):
	'''
	Q : LPARENT U RPARENT
	| TEXT
	'''
	#p[0] = Q(p[2],p[4],"Q")

def p_TEXT(p):
	'''
    TEXT : LPARENT STRING H RPARENT
    |
    '''
	#p[0] = TEXT(p[2],p[3],"TEXT")

def p_H(p):
	'''
	H : PLUS STRING H
	| PLUS U H
	|
	'''
	#p[0] = H(p[2],p[3],p[5],p[6],"H")

def p_ELSE1(p):
	'''
	ELSE1 : ELSE X
	|
	'''
	#p[0] = ELSE1(p[1],"ELSE1")

def p_E(p):
	'''
	E : E PLUS T
	| E MINUS T
	| T
	'''
	#p[0] = E(p[1],p[3],p[4],p[6],p[7],"E")

def p_T(p):
	'''
	T : T TIMES F
	| T DIVIDE F
	| F
	'''
	#p[0] = T(p[1],p[3],p[4],p[6],p[7],"T")

def p_F(p):
	'''
	F : NUMBER
	| U
	| LPARENT E RPARENT
	'''
	#p[0] = F(p[2],p[4],"F")

def p_EL(p):
	'''
	EL : EL OR TL
	| NOT TL
	| TL
	'''
	#p[0] = EL(p[1],p[3],p[5],p[6],"EL")

def p_TL(p):
	'''
	TL : TL AND FL
	| FL
	'''
	#p[0] = TL(p[1],p[3],p[4],"TL")

def p_FL(p):
	'''
	FL : K OPREL K
	| LPARENT EL RPARENT
	'''
	#p[0] = FL(p[1],p[3],p[5],"FL")

def p_OPREL(p):
	'''
	OPREL : LT
	| LTE
	| GT
	| GTE
	| NE
	| EQUAL
	'''

def p_K(p):
	'''
	K : ID
	| NUMBER
	'''

def p_error(p):
	print("Incorrect grammar\n", p)
	print("Error in the line "+str(p.lineno))
'''
def traducir(result):
	graphFile = open('graphviztree.vz','w')
	graphFile.write(result.traducir())
	graphFile.close()
	print ("El programa traducido se guardo en \"graphviztrhee.vz\"")
'''
test = os.getcwd()+"\\test\\prueba2.txt"
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc('SLR')
result = parser.parse(cadena)

#result.imprimir(" ")
#print (result.traducir())
#traducir(result)

symboltable ="\n".join("{} {}".format(x, y) for x, y in zip(tableID, tableType))

print (result)
print (symboltable)