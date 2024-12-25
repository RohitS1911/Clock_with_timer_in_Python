from tkinter import *
from tkinter.ttk import *
from time import strftime
import os
from pygame import mixer
import threading
import time

root = Tk()
root.title("Clock & Alarm")

def time_display():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time_display)

label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor="center")

def set_alarm():
    try:
        hours = int(hours_var.get())
        minutes = int(minutes_var.get())
        seconds = int(seconds_var.get())
        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError("Time cannot be negative.")
        total_seconds = hours * 3600 + minutes * 60 + seconds
        threading.Thread(target=alarm, args=(total_seconds,)).start()
        alarm_status.set(f"Alarm set for {hours:02}:{minutes:02}:{seconds:02}.")
    except ValueError as e:
        alarm_status.set(f"Error: {e}")

def alarm(seconds):
    mixer.init()
    time_elapsed = 0
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
    try:
        sound_path = os.path.join("C:\\Rohit\\Projects\\Alarm\\Sound.mp3")
        mixer.music.load(sound_path)
        mixer.music.play()
        alarm_status.set("Alarm ringing!")
    except Exception as e:
        alarm_status.set(f"Error playing sound: {e}")

frame = Frame(root)
frame.pack(pady=20)

hours_var = StringVar(value="0")
minutes_var = StringVar(value="0")
seconds_var = StringVar(value="0")
alarm_status = StringVar(value="Set alarm time and press Start.")

Label(frame, text="Hours:").grid(row=0, column=0, padx=5)
Entry(frame, textvariable=hours_var, width=5).grid(row=0, column=1, padx=5)
Label(frame, text="Minutes:").grid(row=0, column=2, padx=5)
Entry(frame, textvariable=minutes_var, width=5).grid(row=0, column=3, padx=5)
Label(frame, text="Seconds:").grid(row=0, column=4, padx=5)
Entry(frame, textvariable=seconds_var, width=5).grid(row=0, column=5, padx=5)
Button(frame, text="Start Alarm", command=set_alarm).grid(row=0, column=6, padx=5)

Label(root, textvariable=alarm_status, foreground="green").pack(pady=10)

time_display()
root.mainloop()
