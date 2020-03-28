import ply.lex as lex
import ply.yacc as yacc


tokens = ('program', 'dim', 'as', 'coma', 'semicolon', 'end',
	'sub procedure', 'endsub', 'let', 'equal', 'print', 
	'cls', 'if', 'then', 'else', 'endif', 'while', 'whend',
	'do', 'loop until', 'endo', 'for', 'to', 'next', 'gosub',
	'word', 'float', 'array', 'matrix', 'cube', 'lparent',
	'rparent', 'sum', 'rest', 'multi', 'div', 'greater than', 
	'lesser than', 'greater equal', 'lesser equal', 'nonequal')

t_ignore = r' '

def t_program(t):
	r'program'
	t.type = 'program'
	return t

def t_que(t):
	r'que'
	t.type = 'que'
	return t

def t_tal(t):
	r'tal'
	t.type = 'tal'
	return t

def t_coma(t):
	r'\,'
	t.type = 'coma'
	return t

def t_error(t):
	print("Invalid syntax")
	t.lexer.skip(1)

lex = lex.lex()

def p_S(p):
	'S : X que tal'
	print("Correct syntax\n")

def p_X(p):
	'X : X coma hola'

def p_Y(p):
	'X : hola'

def p_error(p):
	print("Incorrect syntax\n")

parser = yacc.yacc()

while True:
    try:
        s = input('')
    except EOFError:
        break
    parser.parse(s)