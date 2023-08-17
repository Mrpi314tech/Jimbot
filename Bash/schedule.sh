#!/bin/python3
import os
from datetime import datetime as dt
while True:
    add=input('what time? ')
    try:
        add=add.split(':')
        hour=int(add[0])
        minute=int(add[1])
        break
    except:
        print('enter the hours and the minutes seperated by a colon, like 12:30')
while True:
    action=input('whould you like to open a website, or run a command? ')
    if 'command' in action:
        run=input('what command? ')
        print('running command: '+run+' at '+add[0]+':'+add[1]+". Close this window to cancel.")
        break
    elif 'website' in action:
        run=input('what is the url? ')
        print('opening website: '+run+' at '+add[0]+':'+add[1]+". Close this window to cancel.")
        if 'http' in run:
            run='xdg-open '+run
        else:
            run='xdg-open http://'+run
        break
    else:
        print('please say "command" or "website"')
while True:
    hourn=int(dt.now().strftime("%H"))
    if hourn >= 13:
        hourn-=12
    minuten=int(dt.now().strftime("%M"))
    if hourn == hour and minuten==minute:
        os.system(run)
        break
