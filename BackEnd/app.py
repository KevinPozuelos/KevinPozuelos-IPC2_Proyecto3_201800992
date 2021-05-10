from flask import Flask, jsonify, request
from flask_cors import CORS
from regex import RegexXML
from Consulta import Consulta
from documentacion import documentacion
app = Flask(__name__)
CORS(app)
DateArray = []
XML = RegexXML()
handler = Consulta()
docu = documentacion()

  
@app.route('/AlmacenarXML', methods=['POST'])
def GuardarXML():
    
    archivo=request.json['XMLdatos']
    archivo=archivo.split("\n")

    global DateArray
    DateArray=XML.Parserxml(archivo)
    respuesta=jsonify({"mensaje":"Estadisticas.xml, guardado"})
    return respuesta

@app.route('/ListaFechas', methods=['GET'])
def ListaComboBox():
    temporalFechas1=DateArray[0]
    temporalFechas2=DateArray[1]
    fechas=[]
    siguiente=0
    for elemento in temporalFechas1:
        if siguiente == len(temporalFechas1):
            break
        fechas.append(temporalFechas1[siguiente])
        siguiente+=5

    siguiente=0
    for elemento in temporalFechas2:
        fechas.append(elemento[1])
    
    respuesta=jsonify({"ListaFechas":fechas})
    return respuesta

@app.route('/CargarXMLsalida', methods=['GET'])
def CargarXMLsalida():
    with open("Estadistica.xml") as archivo:
        lineas=archivo.readlines()
    respuesta=jsonify({"mensaje":lineas})
    return respuesta

@app.route('/Codigo/<string:Busqueda>', methods=['GET'])
def ConsultarCodigo(Busqueda):

    resultado=handler.ConsultaCodigo(DateArray, Busqueda)
    respuesta=jsonify({"mensaje":resultado})
    
    return respuesta

app.route('/documentacion', methods=['GET'])
def Documentacion():
    docu.abrirdocumetacion()
    respuesta=jsonify({'mensaje':'Documentacion.pdf'})

    

if __name__ =='__main__':
    app.run(debug=True, port=4000)