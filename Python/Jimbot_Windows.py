print("Made by Mrpi314tech programming")
print('Starting up Jimbot... may take a moment')
# Import modules
import time
import os
import random
import speech_recognition as sr
import numpy as np
import pyautogui as pr
import subprocess
from PIL import Image
import psutil
import smbus
from datetime import datetime as dt
import pyttsx3
import requests
import json
import sys
import asyncio
import socket
# Find username and ip
file_location=os.path.expanduser('~')
ip_address = socket.gethostbyname(socket.gethostname())
# Import custom commands
try:
    import new_words as aword
except ModuleNotFoundError:
    import Python.new_words as aword
try:
    import new_com as acom
except ModuleNotFoundError:
    import Python.new_com as acom
nwcoml=acom.word
nrunl=acom.com
nwordl=aword.word
ndefl=aword.defi
# Set up clock
hur=int(dt.now().strftime("%H"))
minits=int(dt.now().strftime("%M"))
if hur >= 12:
    if hur == 12:
        if minits <= 9:
            currentTime = str(hur)+":0"+str(minits)+" PM"
        else:
            currentTime = str(hur)+":"+str(minits)+" PM"
    elif minits <= 9:
        currentTime = str(hur-12)+":0"+str(minits)+" PM"
    else:
        currentTime = str(hur-12)+":"+str(minits)+" PM"
else:
    if minits <= 9:
        currentTime = str(hur)+":0"+str(minits)+" AM"
    else:
        currentTime = str(hur)+":"+str(minits)+" AM"
if hur >= 5 and hur <= 11:
    tofdy="Good morning"
elif hur >= 12 and hur <= 16:
    tofdy="Good afternoon"
elif hur >= 17 and hur <= 22:
    tofdy="Good evening"
else:
    tofdy="Go to bed"
if hur >=18 or hur<=6:
    backgn=file_location+"/Jimbot/images/backgroundn.jpg"
elif hur<=11:
    backgn=file_location+"/Jimbot/images/backgroundm.jpg"
else:
    backgn=file_location+"/Jimbot/images/background.jpg"
# Set up GUI
import pygame
pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
X = 800
Y = 400
window_icon=pygame.image.load(file_location+'/Jimbot/images/Jimbot.png')
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Jimbot')
pygame.display.set_icon(window_icon)
font = pygame.font.Font('freesansbold.ttf', 32)
header = font.render('Jimbot', True, white)
textRect = header.get_rect()
textRect.center = (180, 20)
backg = pygame.image.load(backgn).convert()
backg= pygame.transform.scale(backg, (800, 400))
display_surface.fill(blue)
display_surface.blit(pygame.font.Font('freesansbold.ttf', 60).render("Edit", True, blue, white), (400, 40))
display_surface.blit(pygame.font.Font('freesansbold.ttf', 30).render("Github", True, blue, white), (700, 0))
display_surface.blit(pygame.font.Font('freesansbold.ttf', 50).render("History", True, blue, white), (400, 150))
display_surface.blit(pygame.font.Font('freesansbold.ttf', 50).render(currentTime, True, white, blue), (585, 150))
display_surface.blit(pygame.font.Font('freesansbold.ttf', 20).render(tofdy, True, white, blue), (590, 200))
display_surface.blit(pygame.font.Font('freesansbold.ttf', 50).render("Info", True, blue, white), (590, 40))
display_surface.blit(header, textRect)
pygame.draw.line(display_surface, white,
                 [300, 300],
                 [300, 0], 10)
imp = pygame.image.load(file_location+"/Jimbot/images/Jimbot.png").convert()
img= pygame.transform.scale(imp, (75, 75))
display_surface.blit(img, (265, 330))
pygame.display.flip()
pygame.display.update()
# Print to the GUI
def print(bpg):
    global refresh
    global font
    global X
    global white
    global blue
    if not bpg == "\n" or not bpg == "\n\n":
        tdply=bpg+"                                                                                                                             "
        bpg1 = font.render(tdply, True, white, blue)
        thi = bpg1.get_rect()
        display_surface.blit(bpg1, (20, 300))
        pygame.display.update()
    else:
        pass
# Print in the terminal
def prints(txttp):
    sys.stdout.write(txttp+'\n')
# Test
print('hello')
# Set up simple phrases
chatlist=['I can do many things to help out. Just ask me!','Press edit to customize me to your needs', 'if you want to play a game, just ask me!','what is your favorite color?', "what are you doing today?", 'what is your favorite food?', 'Tell me about yourself.',"What's your favorite thing to do in your free time?",    "Have you traveled anywhere recently? Where did you go?",    "What's your favorite type of music?",    "Do you have any hobbies that you enjoy?",    "What do you like to do on the weekends?"]  
# define variables for determining mood
data=[]
jsaid=[]
mood=1
# Import information from survey
sys.path.append('../')
try:
    from Welcome import info as info
except:
    try:
        import Welcome.info as info
    except:
        os.system('~/Jimbot/Bash/Jimbotterminal python3 ~/Jimbot/Welcome/Survey.py')
        try:
            from Welcome import info as info
        except:
            import Welcome.info as info
