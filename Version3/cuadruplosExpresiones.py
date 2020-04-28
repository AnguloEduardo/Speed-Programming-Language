global operador
global operando1
global operando2
global operando1ID
global operando2ID
global operandosID
global resultado
global operandos
global temporales
global listTemporales

operandos = []
operador = []
operando1 = []
operando1ID = []
operando2 = []
operando2ID = []
operandosID = []
resultado = []
temporales = [100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,
			  119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137]

def genCuadruplo(x):
	global operando1
	global operando2
	global operando1ID
	global operando2ID
	global operandos
	global operador
	global temporales
	global resultado
	global listTemporales
	operando2.append(operandos.pop())
	operando2ID.append(operandosID.pop())
	operando1.append(operandos.pop())
	operando1ID.append(operandosID.pop())
	operador.append(x)
	if x == "=":
		resultado.append(operando1[operando1.__len__() - 1])
		operandosID.append(1)
	else:
		resultado.append(temporales.pop(0))
		operandosID.append(1)
	operandos.append(resultado[resultado.__len__() - 1])
	if operando1[operando1.__len__() - 1] > 99:
		temporales.append(operando1[operando1.__len__() - 1])

	if operando2[operando2.__len__() - 1] > 99:
		temporales.append(operando2[operando2.__len__() - 1])

def pushOperandos(x,y):
	global operandos
	operandos.append(x)
	operandosID.append(y)

def imprimirCuadruplos():
	cuadruplos ="\n".join("{6} {0:2} {6} {1:3} {6} {2:3} {6} {3:3} {6} {4:3} {6} {5:3} {6} ".format
		(x, y, a, z, b, w,'|') for x, y, a, z, b, w in zip(operador,operando1,operando1ID,
		operando2,operando2ID,resultado))
	print ("\nCuadruplos generados:\n\n"+cuadruplos+"\n")
	print ("\nLista de operandos:\n")
	print (operandos)
	print ("\n")
	print ("\nLista de Temporales disponibles:\n")
	print (temporales)
	print ("\n")