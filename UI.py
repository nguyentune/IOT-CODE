import time
print("UI Start")

import tkinter  as tk
from tkinter import *

window = tk.Tk()
window.attributes('-fullscreen',False)
window.title("IOT project")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
print("Size:", screen_width, screen_height)


labelAMONIAValue = tk.Label(text="5.12",
                                    fg="#FF0000",
                                    justify=CENTER,
                                    font="Helvetica 60 bold")

labelAMONIAValue.place(x=0, y=200, width=screen_width / 3, height=100)

labelAMONIA = tk.Label(text="NH3",
                                    fg="#0000ff",
                                    justify=CENTER,
                                    font="Helvetica 60 bold")

labelAMONIA.place(x=0, y=100, width=screen_width / 3, height=100) 

labelTDSValue = tk.Label(text="20",
                                 fg="#FF0000",
                                 justify=CENTER,
                                  #bg = "#333",
                                 font="Helvetica 60 bold")

labelTDSValue.place(x=screen_width / 3, y=200, width=screen_width / 3, height=100)

labelTDS = tk.Label(text="TDS",
                                 fg="#0000ff",
                                 justify=CENTER,
                                  #bg = "#333",
                                 font="Helvetica 60 bold")

labelTDS.place(x=screen_width / 3, y=100, width=screen_width / 3, height=100)

labelPHValue = tk.Label(text="7.11",
                                fg="#FF0000",
                                justify=CENTER,
                                font="Helvetica 60 bold")

labelPHValue.place(x=2 * screen_width / 3, y=200, width=screen_width / 3, height=100)

labelPH = tk.Label(text="PH",
                                fg="#0000ff",
                                justify=CENTER,
                                font="Helvetica 60 bold")

labelPH.place(x=2 * screen_width / 3, y=100, width=screen_width / 3, height=100)


labelIOTs = tk.Label(text="IOT Project",
                                fg="#000000",
                                justify=CENTER,
                                font="TimesNewRoman 30 bold")

labelIOTs.place(x= screen_width / 3, y=0, width=screen_width / 3, height=100)



ButtonON = tk.Button(text="BAT",
                                fg="#0000ff",
                                justify=CENTER,
                                bg = "#333",
                                font="Helvetica 60 bold")

ButtonON.place(x=200, y=400, width=350, height=100)

ButtonOFF = tk.Button(text="TAT",
                                fg="#0000ff",
                                justify=CENTER,
                                bg = "#333",
                                font="Helvetica 60 bold")

ButtonOFF.place(x=1000, y=400, width=350, height=100)

labelLED2 = tk.Label(text="LED2",
                                fg="#33FF33",
                                justify=CENTER,
                                font="Geneva 60 bold")
labelLED2.place(x=1000, y=500, width=350, height=100)

labelLED1 = tk.Label(text="LED1",
                                fg="#33FF33",
                                justify=CENTER,
                                font="Geneva 60 bold")
labelLED1.place(x=200, y=500, width=350, height=100)

# def nut_nhan_1():
#     print("ON")
    
# def nut_nhan_2():
#     print("OFF")
    
# ButtonON.config(command=nut_nhan_1)
# ButtonOFF.config(command=nut_nhan_2)    
while True:
    window.update()
    time.sleep(0.1)