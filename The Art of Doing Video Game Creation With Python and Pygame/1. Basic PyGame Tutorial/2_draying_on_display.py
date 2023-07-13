import pygame as pg
pg.init()

wid = 600
hei = 600
disp = pg.display.set_mode((wid,hei))
pg.display.set_caption("Drawing Objects")

#define colours as RGB tuples
black = (0,0,0)
white = (255,255,255)           # we can create different shades to these coulours
red = (255,0,0)                 # by changing the numbers, instead of 255- 100/ 110 or any
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
magneta = (255,0,255)

# give background colour
disp.fill(blue)

# Draw various shapes
# Line(surface,color,starting point, ending point, thickness)
pg.draw.line(disp,yellow,(0,0),(100,100),5)
pg.draw.line(disp,red,(100,100),(200,300),10)

# Circle(surface, color, center, radius, thickness...0 for fill)
pg.draw.circle(disp,white,(wid//2,hei//2),200,6)
pg.draw.circle(disp,yellow,(wid//2,hei//2),195,0) #thickness 0 to fill the circle

# Rectangle(surface, color, (top-left x, top-left y, width, height))
pg.draw.rect(disp,cyan,(400,0,200,100))
pg.draw.rect(disp,green,(500,100,100,100))  #this is for square



running  = True
while running:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            running = False
    # update the display, if we are adding any updates
    pg.display.update()

pg.quit()