import pygame as pg
import random
import psycopg2
from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
	parser = ConfigParser()
	parser.read(filename)
	db = {}
	if parser.has_section(section):
		params = parser.items(section)
		for param in params:
			db[param[0]] = param[1]
	else:
		raise Exception('Error')
	return db


def act(commands):
	con = None
	try: 
		params = config()
		con = psycopg2.connect(**params)
		cur = con.cursor()
		cur.execute(commands)
		cur.close()
		con.commit()
	except Exception as e:
		print(str(e))
	if con is not None:
		con.close()


pg.init()

name = str(input('Username\n'))
past_lvl = 0
flag = False

con = None
try: 
	params = config()
	con = psycopg2.connect(**params)
	cur = con.cursor()
	cur.execute('select * from users')
	for i in cur.fetchall():
		if i[0] == name:
			past_lvl = i[1]
			flag = True
			break
	cur.close()
	con.commit()
except Exception as e:
	print(str(e))
if con is not None:
	con.close()

clock = pg.time.Clock()

screen = pg.display.set_mode((600, 600))
pg.display.set_caption("Snake")

fps = 10
text = ''

f = pg.font.SysFont(None, 20)

running = True
game_over = False
append = False
game_pause = True
once = True

UPD = pg.USEREVENT + 1
pg.time.set_timer(UPD, 5000)

bg = pg.transform.scale(pg.image.load('bg.jpg'), (600, 600))
gcoin = pg.transform.scale(pg.image.load("gcoin.png"), (20, 20))
scoin = pg.transform.scale(pg.image.load("scoin.png"), (20, 20))
ccoin = pg.transform.scale(pg.image.load("ccoin.png"), (20, 20))

score = past_lvl

body = []
h_x, h_y, h_d = 300, 300, 1 # 1 - right, -1 - left, 2 - up, -2 - down
b_x, b_y = -1, -1
v = 20
v_x, v_y = 20, 0

c_x, c_y = 40, 40
g_x, g_y = 80, 80
s_x, s_y = 120, 120

def upd():
	global c_x, c_y, s_y, s_x, g_y, g_x
	c_x = random.randint(0, 29)*20
	c_y = random.randint(0, 29)*20
	g_x = random.randint(0, 29)*20
	g_y = random.randint(0, 29)*20	
	s_x = random.randint(0, 29)*20
	s_y = random.randint(0, 29)*20
	for i in body:
		while i[0] == c_x and i[1] == c_y:			
			c_x = random.randint(0, 29)*20
			c_y = random.randint(0, 29)*20
		while i[0] == g_x and i[1] == g_y:			
			g_x = random.randint(0, 29)*20
			g_y = random.randint(0, 29)*20
		while i[0] == s_x and i[1] == s_y:			
			s_x = random.randint(0, 29)*20
			s_y = random.randint(0, 29)*20


while running:

	clock.tick(fps)


	for e in pg.event.get():
		if e.type == pg.QUIT:
			running = False
			if not flag:
				act(f'''INSERT INTO users(name, lvl)
					VALUES('{name}', '{score}');''')
			else:
				act(f"UPDATE users SET lvl = '{score}' WHERE name = '{name}';")
		if e.type == UPD and game_pause == False:
			upd()
		if e.type == pg.KEYDOWN:
			if e.key == pg.K_LEFT:
				if abs(h_d) != 1:
					h_d = -1
					v_x = -v
					v_y = 0	
					game_pause = False
			if e.key == pg.K_RIGHT:
				if abs(h_d) != 1:
					h_d = 1
					v_x = v
					v_y = 0
					game_pause = False
			if e.key == pg.K_UP:
				if abs(h_d) != 2:
					h_d = 2
					v_x = 0
					v_y = -v
					game_pause = False
			if e.key == pg.K_DOWN:
				if abs(h_d) != 2:
					h_d = -2
					v_x = 0
					v_y = v	
					game_pause = False
			if e.key == pg.K_ESCAPE:
				game_pause = True

	if not game_over:	
		# Snake movement
		if not game_pause:
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
				if not flag:
					act(f'''INSERT INTO users(name, lvl)
					VALUES('{name}', '{score}');''')
				else:
					act(f"UPDATE users SET lvl = '{score}' WHERE name = '{name}';")
		
				fps = 10 + 2*score//4
			#COIN
			while h_x == c_x and h_y == c_y:			
				c_x = random.randint(0, 29)*20
				c_y = random.randint(0, 29)*20
				append = True

			while h_x == s_x and h_y == s_y:			
				s_x = random.randint(0, 29)*20
				s_y = random.randint(0, 29)*20
				append = True

			while h_x == g_x and h_y == g_y:			
				g_x = random.randint(0, 29)*20
				g_y = random.randint(0, 29)*20
				append = True

		screen.blit(bg, (0, 0))
		screen.blit(ccoin, (c_x, c_y))
		screen.blit(gcoin, (g_x, g_y))
		screen.blit(scoin, (s_x, s_y))
		pg.draw.rect(screen, (255, 100, 0), (h_x, h_y, 20, 20))

		for i in body:
			while i[0] == c_x and i[1] == c_y:			
				c_x = random.randint(0, 29)*20
				c_y = random.randint(0, 29)*20
			while i[0] == g_x and i[1] == g_y:			
				g_x = random.randint(0, 29)*20
				g_y = random.randint(0, 29)*20
			while i[0] == s_x and i[1] == s_y:			
				s_x = random.randint(0, 29)*20
				s_y = random.randint(0, 29)*20
			if h_x == i[0] and h_y == i[1]:
				game_over = True
				if not flag:
					act(f'''INSERT INTO users(name, lvl)
					VALUES('{name}', '{score}');''')
				else:
					act(f"UPDATE users SET lvl = '{score}' WHERE name = '{name}';")
				break
			pg.draw.rect(screen, (255, 150, 0), (i[0], i[1], 20, 20))
		screen.blit(f.render("Lvl: {}    Score: {}".format(score//4, score), True, (255, 255, 0)), (10, 10))
		if game_pause:
			pg.draw.rect(screen, ('grey'), (225, 150, 50, 170))
			pg.draw.rect(screen, ('grey'), (325, 150, 50,170))
	else:
		if once:		
			once = False
			con = None
			try: 
				params = config()
				con = psycopg2.connect(**params)
				cur = con.cursor()
				cur.execute(f'select * from users;')
				text = cur.fetchall()
				st = []
				for i in text:
					st.append(str(i[0]) + ' : ' + str(i[1]))
				cur.close()
				con.commit()
			except Exception as e:
				print(str(e))
			if con is not None:
				con.close()
		screen.fill((255, 0, 0))
		screen.blit(f.render("GAME OVER", True, (255, 255, 255)), (250, 50))
		for k in range(len(st)):
			screen.blit(f.render(st[k], True, (255, 255, 255)), (50, 100+k*40))
	pg.display.update()

pg.quit()
