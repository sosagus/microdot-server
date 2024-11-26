function leer_temp() {
    fetch('/sensors/ds18b20/read')
        .then(response => response.json())
        .then(json => {
            document.querySelector('#temp').innerText = json.temperature;
        })
        .catch(error => console.error('No se pudo leer la temperatura:', error));
}

function enviar_temp() {
    let temperature_slider_value = parseInt(document.querySelector('#temperature-slider').value);
    fetch(`/setpoint/set/${temperature_slider_value}`)
        .then(response => response.json())
        .then(json => {
            document.querySelector('#buzzer-state').innerText = json.buzzer;
        })
        .catch(error => console.error('No se pudo leer la temperatura:', error));
}

function update_temp(value) {
    document.getElementById('temperature_slider_value').innerText = value;
    enviar_temp();
}

setInterval(leer_temp, 500);