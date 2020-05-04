global operador
global operando1
global operando2
global resultado
global operandos
global temporales
global listTemporales
global cont
global saltos

cont = 0
saltos = []
operandos = []
operador = []
operando1 = []
operando2 = []
resultado = []
temporales = [100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,
			  119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137]

def genCuadruplo(x):
	global operando1
	global operando2
	global operandos
	global operador
	global temporales
	global resultado
	global cont

	cont+=1
	operando2.append(operandos.pop())
	operando1.append(operandos.pop())
	operador.append(x)

	if x == "=":
		resultado.append(operando1[operando1.__len__() - 1])
	else:
		resultado.append(temporales.pop(0))

	if operando1[operando1.__len__() - 1] > 99:
		temporales.append(operando1[operando1.__len__() - 1])

	if operando2[operando2.__len__() - 1] > 99:
		temporales.append(operando2[operando2.__len__() - 1])

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
	operando1.append(operandos.pop())
	operando2.append("--")
	operador.append("gotofalso")
	resultado.append("--")
	saltos.append(cont - 1)

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
	saltos.append(cont - 1)

def fin():
	global operando2
	global saltos
	operando2[saltos.pop()] = cont

def imprimirCuadruplos():
	cuadruplos = "\n".join("{4} {0:10} {4} {1:3} {4} {2:3} {4} {3:3} {4}".format
		(x, y, z, w,'|') for x, y, z, w in zip(operador,operando1,operando2,resultado))
	cuadruplosif = "\n".join("{3} {0:10} {3} {1:3} {3} {2:3} {3}".format
		(x, y, z,'|') for x, y, z in zip(operador,operando1,operando2))
	print ("\nCuadruplos generados:\n\n"+cuadruplos+"\n")
	#print ("\nCuadruplos if:\n\n"+cuadruplosif+"\n")
	print ("\nLista de operandos:\n")
	print (operandos)
	print ("\n")
	print ("\nLista de Temporales disponibles:\n")
	print (temporales)
	print ("\n")