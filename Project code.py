# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 13:30:30 2020

@author: joshu
"""
import tkinter as tk   # python3
from PIL import ImageTk, Image
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import math
import tkinter.font as tkFont

f = plt.figure(figsize=(5,4), dpi=100)
f = plt.figure()
a = f.add_subplot(111)

x_len = 200         # Number of points to display
y_range = [-3, 3.5]  # Range of possible Y values to display

#create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

#create the digital chip
cs = digitalio.DigitalInOut(board.D22)

#creating the MCP object
mcp = MCP.MCP3008(spi,cs)

#create hte analog input channel on pin 0
chan0 = AnalogIn(mcp, MCP.P0)
chan1 = AnalogIn(mcp, MCP.P1)
chan2 = AnalogIn(mcp, MCP.P2)
chan3 = AnalogIn(mcp, MCP.P3)
chan4 = AnalogIn(mcp, MCP.P4)
chan5 = AnalogIn(mcp, MCP.P5)
chan6 = AnalogIn(mcp, MCP.P6)
chan7 = AnalogIn(mcp, MCP.P7)

def calcCOM(x):
    ComX = 0
    ComY = 0
    i = 0
    alphaX = 0 #alpha = m1*d1+m2*d2+m3d3+etc
    alphaY = 0 #alpha = m1*d1+m2*d2+m3d3+etc
    beta = 0#beta is m1+m2+m3
    while i < len(x[0]):
        alphaX = (x[0][i] * x[2][i]) + alphaX
        alphaY = (x[1][i] * x[2][i]) + alphaY
        beta = x[2][i] + beta
        i = i + 1
    ComX = alphaX / beta
    ComY = alphaY / beta
    return ComX, ComY

def animate(i):
    a.cla()
    xlist = [0,0,0,.2,5.5,5.5,6,6.5]
    ylist = [0,6.5,11.5,18.5,0,6.5,11.5,18.5]
    # Read voltage from TMP102
    voltage0 = chan0.voltage
    voltage1 = chan1.voltage
    voltage2 = chan2.voltage
    voltage3 = chan3.voltage
    voltage4 = chan4.voltage
    voltage5 = chan5.voltage
    voltage6 = chan6.voltage
    voltage7 = chan7.voltage
    print("voltage0a = ", voltage0)
    print("voltage1a = ", voltage1)
    print("voltage2a = ", voltage2)
    print("voltage3a = ", voltage3)
    print("voltage4a = ", voltage4)
    print("voltage5a = ", voltage5)
    print("voltage6a = ", voltage6)
    print("voltage7a = ", voltage7) 
    
    voltage0 = voltage0 - 1.54
    voltage1 = voltage1 - 1.54
    voltage2 = voltage2 - 1.54
    voltage3 = voltage3 - 1.54
    voltage4 = voltage4 - 1.54
    voltage5 = voltage5 - 1.54
    voltage6 = voltage6 - 1.64
    voltage7 = voltage7 - 1.54
    print("voltage6b = ", voltage6) 
    
    print("voltage6c = ", voltage6)
    
    voltage0 = 1 + voltage0 ** 10
    voltage1 = 1 + voltage1 ** 10
    voltage2 = 1 + voltage2 ** 10
    voltage3 = 1 + voltage3 ** 10
    voltage4 = 1 + voltage4 ** 10
    voltage5 = 1 + voltage5 ** 10
    voltage6 = 1 + voltage6 ** 10
    voltage7 = 1 + voltage7 ** 10
    print("voltage6d = ", voltage6) 
    # Update line with new Y values
    size = [voltage0, voltage1,voltage2,voltage3,voltage4,voltage5,voltage6,voltage7]
    shoe1 = [xlist, ylist, size]
    x = calcCOM(shoe1)
    a.scatter(xlist, ylist, s = size,vmax = 5)
    a.scatter(x[0],x[1])
    plt.xlim(-1,20)
    plt.ylim(-1,20)
    plt.title("Yellow Dot = Center of Mass")
    
    
class SampleApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs) 
        container = tk.Frame(parent)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, DevelopersPage, gaitInfoPage, gaitTestPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.winfo_toplevel().title("TaiChi")
        self.show_frame("StartPage")
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
    def SaveInfo(self, param2,param3,param4,param5,param6,page_name):
        global FirstName
        global LastName
        global Weight
        global Height
        global Gender
        FirstName = param2
        LastName = param3
        Weight = param4
        Height = param5
        frame = self.frames[page_name]
        frame.tkraise()
        
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=" ") # Added
        label.pack()
        label = tk.Label(self ,text="Tai Chi Balance Mat") # Added
        label.pack()
        label = tk.Label(self, text=" ") # Added
        label.pack()
        label = tk.Label(self, text=" ") # Added
        label.pack()
        label = tk.Label(self, text=" ") # Added
        label.pack()
        button1 = tk.Button(self, text="View Developers", command=lambda: controller.show_frame("DevelopersPage"))
        button2 = tk.Button(self, text="Gait Testing", command=lambda: controller.show_frame("gaitInfoPage"))
        button1.pack()
        label = tk.Label(self, text=" ") # Added
        label.pack()
        button2.pack()

class DevelopersPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Developers") # Added
        label.pack()
        label = tk.Label(self, text=" ") # Added
        label.pack()
        label = tk.Label(self, text="Riley Sherwood") # Added
        label.pack()
        label = tk.Label(self, text="Joshua Gogolin") # Added
        label.pack()
        label = tk.Label(self, text="Aarom Lim") # Added
        label.pack()
        label = tk.Label(self, text="Scott Murray") # Added
        label.pack()
        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        button.pack()

class gaitInfoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        e1 = tk.Entry(self)
        e2 = tk.Entry(self)
        e3 = tk.Entry(self)
        e4 = tk.Entry(self)
        e5 = tk.Entry(self)
        label = tk.Label(self, text="Gait Info Page") # Added
        label.pack()
        label = tk.Label(self, text=" ") # Added
        label.pack()
        label = tk.Label(self, text="First Name") # Added
        label.pack()
        e1.pack()
        label = tk.Label(self, text="Last Name") # Added
        label.pack()
        e2.pack()
        label = tk.Label(self, text="Weight") # Added
        label.pack()
        e3.pack()
        label = tk.Label(self, text="Height") # Added
        label.pack()
        e4.pack()
        label = tk.Label(self, text="Gender") # Added
        label.pack()
        e5.pack()
        label = tk.Label(self, text=" ") # Added
        label.pack()
        button2 = tk.Button(self, text="Press to save",command=lambda: controller.SaveInfo(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),("gaitTestPage")))
        button2.pack()
        

class gaitTestPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="gait Test Page") # Added
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"))
        button.pack()
        canvas = FigureCanvasTkAgg(f, self)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk() #Added
    app = SampleApp(root) #added root
    ani = animation.FuncAnimation(f,
        animate,
        interval=50,
        )
    root.mainloop()

print(FirstName)
print(LastName)
