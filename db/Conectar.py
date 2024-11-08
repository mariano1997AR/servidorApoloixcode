import mysql.connector
from flask import jsonify

class DB:
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    
    def conectorDB(self):
        mydb = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database,
        )
        return mydb
    
    def insertarRegistroDB(self,conn,nombre,email):
        db = self.conectorDB()
        mycursor = conn.cursor()
        sql = "INSERT INTO cliente (nombre,email) VALUES (%s,%s)"
        val = (nombre,email)
        mycursor.execute(sql,val)
        db.commit()
        print(mycursor.rowcount, "Registro insertado")

    def obtenerTodosLosDatos(self,conn):
       mycursor = conn.cursor()
       mycursor.execute("SELECT * FROM cliente")
       myresult = mycursor.fetchall()
       for x in myresult:
          print(x)

    def obtenerDato(self,conn,nombre,email,personaAndres):
       mycursor = conn.cursor()
       sql = "SELECT * FROM cliente WHERE nombre = %s AND email = %s"
       emailInsertado = (nombre,email,)
       mycursor.execute(sql,emailInsertado)
       myresult = mycursor.fetchall()
       for x in myresult:
           personaAndres.append(x)
    
    def modificarTablaCliente(self,conn):
        mycursor = conn.cursor() 
        mycursor.execute("ALTER TABLE cliente MODIFY COLUMN email VARCHAR(255) UNIQUE NOT NULL")
        mycursor.close()
