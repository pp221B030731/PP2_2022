import psycopg2
from configparser import ConfigParser
import csv


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


def add_num(name, num):
	commands = (
		f"""
		INSERT INTO accounts(username, tell)
		VALUES('{name}', '{num}');
		"""
		)
	act(commands)


def del_num(name):
	commands = (
		f"""
		DELETE FROM accounts WHERE accounts.username = '{name}';
		"""
		)
	act(commands)


def upd_num(name, num):
	commands = (
		f"""
		UPDATE accounts SET tell = '{num}' WHERE username = '{name}';
		"""
		)
	act(commands)


def upd_name(name, num):
	commands = (
		f"""
		UPDATE accounts SET username = '{name}' WHERE tell = '{num}';
		"""
		)
	act(commands)


def show(f):
	commands = [
		"""
		select * from accounts;
		""",
		"""
		select * from accounts
		order by username;
		""",
		"""
		select * from accounts
		order by tell;
		"""
		]
	con = None
	try: 
		params = config()
		con = psycopg2.connect(**params)
		cur = con.cursor()
		cur.execute(commands[f])
		print(cur.fetchall(), '\n')
		cur.close()
		con.commit()
	except Exception as e:
		print(str(e))
	if con is not None:
		con.close()



while 1:
	c = int(input('1 - Add, 2 - Del, 3 - Update, 4 - quite, 5 - show, 6 - csv\n'))
	if c == 1:
		name = str(input('Name:\n'))
		num = str(input('Number:\n'))
		try:
			add_num(name, num)
			print("Succes\n")
		except:
			print("Error")
			break
	elif c == 2:
		name = str((input('Name:\n')))
		try:
			del_num(name)
			print("Succes\n")
		except:
			print("Error")
			break
	elif c == 3:
		flag = int(input('1 - Change name, 2 - Change number\n'))
		try:
			if flag == 1:
				num = str(input('Number:\n'))		
				name = str(input('Name:\n'))
				upd_name(name, num)
			else:		
				name = str(input('Name:\n'))
				num = str(input('Number:\n'))
				upd_num(name, num)
			print("Succes\n")
		except:
			print("Error")
			break
	elif c == 4:
		break
	elif c == 5:
		f = int(input('Filter mode: 0 - date, 1 - name, 2 - number\n'))
		show(f)
	elif c == 6:
		with open('data.csv') as f:
			r = csv.reader(f)
			for i in r:
				add_num(i[0], i[1])