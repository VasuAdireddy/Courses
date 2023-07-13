import pygame as pg
pg.init()

wid = 600
hei = 300
dis = pg.display.set_mode((wid,hei))
pg.display.set_caption("Adding Sounds")

# Load Sound effects
sound_1 = pg.mixer.Sound('sound(Bounce).wav')
sound_2 = pg.mixer.Sound('sound(Lose).wav')

# Play Sounds
sound_1.play()
pg.time.delay(2000) #2000 milliseconds
sound_2.play()
pg.time.delay(2000)

# changing volume of sounds
sound_2.set_volume(.2)
sound_2.play()

# Load Background music
pg.mixer.music.load('India_Epic_Action_Drums.mp3')

# Play and Stop the Music
pg.mixer.music.play(-1,0.0) #number of loops,start time
pg.time.delay(20000)
pg.mixer.music.stop()

run = True
while run:
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            run = False

pg.quit()