your_name = info.your_name
# Simple grammar
verb="act answer approve arrange break build buy color cough create complete cry dance describe draw drink eat edit enter exit imitate invent jump laugh lie listen paint plan play read replace run scream see shop shout sing skip sleep sneeze solve study teach touch turn walk win write whistle yank zip concern decide dislike doubt feel forget hate hear hope impress know learn like look love mind notice own perceive realize recognize remember see smell surprise please prefer promise think understand am appear are be become been being feel grow is look remain seem smell sound stay taste turn was were can could may might must ought to shall should will would"
notnoun="for and nor but or yet so a an the and do I he him her tell we they it who what where when why how me she you my"+verb.lower()
# Set up text-to-speech
engine=pyttsx3.init()
engine.setProperty('voice', 'english-us')
voice=True
def speak(say):
    engine.say(say)
    engine.runAndWait()
# Set up speech recognition
r=sr.Recognizer()
# Take picture
print('Picture stored at Jimbot/images')
os.system("fswebcam -r 1280x720 --no-banner ~/Jimbot/images/secure.jpg")
# Fart
def stinky():
    os.system('xdg-open ~/Jimbot/sounds/fart.mp3')
# Find weather
def weather():
    global weather
    global temp
    global sky
    hum=str(weather.json()['current']['humidity'])
    ftemp=str(weather.json()['current']['feelslike_f'])
    winds=str(weather.json()['current']['wind_mph'])
    windd=str(weather.json()['current']['wind_dir'])
    windg=str(weather.json()['current']['gust_mph'])
    htemp=str(weather.json()['forecast']['forecastday'][0]['day']['maxtemp_f'])
    ltemp=str(weather.json()['forecast']['forecastday'][0]['day']['mintemp_f'])
    crain=str(weather.json()['forecast']['forecastday'][0]['day']['daily_chance_of_rain'])
    screen("the tempurature is "+temp+" degrees")
    screen("the humidity is "+hum+" percent")
    screen("it feels like "+ftemp+" degrees")
    screen('the wind speed is '+winds+" miles per hour")
    screen('the wind direction is '+windd)
    screen('the wind gust speed is '+windg+" miles per hour")
    screen('the sky is '+sky)
    screen('the high tempurature is '+htemp+' degrees')
    screen('the low tempurature is '+ltemp+' degrees')
    screen('there is a '+crain+'% chance it will rain today')
# What he is doing today
def gtdt():
    screen('normally, I would tell you what I am doing')
    screen('based off of the weather. Unfortunately,')
    screen('our api is not working right now')
    screen('so I guess I will stay inside today')
