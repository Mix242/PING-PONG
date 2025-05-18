from pygame import *
from random import *
win = display.set_mode((600,500))
display.set_caption = ("ПИНГ ПОНГ")
flag = True
finisg = False
FPS = 60
clock = time.Clock()
color = 153,204,255

speed_x = randint(3,4)
if speed_x == 3:
    speed_x*=-1
speed_y = randint(3,4)
if speed_y == 3:
    speed_x*=-1

class GameSprite(sprite.Sprite):
    def __init__(self,pl_image,pl_y,pl_x,pl_speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(pl_image),(size_x,size_y))
        self.speed = pl_speed
        self.rect =self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
    def show_pl(self):
        win.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 2:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= 380:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 2:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <= 380:
            self.rect.y += self.speed

rocket_one = Player("platform.png",250,10,10,30,130)
rocket_two = Player("platform_two.png",250,550,10,30,130)
ball = GameSprite("ball.png",300,250,3,100,100)


while flag:
    for e in event.get():
        if e.type == QUIT:
            flag = False
    
    win.fill(color)
    rocket_one.show_pl()
    rocket_two.show_pl()
    if finisg != True:
        rocket_one.update_l()
        rocket_two.update_r()
        ball.show_pl()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y < 0 or ball.rect.y > 420:
            speed_y *= -1
        if sprite.collide_rect(rocket_one,ball) or sprite.collide_rect(rocket_two,ball):
            speed_x *= -1.1
            speed_y *= -1.1
        
            

    clock.tick(FPS)
    display.update()

