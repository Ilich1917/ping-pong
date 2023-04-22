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
class Player2 (GameSprite):
    def update(self):
        keys =  key.get_pressed()
        if keys[K_UP] and self.rect.y>0:
             self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y<400:
            self.rect.y += self.speed
        #if keys[K_W] and self.rect.y>0:
         #   self.rect.x -= self.speed
        #if keys[K_S] and self.rect.y<650:
           # self.rect.x += self.speed
    
class Ball (GameSprite):
    def __init__(self, image_file, player_x, player_y, speed, width, hight):
        super().__init__(image_file, player_x, player_y, speed, width, hight)
        self.image.fill((0 , 0 , 255))
        draw.circle(self.image, (25,100,60), (width // 2 , hight // 2), width // 2 )
        self.speed_x = speed
        self.speed_y = speed
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if (self.rect.y < 0) or (self.rect.y > 490):
            self.speed_y *= -1

background_color = (0,0,255)
background = Surface((700,500))
background.fill(background_color)
window = display.set_mode((700,500))
game = True
finish = False
player1 = Player1('rocket.png',60,200,10, 20 , 100)
player2 = Player2('rocket.png',640,200,10, 20 , 100)
ball = Ball('rocket.png',100,400,2, 10 , 10)
clock = time.Clock()
FPS = 60
font.init()
font2 = font.SysFont('Arial', 30)

loser1 = font2.render('Player1 Lose', True, (0, 255, 0))
loser2 = font2.render('Player2 Lose', True, (0, 255 , 0))
        
    
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        player1.reset()
        player1.update()
        player2.reset()
        player2.update()
        ball.reset()
        ball.update()

        if sprite.collide_rect(ball, player1):
            ball.speed_x *= -1
        if sprite.collide_rect(ball, player2):
            ball.speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(loser1,(300,250))
        if ball.rect.x > 700:
            finish = True
            window.blit(loser2,(300,250))
       

    clock.tick(FPS)
    display.update()