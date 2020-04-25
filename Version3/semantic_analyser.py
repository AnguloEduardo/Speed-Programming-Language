txt = " "
cont = 0
def incrementarContador():
	global cont
	cont += 1
	return "%d" %cont

class Nodo():
	pass

class PROGRAM(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.name = son1
		self.name = son2
		self.name = son3

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		self.son3.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		txt += id + "->"+son3+"\n\t"
		return "digraph G {\n\t"+txt+"}"

class VARIABLE(Nodo):
	def __init__(self,son1, son2, son3,name):
		self.name = name
		self.name = son1
		self.name = son2
		self.name = son3


	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		self.son3.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		txt += id + "->"+son3+"\n\t"
		return id

class IDLIST(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.name = son1

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		return id

class IDLIST2(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.name = son1

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		return id

class TIPO_ARRAY(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.name = son1

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		return id

class TIPO_MATRIX(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.name = son1

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		return id

class TIPO_CUBE(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.name = son1

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		return id

class DCLARRAY(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.name = son1

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		return id

class DCLMATRIX(Nodo):
	def __init__(self,son1, son2,name):
		self.name = name
		self.name = son1
		self.name = son2


	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		return id

class DCLCUBE(Nodo):
	def __init__(self,son1, son2, son3,name):
		self.name = name
		self.name = son1
		self.name = son2
		self.name = son3


	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		self.son3.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		txt += id + "->"+son3+"\n\t"
		return id

class SP(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.name = son1
		self.name = son2

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		return id

class X(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.name = son1
		self.name = son2

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		return id

class STATEMENTS_LET(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.name = son1
		self.name = son2

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		return id

class STATEMENTS_PRINT(Nodo):
	def __init__(self,son1,name):
		self.name = name

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		return id

class STATEMENTS_INPUT(Nodo):
	def __init__(self,son1, son2, son3,name):
		self.name = name
		self.name = son1
		self.name = son2
		self.name = son3


	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		self.son3.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		txt += id + "->"+son3+"\n\t"
		return id

class STATEMENTS_IF(Nodo):
	def __init__(self,son1, son2, son3,name):
		self.name = name
		self.name = son1
		self.name = son2
		self.name = son3


	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		self.son3.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		txt += id + "->"+son3+"\n\t"
		return id

class STATEMENTS_WHILE(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.name = son1
		self.name = son2

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		return id

class STATEMENTS_DO(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.name = son1
		self.name = son2

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		return id

class STATEMENTS_FOR(Nodo):
	def __init__(self,son1, son2, son3,name):
		self.name = name
		self.name = son1
		self.name = son2
		self.name = son3


	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		self.son3.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		txt += id + "->"+son3+"\n\t"
		return id

class O(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.name = son1

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		return id

class O1(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.name = son1
		self.name = son2

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		return id



class U1(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.name = son1

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		return id

class U2(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.name = son1

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		return id

class U3(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.name = son1

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		return id

class Q(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.name = son1

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		return id

class Q1(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.name = son1

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		return id

class TEXT(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.name = son1
		self.name = son2

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		return id

class H(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.name = son1
		self.name = son2

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		return id

class H1(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.name = son1
		self.name = son2

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		return id

class ELSE1(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.name = son1

	def imprimir(indent):
		self.son1.imprimir(" "+indent)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		return id

class E(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.name = son1
		self.name = son2

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		return id

class E1(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.name = son1

	def imprimir(indent):
		self.son1.imprimir(" "+indent)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		return id

class T(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.name = son1
		self.name = son2

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		return id

class T1(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.name = son1

	def imprimir(indent):
		self.son1.imprimir(" "+indent)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		return id

class F1(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.name = son1

	def imprimir(indent):
		self.son1.imprimir(" "+indent)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		return id

class F2(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.name = son1

	def imprimir(indent):
		self.son1.imprimir(" "+indent)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		return id

class EL(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.name = son1
		self.name = son2

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		return id

class EL1(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.name = son1

	def imprimir(indent):
		self.son1.imprimir(" "+indent)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		return id

class TL(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.name = son1
		self.name = son2

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		return id

class TL1(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.name = son1

	def imprimir(indent):
		self.son1.imprimir(" "+indent)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		return id

class FL(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.name = son1
		self.name = son2

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		return id

class FL1(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.name = son1

	def imprimir(indent):
		self.son1.imprimir(" "+indent)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		return id
'''
class OPREL(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(indent):


	def traducir(self):
		global txt
		id = incrementarContador()

		return id

class K(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(indent):


	def traducir(self):
		global txt
		id = incrementarContador()

		return id
'''