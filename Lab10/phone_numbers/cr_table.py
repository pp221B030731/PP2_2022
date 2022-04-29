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


def create_table():
	commands = (
		"""
		CREATE TABLE accounts(
			username VARCHAR (20) UNIQUE NOT NULL,
			tell VARCHAR (20) UNIQUE NOT NULL
		);
		"""	
	)
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

create_table()