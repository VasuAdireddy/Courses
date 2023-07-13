import pygame as pg
pg.init()

wid = 600
hei = 300
dis = pg.display.set_mode((wid,hei))
pg.display.set_caption("Blitting Images")

# Create Images...returns a surface object with image drawn on it
# We can then get the rect of the surface and use the rect to position the image
dragon_left = pg.image.load("dragon_left.png") #inside the brackets we need to give path of image, since its in same path as the file, here we directly write name
dragon_left_rect = dragon_left.get_rect()  #this will give arectangle arounf=d our image
dragon_left_rect.topleft = (0,0)

dragon_right = pg.image.load("dragon_right.png")
dragon_right_rect = dragon_right.get_rect()
dragon_right_rect.topright = (wid,0)


run = True
while run:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run = False
    #Blit (copy) a surface object at the given coordinates to our display
    dis.blit(dragon_left,dragon_left_rect)
    dis.blit(dragon_right,dragon_right_rect)

    pg.draw.line(dis, (255,255,255),(0,123),(wid,123),2)

    pg.display.update()

pg.quit()