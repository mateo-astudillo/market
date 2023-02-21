from sqlite3 import connect
from os import getenv
from dotenv import load_dotenv

load_dotenv()
DATABASE = getenv("DATABASE")


class User:
	def __init__(self):
		pass

	def add(self, username) -> bool:
		pass

	def remove(self, username) -> bool:
		pass

	def edit(self, username, column, value) -> bool:
		pass

	def change_username(self, username, password, new_username) -> bool:
		pass

	def change_password(self, username, password, new_password) -> bool:
		pass

	def login(self, username, password) -> bool:
		query = "SELECT * FROM User WHERE username = (?) and password = (?);"
		connetion = connect(DATABASE)
		cursor = connetion.cursor()
		cursor.execute( query, (username, password) )
		data = cursor.fetchone()
		connetion.commit()
		connetion.close()
		return bool(data)


class Sale:
	def __init__(self):
		pass

	def create(self, user_id, product_id, price, date):
		pass


class Product:
	def __init__(self):
		pass
	def add(self, name, price, brand) -> bool:
		pass

	def remove(self, name) -> bool:
		pass

	def edit(self, column, value) -> bool:
		pass