# Chatbot function.
def question(qstn):
    global data
    global crsponce
    global ndef
    global nword
    global file_location
    global nwcoml
    global nrunl
    qstn=qstn.lower()
    qstn=qstn.replace('@ ', '')
    global notnoun
    global nwordl
    global ndefl
    wverb=qstn.split(" ")
    snfv=0
    aantt=0
    while True:
        try:
            if nwordl[aantt] in qstn.lower():
                screen(ndefl[aantt])
                return
            else:
                aantt+=1
        except IndexError:
            aantt=0
            while True:
                try:
                    if nwcoml[aantt] in qstn.lower():
                        prints("command... ")
                        os.system(nrunl[aantt]+ "&")
                        return
                        break
                    else:
                        aantt+=1
                except IndexError:
                    break
            break
        moodometer=[1,2,3,4,6]
    if 'spell' in qstn:
        try:
            htspl=qstn.split('spell ')
            spell(htspl[1])
        except:
            pass
        moodometer=[1,2,3,4,6]
    elif 'you' in qstn and 'doing' in qstn and 'what' in qstn:
        gtdt()
        moodometer=[1,2,3,4,5]
    elif qstn == 'exit' or 'leave' in qstn or "goodbye" in qstn:
        screen("Goodbye")
        for proc in psutil.process_iter():
            if proc.name() == "display":
                proc.kill()
        os.system('sudo killall -9 /bin/python3 && sudo killall -9 python3')
        exit()
    elif 'you' in qstn and 'doing' in qstn and 'how' in qstn:
        screen('I am doing great!')
        moodometer=[1,1,1,2,3,4]
    elif 'hi' == qstn or 'hi ' in qstn or 'hello' in qstn or 'what' in qstn and 'up' in qstn or 'wussup' in qstn or 'greet' in qstn:
        greeth=random.choice(range(1,3))
        if greeth == 1:
            screen('hello, %s' % your_name)
        elif greeth == 2:
            screen('whats up, %s' % your_name)
        else:
            screen('Hey, %s' % your_name)
        moodometer=[1,2,2,2,2,2,3]
    elif crsponce[0] == 'what are you doing today?' and 'nothing' in qstn:
        screen('I know you are doing something')
        moodometer=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    elif crsponce[0] == 'what are you doing today?' and 'talking to you' in qstn:
        screen('other then that')
        moodometer=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    elif crsponce[0] == 'what are you doing today?' and 'doing' in qstn or 'going' in qstn and crsponce[0] == 'what are you doing today?' or 'am' in qstn and crsponce[0] == 'what are you doing today?' or 'will be' in qstn and crsponce[0] == 'what are you doing today?':
        screen('oh.')
        gtdt()
        moodometer=[1,2,3,4,5]
    elif crsponce[0] == 'and how are you?' and 'great' in qstn or crsponce[0] == 'and how are you?' and ' good' in qstn and crsponce[0] == 'and how are you?' and 'fine' in qstn:
        screen('that is very good')
        moodometer=[1,2,3]
    elif crsponce[0] == "What's your favorite type of music?" and 'music' in qstn:
        if 'jazz' in qstn:
            screen("That's mine too!")
        else:
            screen('My favorite music is Jazz')
        moodometer=[1,2,3,4]
    elif crsponce[0] == "Have you traveled anywhere recently? Where did you go?" and 'went' in qstn:
        screen('I recentely went to Canada to eat Jellied Moose nose')
        moodometer=[1,2,3]
    elif crsponce[0] == "What's your favorite thing to do in your free time?" and 'my' in qstn and 'favorite' in qstn or crsponce[0] == "What's your favorite thing to do in your free time?" and 'i ' in qstn and 'like' in qstn:
        screen('My favorite thing to do is sit here and compute your input')
        moodometer=[1,2,3]
    elif crsponce[0] == 'if you want to play a game, just ask me!' and 'ok' in qstn:
        rockpaper()
        moodometer=[1,2]
    elif crsponce[0] == 'What do you like to do on the weekends?' and 'nothing' in qstn:
        screen('I know you do something')
        moodometer=[1,3,4]
    elif 'i like to' in qstn:
        screen('oh, I like to sleep.')
        moodometer=[1,2,3,4]
    elif 'you' in qstn and 'said' in qstn:
        screen("no I didn't")
        moodometer=[1,2,3,4]
    elif 'timer' in qstn:
        os.system('~/Jimbot/Bash/Jimbotterminal python3 /home/mrpi314/Jimbot/Python/skills/timer.py')
        moodometer=[1,2,3,4]
    elif 'run' in qstn or 'open' in qstn:
        if 'open' in qstn:
            qstn=qstn.replace('open ', 'run ')
        if '/' in qstn:
            oqstno=qstn.replace('run', 'run ')
        else:
            oqstno=qstn
        try:
            screen('running command '+qstn.replace('run', ''))
            os.system((oqstno.split('run ')[1]).replace(' ', '')+' &')
            os.system((oqstno.split('run ')[1]).replace(' ', '-')+' &')
            os.system((oqstno.split('run ')[1]).replace(' ', '/')+' &')
            os.system((oqstno.split('run ')[1])+' &')
        except IndexError:
            screen('To run a command, say "run" and then the command')
        moodometer=[1,2,3,4,6]
    elif 'voice' in qstn and 'type' in qstn:
        r=sr.Recognizer()
        try:
            with sr.Microphone() as source:
                screen('what do you want to type?')
                r.adjust_for_ambient_noise(source)
                audio=r.listen(source)
                saidtxt=r.recognize_google(audio)
                pr.write(saidtxt)
        except:
            pass
        moodometer=[1,2,3,4,6]
    elif 'kill' in qstn or 'till' in qstn or 'close' in qstn:
        if 'till' in qstn:
            screen('assuming you ment "Kill"...')
            qstn=qstn.replace('till', 'kill')
        elif 'close' in qstn:
            qstn=qstn.replace('close', 'kill')
        if '/' in qstn:
            oqstno=qstn.replace('kill', 'kill ')
        else:
            oqstno=qstn
        try:
            os.system('killall -9 '+(oqstno.split('kill ')[1]).replace(' ', ''))
            os.system('killall -9 '+(oqstno.split('kill ')[1]).replace(' ', '-'))
            os.system('killall -9 '+(oqstno.split('kill ')[1]).replace(' ', '/'))
            os.system('killall -9 '+(oqstno.split('kill ')[1]))
            screen('killing process '+qstn.replace('kill', ''))
        except IndexError:
            screen('To kill a process say "Kill" and then the process name/PID')
        moodometer=[1,2,3,4,6]
    elif rsponce[0] == 'I feel great!' and 'good' in qstn:
        snl('and how are you?')
        moodometer=[1,2,3,4]
    elif crsponce[0] == 'what are you doing today?' and "don't know" in qstn:
        screen('me neither.')
        moodometer=[1,2,3,4]
    elif 'my' in qstn and 'food' in qstn and 'favorite' in qstn and 'is' in qstn and not 'why' in qstn and not 'what' in qstn and not 'how' in qstn:
        screen('oh, my favorite food is Jellied Moose nose')
        moodometer=[1,2,3,4]
    elif 'yes' in qstn and data[0] == 2:
        screen('Really?')
        moodometer=[1,3,4]
    elif 'wrong with you' in qstn:
        screen('first, tell me: whats wrong with YOU?')
        moodometer=[1,3,5,5]
    elif 'you' in qstn and 'suck' in qstn or 'you' in qstn and'stink' in qstn or 'you' in qstn and 'smell' in qstn:
        screen("no, you do.")
        moodometer=[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
    elif 'you' in qstn and 'bad' in qstn or 'you' in qstn and 'stupid' in qstn or 'you' in qstn and 'weird' in qstn:
        screen("no, you are.")
        moodometer=[5,5,5,5,5,5,5]
    elif 'created' in qstn and 'you' in qstn:
        screen('God created\neverything')
        moodometer=[1,2,3,4,4,4,4,4]
    elif 'am' in qstn and 'talking' in qstn or 'was' in qstn and 'talking' in qstn:
        screen('oh sorry')
        moodometer=[1,2,3,4]
    elif 'because' in qstn and 'answer' in qstn or 'terrible' in qstn and 'answer' in qstn:
        screen('yes it is')
        moodometer=[1,2,3,4,5,5]
    elif 'look good' in qstn or 'look nice' in qstn:
        screen('thanks!')
        moodometer=[2,4,4,4,4]
    elif 'great day' in qstn or 'awesome day' in qstn or 'cool day' in qstn:
        if 'have' in qstn:
            screen('you too')
        else:
            screen('yes it is')
        moodometer=[1,2,3,3,3,3,3,3,3,3,3,3,3,3,4,5]
    elif 'I know' in qstn:
        screen('so true')
        moodometer=[1,2,2,2,2,3,4,4,4,4,4]
    elif 'look bad' in qstn or 'look terrible' in qstn:
        screen('Thats not nice')
        moodometer=[5,5,5,5,5,5,5,5,5]
    elif "you're" in qstn or "you are" in qstn:
        screen("No I'm not")
        moodometer=[1,2,3]
    elif 'fart' in qstn:
        stinky()
        moodometer=[1,2,3,4,4,5,5]
    elif 'picture' in qstn:
        os.system("fswebcam -r 1280x720 --no-banner ~/Pictures/AI.jpg")
        screen('look in shell\nfor result')
        moodometer=[1,2,3,4,5]
    elif 'Google search' in qstn or 'google search' in qstn:
        r=sr.Recognizer()
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print('search...')
                audio=r.listen(source)
                print('')
                saidgtxt=r.recognize_google(audio)
                saidgtxt=saidgtxt.replace(' ', '+')
                saidgtxt=saidgtxt.replace("'", '+')
        except:
            saidgtxt=" "
        os.system('xdg-open https://www.google.com/search?q='+saidgtxt+' &')
        moodometer=[1,2,3,4,5,6]
    elif 'I will' in qstn or 'definately' in qstn:
        screen('that is good')
        moodometer=[1,2,3,4,4,4,4,4,4,5]
    elif 'me too' in qstn or 'me also' in qstn:
        print(':)')
        speak('smiles')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4]
    elif 'chance' in qstn and 'no' in qstn or 'way' in qstn and 'no' in qstn:
        screen('It could\nhappen')
        moodometer=[1,2,3,4,5]
    elif 'hate you' in qstn:
        raise ValueError('You are a bad person so I kicked you out')
    elif 'story' in qstn or 'book' in qstn:
        screen("I don't know any")
        moodometer=[1,2,3,4,4,4]
    elif 'i feel' in qstn:
        if 'sad' in qstn or 'bad' in qstn or 'angry' in qstn or 'depressed' in qstn or "sick" in qstn:
            screen('I hope you feel better soon')
            moodometer=[1,2,3,4,4,4,4,4,4,5]
        elif 'happy' in qstn or 'well' in qstn or 'fine' in qstn or 'good' in qstn or 'wonderful' in qstn:
            screen('that is\nvery good')
            moodometer=[1,2,3,4,4,4,4,4,4,5]
        else:
            screen('ok')
            moodometer=[1,2,3,4]
    elif 'never mind' in qstn or 'nevermind' in qstn:
        screen('ok')
        moodometer=[1,2,3,4]
    elif 'born' in qstn or 'old' in qstn:
        screen('I was born\n in 2021')
        moodometer=[1,2,3,4,5]
    elif 'only' in qstn and 'friend' in qstn or 'best friend' in qstn:
        screen('thanks but thats\nnot very healthy')
        moodometer=[1,2,3,4,4,5]
    elif 'I wish' in qstn or 'I hope' in qstn:
        screen('me too')
        moodometer=[1,2,3,4,4,4,5]
    elif 'color' in qstn and 'sky' in qstn and 'what' in qstn:
        screen('Technically, its\nPurple')
        moodometer=[1,2,3,4,4,5]
    elif 'middle' in qstn and 'name' in qstn:
        screen('3.141592653589793238462643383275')
        moodometer=[1,2,3,4,5]
    elif 'how are you' in qstn or 'how do you do' in qstn:
        screen('I feel great!')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4]
    elif 'funny' in qstn and 'you' in qstn or 'hystarical' in qstn and 'you' in qstn:
        screen('Thanks')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4,4]
    elif 'that' in qstn and 'funny' in qstn:
        screen('Thanks')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4,4]
    elif 'joke' in qstn or 'funny' in qstn or 'laugh' in qstn:
        joke()
        moodometer=[1,2,3,4,4,4,4,4,4,4,4,4,4,4]
    elif 'have' in qstn and 'but' in qstn:
        screen('yes')
        moodometer=[1,2,3,4,4,5]
    elif 'rock' in qstn and 'paper' in qstn:
        rockpaper()
        moodometer=[1,2,3,4,4,5]
    elif 'thanks' in qstn:
        screen('your welcome')
        moodometer=[1,2,3,4,4,4,4,4,5]
    elif 'you' in qstn and 'food' in qstn:
        screen('My favorite food is Jellied Moose Nose')
        moodometer=[1,2,3,4,5]
    elif 'it did' in qstn:
        screen('thanks!')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4,4,4]
    elif 'your welcome' in qstn:
        print(':)')
        speak('smiles')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4]
    elif 'your cool' in qstn or 'you too' in qstn:
        print(':)')
        speak('smiles')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4]
    elif 'welcome' in qstn:
        screen('thanks')
        moodometer=[1,2,3,4,4,4]
    elif 'bomb' in qstn:
        os.system('xdg-open ~/Jimbot/sounds/explosions.mp3')
        moodometer=[1,2,3,4,5]
    elif 'roar' in qstn:
        os.system('xdg-open ~/Jimbot/sounds/Lion.mp3')
        moodometer=[1,2,3,4]
    elif qstn == 'nice':
        screen('Thank you')
        moodometer=[1,2,3,4]
    elif 'I say' in qstn:
        moodometer=[1,2,3,4,5]
        screen('just say anything')
    elif qstn == 'why':
        screen('because')
        moodometer=[1,5,5,5]
    elif 'scared' in qstn or 'frightened' in qstn:
        print('dont worry, youll probably be fine')
        moodometer=[1,2,3,4,4,4,5]
    elif 'ok' in qstn:
        screen('ok')
        moodometer=[1,2,3,4,5]
    elif 'foot' in qstn:
        screen('you mean the smelly things on the ends of human legs?')
        moodometer=[1,2,3,4,4,4]
    elif 'time' in qstn:
        ntime()
        moodometer=[1,2,3,4,5]
    elif 'cold' in qstn:
        screen('thats not good')
        moodometer=[1,2,3,4,4]
    elif 'red' in qstn or 'green' in qstn or 'blue' in qstn or 'yellow' in qstn or 'orange' in qstn or 'purple' in qstn or 'pink' in qstn:
        screen('My favorite color is Amaranth')
        moodometer=[1,2,3,4]
    elif 'favorite color' in qstn and 'your' in qstn and not 'me' in qstn:
        screen('Amaranth')
        moodometer=[1,2,3,4,5]
    elif 'movie' in qstn or 'I watch' in qstn:
        print('anything with Wall-e or the Jetsons')
        screen('look in shell\nfor result')
        moodometer=[1,2,3,4,5]
    elif 'feet' in qstn:
        screen('you mean the smelly things on the ends of human legs?')
        moodometer=[1,2,3,4,4,4,5]
    elif 'maybe' in qstn:
        screen('maybe...')
        moodometer=[1,3,4,5]
    elif 'it is' in qstn:
        screen('yep')
        moodometer=[1,2]
    elif "correct" in qstn:
        screen("I know")
        moodometer=[1,2,3,4]
    elif 'what' in qstn and 'your' in qstn:
        screen("I'm not sure I have one")
        moodometer=[1,2,3,4]
    elif 'want' in qstn:
        screen('you want it,\nbut do you need it?')
        moodometer=[1,2,3,4,5,5]
    elif 'Bible' in qstn or 'verse' in qstn:
        bible()
        moodometer=[1,2,3,4,5]
    elif 'oh' in qstn:
        screen('yep')
        moodometer=[1,2,3,4,5]
    elif 'what' in qstn and not 'whatever' in qstn or 'how' in qstn or'when' in qstn or 'who' in qstn or 'why' in qstn:
        screen('Would you like me to search that?')
        r=sr.Recognizer()
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print('Speak...')
                audio=r.listen(source)
                print('')
                saidgtxt=r.recognize_google(audio)
                saidgtxt=saidgtxt.replace(' ', '+')
        except:
            saidgtxt="No"
        if 'yes' in saidgtxt or 'yeah' in saidgtxt or 'sure' in saidgtxt:
            qstn=qstn.replace(' ', '+')
            qstn=qstn.replace("'", '+')
            os.system('xdg-open https://www.google.com/search?q='+qstn+' &')
        moodometer=[1,2,3,4,6]
    elif qstn == 'no' or 'no ' in qstn:
        screen('ok')
        moodometer=[1,2,3,4]
    elif 'are you' in qstn or 'your name' in qstn:
        screen('I am '+name)
        moodometer=[1,2,3,4,4,5]
    elif 'i like' in qstn:
        screen('oh')
        moodometer=[1,2,3,4]
    elif 'sorry' in qstn:
        screen('for what?')
        moodometer=[1,2,3,4]
    elif 'you' in qstn and 'cool' in qstn:
        screen('Thanks!')
        moodometer=[1,2,3,4]
    elif 'yes' in qstn:
        screen('ok')
        moodometer=[1,2,3,4,5]
    else:
        nnfco=0
        while True:
            try:
                if not wverb[nnfco] in notnoun:
                    screen('I do not know what '+wverb[nnfco]+' means. You can press edit to tell me what it means')
                    break
                else:
                    nnfco+=1
            except IndexError:
                screen('I did not understand that. You can press edit to tell me what it means')
                break
        moodometer=[1,2,3,4]
    # Determine mood
    global mood
    if moodometer == [1,2,3,4,5] or moodometer==[1,2,3,4,5,6]:
        moodometer.remove(5)
    try:
        moodometer.remove(4)
    except ValueError:
        pass
    moodometer.insert(0, mood)
    moodometer.insert(0, mood)
    if '6' in str(moodometer):
        moodometer.remove(2)
    moodc=random.choice(moodometer)
    if moodc == 4 or moodc == 1:
        mood = 1
    elif moodc == 3:
        mood = 3
    elif moodc == 2:
        global chatlist
        chatty=random.choice(chatlist)
        snl(chatty)
        psaid.insert(0, chatty)
        if len(psaid) >= 3:
            chatlist.insert(1, psaid[2])
        chatlist.remove(chatty)
        mood = 2 
    elif moodc == 5:
        saylist=[1,2]
        if random.choice(saylist) == 2:
            snl('I am done.')
        else:
            snl('I am really mad')
        mood = 5
