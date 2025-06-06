# DiabeTech MVP

Aplicación web sencilla para registrar y visualizar datos de diabetes. Utiliza Flask y guarda la información en `data.json`.

## Setup

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecuta la aplicación:
   ```bash
   python app.py
   ```

Variables de entorno:

- `PORT`: puerto donde se ejecutará Flask (por defecto `10000`)
- `FLASK_DEBUG`: activa el modo debug con `true`
- `SECRET_KEY`: clave usada por Flask para firmar cookies

Ejemplo:

```bash
PORT=8080 FLASK_DEBUG=true SECRET_KEY=mysecret python app.py
```

Los registros se guardan en `data.json` y se muestran en el panel principal.

## Tests

Instala pytest y ejecuta:

```bash
pytest
```

## License

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

### English

Simple Flask web app to record and display diabetes-related entries. Data is stored in `data.json`. See above for installation and usage. To run tests: `pytest`.
