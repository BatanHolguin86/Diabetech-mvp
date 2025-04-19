from flask import Flask, render_template, request, redirect, url_for
import os
import json

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def dashboard():
    # Se pasa una lista vacía por defecto
    return render_template('dashboard.html', data=[])

# Ruta para recibir datos simulados (opcional para pruebas)
@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.to_dict()
    print("Datos recibidos:", data)

    # Aquí puedes guardar los datos si lo necesitas
    # Por ahora, solo se imprimen y se redirige

    return redirect(url_for('dashboard'))

# Iniciar el servidor correctamente en Render
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
