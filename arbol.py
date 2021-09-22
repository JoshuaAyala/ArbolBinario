#!/usr/bin/python
#coding: utf-8

# Filename  : arbol.py
# Autor     : Joshua Ayala
# Website   : https://github.com/JoshuaAyala/04IDMA/arbol.py
# pep8: 100%

import os, time

class Arbol(object):						# Creamos la clase Arbol que contiene atributos como el nodo raiz, nodo izquierdo y nodo derecho
	def __init__(self, r, iz, de):
		self.raiz = r
		self.izquierda = iz
		self.derecha = de

	def getRaiz(self):						# Función para obtener la raíz y hacer comprobación de contenido
		return self.raiz

	def getPreOrden(self):					# Imprime los datos en Pre Orden
		return self.raiz + self.izquierda + self.derecha

	def getInOrden(self):					# Imprime los datos en In Orden
		return self.izquierda + self.raiz + self.derecha

	def getPostOrden(self):					# Imprime los datos en Post Orden
		return self.izquierda + self.derecha + self.raiz

def goBack(arbolExiste, arbol):					# Pregunta si quieres volver a la función menú pasando parametro de existencia de árbol y datos del árbol
	op = input("¿Desea volver al menú? (S/n)\n  >: ").upper()
	if(op == "S"):
		menu(arbolExiste, arbol)
	else:
		os.system('cls')
		print("\n\n\n		Hasta luego. ")
		time.sleep(2)
		exit()

def menu(arbolExiste, arbol):
	op = int(input("\n¿Qué desea hacer?\n\n  [1] Crear árbol.\n  [2] Agregar elemento a mi árbol.\n  [3] Ver y reccorrer mi árbol.\n  [4] Buscar un elemento de mi árbol.\n\n  [0] Salir.\n\n>: "))
	if(op == 1):
		arbol = Arbol(None, None, None); 					# Se crea el árbol sin valores
		arbolExiste = True									# Variable booleana para comprobación de existencia de árbol
		print("	+- Árbol creado exitosamente.")	
		time.sleep(2)
		menu(arbolExiste, arbol)
	elif(op == 2):
		if(arbolExiste == True):
			r = input("Introduce nodo Raíz:\n  >: ")					# Aquí insertamos el valor del nodo Raíz
			iz = input("Introduce nodo Hijo Izquierdo:\n  >: ")			# Aquí insertamos el valor del nodo Izquierdo
			de = input("Introduce nodo Hijo Derecho:\n  >: ")			# Aquí insertamos el valor del nodo Derecho
			arbol = Arbol(r, iz, de)
			print("+- Datos agregados exitosamente.")
		else:
			print("\n[!] No se ha creado ningún árbol o no tiene elementos.\n")
			goBack(arbolExiste, arbol)
		time.sleep(2)
		menu(arbolExiste, arbol)
	elif(op == 3):
		if(arbolExiste == True):
			if(arbol.raiz == None):
				print("\n[!] El árbol no tiene elementos que mostrar.\n")
				goBack(arbolExiste, arbol)
			else:
				print("	[ Árbol Visual ]\n\n		"+arbol.raiz) 		# Aquí se imprime visualmente el árbol binario
				print("\n	"+arbol.izquierda+"		"+arbol.derecha)
				print("\n	+- PreOrden: ", arbol.getPreOrden())		# Imprime los datos en Pre Orden
				print("	+- InOrden: ", arbol.getInOrden())				# Imprime los datos en In Orden
				print("	+- PostOrden: ", arbol.getPostOrden(), "\n") 	# Imprime los datos en Post Orden
				goBack(arbolExiste, arbol)
		else:
			print("\n[!] No se ha creado ningún árbol o no tiene elementos.\n")
			goBack(arbolExiste, arbol)
	elif(op == 4):
		if(arbolExiste):
			if(arbol.raiz == None):
				print("\n[!] El árbol no tiene elementos que mostrar.\n")
				goBack(arbolExiste, arbol)
			else:
				datoabuscar = input("¿Qué dato deseas buscar?\n>: ")
				if(datoabuscar == arbol.raiz):
					print("	+- El elemento existe en el nodo Raíz.\n")
				elif(datoabuscar == arbol.izquierda):
					print("	+- El elemento existe en el nodo Izquierdo.\n")
				elif(datoabuscar == arbol.derecha):
					print("	+- El elemento existe en el nodo Derecho.\n")
				else:
					print("\n[!] El dato no se encuentra o no existe.\n")
				goBack(arbolExiste, arbol)
		else:
			print("\n[!] No se ha creado ningún árbol o no tiene elementos.\n")
			goBack(arbolExiste, arbol)
	elif(op == 0):
		os.system('cls')
		print("\n\n\n		Hasta luego. ")
		time.sleep(2)
		exit()

def main():
	os.system('cls')
	arbolExiste = False
	arbol = Arbol(None, None, None);
	print("	======================================")
	print("	  ╔═╗╦═╗╔╗ ╔═╗╦    ╔╗ ╦╔╗╔╔═╗╦═╗╦╔═╗")
	print("	  ╠═╣╠╦╝╠╩╗║ ║║    ╠╩╗║║║║╠═╣╠╦╝║║ ║")
	print("	  ╩ ╩╩╚═╚═╝╚═╝╩═╝  ╚═╝╩╝╚╝╩ ╩╩╚═╩╚═╝")
	print("	======================================\n\nBienvenido")
	menu(arbolExiste, arbol)
	
main()
