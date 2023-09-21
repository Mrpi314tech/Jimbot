import os
from pynput import keyboard

file_location = os.path.expanduser('~')

def hotkey(key):
    try:
        if key == keyboard.Key.f10:
            os.system("window_id=$(wmctrl -l | grep 'Jimbot' | awk '{print $1}') && wmctrl -i -a $window_id")
    except AttributeError:
        pass

with keyboard.Listener(on_press=hotkey) as listener:
    listener.join()
