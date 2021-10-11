import re
from gramatica import parse as gram
from flask import Flask, redirect, url_for, render_template, request
from gramgraf import parse as grafica
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
            dot = grafica(tmp)
            return render_template('index.html', resultado="", entry=tmp, graf = dot)
        else:
            return render_template('index.html', entry ="", graf="")
    else:
        return render_template('index.html', entry ="", graf="")

if __name__ == "__main__":
    app.run(debug=True)#para que se actualice al detectar cambios