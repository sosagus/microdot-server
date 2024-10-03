# Aplicacion del servidor
from microdot import Microdot, send_file # Importamos la clase Microdot y la función send_file
from machine import Pin, PWM # Importamos las clases Pin y PWM
import time


app = Microdot() # Instanciamos la clase Microdot

LED1 = Pin(32, Pin.OUT) # Definimos el pin 32 como salida
LED2 = Pin(33, Pin.OUT) # Definimos el pin 33 como salida
LED3 = Pin(25, Pin.OUT) # Definimos el pin 25 como salida

# Definimos la ruta raíz
@app.route('/')
async def index(request):
    return send_file('index.html')




@app.route('/<dir>/<file>') # Definimos la ruta con dos parámetros
async def index(request, dir, file):
    return send_file("/" + dir + "/" + file) # Cambiamos el nombre del archivo a enviar



@app.route('/toggle/led/<int:id>') # Definimos la ruta con un parámetro entero
async def index(request, id):

    # Dependiendo del valor del parámetro id, encendemos o apagamos un LED
    if id == 1:
        LED1.value(not LED1.value())

    elif id == 2:
        LED2.value(not LED2.value())

    elif id == 3:
        LED3.value(not LED3.value())

    return 'OK'

# Corremos el servidor creado en el puerto 80
app.run(port=80)