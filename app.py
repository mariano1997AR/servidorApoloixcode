from flask import Flask, request,jsonify
from flask_cors import CORS
from db.Conectar import DB




app = Flask(__name__)
CORS(app)

#array global para procesar los datos del  usuario
personas = []


@app.route('/enviarDatosClientesApolo',methods=["POST"])
def submit():

    data = request.json
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    #instanciar la conexion de base de datos
    db1 = DB("localhost","root","","clientesargentina")

    #conectar 
    conn = db1.conectorDB()

    #verificar si el email y nombre existe
 
    #insertar datos
    #db1.modificarTablaCliente(conn)
  
    db1.insertarRegistroDB(conn,name,email)

    #Aca puedo procesar los datos y guardarlos en la base de datos
    #print(f"Nombre: {name}, Email: {email}, Message: {message}")

    #enviar una respuesta al cliente
    return jsonify({"status":"sucess","message":"Datos recibidos correctamente"})



if __name__ == '__main__':
    app.run(debug=True)

