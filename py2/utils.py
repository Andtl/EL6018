import sqlite3
from sqlite3 import Error


def crear_BD(fileName, tableName, campos, tipos):

	conn = sqlite3.connect(fileName)
	c = conn.cursor()

        print "len1 " + str(len(campos))
        print "len2 " + str(len(tipos))


	try:
		c.execute('CREATE TABLE {tn} ({c1} {t1}, {c2} {t2}, {c3} {t3}, {c4} {t4}, {c5} {t5})'.format(tn=tableName, c1=campos[0], t1=tipos[0], c2=campos[1],t2=tipos[1],c3=campos[2],t3=tipos[3],c4=campos[3],t4=tipos[3],c5=campos[4],t5=tipos[4]))
	except Error as e:
                print e
		None
	conn.commit()
	conn.close()

    
def leer_BD(fileName,tableName):
	error = 0
	conn = sqlite3.connect(fileName)
	c = conn.cursor()
	try:		
		c.execute('SELECT * FROM {tn}'.format(tn=tableName))
		registros = c.fetchall()
	except Error as e:
		print e
		error = 1


	conn.commit()
	conn.close()

	if error == 1:
		return 0
	else:
		return registros

    
def leer_BD_QUERY(fileName,tableName, q):

	error = 0
	conn = sqlite3.connect(fileName)
	c = conn.cursor()

	try:
		c.execute("SELECT * FROM {tn} WHERE {tn}.nombre_medicamento='{qr}'".format(tn=tableName, qr=q))

		registro = c.fetchall()

	except Error as e:
		print e
		error = 1

	conn.commit()
	conn.close()


	if error == 1:
		return []
	else:
		return registro

def escribir_DB(j,fileName,tableName,campoName):
    
	conn = sqlite3.connect(fileName)
	c = conn.cursor()
    
	c.execute("INSERT INTO {tn} ({cn}) VALUES ('{txt}')".format(tn=tableName, cn=campoName, txt=j))

	conn.commit()
	conn.close()


def llenar_BD_v1 (fileName, tableName, campos):

	error = 0
	conn = sqlite3.connect(fileName)
	c = conn.cursor()

	l1 = ["Adrenalina", "Atropina", "Adenosina", "Amiodarona", "Lidocaina"]
	l2 = [0.01, 0.01, 0.1, 1 ,1]
	l3 = [0.1, 0.1, 3, 50, 20]
	l4 = ["1ml=0.1mg (1ml+ 9 ml SF)", "1ml=0.1mg (1ml+ 9 ml SF)", "1ml=3mg", "1ml=50mg", "1ml=50mg"]
	l5 = [1.2, 1.2, 0.4, 1.2, 0.6]

	try:
		for i in range(0, 5):
			c.execute("INSERT INTO {tn} ({c1},{c2},{c3},{c4},{c5}) VALUES ('{v1}','{v2}','{v3}','{v4}','{v5}')".format(tn=tableName,c1=campos[0],c2=campos[1],c3=campos[2],c4=campos[3],c5=campos[4],v1=l1[i],v2=l2[i],v3=l3[i],v4=l4[i],v5=l5[i]))
	except Error as e:
		print e
		error = 1

	conn.commit()
	conn.close()

	if (error == 1):
		return False
	else:
		return True


def llenar_BD_v2 (fileName, tableName, campos, datos):

        conn = sqlite3.connect(fileName)
        c = conn.cursor()

        print datos

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


        


def medida(dosis,peso):
    return dosis*peso