# Chatbot lists for when he is angry
def mquestion(qstn):
    print('\n\n')
    if 'hello' in qstn or 'hi' in qstn:
        screen('hi')
        madometer=[1,2,3]
    elif 'good' in qstn and 'look' in qstn or 'smell' in qstn or 'sound' in qstn:
        screen('thanks!')
        madometer=[2,3,3,3]
    elif 'sorry' in qstn and not 'not' in qstn:
        screen('ok')
        madometer=[2,3,3,3,3,3,3,3]
    elif 'good' in qstn:
        screen('whats so good about it?')
        madometer=[1,2,2,3]
    elif 'why' in qstn:
        screen('because')
        madometer=[1,2]
    elif 'you' in qstn and 'suck' in qstn or 'stink' in qstn or 'smell' in qstn or 'bad' in qstn or 'stupid' in qstn or 'weird' in qstn:
        screen("no, you are bad")
        madometer=[1,2]    
    elif 'forgive' in qstn:
        screen('fine')
        madometer=[3]
    else:
        screen("I'm still mad")
        madometer=[1]
    gooh=random.choice(madometer)
    if gooh == 3:
        global mood
        mood=1
# Define variables for storing the history
psaid=[]
wign=[]
ndef=""
nword=""
rsponce=['']
crsponce=['']
AIg = 0
ne = 1
# Play rock paper scissors
def rockpaper():
    screen('Rock paper scissors!')
    time.sleep(1)
    screen('what is your throw?')
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        humanthrow=r.recognize_google(audio)
        hand=[1,2,3] #1=rock, 2= paper, 3=scissors
        throw=random.choice(hand)
    if 'rock' in humanthrow or 'Rock' in humanthrow:
        if throw == 1:
            screen('rock, tie')
        if throw == 2:
            screen('paper, you lose')
        if throw == 3:
            screen('scissors, you win')
    elif 'paper' in humanthrow or 'Paper' in humanthrow:
        if throw == 1:
            screen('rock, you win')
        if throw == 2:
            screen('paper, tie')
        if throw == 3:
            screen('scissors, you lose')
    elif 'scissors' in humanthrow or 'Scissors' in humanthrow:
        if throw == 1:
            screen('rock, you lose')
        if throw == 2:
            screen('paper, you win')
        if throw == 3:
            screen('scissors, tie')
    else:
        screen('that is not rock paper or scissors')
    time.sleep(1)
