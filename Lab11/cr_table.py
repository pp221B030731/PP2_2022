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


commands = [
	"""
	CREATE TABLE accounts1(
		username VARCHAR (20) UNIQUE NOT NULL,
		tell VARCHAR (20) UNIQUE NOT NULL
	);
	"""	,
	#TASK 2
	"""
	CREATE OR REPLACE PROCEDURE add_user(name varchar, num varchar)
		as 
		$$
		BEGIN
		insert into accounts1(username, tell)
		values(name, num);
		END; 
		$$
		LANGUAGE plpgsql;
	""",
	"""
		CREATE OR REPLACE PROCEDURE add_user1(name varchar, num varchar)
		as 
		$$
		BEGIN
		update accounts1
			set tell  = $2
			where accounts1.username = name ;
		END; 
		$$
		LANGUAGE plpgsql;
	""",
	#TASK 4
	"""
	CREATE OR REPLACE FUNCTION que(lim integer, x integer)
		returns setof accounts1
		as
		$$
		BEGIN
			return query
			select * from accounts1
			order by username
			limit lim offset x;
		END;
		$$
		LANGUAGE plpgsql;
	""",
	#TASK 5
	"""
	CREATE OR REPLACE PROCEDURE del(name varchar)
        as
        $$
        BEGIN
        	delete
            from  accounts1 
            where accounts1.username = name;
        END;
        $$
        LANGUAGE plpgsql;
	""",
	"""
	CREATE OR REPLACE PROCEDURE del1(num varchar)
        as
        $$
        BEGIN
        	delete
            from  accounts1 
            where accounts1.tell = num;
        END;
        $$
        LANGUAGE plpgsql;
	""",
	#TASK 1
	"""
	CREATE OR REPLACE FUNCTION show()
		returns table(
			username varchar(255),
		    tell varchar(255)
		)
		as
		$$
		BEGIN 
		  return query
		  select s.username, s.tell from accounts1 as s;
		END
		$$ 
		LANGUAGE plpgsql;
	"""
]

con = None
try: 
	params = config()
	con = psycopg2.connect(**params)
	cur = con.cursor()
	for i in commands:
		cur.execute(i)
	cur.close()
	con.commit()
except Exception as e:
	print(str(e))
if con is not None:
	con.close()
