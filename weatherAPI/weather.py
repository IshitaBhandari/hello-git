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
        if city != "":
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
            self.rain = StringVar()

            self.label_weather_icon = Label(weather_frame)
            self.t_weather_icon_url = Label(weather_frame)

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
        print(self.city_name)

        self.temperature = self.data['main']['temp']

        self.temp1 = self.data['dt']
        self.date = datetime.datetime.fromtimestamp(int(self.temp1)).strftime('%Y-%m-%d %H:%M:%S')
        print(self.date)

        self.latitude = self.data['coord']['lat']
        print(self.latitude)
        self.longitude = self.data['coord']['lon']
        print(self.longitude)
        self.des = self.data['weather'][0]['main']
        print(self.des)
        self.description = self.data['weather'][0]['description']
        print(self.description)
        self.minimum = self.data['main']['temp_min']
        print(self.minimum)
        self.maximum = self.data['main']['temp_max']
        print(self.maximum)

        self.temp2 = self.data['sys']['sunrise']
        self.sunrise = datetime.datetime.fromtimestamp(int(self.temp2)).strftime('%Y-%m-%d %H:%M:%S')
        print(self.sunrise)

        self.temp3 = self.data['sys']['sunset']
        self.sunset = datetime.datetime.fromtimestamp(int(self.temp3)).strftime('%Y-%m-%d %H:%M:%S')
        print(self.sunset)

        self.pressure = self.data['main']['pressure']
        print(self.pressure)
        self.humidity = self.data['main']['humidity']
        print(self.humidity)
        self.wind_speed = self.data['wind']['speed']
        print(self.wind_speed)
        self.wind_direction = self.data['wind']['deg']
        print(self.wind_direction)
        self.cloudiness = self.data['clouds']['all']
        print(self.cloudiness)

        if 'rain' in self.city_list:
            self.rain.set("%0.2f mm" % self.city_list['rain'])
        else:
            self.rain.set("No rain today.")

        # PRINT DATA ON SCREEM---------
        label_city = Label(master, text=self.city_name, font=self.custom_heading_font)
        label_city.grid(row=0, columnspan=2, padx=2, pady=2)

        label_time = Label(master, text=self.date, font=self.custom_heading_font)
        label_time.grid(row=1, columnspan=2, padx=2, pady=2)

        label_time = Label(master, text='Temperature', font=self.custom_font)
        label_time.grid(row=2, column=0, padx=2, pady=2)
        label_temp = Label(master, text=self.temperature, font=self.custom_font)
        label_temp.grid(row=2, column=2, padx=2, pady=2)

        label_des = Label(master, text=self.des, font=self.custom_font)
        label_des.grid(row=3, column=0, padx=2, pady=2)
        label_desc = Label(master, text=self.description, font=self.custom_font)
        label_desc.grid(row=3, column=2, padx=2, pady=2)

        # label_temp_day = Label(master, textvariable=self.t_temp_day, font=self.custom_font)
        # label_temp_day.grid(row=4, column=0, rowspan=2, padx=2, pady=2)
        label_time = Label(master, text='Minimum Temperature')
        label_time.grid(row=4, column=0, padx=2, pady=2)
        label_min = Label(master, text=self.minimum)
        label_min.grid(row=4, column=2, padx=2, pady=2)

        label_time = Label(master, text='Maximum Temperature')
        label_time.grid(row=5, column=0, padx=2, pady=2)
        label_max = Label(master, text=self.maximum)
        label_max.grid(row=5, column=2, padx=2, pady=2)

        label_time = Label(master, text='Pressure')
        label_time.grid(row=6, column=0, padx=2, pady=2)
        label_time = Label(master, text=self.pressure)
        label_time.grid(row=6, columnspan=5, padx=2, pady=2)

        label_time = Label(master, text='Humidity')
        label_time.grid(row=7, column=0, padx=4, pady=4)
        label_time = Label(master, text=self.humidity)
        label_time.grid(row=7, columnspan=5, padx=4, pady=4)

        label_time = Label(master, text='Wind Speed')
        label_time.grid(row=8, column=0, padx=4, pady=4)
        label_time = Label(master, text=self.wind_speed)
        label_time.grid(row=8, columnspan=5, padx=4, pady=4)

        label_time = Label(master, text='Wind Direction')
        label_time.grid(row=9, column=0, padx=4, pady=4)
        label_time = Label(master, text=self.wind_direction)
        label_time.grid(row=9, columnspan=5, padx=4, pady=4)

        label_time = Label(master, text='Cloudiness')
        label_time.grid(row=10, column=0, padx=4, pady=4)
        label_time = Label(master, text=self.cloudiness)
        label_time.grid(row=10, columnspan=5, padx=4, pady=4)

        label_time = Label(master, text='Rain')
        label_time.grid(row=11, column=0, padx=4, pady=4)
        Label(master, textvariable=self.rain).grid(row=11, column=1, padx=2, pady=2)

        self.scale_widgets(master)

        # scale the widgets with the master window
        def scale_widgets(masterone):
            masterone.columnconfigure(0, weight=1)
            masterone.columnconfigure(1, weight=1)
            masterone.rowconfigure(0, weight=1)
            masterone.rowconfigure(1, weight=1)
            masterone.rowconfigure(2, weight=1)
            masterone.rowconfigure(3, weight=1)
            masterone.rowconfigure(4, weight=1)
            masterone.rowconfigure(5, weight=1)
            masterone.rowconfigure(6, weight=1)
            masterone.rowconfigure(7, weight=1)
            masterone.rowconfigure(8, weight=1)
            masterone.rowconfigure(9, weight=1)
            masterone.rowconfigure(10, weight=1)
            masterone.rowconfigure(11, weight=1)
            masterone.rowconfigure(12, weight=1)

    # SET WEATHER ICON------------


def show():
    city = entry_city.get()
    print(city)
    for child in content_frame.winfo_children():
        child.destroy()
    weather(content_frame, city)


root = Tk()
root.wm_title("Sunshine")
degree_sign = u'\N{DEGREE SIGN}'
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
