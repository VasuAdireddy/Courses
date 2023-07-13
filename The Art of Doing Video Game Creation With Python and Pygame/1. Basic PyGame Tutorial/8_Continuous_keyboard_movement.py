import pygame as pg
pg.init()

wid = 600
hei = 300
dis = pg.display.set_mode((wid,hei))
pg.display.set_caption("Continuous_Keyboard_Movement")

# define clock / set FPS -helps to set same speed in every computer
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
    #get a list of all keys currently being pressed
    keys = pg.key.get_pressed()
    
    #moving dragon continuously
    if keys[pg.K_LEFT]:
        dragon_rect.x -= velocity
    if keys[pg.K_RIGHT]:
        dragon_rect.x += velocity
    if keys[pg.K_UP]:
        dragon_rect.y -= velocity
    if keys[pg.K_DOWN]:
        dragon_rect.y += velocity
    
    dis.fill((0,0,0))
    dis.blit(dragon_image,dragon_rect)
    pg.display.update()

    #tick the clock
    #if FPS is low, movement is low, if FPS is high, movement is high
    clock.tick(FPS) 

pg.quit()