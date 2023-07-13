import pygame as pg
pg.init()

wid = 1100
hei = 800
dis = pg.display.set_mode((wid,hei))
pg.display.set_caption("Mouse Movements")

dragon_image = pg.image.load("Sahithi.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (900,100)

dragon1_image = pg.image.load("Mercy.png")
dragon1_rect = dragon1_image.get_rect()
dragon1_rect.topleft = (25,25)

# move based on mouse clicks

run = True
while run:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run = False
        # event for mouse click
        print(i)
        if i.type == pg.MOUSEMOTION and i.buttons[0]==1 and (i.pos[0] == (dragon1_rect.centerx - 100) | i.pos[0] == (dragon1_rect.centerx +100) | i.pos[0] == (dragon1_rect.centery - 150) | i.pos[0] == (dragon1_rect.centery +150)) :
            mouse1_x = i.pos[0]          #pos is a tuple with 2 indexs x coordinate, y cordinate
            mouse1_y = i.pos[1]
            dragon1_rect.centerx = mouse1_x
            dragon1_rect.centery = mouse1_y
        # event for moving image along with mouse while holding left button on mouse
        # buttons is 3 index tupple {left click, scroll click, right click}
        if i.type == pg.MOUSEMOTION and i.buttons[0]==1 and (i.pos[0] == (dragon_rect.centerx - 25) | i.pos[0] == (dragon_rect.centerx +25) | i.pos[0] == (dragon_rect.centery - 25) | i.pos[0] == (dragon_rect.centery +25)):
            mouse_x = i.pos[0]
            mouse_y = i.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y

    
    dis.fill((0,0,0))
    dis.blit(dragon_image,dragon_rect)
    dis.blit(dragon1_image,dragon1_rect)
    pg.display.update()

pg.quit()