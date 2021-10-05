from gramatica import parse as gram
from flask import Flask, redirect, url_for, render_template, request
from gramgraf import parse as grafica
app = Flask(__name__)
tmp_val=''

@app.route("/", methods=["POST","GET"])# de esta forma le indicamos la ruta para acceder a esta pagina.
def home():
    if request.method == "POST":
        inpt = request.form["entrada"]
        global tmp_val
        tmp_val=inpt
        result=gram(tmp_val)
        #dot = grafica(tmp_val)
        dot = "Aquí van las gráficas"
        return render_template('index.html', resultado=result, entry=tmp_val, graf = dot)
    else:
        return render_template('index.html', entry ="")

if __name__ == "__main__":
    app.run(debug=True)#para que se actualice al detectar cambios