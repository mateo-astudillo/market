from sqlite3 import connect
from passlib.hash import sha256_crypt as sha
from os import getenv
from dotenv import load_dotenv
from .executor import Executor
load_dotenv()
DATABASE = getenv("DATABASE")
SALT = getenv("SALT")


class User:
	def __init__(self):
		self.id = None

	def set_id(self, username:str) -> bool:
		query = "SELECT %s From User Where %s = ?;"
		id = Executor.execute_select( query, ("id", "username"), (username,) )
		self.id = id[0]
		return bool(id)

	def exists(self, username:str) -> bool:
		query = "SELECT * FROM User WHERE %s = ?;"
		data = Executor.execute_select( query, ("username",), (username,) )
		return bool(data)

	def remove(self, id:str) -> bool:
		query = "DELETE FROM User WHERE id = ?;"
		return Executor.execute_delete( query, (id, ) )

	def set_data(self, id:str, column:str, value:str) -> bool:
		query = "UPDATE User SET %s = ? WHERE %s = ?;"
		return Executor.execute( query, (column, "id"), (value, id) )

	def change_username(self, id:str, username:str) -> bool:
		query = "UPDATE User SET %s = ? WHERE %s = ?;"
		return Executor.execute( query, ("username", "id"), (username, id) )

	def change_password(self, id:str, password:str) -> bool:
		password = self.hash(password)
		query = "UPDATE User SET %s = ? WHERE %s = ?;"
		return Executor.execute( query, ("password", "id"), (password, id) )

	def register(self, username:str, password:str) -> bool:
		password = self.hash(password)
		query = "INSERT INTO User (%s, %s) VALUES(?, ?);"
		return Executor.execute( query, ("username","password"), (username, password) )

	def login(self, username:str, password:str) -> bool:
		password = self.hash(password)
		query = "SELECT * FROM User WHERE %s = ? and %s = ?;"
		data = Executor.execute_select( query, ("username","password"), (username, password))
		try:
			data = data[0]
		except Exception:
			return False
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

	def add(self, name:str, price:int, brand:int) -> bool:
		query = "INSERT INTO Product (%s, %s, %s) VALUES(?, ?, ?);"
		return Executor.execute( query,("name", "price", "brand_id"), (name, price, brand) )

	def remove(self, name:str) -> bool:
		query = "DELETE FROM Product WHERE name = ?;"
		return Executor.execute_delete( query, (name, ) )

	def edit(self, id:str, column:str, value:str) -> bool:
		query = "UPDATE Product SET %s = ? WHERE %s = ?;"
		return Executor.execute( query, (column, "id"), (value,id) )

class Brand:
	def __init__(self):
		pass

	def add(self, name:str) -> bool:
		query = "INSERT INTO Brand (%s) VALUES(?);"
		return Executor.execute( query, ("name",), (name,) )

	def remove(self, name:str) -> bool:
		query = "DELETE FROM Brand WHERE name = ?;"
		return Executor.execute_delete( query, (name, ) )

	def edit(self, id:str, column:str, value:str) -> bool:
		query = "UPDATE Brand SET %s = ? WHERE %s = ?;"
		return Executor.execute( query, (column, "id"), (value,id) )