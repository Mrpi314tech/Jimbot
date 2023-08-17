import sys
import os
import time
try:
    import history
except ModuleNotFoundError:
    try:
        import Python.history as history
    except ModuleNotFoundError:
        import Jimbot.Python.history as history
try:
    import skill_data
except ModuleNotFoundError:
    try:
        import Python.skills.skill_data as skill_data
    except ModuleNotFoundError:
        import Jimbot.Python.skills_data as skill_data
file_location=os.path.expanduser('~')
qstn=history.jsaid[0].split(' ')
ringer=skill_data.ringer
strco=0
tranum=0
brk=0
while True:
    try:
        if 'hour' in qstn[strco]:
            hlong=qstn[strco-1]
            try:
                hlong=int(hlong)
            except:
                os.system('espeak -ven-us "How many hours?"')
                hlong = int(input('how many hours? '))
            hlong*=3600
            while True:
                hlong-=1
                time.sleep(1)
                print(hlong)
                if hlong == 0:
                    os.system('vlc '+ringer)
                    brk=1
                    break
        elif 'minute' in qstn[strco]:
            hlong=qstn[strco-1]
            try:
                hlong=int(hlong)
            except:
                os.system('espeak -ven-us "How many minutes?"')
                hlong = int(input('how many minutes? '))
            hlong*=60
            while True:
                hlong-=1
                time.sleep(1)
                print(hlong)
                if hlong == 0:
                    os.system('vlc '+ringer)
                    brk=1
                    break
        elif 'second' in qstn[strco]:
            hlong=qstn[strco-1]
            try:
                hlong=int(hlong)
            except:
                os.system('espeak -ven-us "How many seconds?"')
                hlong = int(input('how many seconds? '))
                
            while True:
                hlong-=1
                time.sleep(1)
                print(hlong)
                if hlong == 0:
                    os.system('vlc '+ringer)
                    brk=1
                    break
        if brk == 1:
            break
        else:
            strco+=1
    except IndexError:
        break