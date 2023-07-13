import pygame as pg
pg.init()

wid = 600
hei = 300
dis = pg.display.set_mode((wid,hei))
pg.display.set_caption("Mouse Movements")

dragon_image = pg.image.load("dragon_left.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25,25)

# move based on mouse clicks

run = True
while run:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run = False
        # event for mouse click
        if i.type == pg.MOUSEBUTTONDOWN:
            mouse_x = i.pos[0]          #pos is a tuple with 2 indexs x coordinate, y cordinate
            mouse_y = i.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y
        # event for moving image along with mouse while holding left button on mouse
        # buttons is 3 index tupple {left click, scroll click, right click}
        if i.type == pg.MOUSEMOTION and i.buttons[0]==1:
            mouse_x = i.pos[0]
            mouse_y = i.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y

    
    dis.fill((0,0,0))
    dis.blit(dragon_image,dragon_rect)
    pg.display.update()

pg.quit()