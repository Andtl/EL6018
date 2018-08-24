import sqlite3
from Tkinter import *
import tkMessageBox
 

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



def crearBD ():
	print("Creando BD")

	utils.crear_BD(BDFILE,TABLA,CAMPOS, TIPOS)
	print("Base de datos Creada")
	tkMessageBox.showinfo("Exito", "Base de datos creada con Exito")


def cargarBD ():
	print ("Importando BD")
	if (utils.llenar_BD_v1(BDFILE, TABLA, CAMPOS)):
		tkMessageBox.showinfo("Exito", "Medicamentos cargados con Exito")
	else:
		tkMessageBox.showinfo("Error", "No existe base de datos")


def cerrarVentanaRegistro (w):
	w.withdraw()

def cerrarVentanaConsulta (w):
	w.destroy()

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


def calcularDosis (w, dosis, dato, concentracion):

	Label(w, text="", borderwidth=1,font=("Raleway", 15)).grid(row=7, column=0)
	
	if (dato != "" and not dato.isalpha()):

		dosisPaciente = utils.medida(dosis, float(dato))
		dosisPaciente = dosisPaciente * (1.0 / concentracion)
		tkMessageBox.showinfo("Exito", "La dosis para el paciente es: " + str(dosisPaciente) + " ml")
		Label(w, text="Dosis: " + str(dosisPaciente) + " ml", borderwidth=1,font=("Raleway", 15)).grid(row=8, column=0)
		Button(w, text="Volver", font=("Raleway", 10), command = lambda: cerrarVentanaConsulta(w)).grid(row=10, column=1)

	else:
		tkMessageBox.showinfo("Error", "Debe ingresar un peso valido")
		

def buscarRemedio (w, dato):

	registro=utils.leer_BD_QUERY(BDFILE,TABLA, dato)
	print registro
	if (len(registro) == 0):
		tkMessageBox.showinfo("Error", "El medicamento que busca NO EXISTE")
	else:

		windowConsulta = Toplevel(w)
		windowConsulta.resizable(0,0)

		nombre = registro[0][0]
		dosis = str(registro[0][1])
		concentracion = str(registro[0][2])
		procedimiento = registro[0][3]

		Label(windowConsulta, text="Informacion Dosis Medicamento", borderwidth=1,font=("Raleway", 15)).grid(row=0, column=0)
		Label(windowConsulta, text="", borderwidth=1,font=("Raleway", 15)).grid(row=1, column=0)

		Label(windowConsulta, text="Nombre: " + nombre, borderwidth=1,font=("Raleway", 15)).grid(row=2, column=0)
		Label(windowConsulta, text="Dosis: " + dosis + " mg", borderwidth=1,font=("Raleway", 15)).grid(row=3, column=0)
		Label(windowConsulta, text="Concentracion: " + concentracion + " mg/ml", borderwidth=1,font=("Raleway", 15)).grid(row=4, column=0)
		Label(windowConsulta, text="Procedimiento: " + procedimiento, borderwidth=1,font=("Raleway", 15)).grid(row=4, column=0)

		Label(windowConsulta, text="", borderwidth=1,font=("Raleway", 15)).grid(row=5, column=0)

		Label(windowConsulta, text="Ingrese Peso Paciente: ", borderwidth=1, font=("Raleway",12)).grid(row=6,column=0)
		d = Entry(windowConsulta,width=20)
		d.grid(row=6,column=1)
		Button(windowConsulta, text="Calcular", font=("Raleway", 10), command = lambda: calcularDosis(windowConsulta, float(dosis), d.get(), float(concentracion))).grid(row=6, column=2)


if __name__ == '__main__':
	#programa principal

	window = Tk()
	windowRegistro = Toplevel(window)

	window.title("EL6018 - Seminario de Proyecto")
	window.geometry('800x600')

	windowRegistro.protocol("WM_DELETE_WINDOW", "onexit")

	window.resizable(0,0)
	windowRegistro.resizable(0,0)


	for i in range(0, 5):
		window.columnconfigure(i, weight=1)
		window.rowconfigure(i, weight=1)


	lblTitulo = Label(window, text="Sistema de Acceso a Base de Datos", borderwidth=1,font=("Raleway", 25))
	lblTitulo.grid(row=0,column=0)

	lblOpcion = Label(window, text="Seleccionar Opcion", borderwidth=1, font=("Raleway",12))
	lblOpcion.grid(row=1,column=0)

	btnCrear = Button(window, text="Crear BD", font=("Raleway", 10), command= crearBD)
	btnCrear.grid(row=1, column=1)

	btnCargar = Button(window, text="Cargar BD", font=("Raleway", 10), command= cargarBD)
	btnCargar.grid(row=1, column=2)

	btnIngresar = Button(window, text="Ingresar Medicamento", font=("Raleway", 10), command= lambda: abrirVentanaRegistro(windowRegistro))
	btnIngresar.grid(row=2, column=0)

	btnConsultar = Button(window, text="Ver Medicamentos", font=("Raleway", 10), command= lambda: consultarDatosGuardados(window))
	btnConsultar.grid(row=2, column=1)

	lblEspacio = Label(window, text="", borderwidth=2, font=("Raleway",20))
	lblEspacio.grid(row=3,column=0)

	lblTitulo2 = Label(window, text="Ingrese Remedio a Buscar: ", borderwidth=1, font=("Raleway",12))
	lblTitulo2.grid(row=4,column=0)
	txtRemedio = Entry(window,width=20)
	txtRemedio.grid(row=4,column=1)
	btnRemedio = Button(window, text="Buscar", font=("Raleway", 10), command = lambda: buscarRemedio(window, txtRemedio.get()))
	btnRemedio.grid(row=4, column=2)





	windowRegistro.withdraw() # Oculta la ventana v1
	window.mainloop()
