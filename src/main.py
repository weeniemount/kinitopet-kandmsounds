from pynput import keyboard, mouse
import pygame
import threading
from os import path

mouse_button_state = {mouse.Button.left: False, mouse.Button.right: False, mouse.Button.middle: False, mouse.Button.x1 : False, mouse.Button.x2: False}
#im only putting this because vs code runs the script in the main directory, not src lmao
soundsdir = path.dirname(path.realpath(__file__))
soundsdir = soundsdir + "/sounds"

keySoundsDisabled = False
mouseSoundsDisabled = False
mouseScrollSoundsDisabled = False
pcBuzzSoundsDisabled = False
pcAmbienceSoundsDisabled = False

def play_sound(sound_file):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(sound_file)
    sound.play()

# handle keyboard sounds when held down
def on_key_press(key):
    if keySoundsDisabled == False:
        try:
            key_char = key.char
        except AttributeError:
            key_char = str(key)
        print(key_char)
        if key_char == "Key.enter" or key_char == "Key.backspace" or key_char == "Key.space" or key_char == "Key.caps_lock" or key_char == "Key.shift" or key_char == "Key.shift_r" or key_char == "Key.ctrl_l" or key_char == "Key.ctrl_r" or key_char == "Key.alt_l" or key_char == "Key.alt_gr":
            play_sound(soundsdir + "/KeyboardDown2.ogg")
        else:
            play_sound(soundsdir + "/KeyboardDown.ogg")

# handle keyboard sounds when held up
def on_key_release(key):
    if keySoundsDisabled == False:
        try:
            key_char = key.char
        except AttributeError:
            key_char = str(key)
        if key_char == "Key.enter" or key_char == "Key.backspace" or key_char == "Key.space" or key_char == "Key.caps_lock" or key_char == "Key.shift" or key_char == "Key.shift_r" or key_char == "Key.ctrl_l" or key_char == "Key.ctrl_r" or key_char == "Key.alt_l" or key_char == "Key.alt_gr":
            play_sound(soundsdir + "/KeyboardUp2.ogg")
        else:
            play_sound(soundsdir + "/KeyboardUp.ogg")

# handle mouse scrolling sounds
def on_scroll(x, y, dx, dy):
    if mouseScrollSoundsDisabled == False:
        if dy > 0:
            play_sound(soundsdir + "/MouseWheel.ogg")
        elif dy < 0:
            play_sound(soundsdir + "/MouseWheel.ogg")

# handle mouse click sounds
def on_click(x, y, button, pressed):
    if mouseSoundsDisabled == False:
        if mouse_button_state[button] != pressed:
            mouse_button_state[button] = pressed
            action = 'Pressed' if pressed else 'Released'

            if mouse_button_state[mouse.Button.left] or mouse_button_state[mouse.Button.middle] or mouse_button_state[mouse.Button.right] or mouse_button_state[mouse.Button.x1] or mouse_button_state[mouse.Button.x2]:
                play_sound(soundsdir + "/MouseDown.ogg")
            elif mouse_button_state[mouse.Button.left] == False or mouse_button_state[mouse.Button.middle] == False or mouse_button_state[mouse.Button.right] == False or mouse_button_state[mouse.Button.x1] == False or mouse_button_state[mouse.Button.x2] == False:
                play_sound(soundsdir + "/MouseUp.ogg")

def key_listener():
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as keylistener:
        keylistener.join()

def mouse_listener():
    with mouse.Listener(on_click=on_click, on_scroll=on_scroll) as mouselistener:
        mouselistener.join()

def pcBuzzAmbience():
    pygame.mixer.init()
    #pc buzz
    buzzChannel = pygame.mixer.Channel(1)
    buzz = pygame.mixer.Sound(soundsdir + "/AmbientBuzz.ogg")
    buzzChannel.play(buzz, -1)
    #pc ambience
    ambienceChannel = pygame.mixer.Channel(2)
    ambience = pygame.mixer.Sound(soundsdir + "/AmbientPCSounds.ogg")
    ambienceChannel.play(ambience, -1)
    while True:
        if pcBuzzSoundsDisabled == False:
            buzzChannel.unpause()
        else:
            buzzChannel.pause()
        if pcAmbienceSoundsDisabled == False:
            ambienceChannel.unpause()
        else:
            ambienceChannel.pause()

if __name__ == "__main__":
    key_thread = threading.Thread(target=key_listener)
    mouse_thread = threading.Thread(target=mouse_listener)
    buzzThread = threading.Thread(target=pcBuzzAmbience)

    print("Running KinitoPET keyboard and mouse sounds...\nIf you want to stop the sounds, you gotta close the window.")

    key_thread.start()
    mouse_thread.start()
    buzzThread.start()

    key_thread.join()
    mouse_thread.join()
    buzzThread.join()