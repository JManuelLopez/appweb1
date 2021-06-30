#importacion de librerias
from flask import Flask, render_template
#creacion del objeto tipo flask
app = Flask(__name__)
#creacion de ruta raiz a pagina pricipal
@app.route("/")
#creacion de funcion para llamar a index(pagina principal)
def index():

    return render_template('index.html')

@app.route("/gta")
def gta_html():
    return render_template('gta.html')

@app.route("/gta5")
def gta5_html():
    return render_template('gta5.html')

@app.route("/RedDead")
def Red_html():
    return render_template('Red.html')


#configuracion de archivo pricipal en ejecucion

if __name__ == '__main__':
    #Configuracion del puerto de escucha del servidor web
    app.run(port = 80,debug = True)



