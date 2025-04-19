from flask import Flask, render_template, request, redirect

app = Flask(__name__)

data_store = {
    "glucosa": ["105 mg/dL"],
    "comidas": ["Desayuno: Avena y fruta"],
    "entrenos": ["Caminata 30 min"]
}

@app.route("/")
def home():
    return render_template("dashboard.html", data=data_store)

@app.route("/registro", methods=["POST"])
def registro():
    tipo = request.form.get("tipo")
    valor = request.form.get("valor")
    if tipo in data_store:
        data_store[tipo].append(valor)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)