import sys
import os
sys.path.append('../')
try:
    import history
except ModuleNotFoundError:
    import Python.history as history
try:
    import skill_data
except ModuleNotFoundError:
    import Python.skills.skill_data as skill_data
file_location=os.path.expanduser('~')
alias=skill_data.alias
qstn=history.jsaid[0]
if 'on' in qstn:
    os.system('kasa --alias "'+alias+'" on')
elif 'off' in qstn:
    os.system('kasa --alias "'+alias+'" off')
