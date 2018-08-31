import unittest
import os.path
import sqlite3
import os

import sys
sys.path.insert(0, '../app/')
import utils

#############
#   Utils   #
#############

"""
funcs:
- crear_BD 
- borrar_BD 
- leer_BD 
- actualizar_BD 
- leer_BD_QUERY  
- llenar_BD_v1 
- llenar_BD_v2 
- medida 
"""


ARCHIVODATOS = "../app/datos.txt"
ARCHIVOBUSQUEDA = "../app/busqueda.txt"



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

archivo = open(ARCHIVODATOS,"r")
DATOS_LLENADO_BD_v1=[]
for linea in archivo:
    tmp = linea.strip().split(",")
    DATOS_LLENADO_BD_v1.append((tmp[0],float(tmp[1]),tmp[2],tmp[3],float(tmp[4])))


class Test(unittest.TestCase):
    
    # crear_BD
    def test_crear_DB(self):
        utils.crear_BD(BDFILE,TABLA,CAMPOS, TIPOS)
        self.assertTrue(os.path.isfile(BDFILE)) 

    
    # actualizar_BD + leer_BD_QUERY
    def test_actualizar_DB(self):
        nombre = 'Lidocaina'
        datos = ['Lidocaina', 1.0, '20', '1ml=50mg', 0.6]
        utils.actualizar_BD(BDFILE, TABLA, CAMPOS, datos, nombre)
        resultado = utils.leer_BD_QUERY(BDFILE,TABLA, nombre)
        self.assertTrue(tuple(datos)==resultado[-1])      

    # actualizar_BD 
    def test_negativo_actualizar_DB(self):
        nombre = 'Lidocaina'
        datos = ['Lidocaina', 2.0, 2.0,'ejemplo',2.0]
        resultado_bool = utils.actualizar_BD(BDFILE, nombre, CAMPOS, datos, nombre)
        #print(utils.leer_BD(BDFILE,TABLA))
        self.assertFalse(resultado_bool)


    # leer_BD_QUERY
    def test_negativo_leer_DB_QUERY(self):
        nombre = 'Error'
        resultado = utils.leer_BD_QUERY(BDFILE,TABLA, nombre)
        self.assertTrue(resultado==[])    


    # leer_BD
    def test_negativo_leer_DB(self):
        nombre = 'Error'
        resultado = utils.leer_BD(BDFILE,nombre)
        self.assertTrue(resultado==[[]])  

    # borrar_BD
    def test_borrar_DB(self):
        nombre = 'Adrenalina'
        exito = utils.borrar_BD(BDFILE,TABLA, nombre)
        resultado=utils.leer_BD(BDFILE,TABLA)
        self.assertFalse(nombre==resultado[0][0])        
 


    #llenar_BD_v1
    def test_llenar_v1(self):

        os.remove(BDFILE)
        utils.crear_BD(BDFILE,TABLA,CAMPOS, TIPOS)
        utils.llenar_BD_v1(BDFILE, ARCHIVODATOS, TABLA, CAMPOS)
        registros=utils.leer_BD(BDFILE,TABLA)
        self.assertTrue(registros==DATOS_LLENADO_BD_v1)


 #llenar_BD_v2
    def test_llenar_v2(self):
        datos = ['Lidocaina', 1.0, '20', '1ml=50mg', 0.6]
        utils.llenar_BD_v2(BDFILE, TABLA, CAMPOS, datos)
        registros=utils.leer_BD(BDFILE,TABLA)
        self.assertTrue(registros[-1]==tuple(datos))


    # medida
    def test_medida_std(self):
        dosis = 0.01 
        peso_m = 77.3 # peso promedio masculino en Chile
        peso_f = 67.5 # peso promedio femenino en Chile
        concentracion = 2

        dosisPaciente_m = dosis * peso_m * (1.0 / concentracion)
        dosisPaciente_m = round(dosisPaciente_m,3) 

        dosisPaciente_f = dosis * peso_f * (1.0 / concentracion)
        dosisPaciente_f = round(dosisPaciente_f,3) 

        self.assertTrue(utils.medida(dosis,peso_m,concentracion)==dosisPaciente_m)
        self.assertTrue(utils.medida(dosis,peso_f,concentracion)==dosisPaciente_f)

    # medida
    def test_medida_extremos(self):
        dosis = 0.01
        peso_min = 93 # ejemplo de sobre peso masculino
        peso_max = 53 # ejemplo de desnutricion masculina

        concentracion = 2

        dosisPaciente_min = dosis * peso_min * (1.0 / concentracion)
        dosisPaciente_min = round(dosisPaciente_min,3) 

        dosisPaciente_max = dosis * peso_max * (1.0 / concentracion)
        dosisPaciente_max = round(dosisPaciente_max,3) 

        self.assertTrue(utils.medida(dosis,peso_min,concentracion)==dosisPaciente_min)
        self.assertTrue(utils.medida(dosis,peso_max,concentracion)==dosisPaciente_max)
    
    #medida
    def test_negativo_medida(self):
        dosis = 0.01
        peso = 93 # ejemplo de sobre peso masculino

        concentracion = 2

        dosisPaciente = dosis * peso * (1.0 / concentracion)
        dosisPaciente = round(dosisPaciente,3) 

        self.assertFalse(utils.medida(dosis,peso,2)!=dosisPaciente)
        with self.assertRaises(Exception): utils.medida(dosis,peso,0)
    

if __name__ == '__main__':
    unittest.main()
