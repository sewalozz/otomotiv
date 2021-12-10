import pygame as pg
import sys 
import random
pg.init()
en, boy = 640, 480
# RGB 8bitlik her renk 2^8 = 256 ( 0-255 )
RENKLER = {
    "beyaz" : (255,255,0xFF),
    "siyah" : (0,0,0),
    "kirmizi" : (255,0,0),
    "yesil" : (0,255,0),
    "mavi" : (0,0,255),
    "cyan" : (0,255,255),
    "mor" : (109, 48, 184)
}
ekran = pg.display.set_mode((en,boy))
clock = pg.time.Clock()
x,y = 0,0
while True:
    ekran.fill(RENKLER["mor"])
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
    # x , y = pg.mouse.get_pos()
        # if event.type == pg.KEYDOWN:
        #     if(event.key == pg.K_UP):
        #         y -= 5
        #     if(event.key == pg.K_DOWN) :
        #         y += 5

        #     if(event.key == pg.K_LEFT) :
        #         x -= 5
        #     if(event.key == pg.K_RIGHT) :
        #         x += 5
    keys = pg.key.get_pressed()
    x = keys[pg.K_RIGHT] + x
    pg.draw.circle(ekran,RENKLER["cyan"],(x,y),25)
    pg.display.flip()
    clock.tick(30)
