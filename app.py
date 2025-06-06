from flask import Flask, render_template, request, redirect, url_for, flash
import os
import json

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev")

DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "glucosa": ["105 mg/dL"],
        "comidas": ["Desayuno: Avena y fruta"],
        "entrenos": ["Caminata 30 min"],
    }


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

data_store = load_data()

@app.route("/")
def home():
    return render_template("dashboard.html", data=data_store)

@app.route("/registro", methods=["POST"])
def registro():
    tipo = request.form.get("tipo")
    valor = request.form.get("valor")
    if tipo in data_store:
        data_store[tipo].append(valor)
        save_data(data_store)
        flash("Registro agregado")
    return redirect(url_for("home"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
