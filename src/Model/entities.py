from sqlite3 import connect
from os import getenv
from dotenv import load_dotenv

from .utilities import Executor, Encrypter

load_dotenv()
DATABASE = getenv("DATABASE")
SALT = getenv("SALT")


class User:
	@staticmethod
	def exists(username:str) -> bool:
		return Executor.exists(username, "username", "User")

	@staticmethod
	def add(username:str, password:str) -> bool:
		password = Encrypter.hash(password)
		return Executor.execute(
			"INSERT INTO User (%s, %s) VALUES(?, ?);",
			("username","password"),
			(username, password)
		)

	@staticmethod
	def remove(id:str) -> bool:
		return Executor.execute(
			"DELETE FROM User WHERE %s = ?;",
			("id", )
			(id, )
		)

	@staticmethod
	def update(id:str, column:str, value:str) -> bool:
		return Executor.execute(
			"UPDATE User SET %s = ? WHERE %s = ?;",
			(column, "id"),
			(value, id)
		)

	@staticmethod
	def change_username(id:int, username:str) -> bool:
		return Executor.execute(
			"UPDATE User SET %s = ? WHERE %s = ?;",
			("username", "id"),
			(username, id)
		)

	@staticmethod
	def change_password(id:str, password:str) -> bool:
		password = Encrypter.hash(password)
		return Executor.execute(
			"UPDATE User SET %s = ? WHERE %s = ?;",
			("password", "id"),
			(password, id)
		)

	@staticmethod
	def login(username:str, password:str) -> bool:
		password = Encrypter.hash(password)
		try:
			Executor.execute_fetchall(
				"SELECT id FROM User WHERE %s = ? and %s = ?;",
				("username","password"),
				(username, password)
			)[0]
		except:
			return False
		return True

	@staticmethod
	def get_user(id:int) -> tuple:
		"""
		None if not exists
		tuple = (username, name, surname, age)
		"""
		return Executor.execute_fetchone(
			"SELECT %s, %s, %s, %s FROM User WHERE %s = ?",
			("username", "name", "surname", "age", "id"),
			(id, )
		)

	@staticmethod
	def get_id(username:str) -> int:
		return Executor.get_id(username, "username", "User")


class Cart:
	@staticmethod
	def exists(user_id:int, product_id:int) -> bool:
		result = Executor.execute_fetchone(
			"SELECT id FROM Cart WHERE %s = ? and %s = ?;",
			("user_id", "product_id"),
			(user_id, product_id)
		)
		return bool(result)
	
	@staticmethod
	def add(user_id:int, product_id:int, amount:int) -> bool:
		return Executor.execute(
			"INSERT INTO Cart (%s, %s, %s) VALUES (?, ?, ?);",
			("user_id", "product_id", "amount"),
			(user_id, product_id, amount)
		)

	@staticmethod
	def remove(user_id:int, product_id:int) -> bool:
		return Executor.execute(
			"DELETE FROM Cart WHERE %s = ? and %s = ?;",
			("user_id", "product_id"),
			(user_id, product_id)
		)

	@staticmethod
	def update(id:str, column:str, value:str) -> bool:
		return Executor.execute(
			"UPDATE Product SET %s = ? WHERE %s = ?;",
			(column, "id"),
			(value, id)
		)

	@staticmethod
	def get_id(user_id:int, product_id:int) -> int:
		if not Cart.exists(user_id, product_id):
			return None
		id = Executor.execute_fetchone(
			"SELECT id FROM Product WHERE %s = ? AND %s = ?;",
			("name", "brand_id"),
			(name, brand_id)
		)[0]
		return int(id)


class Sale:
	@staticmethod
	def add(user_id:int, product_id:int) -> bool:
		product_price = Executor.execute_fetchone(
			"SELECT %s FROM Product WHERE %s = ?;",
			("price", "id"),
			(product_id, )
		)
		if product_price is None:
			return False
		return Executor.execute(
			"INSERT INTO Sale (%s, %s, %s, %s) VALUES (?, ?, ?, ? );",
			("user_id", "product_id", "price", "date"),
			(user_id, product_id, product_price, "datetime()")
		)

	@staticmethod
	def get_id(date:str) -> int:
		return Executor.get_id(date, "date", "Sale")


