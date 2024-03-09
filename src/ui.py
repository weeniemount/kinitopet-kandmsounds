import os
from tkinter import Tk, Button, Label, ttk
import main

imgpath = os.path.dirname(os.path.realpath(__file__))
imgpath = imgpath + "/images"

def uiThreadf():
    root = Tk()
    root.title("KinitoPET K&M Sounds")
    root.geometry("300x200")
    root.resizable(0,0)
    root.iconbitmap(imgpath + "/icon.ico")

    def setVar(var):
        if var == "mouse":
            main.mouseSoundsDisabled = not main.mouseSoundsDisabled
        elif var == "keyboard":
            main.keySoundsDisabled = not main.keySoundsDisabled
        elif var == "mousescroll":
            main.mouseScrollSoundsDisabled = not main.mouseScrollSoundsDisabled
        elif var == "pcbuzz":
            main.pcBuzzSoundsDisabled = not main.pcBuzzSoundsDisabled
        elif var == "pcambience":
            main.pcAmbienceSoundsDisabled = not main.pcAmbienceSoundsDisabled

    options=Label(text="Options:").place(x=10, y=2)
    separatoro = ttk.Separator(root,orient='horizontal')
    separatoro.place(x=0, y=24, width=400)
    #mouse sounds
    mouseSoundl = Label(text="Mouse Sounds:").place(x=30, y=34)
    mouseSoundb = Button(text="Enable/Disable", command=lambda: setVar("mouse")).place(x=200, y=30)
    #keyboard sounds
    keySoundl = Label(text="Keyboard Sounds:").place(x=30, y=64)
    keySoundB = Button(text="Enable/Disable", command=lambda: setVar("keyboard")).place(x=200, y=60)
    #scroll sounds
    scrollSoundl = Label(text="Scroll Sounds:").place(x=30, y=94)
    scrollSoundb = Button(text="Enable/Disable", command=lambda: setVar("mousescroll")).place(x=200, y=90)
    #buzz sounds
    buzzSoundl = Label(text="PC Buzz Sound:").place(x=30, y=124)
    buzzSoundb = Button(text="Enable/Disable", command=lambda: setVar("pcbuzz")).place(x=200, y=120)
    #ambience sounds
    ambienceSoundl = Label(text="PC Ambience Sound:").place(x=30, y=154)
    ambienceSoundb = Button(text="Enable/Disable", command=lambda: setVar("pcambience")).place(x=200, y=150)

    def on_closing():
        #kill program
        os._exit(status=0)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

key_thread = main.threading.Thread(target=main.key_listener)
mouse_thread = main.threading.Thread(target=main.mouse_listener)
buzzThread = main.threading.Thread(target=main.pcBuzzAmbience)
uiThread = main.threading.Thread(target=uiThreadf)

print("Running KinitoPET keyboard and mouse sounds...\nIf you want to stop the sounds, you gotta close the window.")

key_thread.start()
mouse_thread.start()
buzzThread.start()
uiThread.start()

key_thread.join()
mouse_thread.join()
buzzThread.join()
uiThread.join()