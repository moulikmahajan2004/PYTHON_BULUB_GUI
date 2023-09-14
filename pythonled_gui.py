import tkinter as tk
from gpiozero import LED
import atexit

Red = LED(15)
Multi = LED(18)
Green = LED(14)

window = tk.Tk()
window.title('LED_BULUB_GUI')

var = tk.StringVar()

def Red_glow():
    if Red.is_lit:
        Red.off()
        r1["text"] = "MAKE_RED_ON"
    else:
        Red.on()
        r1["text"] = "MAKE_RED_OFF"

def Green_glow():
    if Green.is_lit:
        Green.off()
        r2["text"] = "MAKE_GREEN_ON"
    else:
        Green.on()
        r2["text"] = "MAKE_GREEN_OFF"

def Multi_glow():
    if Multi.is_lit:
        Multi.off()
        r3["text"] = "MAKE_MULTI_ON"
    else:
        Multi.on()
        r3["text"] = "MAKE_MULTI_OFF"

def CLOSE_GUI():
    window.destroy()

# Register GPIO cleanup to run when the program exits
atexit.register(Red.close)
atexit.register(Multi.close)
atexit.register(Green.close)

# Buttons
r1 = tk.Radiobutton(window, text='MAKE_RED_ON', variable=var, value='A', command=Red_glow, bg="red", height=3, width=15)
r1.grid(row=6, column=10)

r2 = tk.Radiobutton(window, text='MAKE_GREEN_ON', variable=var, value='B', command=Green_glow, bg="green", height=3, width=15)
r2.grid(row=6, column=18)

r3 = tk.Radiobutton(window, text='MAKE_MULTI_ON', variable=var, value='C', command=Multi_glow, bg="purple", height=3, width=15)
r3.grid(row=6, column=20)

exitButton = tk.Button(window, text="EXIT WINDOW", command=CLOSE_GUI, bg='red')
exitButton.grid(row=6, column=24)

# Set the protocol for window closing
window.protocol("WM_DELETE_WINDOW", CLOSE_GUI)
window.mainloop()