class Product:
	@staticmethod
	def exists(name:str, brand_id:int) -> bool:
		result = Executor.execute_fetchone(
			"SELECT id FROM Product WHERE %s = ? AND %s = ?;",
			("brand_id","name"),
			(brand_id, name)
		)
		return bool(result)

	@staticmethod
	def add(name:str, brand:str, stock:int, price:float) -> bool:
		brand_id = Brand.get_id(brand)
		return Executor.execute(
			"INSERT INTO Product (%s, %s, %s, %s) VALUES (?, ?, ?, ?);",
			("name", "brand_id", "stock", "price"),
			(name, brand_id, stock, price)
		)

	@staticmethod
	def remove(name:str, brand_id:str) -> bool:
		return Executor.execute(
			"DELETE FROM Product WHERE %s = ? and %s = ?;",
			("name", "brand_id"),
			(name, brand_id)
		)

	@staticmethod
	def update(id:str, column:str, value:str) -> bool:
		return Executor.execute(
			"UPDATE Product SET %s = ? WHERE %s = ?;",
			(column, "id"),
			(value, id)
		)

	@staticmethod
	def get_all() -> list:
		return Executor.execute_fetchall(
			"SELECT %s, %s, %s, %s FROM Product AS P INNER JOIN Brand As B ON %s = %s;",
			("P.name", "B.name", "P.price","P.stock", "P.brand_id", "B.id")
		)

	@staticmethod
	def get_id(name:str, brand:str) -> int:
		if not Product.exists(name, brand):
			return None
		brand_id = Brand.get_id(brand)
		id = Executor.execute_fetchone(
			"SELECT id FROM Product WHERE %s = ? AND %s = ?;",
			("name", "brand_id"),
			(name, brand_id)
		)[0]
		return int(id)

class Brand:
	@staticmethod
	def exists(name:str) -> bool:
		return Executor.exists(name, "name", "Brand")

	@staticmethod
	def add(name:str) -> bool:
		return Executor.execute(
			"INSERT INTO Brand (%s) VALUES (?);",
			("name", ),
			(name, )
		)

	@staticmethod
	def remove(name:str) -> bool:
		return Executor.execute(
			"DELETE FROM Brand WHERE %s = ?;",
			("name", ),
			(name, )
		)

	@staticmethod
	def update(id:str, column:str, value:str) -> bool:
		return Executor.execute(
			"UPDATE Brand SET %s = ? WHERE %s = ?;",
			(column, "id"),
			(value,id)
		)

	@staticmethod
	def get_id(name:str) -> int:
		return Executor.get_id(name, "name", "Brand")


class Database:
	@staticmethod
	def create():
		queries = [
		# "DROP TABLE User;",
		# "DROP TABLE Product;",
		# "DROP TABLE Sale;",
		# "DROP TABLE Brand;",
		# "DROP TABLE Cart;",
		"""
		CREATE TABLE IF NOT EXISTS "Brand" (
			"id"    INTEGER NOT NULL UNIQUE,
			"name"    VARCHAR(64) NOT NULL UNIQUE,
			PRIMARY KEY("id" AUTOINCREMENT)
		);
		""",
		"""
		CREATE TABLE IF NOT EXISTS "Cart" (
			"id"    INTEGER NOT NULL UNIQUE,
			"user_id"    INTEGER NOT NULL,
			"product_id"    INTEGER NOT NULL,
			"amount"    INTEGER NOT NULL,
			PRIMARY KEY("id" AUTOINCREMENT)
		);
		""",
		"""
		CREATE TABLE IF NOT EXISTS "Product" (
			"id"    INTEGER NOT NULL UNIQUE,
			"brand_id"    INTEGER,
			"name"    VARCHAR(64) NOT NULL,
			"stock"    INTEGER,
			"price"    INTEGER NOT NULL,
			PRIMARY KEY("id" AUTOINCREMENT)
		);
		""",
		"""
		CREATE TABLE IF NOT EXISTS "Sale" (
			"id"    INTEGER NOT NULL UNIQUE,
			"user_id"    INTEGER NOT NULL,
			"product_id"    INTEGER NOT NULL,
			"date"    VARCHAR(64),
			"total"    REAL,
			PRIMARY KEY("id" AUTOINCREMENT)
		);
		""",
		"""
		CREATE TABLE IF NOT EXISTS "User" (
			"id"    INTEGER NOT NULL UNIQUE,
			"username"    VARCHAR(64) NOT NULL UNIQUE,
			"password"    VARCHAR(64) NOT NULL,
			"name"    VARCHAR(64),
			"surname"    VARCHAR(64),
			"age"    INTEGER,
			"credit"    FLOAT,
			PRIMARY KEY("id" AUTOINCREMENT)
		);
		"""
		]
		try:
			connection = connect(DATABASE)
			cursor = connection.cursor()
			for query in queries:
				query = query.replace("\t", "").replace("\n", " ")
				cursor.execute(query)
			connection.commit()
		except Exception as ex:
			print(ex)
			return False
		finally:
			connection.close()
		return True
