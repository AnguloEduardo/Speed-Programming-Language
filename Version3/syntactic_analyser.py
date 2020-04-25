import ply.yacc as yacc
import os
import codecs
import re
from semantic_analyser import *
from symbol_table import *
from cuadruplos import *
from lexical_analyser import tokens
from sys import stdin
from graphviz import Digraph

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
	program : PROGRAM ID VARIABLE SP X END
	'''
	p[0] = PROGRAM(p[3],p[4],p[5],"program")

def p_VARIABLE(p):
	'''
	VARIABLE : DIM IDLIST AS TIPO SEMMICOLON VARIABLE
	'''
	p[0] = VARIABLE(p[2],p[4],p[6],"VARIABLE")

def p_VARIABLE_EMPTY(p):
	'''
	VARIABLE :
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
	p[0] = IDLIST(p[1],"IDLIST")

def p_IDLIST_EMPTY(p):
	'''
	IDLIST :
	'''

def p_TIPO_WORD(p):
	'''
	TIPO : WORD
	'''
	insertType(p[1])

def p_TIPO_FLOAT(p):
	'''
	TIPO : FLOAT
	'''
	insertType(p[1])

def p_TIPO_ARRAY(p):
	'''
	TIPO : ARRAY DCLARRAY
	'''
	insertType(p[1])
	p[0] = TIPO_ARRAY(p[2],"TIPO_ARRAY")

def p_TIPO_MATRIX(p):
	'''
	TIPO : MATRIX DCLMATRIX
	'''
	insertType(p[1])
	p[0] = TIPO_MATRIX(p[2],"TIPO_MATRIX")

def p_TIPO_CUBE(p):
	'''
	TIPO : CUBE DCLCUBE
	'''
	insertType(p[1])
	p[0] = TIPO_CUBE(p[2],"TIPO_CUBE")

def p_DCLARRAY(p):
	'''
	DCLARRAY : LBRACKET Z RBRACKET
	'''
	p[0] = DCLARRAY(p[2],"DCLARRAY")

def p_DCLMATRIX(p):
	'''
	DCLMATRIX : LBRACKET Z RBRACKET LBRACKET Z RBRACKET
	'''
	p[0] = DCLMATRIX(p[2],p[5],"DCLMATRIX")

def p_DCLCUBE(p):
	'''
	DCLCUBE : LBRACKET Z RBRACKET LBRACKET Z RBRACKET LBRACKET Z RBRACKET
	'''
	p[0] = DCLCUBE(p[2],p[5],p[8],"DCLCUBE")

def p_Z(p):
	'''
	Z : NUMBER
	| ID
	'''
def p_SP(p):
	'''
	SP : SUBPROCEDURE ID X ENDSUB SEMMICOLON SP
	'''
	p[0] = SP(p[3],p[6],"SP")

def p_SP_EMPTY(p):
	'''
	SP :
	'''

def p_X(p):
	'''
	X : STATEMENTS SEMMICOLON X
	'''
	p[0] = X(p[1],p[3],"X")

def p_X1(p):
	'''
	X :
	'''

def p_STATEMENTS_LET(p):
	'''
	STATEMENTS : LET U ASSIGN E
	'''
	genCuadruploAssign(p[3])
	p[0] = STATEMENTS_LET(p[2],p[4],"STATEMENTS_LET")

def p_STATEMENTS_PRINT(p):
	'''
	STATEMENTS : PRINT Q
	'''
	p[0] = STATEMENTS_PRINT(p[2],"STATEMENTS_PRINT")

def p_STATEMENTS_INPUT(p):
	'''
	STATEMENTS : INPUT TEXT GTGT U
	'''
	p[0] = STATEMENTS_INPUT(p[2],p[3],p[4],"STATEMENTS_INPUT")

def p_STATEMENTS_CLS(p):
	'''
	STATEMENTS : CLS
	'''

def p_STATEMENTS_IF(p):
	'''
	STATEMENTS : IF EL THEN X ELSE1 ENDIF
	'''
	p[0] = STATEMENTS_IF(p[2],p[4],p[5],"STATEMENTS_IF")

def p_STATEMENTS_WHILE(p):
	'''
	STATEMENTS : WHILE EL X WHEND
	'''
	p[0] = STATEMENTS_WHILE(p[2],p[3],"STATEMENTS_WHILE")

def p_STATEMENTS_DO(p):
	'''
	STATEMENTS : DO X LOOPUNTIL EL ENDO
	'''
	p[0] = STATEMENTS_DO(p[2],p[4],"STATEMENTS_DO")

