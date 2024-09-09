# Aplicacion del servidor
from microdot import Microdot, send_file

app = Microdot()

@app.route('/')
async def index(request):
    return send_file('index.html')

@app.route('/<dir>/<file>')
async def index(request, dir, file):
    return send_file("/{}/{}".format(dir, file))

@app.route('/<img>')
async def index(request, img):
    return send_file("/{}".format(img))

app.run(port=80)