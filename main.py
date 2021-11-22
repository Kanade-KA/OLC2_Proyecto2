import re
from gramatica import parse as gram
from flask import Flask, render_template, request
from gramaticaC3D import parseopt as optimizacion
app = Flask(__name__)
@app.route("/", methods=["POST","GET"])# de esta forma le indicamos la ruta para acceder a esta pagina.
def home():
    if request.method == "POST":
        if request.form['submit_button'] == 'interprete':
            inpt = request.form["entrada"]
            entrada=inpt
            result=gram(entrada, 1)
            return render_template('index.html', resultado=result[0], entry=entrada, graf = "", tabla=result[1], error=result[2])
        if request.form['submit_button'] == 'ast':
            inpt = request.form["entrada"]
            entrada=inpt
            #dot = grafica(tmp)
            return render_template('index.html', resultado="", entry=entrada, graf = "dot")
        if request.form['submit_button']=='traductor':
            inpt = request.form["entrada"]
            entrada=inpt
            result=gram(entrada, 2)
            return render_template('index.html', resultado=result[0], entry=entrada, graf = "", tabla=result[1], error=result[2])
        if request.form['submit_button']=='mirilla':
            inpt = request.form["entrada"]
            entrada=inpt
            inptres = request.form["salida"]
            salida=inptres
            result=optimizacion(salida, 1)
            return render_template('index.html', resultado=salida, entry=entrada, graf = result[0], tabla=result[1], error=result[2])
        if request.form['submit_button']=='mirillas3':
            inpt = request.form["entrada"]
            tmp_val=inpt
            inptres = request.form["salida"]
            salida=inptres
            result=optimizacion(salida, 2)
            return render_template('index.html', resultado=salida, entry=tmp_val, graf = result[0], tabla=result[1], error=result[2])
        if request.form['submit_button']=='bloque1':
            inpt = request.form["entrada"]
            tmp_val=inpt
            inptres = request.form["salida"]
            salida=inptres
            result=optimizacion(salida, 3)
            return render_template('index.html', resultado=salida, entry=tmp_val, graf = result[0], tabla=result[1], error=result[2])
        else:
            return render_template('index.html', entry ="", graf="")
    else:
        return render_template('index.html', entry ="", graf="")

if __name__ == "__main__":
    app.run(debug=True)#para que se actualice al detectar cambios