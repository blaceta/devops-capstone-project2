import logging
from flask import Flask
from flask_talisman import Talisman
from . import config

# Instancia de la aplicación Flask
app = Flask(__name__)
app.config.from_object(config)

# Configuración de Talisman para encabezados de seguridad
# Esto habilita CSP, HSTS, y previene el sniffing de tipos de contenido
talisman = Talisman(app)

# Importar las rutas después de inicializar la app para evitar importaciones circulares
from service import routes, models

# Configuración de logs para monitoreo técnico
if __name__ != "__main__":
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

app.logger.info("Service initialized with Talisman security headers")
