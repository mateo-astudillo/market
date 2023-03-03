from sqlite3 import connect
from os import getenv
from dotenv import load_dotenv

from .utilities import Executor, Encrypter

load_dotenv()
DATABASE = getenv("DATABASE")
SALT = getenv("SALT")


class User:

	@staticmethod
	def get_id(username:str) -> int:
		query = "SELECT %s From User Where %s = ?;"
		id = Executor.execute_select( query, ("id", "username"), (username,) )
		try:
			id = int(id[0][0])
		except:
			return None
		return id

	@staticmethod
	def exists(username:str) -> bool:
		return Executor.exists("User", "username", username)

	@staticmethod
	def remove(id:str) -> bool:
		query = "DELETE FROM User WHERE id = ?;"
		return Executor.execute_delete( query, (id, ) )

	@staticmethod
	def set_data(id:str, column:str, value:str) -> bool:
		query = "UPDATE User SET %s = ? WHERE %s = ?;"
		return Executor.execute( query, (column, "id"), (value, id) )

	@staticmethod
	def change_username(id:int, username:str) -> bool:
		query = "UPDATE User SET %s = ? WHERE %s = ?;"
		return Executor.execute( query, ("username", "id"), (username, id) )

	@staticmethod
	def change_password(id:str, password:str) -> bool:
		password = Encrypter.hash(password)
		query = "UPDATE User SET %s = ? WHERE %s = ?;"
		return Executor.execute( query, ("password", "id"), (password, id) )

	@staticmethod
	def register(username:str, password:str) -> bool:
		password = Encrypter.hash(password)
		query = "INSERT INTO User (%s, %s) VALUES(?, ?);"
		return Executor.execute( query, ("username","password"), (username, password) )

	@staticmethod
	def login(username:str, password:str) -> bool:
		password = Encrypter.hash(password)
		query = "SELECT * FROM User WHERE %s = ? and %s = ?;"
		data = Executor.execute_select( query, ("username","password"), (username, password))
		try:
			data = data[0]
		except Exception:
			return False
		return bool(data)

	@staticmethod
	def get_user(id):
		try:
			user = Executor.execute_select(
				"SELECT %s, %s, %s, %s FROM User WHERE %s = ?",
				("username", "name", "surname", "age", "id"),
				(id,)
			)[0]
		except:
			return None
		return user


class Sale:
	@staticmethod
	def add(user_id:int, product_id:int):
		query = "INSERT INTO Sale (%s, %s, %s, %s) VALUES (?, ?, ?, ? );"
		try:
			product_price = Executor.execute_select(
				"SELECT %s FROM Product WHERE %s = ?;",
				("price", "id"),
				(product_id, )
			)[0]
		except:
			return False
		result = Executor.execute(
			query,
			("user_id", "product_id", "price", "date"),
			(user_id, product_id, product_price, "datetime()")
		)
		return result


class Product:
	@staticmethod
	def exist(name:str):
		return Executor.exists("Product", "name", name)

	@staticmethod
	def add(name:str, price:float, brand:str) -> bool:
		if not Executor.exists("Brand", "name", brand):
			Brand.add(brand)
		brand_id = Brand.get_id(brand)

		if Product.exist(name):
			try:
				Executor.execute_select(
					"SELECT * FROM Product WHERE %s = ? and %s = ?;",
					("name", "brand_id"),
					(name, brand_id)
				)[0]
				return False
			except:
				pass

		result = Executor.execute(
			"INSERT INTO Product (%s, %s) VALUES(?, ?);",
			("name", "brand_id"),
			(name, brand_id)
		)
		Product.set_price(name, brand, price)
		return result

	@staticmethod
	def set_price(name:str, brand:str, price:float):
		brand_id = Brand.get_id(brand)
		result = Executor.execute(
			"UPDATE Product SET %s = ? WHERE %s = ? and %s = ?;",
			("price", "name", "brand_id"),
			(price, name, brand_id)
		)
		return result

	@staticmethod
	def remove(name:str, brand:str) -> bool:
		query = "DELETE FROM Product WHERE name = ? and brand_id = ?;"
		brand_id = Brand.get_id(brand)
		return Executor.execute_delete( query, (name, brand_id) )

	@staticmethod
	def edit(id:str, column:str, value:str) -> bool:
		query = "UPDATE Product SET %s = ? WHERE %s = ?;"
		return Executor.execute( query, (column, "id"), (value,id) )

	def get_all():
		pass


class Brand:
	@staticmethod
	def exists(self, name:str) -> bool:
		return Executor.exists("Brand", "name", name)

	@staticmethod
	def add(name:str) -> bool:
		query = "INSERT INTO Brand (%s) VALUES(?);"
		return Executor.execute( query, ("name",), (name,) )

	@staticmethod
	def get_id(name:str) -> int:
		try:
			id = Executor.execute_select(
				"SELECT %s FROM Brand WHERE %s = ?",
				("id", "name"),
				(name, )
			)[0][0]
		except:
			return None
		return id

	@staticmethod
	def remove(self, name:str) -> bool:
		query = "DELETE FROM Brand WHERE name = ?;"
		return Executor.execute_delete( query, (name, ) )

	@staticmethod
	def edit(self, id:str, column:str, value:str) -> bool:
		query = "UPDATE Brand SET %s = ? WHERE %s = ?;"
		return Executor.execute( query, (column, "id"), (value,id) )


class Database:
	@staticmethod
	def create():
		queries = [
			"""
			CREATE TABLE IF NOT EXISTS User (
				id integer PRIMARY KEY NOT NULL,
				username varchar NOT NULL UNIQUE,
				password varchar NOT NULL,
				name varchar,
				surname varchar,
				age integer,
				credit float DEFAULT 0
			);
			""",

			"""
			CREATE TABLE IF NOT EXISTS Product (
				id integer PRIMARY KEY NOT NULL,
				name varchar NOT NULL,
				price float DEFAULT 0,
				brand_id integer NOT NULL
			);
			""",

			"""
			CREATE TABLE IF NOT EXISTS Sale (
				id integer PRIMARY KEY NOT NULL,
				user_id integer NOT NULL,
				product_id integer NOT NULL,
				date datetime,
				price float
			);
			""",

			"""
			CREATE TABLE IF NOT EXISTS Brand (
				id integer PRIMARY KEY NOT NULL,
				name varchar NOT NULL UNIQUE
			);
			""",

			"""
			CREATE TABLE IF NOT EXISTS Cart (
				id integer PRIMARY KEY NOT NULL,
				user_id integer NOT NULL UNIQUE,
				product_id integer NOT NULL UNIQUE,
				amount varchar NOT NULL DEFAULT 1
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
			result = True
		except Exception as ex:
			print(ex)
			result = False
		finally:
			connection.close()
		return result
