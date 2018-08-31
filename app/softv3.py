#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sqlite3
from Tkinter import *
import tkMessageBox
import math
 

import utils

#DATOS DE CONFIGURACION DE LA BASE DE DATOS

BDFILE = 'DB.sqlite'
TABLA = 'medicamentos'
CAMPO1 = 'nombre_medicamento'
TIPO1 = 'VARCHAR(200)'  
CAMPO2 = 'dosis'
TIPO2 = 'REAL'
CAMPO3 = 'dosis_unica'
TIPO3 = 'REAL'
CAMPO4 = 'peparacion'
TIPO4 = 'VARCHAR(200)'
CAMPO5 = 'volumen'
TIPO5 = 'REAL'



CAMPOS = [CAMPO1, CAMPO2, CAMPO3, CAMPO4, CAMPO5]
TIPOS  = [TIPO1, TIPO2, TIPO3, TIPO4, TIPO5]

ARCHIVODATOS = "datos.txt"
ARCHIVOBUSQUEDA = "busqueda.txt"


def revisarBusqueda (w):

	archivo = open(ARCHIVOBUSQUEDA,"r")
	revisar = ""
	exito = True
	for linea in archivo:
		linea = linea.strip()
		if (linea == "Test"):
			exito = False
		revisar = linea

	if exito:

		linea = linea.split(",")

		lblNombreRemedio.configure(text="Nombre Medicamento: " + linea[0])
		lblDosisRemedio.configure(text="Dosis: " + linea[1])
		lblConcentracionRemedio.configure(text="Dosis: " + linea[2])
		lblProcedimientoRemedio.configure(text="Procedimiento: " + linea[3])
		lblResultado.configure(text="")
		btnCalc.configure(state=NORMAL)
		btnBorrar.configure(state=NORMAL)
		btnActualizar.configure(state=NORMAL)



def crearBD ():
	print("Creando BD")

	utils.crear_BD(BDFILE,TABLA,CAMPOS, TIPOS)
	print("Base de datos Creada")
	tkMessageBox.showinfo("Exito", "Base de datos creada con Exito")


def cargarBD ():
	print ("Importando BD")
	if (utils.llenar_BD_v1(BDFILE, ARCHIVODATOS, TABLA, CAMPOS)):
		tkMessageBox.showinfo("Exito", "Medicamentos cargados con Exito")
	else:
		tkMessageBox.showinfo("Error", "No existe base de datos")


def cerrarVentanaRegistro (w):
	w.withdraw()

def cerrarVentanaConsulta (w):
	w.destroy()

def buscarRemedio (w, dato):

	registro=utils.leer_BD_QUERY(BDFILE,TABLA, dato)
	print registro
	if (len(registro) == 0):
		tkMessageBox.showinfo("Error", "El medicamento que busca NO EXISTE")
	else:

		nombre = registro[0][0]
		dosis = str(registro[0][1])
		concentracion = str(registro[0][2])
		procedimiento = registro[0][3]


		archivo = open(ARCHIVOBUSQUEDA,"w")
		salida = nombre+","+dosis+","+concentracion+","+procedimiento
		archivo.write(salida)
		archivo.close()
		
		btnBorrar.configure(state=NORMAL)
		btnActualizar.configure(state=NORMAL)

		lblNombreRemedio.configure(text="Nombre Medicamento: " + nombre)		
		lblDosisRemedio.configure(text="Dosis: " + dosis + " mg")
		lblConcentracionRemedio.configure(text="Concentracion: " + concentracion + " mg/ml")
		lblProcedimientoRemedio.configure(text="Procedimiento: " + procedimiento)
		lblResultado.configure(text="")
		lblDosisPaciente.configure(text="Dosis para el paciente: SIN INFO")
		btnCalc.configure(state=NORMAL)



