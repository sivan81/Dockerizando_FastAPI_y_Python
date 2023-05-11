## EJEMPLO FASTAPI CON PYTHON (Números primos).

### En este ejercicio de prueba, podemos probar FastAPI con Python y utilizamos Docker para ejecutar nuestra aplicación en un contenedor.

###### Lo único que necesitamos para hacer esta prueba es lo siguiente:

	- Una carpeta, en este caso llamada "app" y dentro de ella nuestro archivo "main.py".
	- El archivo "Dockerfile" para ejecutar en nuestro contenedor Docker.

### LIBRERÍAS NECESARIAS PARA UTILIZAR FASTAPI:
	- from fastapi import FastAPI 
	- from starlette.responses import RedirectResponse

### PARA DECLARAR LA APLICACIÓN Y EJECUTAR FASTAPI, NECESITAREMOS LO SIGUIENTE:

    app = FastAPI() # Declaramos la aplicación
    
    @app.get("/") # De tipo get escuchando en la raiz del proyecto
    def raiz(): # Definimos el método raiz para redireccionarnos a docs
        return RedirectResponse(url="/docs/")
    

#### El resto del código dependerá de lo que quieras realizar, en mi caso ha sido números primos.


------------



### A continuación se especifica lo que debe contener el archivo Dockerfile e incluso dentro se comenta como se debe ejecutar en Docker: (Docker Desktop debe estar en ejecución).

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

## Repositorio de solo lectura

Este repositorio es de solo lectura. No se aceptarán modificaciones directas en el repositorio original. Si deseas contribuir con mejoras o correcciones, por favor, crea una bifurcación (fork) del repositorio y trabaja en tu propia copia. Luego, puedes enviar una solicitud de extracción (pull request) para que se revisen tus cambios. Agradecemos tu interés en el proyecto y tus posibles contribuciones.
