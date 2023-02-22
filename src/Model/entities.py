from sqlite3 import connect
from passlib.hash import sha256_crypt as sha
from os import getenv
from dotenv import load_dotenv

load_dotenv()
DATABASE = getenv("DATABASE")
SALT = getenv("SALT")


class User:
	def __init__(self):
		pass

	def exists(self, username:str) -> bool:
		query = "SELECT * FROM User WHERE username = ?;"
		connection = connect(DATABASE)
		cursor = connection.cursor()
		cursor.execute( query, (username,) )
		data = cursor.fetchone()
		connection.commit()
		connection.close()
		return bool(data)

	def remove(self, username) -> bool:
		query = "DELETE FROM User WHERE username = ?;"
		try:
			connection = connect(DATABASE)
			cursor = connection.cursor()
			cursor.execute(query, (username,) )
			connection.commit()
			result = True
		except Exception:
			print(Exception)
			result = False
		connection.close()
		return result

	def edit(self, username, column, value) -> bool:
		pass

	def change_username(self, username, new_username) -> bool:
		query = "UPDATE User SET username = ? WHERE username = ?;"

		try:
			connection = connect(DATABASE)
			cursor = connection.cursor()
			cursor.execute(query, (new_username, username) )
			connection.commit()
			result = True
		except Exception:
			print(Exception)
			result = False

		connection.close()
		return result

	def change_password(self, username, password, new_password) -> bool:
		pass

	def register(self, username, password) -> bool:
		password = self.hash(password)
		query = "INSERT INTO User (username, password) VALUES(?, ?);"
		try:
			connection = connect(DATABASE)
			cursor = connection.cursor()
			cursor.execute( query, (username, password) )
			connection.commit()
			result = True
		except Exception:
			print(Exception)
			result = False
		connection.close()
		return result

	def login(self, username, password) -> bool:
		password = self.hash(password)
		query = "SELECT * FROM User WHERE username = (?) and password = (?);"
		connection = connect(DATABASE)
		cursor = connection.cursor()
		cursor.execute( query, (username, password) )
		data = cursor.fetchone()
		connection.commit()
		connection.close()
		return bool(data)

	def hash(self, password:str) -> str:
		return sha.using(rounds=1000, salt=SALT).hash(password).split("$")[-1]


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
