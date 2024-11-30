"""
app/entrypoint.py
Punto de entrada para ejecutar aplicación
"""
from app import create_app
from app.config.settings import Setting

app = create_app()
app.config.from_object(Setting)

if __name__ == '__main__':
    app.run(debug=Setting.DEBUG, host=Setting.HOST, port=Setting.PORT)
