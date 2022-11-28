import pygame as pg

# initialize pygame
pg.init()

# create a display ans set its caption
window_width = 600
window_height = 300
display_surface = pg.display.set_mode((window_width,window_height))
pg.display.set_caption("First Game")

# main game loop
running = True
while running:
    # loop through a list of Event objects that have occured
    for evnt in pg.event.get():
        print(evnt)
        if evnt.type == pg.QUIT:
            running = False

# End of Game
pg.quit()