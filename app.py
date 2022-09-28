from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mostrar", methods=['POST', 'GET'])
def mostrar():
    mensagem="o botão foi acionado"
    #linkar botão aqui
    return render_template("index.html",mensagem) #("index.html, variável linkada do caminho")
app.run(debug=True)


