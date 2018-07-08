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

# print("Temperature :", temp)
# print("Speed of the wind :", wind_speed)
# print("Latitude", latitude)
# print("Longitude", longitude)
# print("Description", description)


# ----------FUNCTION TO GET CITY NAME
from django.db.models.functions import window


class weather():
    def __init__(self, master, city):
        weather_frame = Frame(master)
        weather_frame.grid(row=0)
        self.custom_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
        self.custom_heading_font = tkFont.Font(family="Helvetica", size=14, weight="bold")
        self.city_name = StringVar()
        self.temperature = StringVar()
        self.temp1 = StringVar()
        self.date = StringVar()
        self.longitude = StringVar()
        self.latitude = StringVar()
        self.current_weather_url = None
        self.des = StringVar()
        self.description = StringVar()
        self.minimum = StringVar()
        self.maximum = StringVar()
        self.temp2 = StringVar()
        self.sunrise = StringVar()
        self.temp3 = StringVar()
        self.sunset = StringVar()
        self.pressure = StringVar()
        self.humidity = StringVar()
        self.wind_speed = StringVar()
        self.wind_direction = StringVar()
        self.cloudiness = StringVar()

        self.label_weather_icon = Label(weather_frame)

        self.display_screen(weather_frame, city)
        print("done")

    def display_screen(self, master, city):
        print(city)
        self.current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=cf88752e07aade3f7d59bac0574cfcf2'.format(
            city)

        self.city_list = requests.get(self.current_weather_url)

        self.data = self.city_list.json()

        print(self.city_list)
        print(self.data)


        # GET DATA FROM JSON------------

        self.city_name = self.data['name']


        self.temperature = self.data['main']['temp']
        print(self.temperature)

        self.temp1 = self.data['date']
        print(self.temp1)
        self.date = datetime.datetime.fromtimestamp(int(self.temp1)).strftime('%Y-%m-%d %H:%M:%S')
        print(self.date)

        self.latitude = self.data['coord']['lat']
        self.longitude = self.data['coord']['lon']
        self.des = self.data['weather'][0]['main']
        self.description = self.data['weather'][0]['description']
        self.minimum = self.data['main']['temp_min']
        self.maximum = self.data['main']['temp_max']

        self.temp2 = self.data['sys']['sunrise']
        self.sunrise = datetime.datetime.fromtimestamp(int(self.temp2)).strftime('%Y-%m-%d %H:%M:%S')

        self.temp3 = self.data['sys']['sunset']
        self.sunset = datetime.datetime.fromtimestamp(int(self.temp3)).strftime('%Y-%m-%d %H:%M:%S')

        self.pressure = self.data['main']['pressure']
        self.humidity = self.data['main']['humidity']
        self.wind_speed = self.data['wind']['speed']
        self.wind_direction = self.data['speed']['deg']
        self.cloudiness = self.data['clouds']['all']

        # PRINT DATA ON SCREEM---------
        label_city = Label(master, text=self.city_name, font=self.custom_heading_font)
        label_city.grid(row=0, columnspan=2, padx=4, pady=4)

        label_time = Label(master, textvariable=self.date, font=self.custom_font)
        label_time.grid(row=1, columnspan=2, padx=2, pady=2)

        self.set_weather_icon()

        Label(master, textvariable=self.temperature).grid(row=2, column=1, padx=2, pady=2)
        Label(master, textvariable=self.description).grid(row=3, column=1, padx=2, pady=2)

        # label_temp_day = Label(master, textvariable=self.t_temp_day, font=self.custom_font)
        # label_temp_day.grid(row=4, column=0, rowspan=2, padx=2, pady=2)
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

        # Label(master, text="Rain").grid(row=11, column=0, padx=2, pady=2)
        # Label(master, textvariable=self.t_rain).grid(row=11, column=1, padx=2, pady=2)

        self.scale_widgets(master)

        # scale the widgets with the master window
        def scale_widgets(master):
            master.columnconfigure(0, weight=1)
            master.columnconfigure(1, weight=1)
            master.rowconfigure(0, weight=1)
            master.rowconfigure(1, weight=1)
            master.rowconfigure(2, weight=1)
            master.rowconfigure(3, weight=1)
            master.rowconfigure(4, weight=1)
            master.rowconfigure(5, weight=1)
            master.rowconfigure(6, weight=1)
            master.rowconfigure(7, weight=1)
            master.rowconfigure(8, weight=1)
            master.rowconfigure(9, weight=1)
            master.rowconfigure(10, weight=1)
            master.rowconfigure(11, weight=1)
            master.rowconfigure(12, weight=1)

    # SET WEATHER ICON------------

    def set_weather_icon(self):
        with contextlib.closing(urlopen('"http://openweathermap.org/img/w/%s.png" % t_weather_icon')) as raw_data:
            image = Image.open(BytesIO(raw_data.read()))
            weather_icon = ImageTk.PhotoImage(image)
            self.label_weather_icon.configure(image=weather_icon)
            self.label_weather_icon.image = weather_icon
            self.label_weather_icon.grid(row=2, rowspan=2, column=0)



def show():
    city = entry_city.get()
    print(city)
    for child in content_frame.winfo_children():
        child.destroy()
    weather(content_frame, city)


root = Tk()
root.wm_title("Sunshine")
font = tkFont.Font(family="Helvetica", size=10)

top_frame = Frame(root)
top_frame.grid(row=0, columnspan=2, padx=4, pady=4)

Label(top_frame, text="City", font=font).grid(row=0, column=0, sticky="W", padx=4, pady=4)

entry_city = Entry(top_frame, font=font)
entry_city.grid(row=0, column=1, padx=4, pady=4)
entry_city.focus_set()

content_frame = Frame(root)
content_frame.grid(row=1, columnspan=2)

button_city = Button(top_frame, text="Show Weather", command=show, font=font, relief=GROOVE)
button_city.grid(row=1, columnspan=2, padx=4, pady=4)

root.update()
root.minsize(200, root.winfo_height())
root.bind("<Return>", lambda x: show())  # INVOKE FUNCTION ON PrESSING ENTER

# scaling
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

root.mainloop()