def actualizarMedicamento (d, w, w2, nombre):

	datos = []

	if (d[0].get() == "" or d[1].get() == "" or d[2].get() == "" or d[3].get() == "" or d[4].get() == ""):
		d[5].configure(text="Debe llenar todos los campos")
	else:

		datos.append(d[0].get())
		datos.append(d[1].get())
		datos.append(d[2].get())	
		datos.append(d[3].get())
		datos.append(d[4].get())

		if (utils.actualizar_BD(BDFILE, TABLA, CAMPOS, datos, nombre)):
			cerrarVentanaRegistro(w)
			tkMessageBox.showinfo("Guardado", "Medicamento Ingresado con Exito")
			buscarRemedio(w2, datos[0])


		else:
			tkMessageBox.showinfo("Error", "No se pudo actualizar Medicamento")





def guardarMedicamento (d, w):

	datos = []

	if (d[0].get() == "" or d[1].get() == "" or d[2].get() == "" or d[3].get() == "" or d[4].get() == ""):
		d[5].configure(text="Debe llenar todos los campos")
	else:

		datos.append(d[0].get())
		datos.append(d[1].get())
		datos.append(d[2].get())	
		datos.append(d[3].get())
		datos.append(d[4].get())

		if (utils.llenar_BD_v2(BDFILE, TABLA, CAMPOS, datos)):
			cerrarVentanaRegistro(w)
			tkMessageBox.showinfo("Guardado", "Medicamento Ingresado con Exito")



def abrirVentanaRegistro (w) :

	registros=utils.leer_BD(BDFILE,TABLA)

	if (registros == 0):
		tkMessageBox.showinfo("Error", "No hay medicamentos para mostrar")
	else:


		w.deiconify()
		datos = []

		lbl1 = Label(w, text="Nombre Medicamento: ", borderwidth=1, font=("Raleway",12))
		lbl1.grid(row=1,column=0)	
		txt1 = Entry(w,width=20)
		txt1.grid(row=1,column=1)


		lbl2 = Label(w, text="Dosis (mg/kg): ", borderwidth=1, font=("Raleway",12))
		lbl2.grid(row=2,column=0)
		txt2 = Entry(w,width=20)
		txt2.grid(row=2,column=1)

		lbl3 = Label(w, text="Concentracion (mg/ml): ", borderwidth=1, font=("Raleway",12))
		lbl3.grid(row=3,column=0)
		txt3 = Entry(w,width=20)
		txt3.grid(row=3,column=1)

		lbl4 = Label(w, text="Preparacion: ", borderwidth=1, font=("Raleway",12))
		lbl4.grid(row=4,column=0)
		txt4 = Entry(w,width=20)
		txt4.grid(row=4,column=1)

		lbl5 = Label(w, text="Volumen: ", borderwidth=1, font=("Raleway",12))
		lbl5.grid(row=5,column=0)
		txt5 = Entry(w,width=20)
		txt5.grid(row=5,column=1)

		lbl6 = Label(w, text="", borderwidth=1, font=("Raleway",12))
		lbl6.grid(row=6,column=0)


		datos.append(txt1)
		datos.append(txt2)
		datos.append(txt3)
		datos.append(txt4)
		datos.append(txt5)
		datos.append(lbl6)
		
		
		btn1 = Button(w, text="Guardar", font=("Raleway", 10), command= lambda: guardarMedicamento(datos, w))
		btn1.grid(row=7, column=0)

		btn2 = Button(w, text="Volver", font=("Raleway", 10), command = lambda: cerrarVentanaRegistro(w))
		btn2.grid(row=7, column=1)


