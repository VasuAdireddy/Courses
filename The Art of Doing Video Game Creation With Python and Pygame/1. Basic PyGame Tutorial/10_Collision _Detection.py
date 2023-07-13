import pygame as pg,random
pg.init()

wid = 600
hei = 300
dis = pg.display.set_mode((wid,hei))
pg.display.set_caption("Collision Detection")

FPS = 60
clock = pg.time.Clock()

velocity = 5
dragon_image = pg.image.load("dragon_left.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25,25)

coin_image = pg.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.center = (wid//2,hei//2)

run = True
while run:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run = False
    
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and dragon_rect.left>0:
        dragon_rect.x -= velocity
    if keys[pg.K_RIGHT] and dragon_rect.right<wid:
        dragon_rect.x += velocity
    if keys[pg.K_UP] and dragon_rect.top>0:
        dragon_rect.y -= velocity
    if keys[pg.K_DOWN] and dragon_rect.bottom < hei:
        dragon_rect.y += velocity
    
    #check for collision
    if dragon_rect.colliderect(coin_rect):
        coin_rect.x = random.randint(0,wid-32)   #32 is pixel size of coin
        coin_rect.y = random.randint(0,hei -32)
    
    dis.fill((0,0,0))

    #draw rectangles to represent rectangles of each object
    pg.draw.rect(dis, (0,255,0),dragon_rect,1)
    pg.draw.rect(dis,(255,255,0),coin_rect,1)

    dis.blit(dragon_image,dragon_rect)
    dis.blit(coin_image,coin_rect)
    pg.display.update()

    clock.tick(FPS)

pg.quit()
