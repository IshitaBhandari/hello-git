import tkinter as tk
import requests
from tkinter import *
from urllib.request import urlopen
from io import BytesIO
from PIL import Image, ImageTk
import datetime
from tkinter import font as tkFont
import contextlib
import json
from sys import platform as sp
import socket
import string








#print("Temperature :", temp)
#print("Speed of the wind :", wind_speed)
#print("Latitude", latitude)
#print("Longitude", longitude)
#print("Description", description)


#----------FUNCTION TO GET CITY NAME
from django.db.models.functions import window


def get_city():
    city = str(entry1.get())

    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=cf88752e07aade3f7d59bac0574cfcf2'.format(
        city)
    city_list = requests.get(current_weather_url)
    tempd = city_list.json()
    print(city_list)
    return(tempd)



def screen_contents():
    window = tk.Tk()                        #variable declared as frame
    window.title("WEATHER APP")             #title of the frame
    window.geometry('400x400')              #size of the frame

    #LABEL-------
    title = tk.Label(text="ENTER CITY", tkFont=("Times New Roman", 20))
    title.grid()                            #default 0*0

    #Entry field--------
    entry1 = tk.Entry()
    entry1.grid(column=1,row=0)

    #Button widget--------
    button1 = tk.Button(text="SHOW WEATHER")
    button1.grid(column=1,row=1)

    window.mainloop()  # acts as a function for window to pop out


def custom_heading_font(args):
    pass


def display_screen(self, master):


    data = get_city()

    #GET DATA FROM JSON------------
    city_name = data['sys']['name']

    temperature = data['main']['temp']

    temp1 = data['main']['date']
    date = datetime.datetime.fromtimestamp(int(temp1)).strftime('%Y-%m-%d %H:%M:%S')

    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    des = data['weather'][0]['main']
    description = data['weather'][0]['description']
    minimum = data['main']['temp_min']
    maximum = data['main']['temp_max']

    temp2 = data['sys']['sunrise']
    sunrise = datetime.datetime.fromtimestamp(int(temp2)).strftime('%Y-%m-%d %H:%M:%S')

    temp3 = data['sys']['sunset']
    sunset = datetime.datetime.fromtimestamp(int(temp3)).strftime('%Y-%m-%d %H:%M:%S')

    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    wind_direction = data['speed']['deg']
    cloudiness = data['clouds']['all']

    #PRINT DATA ON SCREEM---------
    label_city = Label(master, text=self.city_name, font=self.custom_heading_font)
    label_city.grid(row=0, columnspan=2, padx=4, pady=4)

    label_time = Label(master, textvariable=self.date, font=self.custom_font)
    label_time.grid(row=1, columnspan=2, padx=2, pady=2)

    self.set_weather_icon()

    Label(master, textvariable=self.temperature).grid(row=2, column=1, padx=2, pady=2)
    Label(master, textvariable=self.description).grid(row=3, column=1, padx=2, pady=2)

    #label_temp_day = Label(master, textvariable=self.t_temp_day, font=self.custom_font)
    #label_temp_day.grid(row=4, column=0, rowspan=2, padx=2, pady=2)
    Label(master, textvariable=self.minimum).grid(row=4, column=1, padx=2, pady=2)
    Label(master, textvariable=self.maximum).grid(row=5, column=1, padx=2, pady=2)

    Label(master, text="Pressure").grid(row=6, column=0, padx=2, pady=2)
    Label(master, textvariable=self.pressure).grid(row=6, column=1, padx=2, pady=2)

    Label(master, text="Humidity").grid(row=7, column=0, padx=2, pady=2)
    Label(master, textvariable=self.humidity).grid(row=7, column=1, padx=2, pady=2)

    Label(master, text="Wind Speed").grid(row=8, column=0, padx=2, pady=2)
    Label(master, textvariable=self.wind_speed).grid(row=8, column=1, padx=2, pady=2)

    Label(master, text="Wind Direction").grid(row=9, column=0, padx=2, pady=2)
    Label(master, textvariable=self.wind_direction).grid(row=9, column=1, padx=2, pady=2)

    Label(master, text="Cloudiness").grid(row=10, column=0, padx=2, pady=2)
    Label(master, textvariable=self.cloudiness).grid(row=10, column=1, padx=2, pady=2)

    #Label(master, text="Rain").grid(row=11, column=0, padx=2, pady=2)
    #Label(master, textvariable=self.t_rain).grid(row=11, column=1, padx=2, pady=2)

    self.scale_widgets(master)



#SET WEATHER ICON------------

    def set_weather_icon(self):
        with contextlib.closing(urlopen(self.t_weather_icon_url)) as raw_data:
            image = Image.open(BytesIO(raw_data.read()))
        weather_icon = ImageTk.PhotoImage(image)
        self.label_weather_icon.configure(image=weather_icon)
        self.label_weather_icon.image = weather_icon  # keep a reference
        # When a PhotoImage object is garbage-collected by Python
        # (e.g. when you return from a function which stored an image in a local variable),
        # the image is cleared even if it is being displayed by a Tkinter widget.
        # To avoid this, the program must keep an extra reference to the image object.
        self.label_weather_icon.grid(row=2, rowspan=2, column=0)




