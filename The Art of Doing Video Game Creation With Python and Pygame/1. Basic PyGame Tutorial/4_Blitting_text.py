from tkinter import CENTER
import pygame as pg
pg.init()

wid = 600
hei = 300
dis = pg.display.set_mode((wid,hei))
pg.display.set_caption("Blitting Images")

green = (0,255,0)
black = (0,0,0)
dark_green = (10,50,10)

# See all available system fonts
#fonts = pg.font.get_fonts()
#for i in fonts:
#    print(i)

#load / define files
system_font = pg.font.SysFont('calibri',64)
custom_font = pg.font.Font("fontStyle.ttf",32)

# Define Text
system_text = system_font.render("Godavari pongindhi",True, green, dark_green)
system_text_rect = system_text.get_rect()
system_text_rect.center = (wid//2,hei//2)

custom_text = custom_font.render("Pichi Lan***ku",True, green)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (wid//2,hei//2 + 100)

run = True
while run:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run = False
    # Blit the text surface to the display surface
    dis.blit(system_text,system_text_rect)
    dis.blit(custom_text,custom_text_rect)
    pg.display.update()

pg.quit()