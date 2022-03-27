import pygame as pg 
import datetime


pg.init()

clock = pg.time.Clock()

bg = pg.transform.scale(pg.image.load("m_bg.jpg"), (800, 600))
l =  pg.transform.scale(pg.image.load("l_h.png"), (800, 600))
r =  pg.transform.scale(pg.image.load("r_h.png"), (1200, 900))

def rot_center(surf, image, angle, x, y):
    
    rotated_image = pg.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)
    surf.blit(rotated_image, new_rect)



screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Clock")

run = True

while run:
	t = datetime.datetime.now()


	clock.tick(30)
	for e in pg.event.get():
		if e.type == pg.QUIT:
			run = False

	screen.blit(bg, (0, 0))
	rot_center(screen, l, -t.second*(6), 400, 300)
	rot_center(screen, r, -t.minute*(6), 400, 300)

	pg.display.update()

pg.quit()
