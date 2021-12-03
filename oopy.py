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
x = en // 2
y = 15
dusme_hizi = 5
while True:
    ekran.fill(RENKLER["mor"])
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
    if(y >= boy-15 or y <= 14):
        dusme_hizi *= -1
    y += dusme_hizi
    for i in range(10):
        pg.draw.circle(ekran,RENKLER["cyan"],(random.randrange(10,620),y),random.randrange(15,25))
    pg.display.flip()
    clock.tick(30)