def consultarDatosGuardados(w):
	
	registros=utils.leer_BD(BDFILE,TABLA)

	if (registros == 0):
		tkMessageBox.showinfo("Error", "No hay medicamentos para mostrar")
	else:

		windowConsulta = Toplevel(w)
		windowConsulta.resizable(0,0)

		print("reading DB")

		registros=utils.leer_BD(BDFILE,TABLA)
	    
		salida = ""
		r = 0
		c = 0

		for i in registros:	
			
			Label(windowConsulta, text="Nombre: " + i[0] + " - ", borderwidth=1,font=("Raleway", 10)).grid(row=r, column=0)
			Label(windowConsulta, text="Dosis: " + str(i[1]) + " mg - ", borderwidth=1,font=("Raleway", 10)).grid(row=r, column=1)
			Label(windowConsulta, text="Concentracion:" + str(i[2]) + " mg/ml - ", borderwidth=1,font=("Raleway", 10)).grid(row=r, column=2)
			Label(windowConsulta, text="Preparacion: " + i[3] + " - ", borderwidth=1,font=("Raleway", 10)).grid(row=r, column=3)
			Label(windowConsulta, text="Volumen: " + str(i[4]) + " - ", borderwidth=1,font=("Raleway", 10)).grid(row=r, column=4)
			Label(windowConsulta, text="-----", borderwidth=1,font=("Raleway", 10)).grid(row=r+1, column=0)
			r+= 1
		
		print salida

		btn1 = Button(windowConsulta, text="Volver", font=("Raleway", 10), command = lambda: cerrarVentanaConsulta(windowConsulta))
		btn1.grid(row=r, column=1)




def menuActualizarMedicamento (w, w2, dato): 

	dato = dato.strip().split(" ")
	nombre = dato[2]

	resultado = utils.leer_BD_QUERY(BDFILE,TABLA, nombre)

	if (resultado == []):
		tkMessageBox.showinfo("Error", "No hay medicamentos para mostrar")
	else:

		resultado = resultado[0]

		w.deiconify()
		datos = []

		lbl1 = Label(w, text="Nombre Medicamento: ", borderwidth=1, font=("Raleway",12))
		lbl1.grid(row=1,column=0)	
		txt1 = Entry(w, width=20)
		txt1.insert(END, resultado[0])
		txt1.grid(row=1,column=1)


		lbl2 = Label(w, text="Dosis (mg/kg): ", borderwidth=1, font=("Raleway",12))
		lbl2.grid(row=2,column=0)
		txt2 = Entry(w,width=20)
		txt2.insert(END, resultado[1])		
		txt2.grid(row=2,column=1)

		lbl3 = Label(w, text="Concentracion (mg/ml): ", borderwidth=1, font=("Raleway",12))
		lbl3.grid(row=3,column=0)
		txt3 = Entry(w,width=20)
		txt3.insert(END, resultado[2])
		txt3.grid(row=3,column=1)

		lbl4 = Label(w, text="Preparacion: ", borderwidth=1, font=("Raleway",12))
		lbl4.grid(row=4,column=0)
		txt4 = Entry(w,width=20)
		txt4.insert(END, resultado[3])
		txt4.grid(row=4,column=1)

		lbl5 = Label(w, text="Volumen: ", borderwidth=1, font=("Raleway",12))
		lbl5.grid(row=5,column=0)
		txt5 = Entry(w,width=20)
		txt5.insert(END, resultado[4])
		txt5.grid(row=5,column=1)

		lbl6 = Label(w, text="", borderwidth=1, font=("Raleway",12))
		lbl6.grid(row=6,column=0)


		datos.append(txt1)
		datos.append(txt2)
		datos.append(txt3)
		datos.append(txt4)
		datos.append(txt5)
		datos.append(lbl6)
		
		
		btn1 = Button(w, text="Actualizar", font=("Raleway", 10), command= lambda: actualizarMedicamento(datos, w, w2, nombre))
		btn1.grid(row=7, column=0)

		btn2 = Button(w, text="Volver", font=("Raleway", 10), command = lambda: cerrarVentanaRegistro(w))
		btn2.grid(row=7, column=1)







