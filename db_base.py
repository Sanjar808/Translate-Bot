import sqlite3

class Database():

	def __init__(self):
		self.conn = sqlite3.connect("translate_person.db")
		self.cur = self.conn.cursor()

	def create_users(self):
		self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
			tel_id varchar(50),
			name varchar(30)
			)""")

	def select_users(self,id):
		self.cur.execute(f"SELECT * FROM users WHERE tel_id = '{id}'")
		data = self.cur.fetchone()
		if data is None:
			return False 
		else:
			return True 

	def insert_users(self,tel_id,name):
		self.cur.execute(f"INSERT INTO users VALUES('{tel_id}','{name}')")
		return self.conn.commit()

	def count_users(self):
		self.cur.execute(f"SELECT COUNT(*) FROM users")
		return self.cur.fetchone()