import tkinter as tk 
import requests
import time

def getWeather(kill):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=1b3c74467ca0dcf8f87ec9025ce21b4b"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273 )
    min_temp = int(json_data['main']['temp_min'] - 273.15 )
    max_temp = int(json_data['main']['temp_max'] - 273.15 )
    pressure = json_data['main']['pressure']
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] -21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] -21600))
    
    hd = condition + "\n" + str(temp) + "°C"
    dt = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp)  + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    
    label.config()
    label1.config(text= hd)
    label2.config(text= dt)

kill = tk.Tk()
kill.title("weather")
kill.geometry("600x700")

g = ("Impact", 20)
h = ("Arial", 20, "bold")

label = tk.Label(kill, text ="\n Enter City to find Weather Reports", font = g)
label.pack()
textfield = tk.Entry(kill,justify= "center", font=h)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(kill,  font = g)
label1.pack()
label2 = tk.Label(kill,  font = h)
label2.pack()
kill.mainloop()
