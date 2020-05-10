import ply.yacc as yacc
import os
import codecs
import re
from symbol_table import *
from cuadruplosExpresiones import *
from lexical_analyser import tokens
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
	program : PROGRAM ID VARIABLE SP X END SEMMICOLON
	'''

def p_VARIABLE(p):
	'''
	VARIABLE : DIM IDLIST AS TIPO SEMMICOLON VARIABLE
	|
	'''

def p_IDLIST(p):
	'''
	IDLIST : ID
	'''
	insertID(p[1])

def p_IDLIST2(p):
	'''
	IDLIST : IDLIST COMMA ID
	'''
	insertID(p[3])

def p_TIPO_WORD(p):
	'''
	TIPO : WORD
	| FLOAT
	| ARRAY DCLARRAY
	| MATRIX DCLMATRIX
	| CUBE DCLCUBE
	'''
	insertType(p[1])

def p_DCLARRAY(p):
	'''
	DCLARRAY : LBRACKET Z RBRACKET
	'''

def p_DCLMATRIX(p):
	'''
	DCLMATRIX : LBRACKET Z RBRACKET LBRACKET Z RBRACKET
	'''

def p_DCLCUBE(p):
	'''
	DCLCUBE : LBRACKET Z RBRACKET LBRACKET Z RBRACKET LBRACKET Z RBRACKET
	'''

def p_Z(p):
	'''
	Z : NUMBER
	| ID
	'''

def p_SP(p):
	'''
	SP : SUBPROCEDURE ID X ENDSUB SEMMICOLON SP
	|
	'''

def p_X(p):
	'''
	X : STATEMENTS SEMMICOLON X
	|
	'''

def p_STATEMENTS_LET(p):
	'''
	STATEMENTS : LET U ASSIGN E
	'''
	genCuadruplo(p[3])

def p_STATEMENTS_PRINT(p):
	'''
	STATEMENTS : PRINT Q
	'''

def p_STATEMENTS_INPUT(p):
	'''
	STATEMENTS : INPUT TEXT GTGT VAR
	'''

def p_STATEMENTS_INPUT_VAR(p):
	'''
	VAR : ID
	| ID DCLARRAY
	| ID DCLMATRIX
	| ID DCLCUBE
	'''
def p_STATEMENTS_CLS(p):
	'''
	STATEMENTS : CLS
	'''
	genCuadruploCLS()

def p_STATEMENTS_IF(p):
	'''
	STATEMENTS : IF EL THEN1 X ELSE1 X ENDIF
	'''
	finIF()

def p_STATEMENTS_IF_ELSE1(p):
	'''
	ELSE1 : ELSE
	'''
	goto()

def p_STATEMENTS_IF_ELSE1_EMPTY(p):
	'''
	ELSE1 :
	'''

def p_STATEMENTS_IF_THEN1(p):
	'''
	THEN1 : THEN
	'''
	gotofalso()

def p_STATEMENTS_WHILE(p):
	'''
	STATEMENTS : WHILE1 EL DO1 X WHEND
	'''
	finWhile()

def p_STATEMENTS_WHILE_WHILE1(p):
	'''
	WHILE1 : WHILE
	'''
	origen()

def p_STATEMENTS_WHILE_DO1(p):
	'''
	DO1 : DO
	'''
	gotofalso()

def p_STATEMENTS_DO(p):
	'''
	STATEMENTS : DO2 X LOOPUNTIL EL ENDO
	'''
	finDoWhile()

def p_STATEMENTS_DO_DO2(p):
	'''
	DO2 : DO
	'''
	origen()

def p_STATEMENTS_FOR(p):
	'''
	STATEMENTS : FOR ID1 ASSIGN E TO1 E DO3 X NEXT
	'''
	finFor()

def p_STATEMENTS_FOR_ID(p):
	'''
	ID1 : ID
	'''
	pushOperandos(int(buscar(p[1])))

def p_STATEMENTS_FOR_TO(p):
	'''
	TO1 : TO
	'''
	genCuadruploFor("=")

def p_STATEMENTS_FOR_DO(p):
	'''
	DO3 : DO
	'''
	forAction3()

def p_STATEMENTS_GOSUB(p):
	'''
	STATEMENTS : GOSUB ID
	'''

def p_U(p):
	'''
	U : ID
	'''
	pushOperandos(int(buscar(p[1])))


def p_U1(p):
	'''
	U : ID DCLARRAY
	'''
	pushOperandos(int(buscar(p[1])))

def p_U2(p):
	'''
	U : ID DCLMATRIX
	'''
	pushOperandos(int(buscar(p[1])))

def p_U3(p):
	'''
	U : ID DCLCUBE
	'''
	pushOperandos(int(buscar(p[1])))

def p_Q(p):
	'''
	Q : LPARENT VAR RPARENT
	'''

def p_Q1(p):
	'''
	Q : TEXT
	'''

def p_TEXT(p):
	'''
    TEXT : LPARENT STRING H RPARENT
    '''

def p_TEXT_EMPTY(p):
	'''
	TEXT :
	'''

def p_H(p):
	'''
	H : PLUS STRING H
	'''

def p_H1(p):
	'''
	H : PLUS U H
	'''

def p_H_EMPTY(p):
	'''
	H :
	'''

def p_E(p):
	'''
	E : E PLUS T
	| E MINUS T
	'''
	genCuadruplo(p[2])

def p_E1(p):
	'''
	E : T
	'''

def p_T(p):
	'''
	T : T TIMES F
	| T DIVIDE F
	'''

def p_T1(p):
	'''
	T : F
	'''

def p_F(p):
	'''
	F : NUMBER
	'''
	pushOperandos(int(p[1])*(-1))

def p_F1(p):
	'''
	F : U
	'''

def p_F2(p):
	'''
	F : LPARENT E RPARENT
	'''

def p_EL(p):
	'''
	EL : EL OR TL
	'''
	genCuadruplo(p[2])

def p_EL1(p):
	'''
	EL : TL NOT
	| TL
	'''

def p_TL(p):
	'''
	TL : TL AND FL
	'''
	genCuadruplo(p[2])

def p_TL1(p):
	'''
	TL : FL
	'''

def p_FL(p):
	'''
	FL : K OPREL K
	'''
	genCuadruplo(p[2])

def p_FL1(p):
	'''
	FL : LPARENT EL RPARENT
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
	p[0] = p[1]

def p_K(p):
	'''
	K : ID
	'''
	pushOperandos(int(buscar(p[1])))

def p_K1(p):
	'''
	K : NUMBER
	'''
	pushOperandos(int(p[1])*(-1))

def p_error(p):
	print("Incorrect grammar\n", p)
	print("Error in the line "+str(p.lineno))

def traducir(result):
	graphFile = open('graphviztree.vz','w')
	graphFile.write(result.traducir())
	graphFile.close()
	print ("El programa traducido se guardo en \"graphviztrhee.vz\"")

test = os.getcwd()+"\\test\\prueba2.txt"
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()
parser = yacc.yacc('SLR')
result = parser.parse(cadena)
imprimirSymbolTable()
imprimirCuadruplos()
print (result)