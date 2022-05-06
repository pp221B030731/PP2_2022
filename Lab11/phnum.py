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


while 1:
	con = None
	try: 
		params = config()
		con = psycopg2.connect(**params)
		cur = con.cursor()
		c = int(input('1 - Show, 2 - Add, 3 - List, 4 - Que, 5 - Del, 6 - Quite\n'))
		if c == 1:
			try:
				cur.execute(f'select * from show();')
				ans = cur.fetchall()
				print(ans)
			except:
				print("Error")
				cur.close()
				con.commit()
				if con is not None:
					con.close()
				break
		elif c == 2:
			f = True
			cur.execute(f'select * from show();')
			ans = cur.fetchall()
			name = str(input('Name:\n'))
			num = str(input('Number:\n'))
			for i in ans:
				if i[0] == name:
					cur.execute(f"call add_user1('{name}', '{num}');")
					f = False
					break
			if f:		
				cur.execute(f"call add_user('{name}', '{num}');")
		elif c == 3:
			t = True
			l = []
			n = int(input('Number of objects:\n'))
			for k in range(n):
				name = input(f'{k+1}: Name: \n')
				num = input(f'{k+1}: Number: \n')
				for j in num:
					if '9' >= j >= '0':
						continue
					else:
						l.append((name, num))
						t = False
						break
				if t:		
					f = True
					cur.execute(f'select * from show();')
					ans = cur.fetchall()
					for i in ans:
						if i[0] == name:
							cur.execute(f"call add_user1('{name}', '{num}');")
							f = False
							break
					if f:		
						cur.execute(f"call add_user('{name}', '{num}');")
			print("WRONG conntacts: ", l)
		elif c == 4:
			try:
				lim = int(input('Limit:\n'))
				offs = int(input('Offset:\n'))
				cur.execute(f"select * from que('{lim}', '{offs}');")
				ans = cur.fetchall()
				print(ans)
			except:
				print("Error")
				cur.close()
				con.commit()
				if con is not None:
					con.close()
				break
		elif c == 5:
			flag = int(input('1- By name, 2 - By number\n'))
			try:	
				if flag == 1:
					name = input('Name: \n')
					cur.execute(f"call del('{name}');")
				else:
					num = input('Number:\n')
					cur.execute(f"call del1('{num}');")
			except:
				print("Error")
				cur.close()
				con.commit()
				if con is not None:
					con.close()
				break
		else:
			cur.close()
			con.commit()
			if con is not None:
				con.close()
			break
		cur.close()
		con.commit()
	except Exception as e:
		print(str(e))
	if con is not None:
		con.close()