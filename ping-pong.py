from pygame import *
from random import randint
background_color = (0,0,255)
background = Surface((700,500))
background.fill(background_color)
window = display.set_mode((700,500))
game = True
finish = False
clock = time.Clock()
FPS = 60
font.init()
font2 = font.SysFont('Arial', 30)
win = font2.render('You WIN', True, (0, 255, 0))
loser = font2.render('You Lose', True, (255, 0 , 0))
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
 
       

    clock.tick(FPS)
    display.update()