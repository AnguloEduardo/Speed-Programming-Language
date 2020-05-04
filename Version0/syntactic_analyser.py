import ply.yacc as yacc
import os
import codecs
import re
from syntax_analyser import tokens
from sys import stdin

precendence = (
	('right','ASSING'),
	('left','NE'),
	('left','AND','OR','NOT'),
	('left','LT','LTE','GT','GTE'),
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE'),
	('left','LPARENT','RPARENT')
)

def p_PROGRAM(p):
	'''
	program : PROGRAM ID V SP X END
	'''

def p_V(p):
	'''
	V : DIM IDLIST AS TIPO SEMMICOLON V
	|
	'''

def p_IDLIST(P):
	'''
	IDLIST : ID
	| IDLIST COMMA ID
	|
	'''

def p_TIPO(p):
	'''
	TIPO : WORD
	| FLOAT
	| ARRAY LBRACKET E RBRACKET
	| MATRIX LBRACKET E RBRACKET LBRACKET E RBRACKET
	| CUBE LBRACKET E RBRACKET LBRACKET E RBRACKET LBRACKET E RBRACKET
	'''

def p_SP(p):
	'''
	SP : SUBPROCEDURE ID V X ENDSUB SEMMICOLON SP
	|
	'''
def p_X(p):
	'''
	X : S SEMMICOLON X
	|
	'''

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

def p_O(p):
	'''
	O : E
	| E ASSIGN E
	'''

def p_U(p):
	'''
	U : ID
	| ID LBRACKET E RBRACKET
	| ID LBRACKET E RBRACKET LBRACKET E RBRACKET
	| ID LBRACKET E RBRACKET LBRACKET E RBRACKET LBRACKET E RBRACKET
	'''

def p_Q(p):
	'''
	Q : LPARENT U RPARENT
	| TEXT
	'''

def p_TEXT(p):
	'''
    TEXT : LPARENT STRING H RPARENT
    |
    '''

def p_H(p):
	'''
	H : PLUS STRING H
	| PLUS U H
	|
	'''

def p_ELSE1(p):
	'''
	ELSE1 : ELSE X
	|
	'''

def p_E(p):
	'''
	E : E PLUS T
	| E MINUS T
	| T
	'''

def p_T(p):
	'''
	T : T TIMES F
	| T DIVIDE F
	| F
	'''

def p_F(p):
	'''
	F : NUMBER
	| U
	| LPARENT E RPARENT
	'''

def p_EL(p):
	'''
	EL : EL OR TL
	| NOT TL
	| TL
	'''

def p_TL(p):
	'''
	TL : TL AND FL
	| FL
	'''

def p_FL(p):
	'''
	FL : K OPREL K
	| LPARENT EL RPARENT
	'''

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

test = os.getcwd()+"\\test\\prueba2.txt"
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc('SLR')
result = parser.parse(cadena)

print (result)