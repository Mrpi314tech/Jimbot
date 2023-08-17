#sudo python3 ~/Jimbot/Python/keypressed.py
import keyboard
import os
file_location=os.path.expanduser('~')
def hotkey(event):
    if event.name == 'f10':
        os.system("window_id=$(wmctrl -l | grep 'Jimbot' | awk '{print $1}') && wmctrl -i -a $window_id")
keyboard.on_press(hotkey)
keyboard.wait()

