import pygame as pg
import random


pg.init()

# Settings
S_W, S_H = 400, 600
fps = 30
SPEED = 5
SCORE = 0
running = True
dead = False
y1 = 0
counter = SCORE

# Music
pg.mixer.music.load("background.wav")
pg.mixer.music.play(-1)

# Font
font = pg.font.SysFont("Verdana", 60)
font_small = pg.font.SysFont("Verdana", 20)


# Display
clock = pg.time.Clock()
screen = pg.display.set_mode((S_W, S_H))
pg.display.set_caption("Race")
bg1 = pg.image.load("road.png")
bg2 = pg.image.load("road.png")

go = font.render("Game Over", True, (0, 0, 0))

# Player

class Player(pg.sprite.Sprite):
	def __init__(self):
			super().__init__()
			self.image = pg.image.load("Player.png")
			self.rect = self.image.get_rect()
			self.rect.center = (160, 520)
	
	def move(self):
		k = pg.key.get_pressed()
		if k[pg.K_a]:
			if self.rect.left > 44:
				self.rect.move_ip(-7, 0)
		if k[pg.K_d]:
			if self.rect.right < 356:
				self.rect.move_ip(7, 0)


# Enemy

class Enemy(pg.sprite.Sprite):
	def __init__(self, y):
		super().__init__()
		self.y0 = y
		self.image = pg.image.load("Enemy.png")
		self.rect = self.image.get_rect()
		self.rect.center = (random.randint(40, 360), self.y0)

	def move(self):
		self.rect.move_ip(0, SPEED+2)
		if self.rect.top > 600:
			self.rect.center = (random.randint(40, 360), self.y0)


# Coins

class Coins(pg.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.type = random.randint(1, 10)
		if self.type == 1:
			self.letter = 'g'
			self.cost = 3
		elif 2 <= self.type < 5:
			self.letter = 's'
			self.cost = 2
		else:
			self.letter = 'c'
			self.cost = 1
		self.image = pg.image.load(self.letter+"coin.png")
		self.rect = self.image.get_rect()
		self.rect.center = (random.randint(40, 360), -50)


	def change(self):
		self.type = random.randint(1, 10)
		if self.type == 1:
			self.letter = 'g'
			self.cost = 5
		elif 2 <= self.type < 5:
			self.letter = 's'
			self.cost = 2
		else:
			self.letter = 'c'
			self.cost = 1
		self.image = pg.image.load(self.letter+"coin.png")
		self.rect = self.image.get_rect()
		self.rect.center = (random.randint(40, 360), -50)


	def move(self):
		self.rect.move_ip(0, SPEED)
		if self.rect.top > 600:
			self.change()

	
# Objects

player = Player()
enemy1 = Enemy(-93)
enemy2 = Enemy(-186)
coin = Coins()

# Groups
enemies = pg.sprite.Group()
enemies.add(enemy1)
enemies.add(enemy2)
al_l = pg.sprite.Group()
al_l.add(enemy1)
al_l.add(enemy2)
al_l.add(player)
al_l.add(coin)
coins = pg.sprite.Group()
coins.add(coin)

INC_SPEED = pg.USEREVENT + 1
pg.time.set_timer(INC_SPEED, 2000)


# MAIN
while running:

	clock.tick(fps)

	for e in pg.event.get():
		if e.type == pg.QUIT:
			running = False
		if e.type == INC_SPEED:
			SPEED += 100

	if not dead:
		# Scores
		scores = font_small.render(str(SCORE), True, (0, 0, 0))

		# Game
		y1 += SPEED
		if y1 >= 600:
			y1 = 0
		screen.blit(bg1, (0, y1))
		screen.blit(bg2, (0, y1-600))
		
		if counter >= 10:
			counter = 0
			SPEED += 1

		for o in al_l:
			o.move()
			screen.blit(o.image, o.rect)

		screen.blit(scores, (10, 10))

		if pg.sprite.spritecollideany(player, coins):
			pg.mixer.Sound("coin.wav").play()
			SCORE += coin.cost
			counter += coin.cost
			coin.change()

		if pg.sprite.spritecollideany(player, enemies):
			pg.mixer.music.pause()
			SCORE = -1
			dead =True

	else:
		if SCORE == -1:
			pg.mixer.Sound('crash.wav').play()
			SCORE = 0

		screen.fill((255, 0, 0))
		screen.blit(go, (30, 250))
		
		for o in al_l:
			o.kill()

	pg.display.update()


pg.quit()