def p_STATEMENTS_FOR(p):
	'''
	STATEMENTS : FOR O TO E X NEXT
	'''
	p[0] = STATEMENTS_FOR(p[2],p[4],p[5],"STATEMENTS_FOR")

def p_STATEMENTS_GOSUB(p):
	'''
	STATEMENTS : GOSUB ID
	'''

def p_O(p):
	'''
	O : E
	'''
	p[0] = O(p[1],"O")

def p_O1(p):
	'''
	O : E ASSIGN E
	'''
	p[0] = O1(p[1],p[3],"O1")

def p_U(p):
	'''
	U : ID
	'''
	pushOperandos(p[1])

def p_U1(p):
	'''
	U : ID DCLARRAY
	'''
	pushOperandos(p[1])
	p[0] = U1(p[2],"U1")

def p_U2(p):
	'''
	U : ID DCLMATRIX
	'''
	pushOperandos(p[1])
	p[0] = U2(p[2],"U2")

def p_U3(p):
	'''
	U : ID DCLCUBE
	'''
	pushOperandos(p[1])
	p[0] = U3(p[2],"U3")

def p_Q(p):
	'''
	Q : LPARENT U RPARENT
	'''
	p[0] = Q(p[2],"Q")

def p_Q1(p):
	'''
	Q : TEXT
	'''
	p[0] = Q1(p[1],"Q1")

def p_TEXT(p):
	'''
    TEXT : LPARENT STRING H RPARENT
    '''
	p[0] = TEXT(p[2],p[3],"TEXT")

def p_TEXT_EMPTY(p):
	'''
	TEXT :
	'''
def p_H(p):
	'''
	H : PLUS STRING H
	'''
	p[0] = H(p[2],p[3],"H")

def p_H1(p):
	'''
	H : PLUS U H
	'''
	p[0] = H1(p[2],p[3],"H1")

def p_H_EMPTY(p):
	'''
	H :
	'''

def p_ELSE1(p):
	'''
	ELSE1 : ELSE X
	'''
	p[0] = ELSE1(p[2],"ELSE1")

def p_ELSE1_EMPTY(p):
	'''
	ELSE1 :
	'''

def p_E(p):
	'''
	E : E PLUS T
	| E MINUS T
	'''
	genCuadruplo(p[2])
	p[0] = E(p[1],p[3],"E")

def p_E1(p):
	'''
	E : T
	'''
	p[0] = E1(p[1],"E1")

def p_T(p):
	'''
	T : T TIMES F
	| T DIVIDE F
	'''
	genCuadruplo(p[2])
	p[0] = T(p[1],p[3],"T")

def p_T1(p):
	'''
	T : F
	'''
	p[0] = T1(p[1],"T1")

def p_F(p):
	'''
	F : NUMBER
	'''
	pushOperandos(p[1])

def p_F1(p):
	'''
	F : U
	'''
	p[0] = F1(p[1],"F1")

def p_F2(p):
	'''
	F : LPARENT E RPARENT
	'''
	p[0] = F2(p[2],"F2")

def p_EL(p):
	'''
	EL : EL OR TL
	'''
	#genCuadruplo(p[2])
	p[0] = EL(p[1],p[3],"EL")

def p_EL1(p):
	'''
	EL : TL NOT
	| TL
	'''
	p[0] = EL1(p[1],"EL1")

def p_TL(p):
	'''
	TL : TL AND FL
	'''
	#genCuadruplo(p[2])
	p[0] = TL(p[1],p[3],"TL")

def p_TL1(p):
	'''
	TL : FL
	'''
	p[0] = TL1(p[1],"TL1")

def p_FL(p):
	'''
	FL : K OPREL K
	'''

	p[0] = FL(p[1],p[3],"FL")

def p_FL1(p):
	'''
	FL : LPARENT EL RPARENT
	'''
	p[0] = FL1(p[2],"FL1")

def p_OPREL(p):
	'''
	OPREL : LT
	| LTE
	| GT
	| GTE
	| NE
	| EQUAL
	'''
	#genCuadruplo(p[1])

def p_K(p):
	'''
	K : ID
	'''
	#pushOperandos(p[1])

def p_K1(p):
	'''
	K : NUMBER
	'''
	#pushOperandos(p[1])

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

#result.imprimir( )
#print (result.traducir())
#traducir(result)
imprimirSymbolTable()
imprimirCuadruplos()
print (result)