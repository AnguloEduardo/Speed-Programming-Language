global operador
global operando1
global operando2
global resultado
global operandos
global temporales
global listTemporales

operandos = []
operador = []
operando1 = []
operando2 = []
resultado = []
temporales = ["T1","T2","T3","T4","T5","T6","T7","T8","T9","T10","T11","T12","T13",
			  "T14","T15","T16","T17","T18","T19","T20","T21","T22","T23","T24"]
listTemporales = ["T1","T2","T3","T4","T5","T6","T7","T8","T9","T10","T11","T12","T13",
			  	  "T14","T15","T16","T17","T18","T19","T20","T21","T22","T23","T24"]

def genCuadruplo(x):
	global operando1
	global operando2
	global operandos
	global operador
	global temporales
	global resultado
	global listTemporales
	operando2.append(operandos.pop())
	operando1.append(operandos.pop())
	operador.append(x)
	if x == "=":
		resultado.append(operando1[operando1.__len__() - 1])
	else:
		resultado.append(temporales.pop(0))
	operandos.append(resultado[resultado.__len__() - 1])
	if operando1[operando1.__len__() - 1] in listTemporales:
		temporales.append(operando1[operando1.__len__() - 1])

	if operando2[operando2.__len__() - 1] in listTemporales:
		temporales.append(operando2[operando2.__len__() - 1])

def pushOperandos(x):
	global operandos
	operandos.append(x)

def imprimirCuadruplos():
	cuadruplos ="\n".join("{4} {0:2s} {4} {1:3s} {4} {2:3s} {4} {3:3s} {4}".format(
				x, y, z, w,'|') for x, y, z, w in zip(operador,operando1,operando2,resultado))
	print ("\nCuadruplos generados:\n\n"+cuadruplos+"\n")
	print ("\nLista de operandos:\n")
	print (operandos)
	print ("\n")
	print ("\nLista de Temporales disponibles:\n")
	print (temporales)
	print ("\n")