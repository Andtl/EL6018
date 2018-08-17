import sqlite3
from tkinter import *

import utils

#DATOS DE CONFIGURACION DE LA BASE DE DATOS 
BDFILE = 'DB.sqlite'
TABLA = 'megatabla'
CAMPO = 'texto_random'
TIPO = 'VARCHAR(200)'  

def crearBD():
	print("Creando BD")

	utils.crear_BD(BDFILE,TABLA,CAMPO,TIPO)

	print("Base de datos Creada")
	lbl5.configure(text="Base de Datos Creada!!")




def leerBD():

	print("reading DB")
	lbl2.configure(text="reading DB")

	registros=utils.leer_BD(BDFILE,TABLA)
    
	salida = ""
	for i in registros:
		salida+= i[0]
		salida+="\n"

	lbl2.configure(text=salida)
	print(salida)


def escribirBD():
	
	text = txt.get()
	print(text)
	
	try:
		utils.escribir_DB(text,BDFILE,TABLA,CAMPO)
		lbl3.configure(text="Saved")
    
	except sqlite3.IntegrityError:
		print('ERROR: ERROR')


 


if __name__ == '__main__':
	#programa principal

	window = Tk()

	window.title("EL6018 - Seminario de Proyecto")
	window.geometry('640x480+200+200')

	lbl5 = Label(window, text="Creacion de Base de Datos:", font=("Raleway", 10)) 
	lbl5.grid(row=1, column=0)

	lbl = Label(window, text="Acceso Base de Datos", font=("Raleway", 25))
	lbl.grid(row=0, column=0)

	btn3 = Button(window, text="Creacion", font=("Raleway", 10), command= crearBD)
	btn3.grid(row=1, column=1)

	btn = Button(window, text="Busqueda", font=("Raleway", 10), command= leerBD)
	btn.grid(row=2, column=0)

	lbl2 = Label(window, text="Resultados de Busqueda:", font=("Raleway", 15))
	lbl2.grid(row=3, column=0)

	lbl3 = Label(window, text="Guardado", font=("Raleway",12))
	lbl3.grid(row=4, column=0)

	lbl4 = Label(window, text="Elemento a guardar: ", font=("Raleway", 10)) 
	lbl4.grid(row=5, column=0)

	#campo de texto
	txt = Entry(window,width=20)
	txt.grid(row=5,column=1)

	btn2 = Button(window, text="Save", font=("Raleway", 10), command= escribirBD)
	btn2.grid(row=5, column=2)


	window.mainloop()
