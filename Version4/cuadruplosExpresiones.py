global operador
global operando1
global operando2
global resultado
global operandos
global temporales
global listTemporales
global cont
global saltos
global ID
global Tf

Tf = 0
ID = 0
cont = 0
saltos = []
operandos = []
operador = []
operando1 = []
operando2 = []
resultado = []
temporales = []
listTemporales = [100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,
			  119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137]

def genCuadruplo(x):
	global operando1
	global operando2
	global operandos
	global operador
	global listTemporales
	global resultado
	global cont
	cont+=1
	operando2.append(operandos.pop())
	operando1.append(operandos.pop())
	operador.append(x)

	if x == "=":
		resultado.append(operando1[operando1.__len__() - 1])
	else:
		resultado.append(listTemporales.pop(0))

	if operando1[operando1.__len__() - 1] > 99:
		listTemporales.append(operando1[operando1.__len__() - 1])

	if operando2[operando2.__len__() - 1] > 99:
		listTemporales.append(operando2[operando2.__len__() - 1])

	operandos.append(resultado[resultado.__len__() - 1])

def pushOperandos(x):
	global operandos
	operandos.append(x)

def gotofalso():
	global saltos
	global cont
	global operando1
	global operando2
	global operador
	global resultado
	cont+=1
	operador.append("gotofalso")
	operando1.append(operandos.pop())
	operando2.append("--")
	resultado.append("--")
	saltos.append(cont-1)

def goto():
	global cont
	global saltos
	global operando1
	global operando2
	global operador
	global resultado
	cont+=1
	operador.append("goto")
	operando1.append("--")
	operando2.append("--")
	resultado.append("--")
	operando2[saltos.pop()] = cont
	saltos.append(cont-1)

def finIF():
	global operando2
	global saltos
	operando2[saltos.pop()] = cont

def genCuadruploCLS():
	global cont
	global operando1
	global operando2
	global operador
	global resultado
	cont+=1
	operador.append("CLS")
	operando1.append("--")
	operando2.append("--")
	resultado.append("--")

def origen():
	global cont
	saltos.append(cont)

def finWhile():
	global cont
	global saltos
	global operando1
	global operando2
	global operador
	global resultado
	cont+=1
	operando2[saltos.pop()] = cont
	operador.append("goto")
	operando1.append("--")
	operando2.append(saltos.pop())
	resultado.append("--")

def finDoWhile():
	global saltos
	global cont
	global operando1
	global operando2
	global operador
	global resultado
	cont+=1
	operador.append("gotofalso")
	operando1.append(operandos.pop())
	operando2.append(saltos.pop())
	resultado.append("--")

def genCuadruploFor(x):
	global operando1
	global operando2
	global operandos
	global operador
	global listTemporales
	global resultado
	global cont
	global ID
	cont+=1
	operando2.append(operandos.pop())
	ID = operandos.pop()
	operando1.append(ID)
	operador.append(x)
	resultado.append(operando1[operando1.__len__() - 1])
	operandos.append(operando1[operando1.__len__() - 1])

	if operando1[operando1.__len__() - 1] > 99:
		listTemporales.append(operando1[operando1.__len__() - 1])

	if operando2[operando2.__len__() - 1] > 99:
		listTemporales.append(operando2[operando2.__len__() - 1])

	operandos.append(resultado[resultado.__len__() - 1])

def forAction3():
	global operandos
	global operador
	global operando1
	global operando2
	global resultado
	global listTemporales
	global cont
	global ID
	global Tf
	cont+=1
	operador.append("=")
	operando1.append(listTemporales.pop(0))#liberar
	operando2.append(operandos.pop())
	resultado.append(operando1[operando1.__len__() - 1])
	operandos.append(resultado[resultado.__len__() - 1])
	cont+=1
	Tf = operandos.pop()
	operador.append("<=")
	operando1.append(ID)
	operando2.append(Tf)
	resultado.append(listTemporales.pop(0))
	operandos.append(resultado[resultado.__len__() - 1])
	cont+=1
	operador.append("gotofalso")
	operando1.append(operandos.pop())
	operando2.append("--")
	resultado.append("--")
	listTemporales.append(operando1[operando1.__len__() - 1])
	saltos.append(cont-2)

def finFor():
	global operandos
	global operador
	global operando1
	global operando2
	global resultado
	global listTemporales
	global cont
	global ID
	global tf
	cont+=1
	ID = operandos.pop()
	operador.append("+")
	operando1.append(ID)
	operando2.append(-1)
	resultado.append(listTemporales.pop(0))
	operandos.append(resultado[resultado.__len__() - 1])
	cont+=1
	operador.append("=")
	operando1.append(ID)
	operando2.append(operandos.pop())
	resultado.append(ID)
	operandos.append(resultado[resultado.__len__() - 1])
	listTemporales.append(operando2[operando2.__len__() - 1])
	cont+=1
	retorno = saltos.pop()
	operador.append("goto")
	operando1.append("--")
	operando2.append(retorno)
	resultado.append("--")
	operando2[retorno+1] = cont
	listTemporales.append(Tf)


def imprimirCuadruplos():
	cuadruplos = "\n".join("{4} {0:10} {4} {1:3} {4} {2:3} {4} {3:3} {4}".format
		(x, y, z, w,'|') for x, y, z, w in zip(operador,operando1,operando2,resultado))
	print ("\nCuadruplos generados:\n\n"+cuadruplos+"\n")
	print ("\nLista de operandos:\n")
	print (operandos)
	print ("\n")
	print ("\nLista de listTemporales disponibles:\n")
	print (listTemporales)
	print ("\n")