from pynput import keyboard, mouse
import pygame
import time
import threading
mouse_button_state = {mouse.Button.left: False, mouse.Button.right: False, mouse.Button.middle: False, mouse.Button.x1 : False, mouse.Button.x2: False}

keySoundsDisabled = False
mouseSoundsDisabled = False
mouseScrollSoundsDisabled = False

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
            play_sound("sounds/KeyboardDown2.ogg")
        else:
            play_sound("sounds/KeyboardDown.ogg")

# handle keyboard sounds when held up
def on_key_release(key):
    if keySoundsDisabled == False:
        try:
            key_char = key.char
        except AttributeError:
            key_char = str(key)
        if key_char == "Key.enter" or key_char == "Key.backspace" or key_char == "Key.space" or key_char == "Key.caps_lock" or key_char == "Key.shift" or key_char == "Key.shift_r" or key_char == "Key.ctrl_l" or key_char == "Key.ctrl_r" or key_char == "Key.alt_l" or key_char == "Key.alt_gr":
            play_sound("sounds/KeyboardUp2.ogg")
        else:
            play_sound("sounds/KeyboardUp.ogg")

# handle mouse scrolling sounds
def on_scroll(x, y, dx, dy):
    if mouseScrollSoundsDisabled == False:
        if dy > 0:
            play_sound("sounds/MouseWheel.ogg")
        elif dy < 0:
            play_sound("sounds/MouseWheel.ogg")

# handle mouse click sounds
def on_click(x, y, button, pressed):
    if mouseSoundsDisabled == False:
        if mouse_button_state[button] != pressed:
            mouse_button_state[button] = pressed
            action = 'Pressed' if pressed else 'Released'

            if mouse_button_state[mouse.Button.left] or mouse_button_state[mouse.Button.middle] or mouse_button_state[mouse.Button.right] or mouse_button_state[mouse.Button.x1] or mouse_button_state[mouse.Button.x2]:
                play_sound("sounds/MouseDown.ogg")
            elif mouse_button_state[mouse.Button.left] == False or mouse_button_state[mouse.Button.middle] == False or mouse_button_state[mouse.Button.right] == False or mouse_button_state[mouse.Button.x1] == False or mouse_button_state[mouse.Button.x2] == False:
                play_sound("sounds/MouseUp.ogg")

def key_listener():
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as keylistener:
        keylistener.join()

def mouse_listener():
    with mouse.Listener(on_click=on_click, on_scroll=on_scroll) as mouselistener:
        mouselistener.join()

if __name__ == "__main__":
    try:
        key_thread = threading.Thread(target=key_listener)
        mouse_thread = threading.Thread(target=mouse_listener)

        key_thread.start()
        mouse_thread.start()

        key_thread.join()
        mouse_thread.join()
        print("Running KinitoPET keyboard and mouse sounds...\nIf you want to stop the sounds, you gotta close the window.")
    except KeyboardInterrupt:
        print("Script interrupted by user.")