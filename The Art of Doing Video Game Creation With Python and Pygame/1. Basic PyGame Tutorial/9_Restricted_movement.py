import pygame as pg
pg.init()

wid = 600
hei = 300
dis = pg.display.set_mode((wid,hei))
pg.display.set_caption("Continuous_Keyboard_Movement")

FPS = 60
clock = pg.time.Clock()

velocity = 5
dragon_image = pg.image.load("dragon_left.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (wid//2,hei//2)

run = True
while run:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run = False
    
    keys = pg.key.get_pressed()
    
    # restric the movement of image and movement using WSAD
    if (keys[pg.K_LEFT] or keys[pg.K_a]) and dragon_rect.left > 0:
        dragon_rect.x -= velocity
    if (keys[pg.K_RIGHT] or keys[pg.K_d]) and dragon_rect.right < wid:
        dragon_rect.x += velocity
    if (keys[pg.K_UP] or keys[pg.K_w]) and dragon_rect.top > 0:
        dragon_rect.y -= velocity
    if (keys[pg.K_DOWN] or keys[pg.K_s]) and dragon_rect.bottom < hei:
        dragon_rect.y += velocity
    
    dis.fill((0,0,0))
    dis.blit(dragon_image,dragon_rect)
    pg.display.update()

    clock.tick(FPS) 

pg.quit()