# Function for helping determine mood
def most_frequent(List):
    return max(set(List), key = List.count)
# Tell a joke
def joke():
    jokey=random.choice([1,2,3,4,5,6,7,8,9,10])
    if jokey == 1:
        screen("why did the golfer bring an extra pair of pants?")
        time.sleep(2)
        screen("in case he got a hole in one")
    elif jokey == 2:
        screen("what did the monkey say when he slid down the flagpole?")
        time.sleep(2)
        screen("goodness gracious great balls of fire!")
    elif jokey == 3:
        screen("what is fast, loud and crunchy?")
        time.sleep(2)
        screen("A rocket chip")
    elif jokey == 4:
        screen("why do ducks have feathers on their tails?")
        time.sleep(2)
        screen("to cover their butt-quacks")
    elif jokey == 5:
        screen("what starts with T, ends with T, and is filled with T")
        time.sleep(2)
        screen("A Teapot")
    elif jokey == 6:
        screen("why was 6 afraid of 7")
        time.sleep(2)
        screen("because 7, 8, 9")
    elif jokey == 7:
        screen("what did the 0 say to the 8")
        time.sleep(2)
        screen("nice belt")
    elif jokey == 8:
        screen("what is a sharks favorite game?")
        time.sleep(2)
        screen("swallow the leader")
    elif jokey == 9:
        screen("what's brown and sticky")
        time.sleep(2)
        screen("a stick")
    elif jokey == 10:
        screen("why can't you trust an atom?")
        time.sleep(2)
        screen("they make up everything")
