from fastapi import FastAPI # Primero se debe instalar para poder importar: pip install fastapi[all] (instalar en terminal)
from starlette.responses import RedirectResponse # importamos esta librería

app = FastAPI() # Declaramos la aplicación

@app.get("/") # De tipo get escuchando en la raiz del proyecto
def raiz(): # Definimos el método raiz para redireccionarnos a docs
    return RedirectResponse(url="/docs/")


@app.get("/validar/{numero}")
def es_primo(numero: int):
    # Función que maneja la solicitud GET en la ruta "/validar/{numero}"
    if numero < 2:
        # Si el número es menor a 2, no es primo
        respuesta = "Los números menores a 2 no son primos."
    else:
        # Si el número es mayor o igual a 2, se verifica si es primo llamando a la función is_prime()
        respuesta = "El número es primo." if is_prime(numero) else "El número no es primo."
        
    return {
        "numero": numero,
        "validacion": respuesta
    }

def is_prime(numero):
    # Función que verifica si un número es primo o no
    for i in range(2, int(numero ** 0.5) + 1):
        # Itera desde 2 hasta la raíz cuadrada del número (ambos inclusive)
        if numero % i == 0:
            # Si el número es divisible entre algún valor del bucle, no es primo
            return False
    # Si el bucle completa todas las iteraciones sin encontrar un divisor, el número es primo
    return True