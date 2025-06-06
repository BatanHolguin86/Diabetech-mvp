from flask import Flask, render_template, request, redirect, url_for, flash
import os
import json
from pathlib import Path

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev")
app.config["JSON_AS_ASCII"] = False

DATA_FILE = Path(os.environ.get("DATA_FILE", Path(__file__).with_name("data.json")))
VALID_TYPES = {"glucosa", "comidas", "entrenos"}

def load_data():
    if DATA_FILE.exists():
        with DATA_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    return {"glucosa": [], "comidas": [], "entrenos": []}


def save_data(data):
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route("/")
def home():
    data = load_data()
    return render_template("dashboard.html", data=data)

@app.route("/registro", methods=["POST"])
def registro():
    tipo = request.form.get("tipo")
    valor = request.form.get("valor", "").strip()
    if tipo not in VALID_TYPES or not valor:
        flash("Tipo o valor inválido", "error")
    else:
        data = load_data()
        data.setdefault(tipo, []).append(valor)
        save_data(data)
        flash("Registro agregado", "success")
    return redirect(url_for("home"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