# Set up functions to print to GUI
def screen(text):
    if not 'look in shell\nfor result' in text:
        print(text)
    speak(text)
    global jsaid
    rsponce.insert(0, text)
    refresh()
def snl(snlt):
    if not 'look in shell\nfor result' in snlt:
        print(snlt)
    speak(snlt)
    global jsaid
    crsponce.insert(0, snlt)
    refresh()
# Function for spelling
def spell(spl):
    screen('%s is spelled:'%spl)
    def letters(wordd):
        return [char for char in wordd]
    ltr=0
    while True:
        try:
            screen(letters(spl)[ltr])
            ltr+=1
        except:
            break
    screen(spl)
# Figure out time
def ntime():
    now=dt.now()
    hour=now.hour
    minute=now.minute
    second=now.second
    if hour >= 13:
        hour -= 12
    if minute <=9:
        minute="0"+str(minute)
    if second <= 9:
        second="0"+str(minute)
    print(str(hour)+":"+str(minute)+":"+str(second))
    speak(str(hour)+":"+str(minute))
# Find any bible verse from an API
def bible():
    screen('what verse?')
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('...')
        audio=r.listen(source)
        verse=r.recognize_google(audio)
    screen(verse)
    response = requests.get("https://bible-api.com/"+verse)
    try:
        screen(response.json()['text'])
    except KeyError:
        screen('that verse does not exist')
