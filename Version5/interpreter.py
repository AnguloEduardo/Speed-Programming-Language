from traduction import *
import os

global PC
global saltosPC
global finprograma
global operando1value
global operando2value
finprograma = True
saltosPC = []
operando1value = []
operando2value = []
PC = 0

def ejecution():
	global PC
	global saltosPC
	global finprograma
	global operando1value
	global operando2value
	global operando1
	global operando2
	global resultado
	global temporales
	#----------Ejecutando todos los cuadruplos----------#
	while finprograma:
		#----------Ejecuntando el input----------#
		if operador[PC] == "INPUT":
			print(texto[operando1[PC]])
			tableValue[operando2[PC]-1] = int(input())
			PC+=1
		#----------Ejecuntando el print----------#
		elif operador[PC] == "PRINT":
			if operando1[PC] == "--":
				print(tableValue[operando2[PC]-1])
			elif operando2[PC] == "--":
				print(texto[operando1[PC]])
			else:
				print(texto[operando1[PC]],tableValue[operando2[PC]-1])
			PC+=1
		#----------Ejecuntando las operaciones aritmeticas y logicas----------#
		elif ((operador[PC] == "+") or (operador[PC] == "-") or (operador[PC] == "*")
			or (operador[PC] == "/") or (operador[PC] == "&&") or (operador[PC] == "||")
			or (operador[PC] == "<") or (operador[PC] == ">") or (operador[PC] == "<=")
			or (operador[PC] == ">=") or (operador[PC] == "==") or (operador[PC] == "<>")):

			if operando1[PC] > 99: #Revisando si es un temporal
				operando1value = temporales[operando1[PC]-100]
			elif operando1[PC] <= 0: #Revisando si es una constante
				operando1value = operando1[PC]*(-1)
			else: #Reemplazando el valor de la tabla de simbolos
				operando1value = tableValue[operando1[PC]-1]

			if operando2[PC] > 99: #Revisando si es un temporal
				operando2value = temporales[operando2[PC]-100]
			elif operando2[PC] <= 0: #Revisando si es una constante
				operando2value = operando2[PC]*(-1)
			else: #Reemplazando el valor de la tabla de simbolos
				operando2value = tableValue[operando2[PC]-1]

			if operador[PC] == "+":
				if resultado[PC] > 99:
					temporales[resultado[PC]-100] = operando1value + operando2value
				else:
					tableValue[resultado[PC]-1] = operando1value + operando2value
				PC+=1
			elif operador[PC] == "-":
				if resultado[PC] > 99:
					temporales[resultado[PC]-100] = operando1value - operando2value
				else:
					tableValue[resultado[PC]-1] = operando1value - operando2value
				PC+=1
			elif operador[PC] == "*":
				if resultado[PC] > 99:
					temporales[resultado[PC]-100] = operando1value * operando2value
				else:
					tableValue[resultado[PC]-1] = operando1value * operando2value
				PC+=1
			elif operador[PC] == "/":
				if resultado[PC] > 99:
					temporales[resultado[PC]-100] = operando1value / operando2value
				else:
					tableValue[resultado[PC]-1] = operando1value / operando2value
				PC+=1
			elif operador[PC] == "&&":
				if resultado[PC] > 99:
					if operando1value and operando2value:
						temporales[resultado[PC]-100] = 1
					else:
						temporales[resultado[PC]-100] = 0
				else:
					if operando1value and operando2value:
						tableValue[resultado[PC]-1] = 1
					else:
						tableValue[resultado[PC]-1] = 0
				PC+=1
			elif operador[PC] == "||":
				if resultado[PC] > 99:
					if operando1value or operando2value:
						temporales[resultado[PC]-100] = 1
					else:
						temporales[resultado[PC]-100] = 0
				else:
					if operando1value or operando2value:
						tableValue[resultado[PC]-1] = 1
					else:
						tableValue[resultado[PC]-1] = 0
				PC+=1
			elif operador[PC] == "<":
				if resultado[PC] > 99:
					if operando1value < operando2value:
						temporales[resultado[PC]-100] = 1
					else:
						temporales[resultado[PC]-100] = 0
				else:
					if operando1value < operando2value:
						tableValue[resultado[PC]-1] = 1
					else:
						tableValue[resultado[PC]-1] = 0
				PC+=1
			elif operador[PC] == ">":
				if resultado[PC] > 99:
					if operando1value > operando2value:
						temporales[resultado[PC]-100] = 1
					else:
						temporales[resultado[PC]-100] = 0
				else:
					if operando1value > operando2value:
						tableValue[resultado[PC]-1] = 1
					else:
						tableValue[resultado[PC]-1] = 0
				PC+=1
			elif operador[PC] == "<=":
				if resultado[PC] > 99:
					if operando1value <= operando2value:
						temporales[resultado[PC]-100] = 1
					else:
						temporales[resultado[PC]-100] = 0
				else:
					if operando1value <= operando2value:
						tableValue[resultado[PC]-1] = 1
					else:
						tableValue[resultado[PC]-1] = 0
				PC+=1
			elif operador[PC] == ">=":
				if resultado[PC] > 99:
					if operando1value >= operando2value:
						temporales[resultado[PC]-100] = 1
					else:
						temporales[resultado[PC]-100] = 0
				else:
					if operando1value >= operando2value:
						tableValue[resultado[PC]-1] = 1
					else:
						tableValue[resultado[PC]-1] = 0
				PC+=1
			elif operador[PC] == "==":
				if resultado[PC] > 99:
					if operando1value == operando2value:
						temporales[resultado[PC]-100] = 1
					else:
						temporales[resultado[PC]-100] = 0
				else:
					if operando1value == operando2value:
						tableValue[resultado[PC]-1] = 1
					else:
						tableValue[resultado[PC]-1] = 0
				PC+=1
			elif operador[PC] == "<>":
				if resultado[PC] > 99:
					if operando1value != operando2value:
						temporales[resultado[PC]-100] = 1
					else:
						temporales[resultado[PC]-100] = 0
				else:
					if operando1value != operando2value:
						tableValue[resultado[PC]-1] = 1
					else:
						tableValue[resultado[PC]-1] = 0
				PC+=1
		elif operador[PC] == "=":
			if operando2[PC] > 99: #Revisando si es un temporal
				operando2value = temporales[operando2[PC]-100]
			elif operando2[PC] <= 0: #Revisando si es una constante
				operando2value = operando2[PC]*(-1)
			else: #Reemplazando el valor de la tabla de simbolos
				operando2value = tableValue[operando2[PC]-1]

			if operando1[PC] > 99: #Revisando si es un temporal
				temporales[operando1[PC]-100] = operando2value
			else: #Reemplazando el valor de la tabla de simbolos
				if tableType[operando1[PC]-1] == "word":
					tableValue[operando1[PC]-1] = int(operando2value)
				else:
					tableValue[operando1[PC]-1] = float(operando2value)
			PC+=1
		elif operador[PC] == "goto":
			PC = operando2[PC]
		elif operador[PC] == "gotofalso":
			if temporales[operando1[PC]-100]:
				PC+=1
			else:
				PC = operando2[PC]
		elif operador[PC] == "gotosub":
			saltosPC.append(PC+1)
			PC = operando2[PC]
		elif operador[PC] == "return":
			PC = saltosPC.pop()
		elif operador[PC] == "CLS":
			os.system("cls")
			PC+=1
		elif operador[PC] == "finprograma":
			finprograma = False
		else:
			PC+=1