from flask import Flask, jsonify, request
from flask_cors import CORS
from regex import ParserXML

app = Flask(__name__)
CORS(app)

xml = ParserXML()

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"
  
@app.route('/parsearXML', methods=['POST'])
def Parsear():
      dato = request.json['xml']
      dato = dato.split("\n")
      xml.eDatos(dato)
      r = jsonify({"msj":"ARCHIVO XML PROCESADO"})
      return r

@app.route('/salida', methods=['GET'])
def crearSalida():
      with open("Estadisticas.xml") as archivo:
        linea = archivo.readlines()
        r = jsonify({"mensaje":linea})
        return r




if __name__ =='__main__':
    app.run(debug=True, port=400)