def menuBorrarMedicamento(w, dato):
	
	nombre = dato.strip().split(" ")
	nombre = nombre[2]

	exito = utils.borrar_BD(BDFILE,TABLA, nombre)

	if (exito):
		tkMessageBox.showinfo("Exito", "Medicamento borrado con éxito")
		archivo = open(ARCHIVOBUSQUEDA, "w")
		archivo.write("T")
		archivo.close()

		#PORSEGURIDAD !!!
		lblNombreRemedio.configure(text="Nombre Medicamento: SIN INFO")
		lblDosisRemedio.configure(text="Dosis: SIN INFO")
		lblConcentracionRemedio.configure(text="Concentración: SIN INFO")
		lblProcedimientoRemedio.configure(text="Procedimiento: SIN INFO")
		btnCalc.configure(state=DISABLED)
		btnBorrar.configure(state=DISABLED)
		btnActualizar.configure(state=DISABLED)
		lblDosisPaciente.configure(text="Dosis para el paciente: SIN INFO")	
	else:
		tkMessageBox.showinfo("Error", "No se pudo borrar Medicamento")







def calcularDosis (w, dosis, dato, concentracion):
	
	dosis = dosis.strip().split(" ")
	concentracion = concentracion.strip().split(" ")


	dosis = float(dosis[1])
	concentracion = float(concentracion[1])

	if (dato != "" and not dato.isalpha()):
		try:
			dosisPaciente = utils.medida(dosis, float(dato),concentracion)
		
			salida = "Dosis para el paciente: {0:.2f}".format(dosisPaciente)
			
			lblDosisPaciente.configure(text=salida + " ml")

		except AssertionError:
			tkMessageBox.showinfo("Error", "Debe ingresar un peso valido")	
	else:
		tkMessageBox.showinfo("Error", "Debe ingresar un peso valido")
		


def caca():
    tkMessageBox.showinfo("Error", "No me has terminado la tarea")


