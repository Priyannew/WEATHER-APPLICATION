from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

master = Tk()

master.title("WEATHER APPLICATION")
master.geometry("900x500+300+200")
#image = PhotoImage(file = "C:/Users/ELCOT/Desktop/MINI_PROJECT BASED ON PYTHON/WEATHER_APP/wea.png")
#bakground_label = Label(master,image=image)
#bakground_label.place(x=0,y=0,relwidth=1,relheight=1)

def getweather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    #weather app
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c812773c5420b7abaf6968a3fc32a37f"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(temp,"°"))
    c.config(text=(condition,'|',"FEELS","LIKE",temp,""))

    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)





    

#search bar
search_bar = PhotoImage(file="D:\MINI_PROJECT BASED ON PYTHON\WEATHER_APP/Copy of search.png")
my_image = Label(image=search_bar)
my_image.place(x=20,y=20)

textfield = Entry(master,justify = "center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus

search_icon = PhotoImage(file="D:\MINI_PROJECT BASED ON PYTHON\WEATHER_APP/Copy of search_icon.png")
myimage_icon = Button(image = search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getweather)
myimage_icon.place(x=400,y=34)

#logo
logo_img =PhotoImage(file="D:\MINI_PROJECT BASED ON PYTHON\WEATHER_APP\Copy of logo.png")
logo = Label(image=logo_img)
logo.place(x=150,y=100)

#Bottom box
frame_img = PhotoImage(file = "Copy of box.png")
frame_myimg = Label(image = frame_img)
frame_myimg.pack(padx=5,pady=5,side=BOTTOM)

#time
name = Label(master,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock = Label(master,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
label1 = Label(master,text="WIND",font=("helvetica",15,'bold'),fg='white',bg="#1ab5ef")
label1.place(x=120,y=400)

label1 = Label(master,text="HUMIDITY",font=("helvetica",15,'bold'),fg='white',bg="#1ab5ef")
label1.place(x=250,y=400)


label1 = Label(master,text="DESCCRIPTION",font=("helvetica",15,'bold'),fg='white',bg="#1ab5ef")
label1.place(x=430,y=400)

label1 = Label(master,text="PRESSURE",font=("helvetica",15,'bold'),fg='white',bg="#1ab5ef")
label1.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)

w=Label(text="......",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="......",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="......",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="......",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)



master.mainloop()
