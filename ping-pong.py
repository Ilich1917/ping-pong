from pygame import *
from random import randint
class GameSprite (sprite.Sprite):
    def __init__(self, image_file, player_x, player_y, player_speed, width, hight):
        super().__init__()
        #self.image = transform.scale(image.load(image_file),(width, hight))
        self.image = Surface((width,hight))
        self.image.fill((255,255,255))
        self.speed = player_speed
        self.rect  = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = 'left'
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player1 (GameSprite):
    def update(self):
        keys =  key.get_pressed()
        if keys[K_w] and self.rect.y>0:
             self.rect.y -= self.speed
        if keys[K_s] and self.rect.y<400:
            self.rect.y += self.speed
        #if keys[K_W] and self.rect.y>0:
         #   self.rect.x -= self.speed
        #if keys[K_S] and self.rect.y<650:
           # self.rect.x += self.speed
background_color = (0,0,255)
background = Surface((700,500))
background.fill(background_color)
window = display.set_mode((700,500))
game = True
finish = False
player1 = Player1('rocket.png',325,450,10, 50 , 50)
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
        player1.reset()
        player1.update()
       

    clock.tick(FPS)
    display.update()