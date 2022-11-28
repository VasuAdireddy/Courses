import pygame as pg
pg.init()

wid = 600
hei = 300
dis = pg.display.set_mode((wid,hei))
pg.display.set_caption("Discrete Movement")


#Set game values
velocity = 20

# Load Images
dragon_image = pg.image.load("dragon_left.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = wid//2
dragon_rect.bottom = hei


run =True
while run:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run = False
        # check for discrete movement
        if i.type == pg.KEYDOWN:
            if i.key == pg.K_LEFT:
                dragon_rect.x -= velocity 
            if i.key ==pg.K_RIGHT:
                dragon_rect.x += velocity
            if i.key == pg.K_UP:
                dragon_rect.y -= velocity
            if i.key == pg.K_DOWN:
                dragon_rect.y += velocity
    
    #fill the display surface to clear/cover old images
    dis.fill((0,0,0))

    dis.blit(dragon_image,dragon_rect)
    pg.display.update()


pg.quit()