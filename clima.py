
from flask import Flask, render_template, request, redirect, url_for
import requests, datetime
app = Flask(__name__)

@app.route('/clima', methods = ['POST'])
def clima():
    Nombre= request.form["nombre"]
    Apellido= request.form["Apellido"]
    Pais= request.form["Pais"]
    Ciudad= request.form["Ciudad"]
    inf = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+Ciudad+'&appid=66ff3b85e59c2b2ba47b9d1545791f81').json()
    temperaturacen = str(inf['main']['temp'] - 273.15)
    sensasion = str(inf['main']['feels_like'] - 273.15)
    minsen = str(inf['main']['temp_min'] - 273.15)
    maxsen = str(inf['main']['temp_max'] - 273.15)
    humedad = str(inf['main']['humidity'])
    presion = str(inf['main']['pressure'])
    amanecer = str(datetime.datetime.fromtimestamp(inf['sys']['sunrise']).strftime("%I:%M %p"))
    Atardecer = str(datetime.datetime.fromtimestamp(inf['sys']['sunset']).strftime("%I:%M %p"))
    texto = ("Hola "+Nombre+" "+Apellido+", estás son las condiciones para "+Ciudad+", "+Pais+": "+"\n Temperatura: "+temperaturacen+ 
    "\n Sensacion termica: "+sensasion+"\n Temperatura minima: "+minsen+"\n Temperatura maxima: "+maxsen+"\n Humedad: "+humedad+
    "\n Presion: "+presion+"\n Amanecer: "+amanecer+"\n Atardecer: "+Atardecer)
    return texto
 


@app.route('/rutainicial')
def ruta():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
