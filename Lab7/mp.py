import pygame as pg 

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("MP")

run = True

songs = ['1.mp3', '2.mp3']

pg.mixer.music.load(songs[0])
pg.mixer.music.play(-1)
i = 0

while run:

	for e in pg.event.get():
		if e.type == pg.QUIT:
			run = False
		if e.type == pg.KEYDOWN:
			if e.key == pg.K_RIGHT:
				i += 1
				if i >= len(songs):
					i = 0
				pg.mixer.music.stop()
				pg.mixer.music.load(songs[i])
				pg.mixer.music.play(-1)
			elif e.key == pg.K_LEFT:
				i -= 1
				if i < 0:
					i = len(songs)-1
				pg.mixer.music.stop()
				pg.mixer.music.load(songs[i])
				pg.mixer.music.play(-1)
			elif e.key == pg.K_DOWN:
				pg.mixer.music.pause()
			elif e.key == pg.K_UP:
				pg.mixer.music.unpause()

	screen.fill((255, 255, 255))
	pg.display.update()


pg.quit()
