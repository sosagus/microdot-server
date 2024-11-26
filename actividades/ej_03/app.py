# Aplicacion del servidor

from boot import do_connect
from microdot import Microdot, send_file
from machine import Pin, PWM, ADC
import time
import ds18x20
import onewire

app = Microdot()

led1 = Pin(32, Pin.OUT)
led2 = Pin(33, Pin.OUT)
led3 = Pin(25, Pin.OUT)
buzzer = Pin(14, Pin.OUT)
ds_pin = Pin(15)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
tempCelsius = 24

do_connect()

@app.route('/')
async def index(request):
    return send_file('index.html')

@app.route('/<dir>/<file>')
async def static(request, dir, file):
    return send_file("/{}/{}".format(dir, file))

@app.route('/toggle/led/<int:id>')
async def index(request, id):
    if id == 1:
        led1.value(not led1.value())
    elif id == 2:
        led2.value(not led2.value())
    elif id == 3:
        led3.value(not led3.value())
    return 'OK'

@app.route('/sensors/ds18b20/read')
async def temperature_measuring(request):
    global ds_sensor
    ds_sensor.convert_temp()
    time.sleep_ms(1)
    roms = ds_sensor.scan()
    for rom in roms:
        tempCelsius = ds_sensor.read_temp(rom)
    json = {'temperature': tempCelsius};
    return json

@app.route('/setpoint/set/<int:value>')
async def setpoint_calculation(request, value):
    json = {}
    print("Calculate setpoint")
    if value >= tempCelsius:
        buzzer.on()
        json = {'buzzer': 'On'}
    else:
        buzzer.off()
        json = {'buzzer': 'Off'}
    return json

app.run(port=80)