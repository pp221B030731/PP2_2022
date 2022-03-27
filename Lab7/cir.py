import pygame as pg 

pg.init()

clock = pg.time.Clock()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Cir")

x, y = 25, 25

run = True

while run:
	
	clock.tick(30)

	for e in pg.event.get():
		if e.type == pg.QUIT:
			run = False
		if e.type == pg.KEYDOWN:
			if e.key == pg.K_RIGHT:
				x += 20
				if x > 775:
					x = 775							
			if e.key == pg.K_LEFT:
				x -= 20
				if x < 25:
					x = 25	
			if e.key == pg.K_DOWN:
				y += 20
				if y > 575:
					y = 575
			if e.key == pg.K_UP:
				y -= 20
				if y < 25:
					y = 25

	screen.fill((255, 255, 255))
	pg.draw.circle(screen, (255,0,0), (x, y), 25)
	pg.display.update()



pg.quit()
