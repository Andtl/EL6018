import unittest
import os.path
import sqlite3

import sys
sys.path.insert(0, '../app/')

import utils



class Test(unittest.TestCase):
    
    def test_crear_DB(self):
        BDFILE = 'DB.sqlite'
        TABLA = 'megatabla'
        CAMPO = 'texto_random'
        TIPO = 'VARCHAR(200)'
        utils.crear_BD(BDFILE,TABLA,CAMPO,TIPO)
        self.assertTrue(os.path.isfile(BDFILE))

    def test_BD_table(self):
        BDFILE = 'DB.sqlite'
        TABLA = 'megatabla'
        CAMPO = 'texto_random'
        TIPO = 'VARCHAR(200)'  

        conn = sqlite3.connect(BDFILE)
        c = conn.cursor()
        try:
            c.execute('SELECT count(*) FROM sqlite_master WHERE type = \'table\' AND name = \'{tn}\''.\
                              format(tn=TABLA))
        except:
            self.assertTrue(1==0)
        conn.commit()
        conn.close()   
        
        
    def test_IO_BD(self):
        BDFILE = 'DB.sqlite'
        TABLA = 'megatabla'
        CAMPO = 'texto_random'
        txt = 'new entry'
        utils.escribir_DB(txt,BDFILE,TABLA,CAMPO)
        a=utils.leer_BD(BDFILE,TABLA)
        self.assertTrue(txt==a[-1][0])


    def test_medida_std(self):
        dosis = 0.01 
        peso_m = 77.3 # peso promedio masculino en Chile
        peso_f = 67.5 # peso promedio femenino en Chile
        self.assertTrue(utils.medida(dosis,peso_m)==dosis*peso_m)
        self.assertTrue(utils.medida(dosis,peso_f)==dosis*peso_f)

    def test_medida_extremos(self):
        dosis = 0.01
        peso_min = 93 # ejemplo de sobre peso masculino
        peso_max = 53 # ejemplo de desnutricion masculina
        self.assertTrue(utils.medida(dosis,peso_min)==dosis*peso_min)
        self.assertTrue(utils.medida(dosis,peso_max)==dosis*peso_max)


if __name__ == '__main__':
    unittest.main()
