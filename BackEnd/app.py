from flask import Flask
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)
@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"
  
if __name__ =='__main__':
    app.run(debug=True, port=400)