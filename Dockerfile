# Definimos dos línas, una para descargar la imagen necesaria de FastAPI
# Y la otra para indicar de qué directorio va a tomar la información

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY ./app /app

# A continuación debemos escribir en el terminal el nombre de la imagen. En este caso será esta.
# docker build -t fastapipropio .

# Después de esto, ejecutamos en nuestro contenedor en background de la siguiente manera
# docker run -d --name fastapicontainer -p 80:80 fastapipropio
# correrá en el puerto 80 y windows te pedirá permitir.

# Ya en el navegador, podrá verse en ejecución (siempre con Docker desktop ejecutando) en la siguiente dirección:
# 127.0.0.1/docs

