#importacion de las librerias necesarias del backend
from flask import Flask,request
from werkzeug.utils import secure_filename
import os

app=Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"
ALLOWED_EXTENSIONS =set(["mp4","m4v"])

def allowed_file(file):
    file= file.split('.')
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    return False

@app.route('/')
def index():
    return "corriendo el servidor base"

@app.route('/upload',methods=["POST"])
def upload():
    file  = request.files["uploadFile"]
    filename = secure_filename(file.filename)
    if file and allowed_file(filename):
        file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
        return"formato correcto admitido"
    return "error en el formato del archivo"

if __name__ == '__main__':
    app.run(debug=True, port=3000)