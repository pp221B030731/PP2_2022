import pygame as pg
import random

pg.init()

clock = pg.time.Clock()

screen = pg.display.set_mode((600, 600))
pg.display.set_caption("Snake")

fps = 10

f = pg.font.SysFont(None, 20)

running = True
game_over = False
append = False

bg = pg.transform.scale(pg.image.load('bg.jpg'), (600, 600))
coin = pg.transform.scale(pg.image.load("coin.png"), (20, 20))
score = 0 

body = []
h_x, h_y, h_d = 300, 300, 1 # 1 - right, -1 - left, 2 - up, -2 - down
b_x, b_y = -1, -1
v = 20
v_x, v_y = 20, 0

c_x, c_y = 40, 40

while running:

	clock.tick(fps)


	for e in pg.event.get():
		if e.type == pg.QUIT:
			running = False
		if e.type == pg.KEYDOWN:
			if e.key == pg.K_LEFT:
				if abs(h_d) != 1:
					h_d = -1
					v_x = -v
					v_y = 0	
			if e.key == pg.K_RIGHT:
				if abs(h_d) != 1:
					h_d = 1
					v_x = v
					v_y = 0
			if e.key == pg.K_UP:
				if abs(h_d) != 2:
					h_d = 2
					v_x = 0
					v_y = -v
			if e.key == pg.K_DOWN:
				if abs(h_d) != 2:
					h_d = -2
					v_x = 0
					v_y = v	
	if not game_over:	
		# Snake movement
		body.append([h_x, h_y])
		body.pop(0)
		if append:
			pg.mixer.Sound("hap.wav").play()
			body.append([h_x, h_y])
			score += 1
			append = False	
		h_x += v_x
		h_y += v_y

		if h_x < 0 or h_x > 580 or h_y < 0 or h_y > 580:
			game_over = True

		fps = 10 + 2*score//4
		#COIN
		while h_x == c_x and h_y == c_y:			
			c_x = random.randint(0, 29)*20
			c_y = random.randint(0, 29)*20
			append = True

		screen.blit(bg, (0, 0))
		screen.blit(coin, (c_x, c_y))
		pg.draw.rect(screen, (255, 100, 0), (h_x, h_y, 20, 20))

		for i in body:
			while i[0] == c_x and i[1] == c_y:			
				c_x = random.randint(0, 29)*20
				c_y = random.randint(0, 29)*20
			if h_x == i[0] and h_y == i[1]:
				game_over = True
				break
			pg.draw.rect(screen, (255, 150, 0), (i[0], i[1], 20, 20))
		screen.blit(f.render("Lvl: {}    Score: {}".format(score//4, score), True, (255, 255, 0)), (10, 10))
	else:
		screen.fill((255, 0, 0))
		screen.blit(f.render("GAME OVER", True, (255, 255, 255)), (250, 250))
	pg.display.update()

pg.quit()
