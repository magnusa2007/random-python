import pygame as pg
import math, os
from camera import getFace

rot = pg.transform.rotate

scale =  pg.transform.scale


pg.init()
bg = pg.display.set_mode((312, 312))
body1 = pg.image.load(r'media\layer1.png')
body2 = pg.image.load(r'media\layer2.png')
body3 = pg.image.load(r'media\layer3.png')

eye = pg.image.load(r'media\eye.png')
cat = pg.image.load(r'media\cat.png')



catmode = False
pg.display.flip()
while True:
    for event in pg.event.get():
        if event.type == 769:
            if event.key == pg.K_c:
                catmode = not catmode
                print('Miow')
    face = getFace()
    x,y = face['nose']
    aX,aY = face['nose']
    bX,bY = face['forhead']
    size = math.dist(face['nose'],face['forhead'])*10
    mouth = int((face["lip"][1]-face["blip"][1])*-size*600)
    os.system('cls')
    print(f'mouth: {int((face["lip"][1]-face["blip"][1])*-size*100)}\nsize:{size}')
    mouth = min(29,mouth)
    mouth = max(0,mouth)
    radius=math.degrees(math.atan2(aY-bY,aX-bX))-90
    bg.fill((47, 235, 44))
    mag = pg.Surface((312, 312))
    mag.fill((47, 235, 44))
    mag.blit(body1, (0,0))
    mag.blit(body2, (0,mouth))
    mag.blit(body3, (0,0))
    mag.blit(eye, (60,y+100))
    if catmode: mag.blit(cat,(0,0))
    bg.blit(rot(mag,radius),(-(x*312-156),y*312-156))
    pg.display.update()

    
    
    
    