from pygame import *

win = display.set_mode((600,500))
display.set_caption = ("ПИНГ ПОНГ")
flag = True
FPS = 60
clock = time.Clock()
color = 153,204,255
win.fill(color)
while flag:


    for e in event.get():
        if e.type == QUIT:
            flag = False
    clock.tick(FPS)
    display.update()

