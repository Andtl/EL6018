import sqlite3
from sqlite3 import Error


def crear_BD(fileName, tableName, campos, tipos):
    
    conn = sqlite3.connect(fileName)
    c = conn.cursor()

    print("len1 " + str(len(campos)))
    print("len2 " + str(len(tipos)))
    
    try:
        c.execute('CREATE TABLE {tn} ({c1} {t1}, {c2} {t2}, {c3} {t3}, {c4} {t4}, {c5} {t5})'.format(tn=tableName, 
                                                                                                     c1=campos[0], 
                                                                                                     t1=tipos[0],
                                                                                                     c2=campos[1],
                                                                                                     t2=tipos[1],
                                                                                                     c3=campos[2],
                                                                                                     t3=tipos[3],
                                                                                                     c4=campos[3],
                                                                                                     t4=tipos[3],
                                                                                                     c5=campos[4],
                                                                                                     t5=tipos[4]))
    except Error as e:
        print (e)
        None
    conn.commit()
    conn.close()

def borrar_BD (fileName, tableName, id):

	error = 0
	conn = sqlite3.connect(fileName)
	c = conn.cursor()

	try:
		c.execute("DELETE FROM {tn} WHERE {tn}.nombre_medicamento='{cm}'".format(tn=tableName, cm=id))
	except Error as e:
		error = 1
		print (e)

	conn.commit()
	conn.close()

	if error == 1:
		return False
	else:
		return True


def leer_BD(fileName,tableName):
	error = 0
	conn = sqlite3.connect(fileName)
	c = conn.cursor()
	try:		
		c.execute('SELECT * FROM {tn}'.format(tn=tableName))
		registros = c.fetchall()
	except Error as e:
		print (e)
		error = 1


	conn.commit()
	conn.close()

	if error == 1:
		return [[]]
	else:
		return registros

def actualizar_BD (fileName, tableName, campos, datos, ind):


	error = 0
	conn = sqlite3.connect(fileName)
	c = conn.cursor()

	try:
		q = "UPDATE {tn} SET {cn1} = '{d1}', {cn2} = '{d2}', {cn3} = '{d3}', {cn4} = '{d4}', {cn5} = '{d5}' WHERE {tn}.nombre_medicamento='{ind}'".format(tn=tableName,cn1=campos[0],cn2=campos[1],cn3=campos[2],cn4=campos[3],cn5=campos[4],d1=datos[0],d2=datos[1],d3=datos[2],d4=datos[3],d5=datos[4],ind=ind)
		c.execute(q)
	
	except Error as e:
		print (e)
		error = 1

	conn.commit()
	conn.close()

	if error == 1:
		return False
	else:
		return True


def leer_BD_QUERY(fileName,tableName, q):

	error = 0
	conn = sqlite3.connect(fileName)
	c = conn.cursor()

	try:
		c.execute("SELECT * FROM {tn} WHERE {tn}.nombre_medicamento='{qr}'".format(tn=tableName, qr=q))

		registro = c.fetchall()

	except Error as e:
		print (e)
		error = 1

	conn.commit()
	conn.close()


	if error == 1:
		return []
	else:
		return registro


def llenar_BD_v1 (fileName, txtFile, tableName, campos):

	error = 0
	conn = sqlite3.connect(fileName)
	c = conn.cursor()

	archivo = open(txtFile,"r")


	l1 = []
	l2 = []
	l3 = []
	l4 = []
	l5 = []


	for linea in archivo:
		tmp = linea.strip().split(",")

		l1.append(tmp[0])
		l2.append(tmp[1])
		l3.append(tmp[2])
		l4.append(tmp[3])
		l5.append(tmp[4])
		
	for i in range(0, 5):
		c.execute("INSERT INTO {tn} ({c1},{c2},{c3},{c4},{c5}) VALUES ('{v1}','{v2}','{v3}','{v4}','{v5}')".format(tn=tableName,c1=campos[0],c2=campos[1],c3=campos[2],c4=campos[3],c5=campos[4],v1=l1[i],v2=l2[i],v3=l3[i],v4=l4[i],v5=l5[i]))
	
	conn.commit()
	conn.close()
	archivo.close()


def llenar_BD_v2 (fileName, tableName, campos, datos):

        conn = sqlite3.connect(fileName)
        c = conn.cursor()

        print (datos)

        l1 = [datos[0]]
        l2 = [datos[1]]
        l3 = [datos[2]]
        l4 = [datos[3]]
        l5 = [datos[4]]


        for i in range(0, 1):
                c.execute("INSERT INTO {tn} ({c1},{c2},{c3},{c4},{c5}) VALUES ('{v1}','{v2}','{v3}','{v4}','{v5}')".format(tn=tableName,c1=campos[0],c2=campos[1],c3=campos[2],c4=campos[3],c5=campos[4],v1=l1[i],v2=l2[i],v3=l3[i],v4=l4[i],v5=l5[i]))

        conn.commit()
        conn.close()

        return True


        


def medida(dosis,peso,concentracion):
	assert concentracion != 0
	dosisPaciente = dosis * peso * (1.0 / concentracion)
	dosisPaciente = round(dosisPaciente,3) 
	return dosisPaciente
	























