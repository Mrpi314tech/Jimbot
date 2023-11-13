# import pygame module in this program
import pygame
import os
import time
import socket
import psutil
import random
import threading
ip_address = os.popen('hostname -I').read().split(' ')[0]
file_location=os.path.expanduser('~')
pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (56, 182, 255)
X = 350
Y = 120
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('stats')
pygame.display.set_icon(pygame.image.load(file_location+'/Jimbot/images/Jimbot.png'))
font = pygame.font.Font('freesansbold.ttf', 32)
display_surface.fill(blue)
pygame.display.update()
pygame.display.flip()
TM_var="TM"
gameypos=330
lazerx=800
playgame=False
lazery=random.choice(range(0, 400))
while True:
    RAM=os.popen('free -h').read()
    RAM=RAM.split('\n')
    RAM=RAM[1].split('      ')
    I1, I2, I3=psutil.getloadavg()
    cpu_round=str((I3/os.cpu_count())*100).split('.')[0]
    try:
        if int(cpu_round[1]) >= 0.5:
            cpu_usage=str(int(cpu_round)+1)
        else:
            cpu_usage=cpu_round
    except IndexError:
        cpu_usage=cpu_round
    display_surface.fill(blue)
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 30).render(ip_address, True, white), (0, 0))
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 30).render('RAM: '+RAM[2].replace(' ', '')+' of '+RAM[1].replace(' ', ''), True, white), (0, 40))
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 30).render("CPU: "+cpu_usage+"%", True, white), (0, 80))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()