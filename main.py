import re
from gramatica import parse as gram
from flask import Flask, redirect, url_for, render_template, request
#from gramgraf import parse as grafica
from gramatica import parsetrad as traductor
from gramaticaC3D import parseopt as optimizacion
app = Flask(__name__)
tmp_val=''

@app.route("/", methods=["POST","GET"])# de esta forma le indicamos la ruta para acceder a esta pagina.
def home():
    if request.method == "POST":
        if request.form['submit_button'] == 'interprete':
            inpt = request.form["entrada"]
            global tmp_val
            tmp_val=inpt
            result=gram(tmp_val)
            return render_template('index.html', resultado=result[0], entry=tmp_val, graf = "", tabla=result[1], error=result[2])
        if request.form['submit_button'] == 'ast':
            inpt = request.form["entrada"]
            global tmp
            tmp=inpt
            #dot = grafica(tmp)
            return render_template('index.html', resultado="", entry=tmp, graf = "dot")
        if request.form['submit_button']=='traductor':
            inpt = request.form["entrada"]
            global tmp_val3
            tmp_val3=inpt
            result=traductor(tmp_val3)
            return render_template('index.html', resultado=result[0], entry=tmp_val3, graf = "", tabla=result[1], error=result[2])
        if request.form['submit_button']=='mirilla':
            inpt = request.form["entrada"]
            tmp_val=inpt

            inptres = request.form["salida"]
            global tmp_val4
            tmp_val4=inptres
            result=optimizacion(tmp_val4)
            return render_template('index.html', resultado=tmp_val4, entry=tmp_val, graf = result[0], tabla=result[1], error=result[2])
        else:
            return render_template('index.html', entry ="", graf="")
    else:
        return render_template('index.html', entry ="", graf="")

if __name__ == "__main__":
    app.run(debug=True)#para que se actualice al detectar cambios