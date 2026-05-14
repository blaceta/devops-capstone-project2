# Usar una imagen base de Python ligera para mayor eficiencia
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de dependencias primero para aprovechar la caché de capas de Docker
COPY requirements.txt .

# Instalar dependencias de producción
# --no-cache-dir reduce el tamaño final de la imagen
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código fuente del microservicio
COPY service/ ./service/

# Crear un usuario no raíz por seguridad (Principio de menor privilegio)
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Exponer el puerto en el que corre la aplicación Flask
EXPOSE 8080

# Comando para iniciar el servidor de producción Gunicorn
# Se configuran los workers para manejar la concurrencia de forma eficiente
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--log-level", "info", "service:app"]