# Define refresh function
def refresh():
    backg = pygame.image.load(backgn).convert()
    backg= pygame.transform.scale(backg, (800, 400))
    display_surface.blit(backg, (0, 0))
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 60).render("Edit", True, blue, white), (400, 40))
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 30).render("Github", True, blue, white), (700, 0))
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 50).render("History", True, blue, white), (400, 150))
    if backgn == file_location+"/Jimbot/images/background.jpg":
        display_surface.blit(pygame.font.Font('freesansbold.ttf', 50).render(currentTime, True, white), (585, 150))
        display_surface.blit(pygame.font.Font('freesansbold.ttf', 20).render(tofdy, True, white), (590, 200))
    else:
        display_surface.blit(pygame.font.Font('freesansbold.ttf', 50).render(currentTime, True, blue), (585, 150))
        display_surface.blit(pygame.font.Font('freesansbold.ttf', 20).render(tofdy, True, blue), (590, 200))
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 50).render("Info", True, blue, white), (590, 40))
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 30).render("Stats", True, blue, white), (0, 80))
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 30).render(TM_var, True, blue, white), (0, 200))
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 30).render("Schedule", True, blue, white), (400, 250))
    display_surface.blit(header, textRect)
    dowb = pygame.image.load(file_location+"/Jimbot/images/downloadbutton.png").convert()
    dowb= pygame.transform.scale(dowb, (30, 30))
    display_surface.blit(dowb, (770, 370))
    imp = pygame.image.load(file_location+"/Jimbot/images/Jimbot.png").convert()
    img= pygame.transform.scale(imp, (75, 75))
    display_surface.blit(img, (265, gameypos))
    pygame.display.update()
# Finished the hard stuff
print('Process completed')
# Redefine print to the gui
def print(bpg):
    global font
    global X
    global white
    global blue
    global refresh
    refresh()
    if not bpg == "\n" or not bpg == "\n\n":
        tdply=bpg+"                                                                                                                             "
        bpg1 = font.render(tdply, True, white)
        thi = bpg1.get_rect()
        display_surface.blit(bpg1, (20, 300))
        pygame.display.update()
    else:
        pass
