global tableID
global tableType
global tableValue
global repetido
global indice
global contador

tableID = []
tableType = []
tableValue = []
indice = []
contador = 0
repetido = False

def insertType(p):
	global tableID
	global tableType
	global repetido
	if not repetido:
		while len(tableID) > len(tableType):
			tableType.append(p)
			tableValue.append("---")

def insertID(p):
	global contador
	global repetido
	global tableID
	contador+=1
	for x in tableID:
		if x == p:
			repetido = True
			print ("\nError, variable --"+str(p)+"-- is already declared")
			break
	if not repetido:
		tableID.append(p)
		indice.append(contador)

def SP_insertID(p, cont):
	global contador
	global repetido
	global tableID
	contador+=1
	for x in tableID:
		if x == p:
			repetido = True
			print ("\nError, variable --"+str(p)+"-- is already declared")
			break
	if not repetido:
		tableID.append(p)
		tableType.append("SP")
		tableValue.append(cont)
		indice.append(contador)

def imprimirSymbolTable():
	global repetido
	global tableType
	global tableID
	if not repetido:
		symboltable ="\n".join("{4} {0:3} {4} {1:8s} {4} {2:6s} {4} {3:6} {4}".format(w, x, y, z, '|')
			for w, x, y, z in zip(indice, tableID, tableType, tableValue))
		print ("\nTabla de simbolos:\n\n" + symboltable)
	else:
		tableID = []
		tableType = []
		print ("\nError in the symbol table")

def buscar(id):
	return int(tableID.index(id)+1)