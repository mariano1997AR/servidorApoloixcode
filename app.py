from flask import Flask, request,jsonify
from flask_cors import CORS
#from db.Conectar import DB
import os




app = Flask(__name__)
CORS(app , resources={r"/*": {"origins": "*"}})

#array global para procesar los datos del  usuario
personas = []
@app.route('/')
def index():
    return 'hola mundo'



@app.route('/submit',methods=["POST"])
def submit():

    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    #instanciar la conexion de base de datos
    #db1 = DB("localhost","root","","clientesargentina")

    #conectar 
    #conn = db1.conectorDB()

    #verificar si el email y nombre existe
 
    #insertar datos
    #db1.modificarTablaCliente(conn)
  
    #db1.insertarRegistroDB(conn,name,email)

    #Aca puedo procesar los datos y guardarlos en la base de datos
    #print(f"Nombre: {name}, Email: {email}, Message: {message}")

    #enviar una respuesta al cliente
    #return jsonify({"status":"sucess","message":"Datos recibidos correctamente"})
    try:
        # Intentando obtener los datos del formulario
        data = request.get_json()  # Si estás esperando datos en formato JSON
        # data = request.form  # Si los datos están en formato form-data (por ejemplo, un formulario HTML tradicional)
        
        # Aquí puedes hacer algo con los datos (guardar en base de datos, procesarlos, etc.)
        print(data)  # Solo para depurar, puedes eliminarlo después

        return jsonify({"message": "Datos recibidos correctamente"}), 200

    except Exception as e:
        # Si ocurre un error, lo capturamos y lo mostramos
        return jsonify({"error": str(e)}), 500

# Manejar las solicitudes OPTIONS explícitamente
@app.route('/submit', methods=['OPTIONS'])
def options():
    response = jsonify()
    response.status_code = 200
    return response

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')  # o 'http://localhost:5173'
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(debug=True,host="0.0.0.0", port=port)