if __name__ == '__main__':
	#programa principal


	window = Tk()
	windowRegistro = Toplevel(window)
	window.title("EL6018 - Seminario de Proyecto")
	window.geometry('800x800')

	windowRegistro.protocol("WM_DELETE_WINDOW", "onexit")

	window.resizable(0,0)
	windowRegistro.resizable(0,0)

	window.rowconfigure(1, weight=1)
	window.rowconfigure(12, weight=1)


	# Crear el menu principal
	menubarra = Menu(window)

	# Crea un menu Archivo y lo agrega al menu barra
	menuarchivo = Menu(menubarra, tearoff=0)
	menuarchivo.add_command(label="Crear Base de Datos", command=crearBD)
	menuarchivo.add_command(label="Cargar Nueva Lista", command=cargarBD)
	menuarchivo.add_command(label="Ver Lista Actual", command=lambda: consultarDatosGuardados(window))
	menuarchivo.add_separator()
	menuarchivo.add_command(label="Salir", command=window.quit)

	menubarra.add_cascade(label="Archivo", menu=menuarchivo)

	# Crea un menu Editar y lo agrega al menu barra
	menueditar = Menu(menubarra, tearoff=0)
	menueditar.add_command(label="Agregar Medicamento", command=lambda: abrirVentanaRegistro(windowRegistro))
	menueditar.add_command(label="Borrar Medicamento", command=lambda: menuBorrarDatosDB(window))
	menueditar.add_command(label="Reemplazar Medicamento", command=caca)
	menubarra.add_cascade(label="Editar", menu=menueditar)

	# Crea un menu Aiudaaa y lo agrega al menu barra
	menuayuda = Menu(menubarra, tearoff=0)
	menuayuda.add_command(label="Acerca de...", command=caca)
	menubarra.add_cascade(label="Ayuda", menu=menuayuda)




	btnBorrar = Button(window, text="Borrar Medicamento", font=("Raleway", 10),background="LightBlue", state=DISABLED, command = lambda: menuBorrarMedicamento(window, lblNombreRemedio["text"]))
	btnBorrar.grid(row=4,column=0)
	btnActualizar = Button(window, text="Actualizar Medicamento", font=("Raleway", 10),background="LightBlue", state=DISABLED, command = lambda: menuActualizarMedicamento(windowRegistro, window, lblNombreRemedio["text"]))
	btnActualizar.grid(row=4,column=1)

	lblTituloBusqueda = Label(window, text="Información de Dosis Medicamento", borderwidth=1,font=("Raleway", 10),background="LightBlue").grid(row=6, column=0,sticky=W)
	lblNombreRemedio = Label(window, text="Nombre Medicamento: SIN INFO", borderwidth=1,font=("Raleway", 10),background="LightBlue")
	lblNombreRemedio.grid(row=7, column=0,sticky=W)
	lblDosisRemedio = Label(window, text="Dosis: SIN INFO", borderwidth=1,font=("Raleway", 10),background="LightBlue")
	lblDosisRemedio.grid(row=8, column=0,sticky=W)
	lblConcentracionRemedio = Label(window, text="Concentración: SIN INFO", borderwidth=1,font=("Raleway", 10),background="LightBlue")
	lblConcentracionRemedio.grid(row=9, column=0,sticky=W)
	lblProcedimientoRemedio = Label(window, text="Procedimiento: SIN INFO", borderwidth=1,font=("Raleway", 10),background="LightBlue")
	lblProcedimientoRemedio.grid(row=10, column=0,sticky=W)

	# Crea un boton y barra buscar
	lblCalcular = Label(window, text="Ingrese Peso Paciente: ", font=("Raleway",10), background="LightBlue")
	lblCalcular.grid(row=11,column=0, sticky=W)
	d = Entry(window, width=20)
	d.grid(row=11,column=1, sticky=W)
	btnCalc = Button(window, text="Calcular", font=("Raleway", 10),background="LightBlue", state=DISABLED, command = lambda: calcularDosis(window, lblDosisRemedio["text"], d.get(), lblConcentracionRemedio["text"]))
	btnCalc.grid(row=11, column=2, sticky=W)


	# Crea un boton y barra buscar
	Label(window, text="",background="LightBlue").grid(row=0,column=0)
	lblTitulo2 = Label(window, text="Ingrese Remedio a Buscar: ", borderwidth=1, font=("Raleway",12),background="LightBlue")
	lblTitulo2.grid(row=1,column=1, sticky=W)
	txtRemedio = Entry(window,width=20)
	txtRemedio.grid(row=1,column=2, sticky=W)
	btnRemedio = Button(window, text="Buscar", font=("Raleway", 10), command = lambda: buscarRemedio(window, txtRemedio.get()),background="CadetBlue")
	btnRemedio.grid(row=1, column=3, sticky=W)

	# Mostrar el menu
	window.config(menu=menubarra,background="LightBlue")

	lblTemp = Label(window, text="",background="LightBlue").grid(row=12,column=0)
	lblTemp = Label(window, text="",background="LightBlue").grid(row=5,column=0)
	lblTemp = Label(window, text="",background="LightBlue").grid(row=3,column=0)

	lblTitulo5 = Label(window, text="Resultados de la búsqueda", borderwidth=1, font=("Raleway",12),background="LightBlue")
	lblTitulo5.grid(row=2,column=0)

	lblResultado = Label(window, text="Su búsqueda no produjo resultados", borderwidth=1,font=("Raleway", 10),background="LightBlue")
	lblResultado.grid(row=3, column=0)


	windowRegistro.withdraw() # Ventana ql no saía como sacarla jaja


	lblDosisPaciente = Label(window, text="Dosis para el paciente: SIN INFO",font=("Raleway",14),background="LightBlue")
	lblDosisPaciente.grid(row=12, column=0)

	revisarBusqueda(window)

	# Mostrar la ventana
	window.mainloop()
