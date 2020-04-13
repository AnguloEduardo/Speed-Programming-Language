import ply.yacc as yacc
import os
import codecs
import re
from syntax_analyser import tokens
from sys import stdin
# Problema con las comas y con los strings
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
	print("program")

def p_V(p):
	'''
	V : DIM IDLIST AS TIPO SEMMICOLON V
	|
	'''
	print("V")

def p_IDLIST(P):
	'''
	IDLIST : ID
	| IDLIST COMMA ID
	|
	'''
	print("IDLIST")

def p_TIPO(p):
	'''
	TIPO : WORD
	| FLOAT
	| ARRAY LBRACKET E RBRACKET
	| MATRIX LBRACKET E RBRACKET LBRACKET E RBRACKET
	| CUBE LBRACKET E RBRACKET LBRACKET E RBRACKET LBRACKET E RBRACKET
	'''
	print("TIPO")

def p_SP(p):
	'''
	SP : SUBPROCEDURE ID V X ENDSUB SEMMICOLON SP
	|
	'''
	print("SP")

def p_X(p):
	'''
	X : S R
	|
	'''
	print("X")

def p_R(p):
	'''
	R : SEMMICOLON S R
	|
	'''
	print("R")

def p_S(p):
	'''
	S : LET E ASSIGN E
	| PRINT Q
	| INPUT H GTGT U
	| CLS
	| IF EL THEN X ELSE1 ENDIF
	| WHILE EL X WHEND
	| DO X LOOPUNTIL EL ENDO
	| FOR O TO E X NEXT
	| GOSUB ID
	'''
	print("S")

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
	print("Q")

def p_H(p):
	'''
	H : TEXT
	|
	'''

def p_TEXT(p):
	'''
    TEXT : LPARENT STRING RPARENT
    '''
    #print("TEXT")

def p_ELSE1(p):
	'''
	ELSE1 : ELSE X
	|
	'''
	print("ELSE1")

def p_E(p):
	'''
	E : E PLUS T
	| E MINUS T
	| T
	'''
	print("E")

def p_T(p):
	'''
	T : T TIMES F
	| T DIVIDE F
	| F
	'''
	print("T")

def p_F(p):
	'''
	F : NUMBER
	| U
	| LPARENT E RPARENT
	'''
	print("F")

def p_EL(p):
	'''
	EL : EL OR TL
	| NOT TL
	| TL
	'''
	print("EL")

def p_TL(p):
	'''
	TL : TL AND FL
	| FL
	'''
	print("TL")

def p_FL(p):
	'''
	FL : K OPREL K
	| LPARENT EL RPARENT
	'''
	print("FL")

def p_OPREL(p):
	'''
	OPREL : LT
	| LTE
	| GT
	| GTE
	| NE
	| EQUAL
	'''
	print("OPREL")

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