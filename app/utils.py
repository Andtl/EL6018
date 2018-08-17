import sqlite3


def crear_BD(fileName,tableName,campoName,typeName):
	conn = sqlite3.connect(fileName)
	c = conn.cursor()
	try:
		c.execute('CREATE TABLE {tn} ({nf} {ft})'.format(tn=tableName, nf=campoName, ft=typeName))
	except:
		None
	conn.commit()
	conn.close()

    
def leer_BD(fileName,tableName):

	conn = sqlite3.connect(fileName)
	c = conn.cursor()

	c.execute('SELECT * FROM {tn}'.format(tn=tableName))

	registros = c.fetchall()

	conn.commit()
	conn.close()

	return registros



def escribir_DB(j,fileName,tableName,campoName):
    
	conn = sqlite3.connect(fileName)
	c = conn.cursor()
    
	c.execute("INSERT INTO {tn} ({cn}) VALUES ('{txt}')".format(tn=tableName, cn=campoName, txt=j))

	conn.commit()
	conn.close()


def medida(dosis,peso):
    return dosis*peso
