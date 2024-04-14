from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

###### COLLECTIONS

codes = { 
    "01d" : "clear_sky.jpg" ,                                           # Do 18 kodów zawartych w każdej odpowiedzi API 
    "01n" : "clear_sky.jpg" ,                                           # jest przypisana reszta (paredziesiąt) możliwych 
    "02d" : "few_clouds.jpg" ,                                          # stanów pogodowych. Ogranicza to liczbę potrzebnych 
    "02n" : "few_clouds.jpg" ,                                          # obrazków do 9. 
    "03d" : "scattered_clouds.jpg" ,                                    # # https://openweathermap.org/weather-conditions
    "03n" : "scattered_clouds.jpg" ,                                    # Przywiązanie nazwy pliku do kodu za pomocą słownika
    "04d" : "broken_clouds.jpg" ,                                       # jest prostym sposobem na uzupełnienie zmiennej  
    "04n" : "broken_clouds.jpg" ,                                       # adresu w szablonie HTML.
    "09d" : "shower_rain.jpg" , 
    "09n" : "shower_rain.jpg" , 
    "10d" : "rain.jpg" , 
    "10n" : "rain.jpg" , 
    "11d" : "thunderstorm.jpg" , 
    "11n" : "thunderstorm.jpg" , 
    "13d" : "snow.jpg" , 
    "13n" : "snow.jpg" , 
    "50d" : "mist.jpg" ,
    "50n" : "mist.jpg"
    }

###### API                                                              # w zrozumieniu zmiennych w tej sekcji może pomóc 
                                                                        # przeczytanie pliku "weatherapp/surowe.txt"
# Api Key
#    8a06d7c3e87f1ec748a21ec17a8e24d0                                   # Max 60 wywołań API na minutę, 1000 na dzień, 1,000,000 na miesiąc. 

api_call = 'https://api.openweathermap.org/data/2.5/weather?q=Lublin,PL&appid=8a06d7c3e87f1ec748a21ec17a8e24d0&lang=pl&units=metric' #https://openweathermap.org/current

json_response = urllib.request.urlopen(api_call).read()                 # https://docs.python.org/3/library/urllib.request.html 
response = json.loads(json_response)                                    # Funkcja json.loads() zmienia format json na pythonowy dziennik. 
    
main_weather = response['weather'][0]                                   # Wyciąganie potrzebnych informacji z dziennika. 
main_weather_description = main_weather['description']
main_weather_code = main_weather["icon"]

image_path = codes[main_weather_code]                                   # Przywiązanie kodu pogodowego z API do ścieżki do 
                                                                        # pasującego do pogody zdjęcia. 
secondary_weather = response['main']                                    
temperature = secondary_weather['temp']                                 # Wyciąganie dodatkowych informacji z dziennika.
temperature_felt = secondary_weather['feels_like']
pressure = secondary_weather['pressure'] 
humidity = secondary_weather['humidity'] 

###### ROUTES

@app.route('/')
def home():
    return render_template(
        'home.html' , 
        main_weather_description = main_weather_description ,           # Przesłanie zmiennych do szablonu html. 
        image = image_path)

@app.route('/details')
def details():
    return render_template(
        'details.html' , 
        main_weather_description = main_weather_description ,           # Przesłanie zmiennych opisujących dodatkowe cechy
        image = image_path ,                                            # pogodowe do szablonu html. 
        temperature = temperature , 
        temperature_felt = temperature_felt , 
        pressure = pressure ,
        humidity = humidity
        )

###### RUN LOOP

if __name__ == '__main__':
    app.run(debug=True)