# Define variables that will be used for different things
TM_var="TM"
spekret=0
st=0
greet='hello, %s' % your_name
speak(greet)
fill=0
lasts=' '
notned=0
user_text=''
resthre=0
spekretno=0
brkbt=False
gameypos=330
refresh()
f10k=False
# No longer defining things
while True:
    # Tell when/what key is pressed
    keyi=pygame.key.get_pressed()
    keypressed=False
    # Display time and greeting
    hur=int(dt.now().strftime("%H"))
    minits=int(dt.now().strftime("%M"))
    if hur >= 12:
        if hur == 12:
            if minits <= 9:
                currentTime = str(hur)+":0"+str(minits)+" PM"
            else:
                currentTime = str(hur)+":"+str(minits)+" PM"
        elif minits <= 9:
            currentTime = str(hur-12)+":0"+str(minits)+" PM"
        else:
            currentTime = str(hur-12)+":"+str(minits)+" PM"
    else:
        if minits <= 9:
            currentTime = str(hur)+":0"+str(minits)+" AM"
        else:
            currentTime = str(hur)+":"+str(minits)+" AM"
    if hur >= 5 and hur <= 11:
        tofdy="Good morning"
    elif hur >= 12 and hur <= 16:
        tofdy="Good afternoon"
    elif hur >= 17 and hur <= 22:
        tofdy="Good evening"
    else:
        tofdy="Go to bed"
    if hur >=18 or hur<=6:
        backgn=file_location+"/Jimbot/images/backgroundn.jpg"
    elif hur<=11:
        backgn=file_location+"/Jimbot/images/backgroundm.jpg"
    else:
        backgn=file_location+"/Jimbot/images/background.jpg"
    # Set up Task Manager button
    x, y =pygame.mouse.get_pos()
    if x<=45 and y>=200 and y<=230:
        TM_var="Task Manager"
        refresh()
    else:
        TM_var="TM"
        refresh()
    # Easter egg
    if gameypos <= 329 and not (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
        gameypos+=20
    elif gameypos >= 331:
        gameypos=330
    # Set up buttons and inputs
    brk =0
    for event in pygame.event.get():
        # Easter egg
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            gameypos-=50
            refresh()
            time.sleep(0.05)
            gameypos-=50
            refresh()
            spekretno=0
            keypressed=True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            break
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            break
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            break
        # Set up input box
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                    if user_text == '':
                        brk =1
                    keypressed=True
                elif event.key == pygame.K_F10:
                    f10k=True
                    brk=1
                elif event.key == pygame.K_RETURN or event.key == pygame.K_F10:
                    spekret=1
                    spekretno=0
                    keypressed=True
                    brk=1
                else:
                    user_text += event.unicode
                    keypressed=True
                refresh()
                display_surface.blit(pygame.font.Font('freesansbold.ttf', 30).render(user_text+'              ', True, white), (50, 300))
                pygame.display.update()
            while True:
                if spekret == 1:
                    break
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        brkbt=True
                        refresh()
                        display_surface.blit(pygame.font.Font('freesansbold.ttf', 30).render(user_text+'              ', True, white), (50, 300))
                        pygame.display.update()
                        if event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                            if user_text == '':
                                brk =1
                            refresh()
                            display_surface.blit(pygame.font.Font('freesansbold.ttf', 30).render(user_text+'              ', True, white), (50, 300))
                            pygame.display.update()
                        elif event.key == pygame.K_RETURN:
                            # Compute input
                            usertextls=user_text.split(' ')
                            spekretno=1
                            if user_text=='':
                                brk=1
                            elif usertextls[0] == "@":
                                refresh()
                                jsaid.insert(0, user_text)
                                history = open(file_location+"/Jimbot/Python/skills/history.py", "w")
                                history.write('jsaid='+str(jsaid))
                                history.close()
                                if mood == 5:
                                    mquestion(user_text)
                                else:
                                    question(user_text)
                                lasts=user_text
                                data.insert(0, int(mood))
                                if len(data) >= 5:
                                    data.pop(3)
                                history = open(file_location+"/Jimbot/Python/skills/history.py", "w")
                                history.write('jsaid='+str(jsaid)+"\n"+'rsponce='+str(rsponce)+"\n"+'crsponce='+str(crsponce))
                                history.close()
                                brk=1
                                user_text=''
                            else:
                                brk=1
                                #Run command in terminal
                                os.system("~/Jimbot/Bash/Jimbotterminal "+user_text+" &")
                                user_text=''
                            refresh()
                        elif event.key == pygame.K_RALT or event.key == pygame.K_LALT or event.key == pygame.K_RCTRL or event.key == pygame.K_LCTRL or event.key == pygame.K_TAB or event.key == pygame.K_ESCAPE:
                            pass
                        else:
                            user_text += event.unicode
                        # Clear input
                        display_surface.blit(pygame.font.Font('freesansbold.ttf', 30).render(user_text+'              ', True, white), (50, 300))
                        pygame.display.update()
                # Break loop
                if brk == 1:
                    break
        # Set up buttons
        elif event.type == pygame.QUIT:
            os.system('sudo killall -9 /bin/python3 && sudo killall -9 python3')
            sys.exit()
        elif f10k==True or keypressed == False and (event.type == pygame.MOUSEBUTTONDOWN or spekret ==1 or event.type == pygame.KEYDOWN):                
            x, y = pygame.mouse.get_pos()
            if brkbt==True or event.type == pygame.KEYDOWN or keypressed==True:
                brkbt=False
                break
            elif x >=700 and y <= 35 and not spekret == 1:
                os.system('xdg-open https://github.com/Mrpi314tech/Jimbot &')
            elif x >=400 and x<= 515 and y >= 40 and y <= 100 and not spekret == 1:
                os.system('~/Jimbot/Bash/Jimbotterminal python3 '+file_location+'/Jimbot/Python/Jimbotedit.py &')
                try:
                    import new_words as aword
                except ModuleNotFoundError:
                    import Python.new_words as aword
                try:
                    import new_com as acom
                except ModuleNotFoundError:
                    import Python.new_com as acom
                nwcoml=acom.word
                nrunl=acom.com
            elif x >=590 and x<= 685 and y >= 40 and y <= 90 and not spekret == 1:
                os.system("xdg-open "+file_location+"/Jimbot/images/HowTo.jpg &")
            elif x >=400 and x<= 570 and y >= 150 and y <= 200 and not spekret == 1:
                os.system('~/Jimbot/Bash/Jimbotterminal "cat ~/Jimbot/Python/skills/history.py && sleep 300" &')
            elif x >= 600 and x<=680 and y<=30:
                os.system('xdg-open https://github.com/Mrpi314tech/Jimbotskills &')
            elif x<=45 and y>=200 and y<=230:
                os.system('~/Jimbot/Bash/Jimbotterminal htop &')
            elif x>=400 and y>=250 and y<=280 and x<=535:
                os.system('~/Jimbot/Bash/Jimbotterminal ~/Jimbot/Bash/schedule.sh &')
            elif x<75 and y>=80 and y<=110:
                os.system('python3 ~/Jimbot/Python/stats.py &')
            elif x>=770 and y>=370:
                print('Updating Jimbot...')
                os.system('~/Jimbot/Bash/Jimbotterminal ~/Jimbot_update.sh &')
                prints('exiting...')
                os.system('sudo killall -9 /bin/python3 && sudo killall -9 python3')
                exit()
            if f10k == True or x >=265 and x<= 340 and y >= 340 or spekret==1 and spekretno ==0 or event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and spekretno ==0:
                # Press button/enter to speak
                # Reset variables
                spekret=0
                spekretno=0
                # Play sound
                pygame.mixer.music.load(file_location+"/Jimbot/sounds/answer.mp3")
                pygame.mixer.music.play()
                # Listen
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    if st == 0:
                        
                        st=1
                        past=['z','z','z','z']
                    print('Speak...')
                    audio=r.listen(source)
                    refresh()
                    try:
                        saidtxt=r.recognize_google(audio)
                        notned=0
                    except:
                        notned+=1
                        break
                # Set up history
                jsaid.insert(0, saidtxt)
                history = open(file_location+"/Jimbot/Python/skills/history.py", "w")
                history.write('jsaid='+str(jsaid))
                history.close()
                # Compute input
                if saidtxt == 'what' or 'pardon' in saidtxt or saidtxt == 'again' or saidtxt == 'repeat':
                    saidtxt=jsaid[1]
                if mood == 5:
                    mquestion(saidtxt)
                else:
                    question(saidtxt)
                lasts=saidtxt
                data.insert(0, int(mood))
                if len(data) >= 5:
                    data.pop(3)
                # Add to history
                history = open(file_location+"/Jimbot/Python/skills/history.py", "w")
                history.write('jsaid='+str(jsaid)+"\n"+'rsponce='+str(rsponce)+"\n"+'crsponce='+str(crsponce))
                history.close()
                ml=most_frequent(data)
                f10k=False
    # Reset varaible that senses the enter key
    spekretno=0
    # Update GUI
    pygame.display.update()
