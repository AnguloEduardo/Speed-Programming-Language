global tableID
global tableType
global repetido

tableID = []
tableType = []
repetido = False

def insertType(p):
	global tableID
	global tableType
	global repetido
	if not repetido:
		while len(tableID) > len(tableType):
			tableType.append(p)

def insertID(p):
	global repetido
	global tableID
	for x in tableID:
		if x == p:
			repetido = True
			print ("\nError, variable --"+str(p)+"-- is already declared")
			break
	if not repetido:
		tableID.append(p)

def imprimirSymbolTable():
	global repetido
	global tableType
	global tableID
	if not repetido:
		symboltable ="\n".join("{2} {0:4s} {2} {1:6s} {2}".format(x, y, '|') for x, y in zip(tableID, tableType))
		print ("\nTabla de simbolos:\n\n" + symboltable)
	else:
		tableID = []
		tableType = []
		print ("\nError in the symbol table")

def buscar(id):
	return (tableID.index(id)+1)