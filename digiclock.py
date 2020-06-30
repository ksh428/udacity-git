from tkinter import *
import time
import sys

def currtime():
    timenow=time.strftime("%H:%M:%S") #gets the current time in string format
    clock.config(text=timenow) #.config is used to update any widget
    clock.after(200,currtime)

root=Tk()
root.geometry("250x100")
clock=Label(root,font=("times",50,"bold"),bg="black",fg="#00ffff")
clock.pack()
currtime()

root.mainloop()

