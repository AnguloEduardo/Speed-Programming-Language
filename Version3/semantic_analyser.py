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

class V(Nodo):
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

class TIPO(Nodo):
	def __init__(self,son1,son2,son3,son4,son5,son6,name):
		self.name = name
		self.name = son1
		self.name = son2
		self.name = son3
		self.name = son4
		self.name = son5
		self.name = son6

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		self.son3.imprimir(" "+ident)
		self.son4.imprimir(" "+ident)
		self.son5.imprimir(" "+ident)
		self.son6.imprimir(" "+ident)

		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()
		son4 = self.son4.traducir()
		son5 = self.son5.traducir()
		son6 = self.son6.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		txt += id + "->"+son3+"\n\t"
		txt += id + "->"+son4+"\n\t"
		txt += id + "->"+son5+"\n\t"
		txt += id + "->"+son6+"\n\t"
		return id

class SP(Nodo):
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

class S(Nodo):
	def __init__(self,son1,son2,son3,son4,son5,son6,son7,
				 son8,son9,son10,son11,son12,son13,son14,
				 son15,name):
		self.name = name
		self.name = son1
		self.name = son2
		self.name = son3
		self.name = son4
		self.name = son5
		self.name = son6
		self.name = son7
		self.name = son8
		self.name = son9
		self.name = son10
		self.name = son11
		self.name = son12
		self.name = son13
		self.name = son14
		self.name = son15

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		self.son3.imprimir(" "+ident)
		self.son4.imprimir(" "+ident)
		self.son5.imprimir(" "+ident)
		self.son6.imprimir(" "+ident)
		self.son7.imprimir(" "+ident)
		self.son8.imprimir(" "+ident)
		self.son9.imprimir(" "+ident)
		self.son10.imprimir(" "+ident)
		self.son11.imprimir(" "+ident)
		self.son12.imprimir(" "+ident)
		self.son13.imprimir(" "+ident)
		self.son143imprimir(" "+ident)
		self.son15.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()
		son4 = self.son4.traducir()
		son5 = self.son5.traducir()
		son6 = self.son6.traducir()
		son7 = self.son7.traducir()
		son8 = self.son8.traducir()
		son9 = self.son9.traducir()
		son10 = self.son10.traducir()
		son11 = self.son11.traducir()
		son12 = self.son12.traducir()
		son13 = self.son13.traducir()
		son14 = self.son14.traducir()
		son15 = self.son15.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		txt += id + "->"+son3+"\n\t"
		txt += id + "->"+son4+"\n\t"
		txt += id + "->"+son5+"\n\t"
		txt += id + "->"+son6+"\n\t"
		txt += id + "->"+son7+"\n\t"
		txt += id + "->"+son8+"\n\t"
		txt += id + "->"+son9+"\n\t"
		txt += id + "->"+son10+"\n\t"
		txt += id + "->"+son11+"\n\t"
		txt += id + "->"+son12+"\n\t"
		txt += id + "->"+son13+"\n\t"
		txt += id + "->"+son14+"\n\t"
		txt += id + "->"+son15+"\n\t"
		return id

class O(Nodo):
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
		return id

class U(Nodo):
	def __init__(self,son1,son2,son3,son4,son5,son6name):
		self.name = name
		self.name = name
		self.name = son1
		self.name = son2
		self.name = son3
		self.name = son4
		self.name = son5
		self.name = son6

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		self.son3.imprimir(" "+ident)
		self.son4.imprimir(" "+ident)
		self.son5.imprimir(" "+ident)
		self.son6.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()
		son4 = self.son4.traducir()
		son5 = self.son5.traducir()
		son6 = self.son6.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		txt += id + "->"+son3+"\n\t"
		txt += id + "->"+son4+"\n\t"
		txt += id + "->"+son5+"\n\t"
		txt += id + "->"+son6+"\n\t"
		return id

class Q(Nodo):
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
	def __init__(self,son1,son2,son3,son4,name):
		self.name = name
		self.name = son1
		self.name = son2
		self.name = son3
		self.name = son4

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		self.son3.imprimir(" "+ident)
		self.son4.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()
		son4 = self.son4.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		txt += id + "->"+son3+"\n\t"
		txt += id + "->"+son4+"\n\t"
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
	def __init__(self,son1,son2,son3,son4,son5,name):
		self.name = name
		self.name = son1
		self.name = son2
		self.name = son3
		self.name = son4
		self.name = son5

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		self.son3.imprimir(" "+ident)
		self.son4.imprimir(" "+ident)
		self.son5.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()
		son4 = self.son4.traducir()
		son5 = self.son5.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		txt += id + "->"+son3+"\n\t"
		txt += id + "->"+son4+"\n\t"
		txt += id + "->"+son5+"\n\t"
		return id

class T(Nodo):
	def __init__(self,son1,son2,son3,son4,son5,name):
		self.name = name
		self.name = son1
		self.name = son2
		self.name = son3
		self.name = son4
		self.name = son5

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		self.son3.imprimir(" "+ident)
		self.son4.imprimir(" "+ident)
		self.son5.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()
		son4 = self.son4.traducir()
		son5 = self.son5.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		txt += id + "->"+son3+"\n\t"
		txt += id + "->"+son4+"\n\t"
		txt += id + "->"+son5+"\n\t"
		return id

class F(Nodo):
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

class EL(Nodo):
	def __init__(self,son1,son2,son3,son4,name):
		self.name = name
		self.name = son1
		self.name = son2
		self.name = son3
		self.name = son4

	def imprimir(indent):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		self.son3.imprimir(" "+ident)
		self.son4.imprimir(" "+ident)
		print (ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()
		son4 = self.son4.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"
		txt += id + "->"+son2+"\n\t"
		txt += id + "->"+son3+"\n\t"
		txt += id + "->"+son4+"\n\t"
		return id

class TL(Nodo):
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
		return id

class FL(Nodo):
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