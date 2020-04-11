import ply.lex as lex
import ply.yacc as yacc
import re
import codecs
import os
import sys


tokens = [ 'ID', 'NUMBER', 'COMMA', 'SEMMICOLON', 'LPARENT', 
		   'RPARENT', 'ASSIGN', 'PLUS', 'MINUS', 'TIMES', 
		   'DIVIDE', 'NE', 'LT', 'LTE', 'GT', 'GTE']

reserved = {
		'program':'PROGRAM', 
		'dim':'DIM', 
		'as':'AS', 
		'end':'END',
		'subprocedure':'SUBPROCEDURE', 
		'endsub':'ENDSUB', 
		'let':'LET',
		'print':'PRINT', 
		'cls':'CLS', 
		'if':'IF', 
		'then':'THEN', 
		'else':'ELSE', 
		'endif':'ENDIF', 
		'while':'WHILE', 
		'whend':'WHEND',
		'do':'DO', 
		'loopunitl':'LOOPUNTIL', 
		'endo':'ENDO', 
		'for':'FOR', 
		'to':'TO', 
		'next':'NEXT', 
		'gosub':'GOSUB',
		'word':'WORD', 
		'float':'FLOAT', 
		'array':'ARRAY', 
		'matrix':'MATRIX', 
		'cube':'CUBE'
}

tokens = tokens+list(reserved.values())

t_ignore = '\t\r '
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_NE = '<>'
t_LT = '<'
t_LTE = '<='
t_GT = '>'
t_GTE = '>='
t_LPARENT = '\('
t_RPARENT = '\)'
t_COMMA = ','
t_SEMMICOLON = ';'

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	t.type = reserved.get(t.value,'ID')
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_COMMENT(t):
	r'\#.*'
	pass

def t_NUMBER(t):
	r'\d+'
	return t

def t_error(t):
	print ("Illegal character ", t.value[0])
	t.lexer.skip(1)

test = os.getcwd()+"\\test\\"+"prueba1.py"
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

lexer = lex.lex()

lexer.input(cadena)

while True:
	tok = lexer.token()
	if not tok : break
	print (tok)