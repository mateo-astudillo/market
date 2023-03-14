from sqlite3 import connect
from os import getenv
from dotenv import load_dotenv
from re import match
from passlib.hash import sha256_crypt as sha

load_dotenv()
DATABASE = getenv("DATABASE")
SALT = getenv("SALT")


class Executor:
	@staticmethod
	def execute(query:str, columns:tuple, values:tuple) -> bool:
		try:
			connection = connect(DATABASE)
			cursor = connection.cursor()
			cursor.execute(query % columns, values)
			connection.commit()
		except Exception as ex:
			print(ex)
			return False
		finally:
			connection.close()
		return True

	@staticmethod
	def execute_fetchone(query:str, columns:tuple ,values:tuple = None) -> tuple:
		"""
		returns "None" if there is no record
		"""
		try:
			connection = connect(DATABASE)
			cursor = connection.cursor()
			if values == None:
				cursor.execute(query % columns)
			else:
				cursor.execute(query % columns, values)
			result = cursor.fetchone()
			connection.commit()
		except Exception as ex:
			print(ex)
			return None
		finally:
			connection.close()
		return result

	@staticmethod
	def execute_fetchall(query:str, columns:tuple ,values:tuple = None) -> list:
		try:
			connection = connect(DATABASE)
			cursor = connection.cursor()
			if values == None:
				cursor.execute(query % columns)
			else:
				cursor.execute(query % columns, values)
			result = cursor.fetchall()
			connection.commit()
		except Exception as ex:
			print(ex)
			return None
		finally:
			connection.close()
		return result

	@staticmethod
	def exists(value:str, column:str, table:str) -> bool:
		data = Executor.execute_fetchone(
			"SELECT id FROM %s WHERE %s = ?;",
			(table, column),
			(value, )
		)
		return bool(data)

	@staticmethod
	def get_id(value:str, column:str, table:str) -> int:
		try:
			id = Executor.execute_fetchone(
				"SELECT %s FROM %s WHERE %s = ?",
				("id", table, column),
				(value, )
			)[0]
		except:
			return None
		return int(id)


class Encrypter:
	@staticmethod
	def hash(password:str) -> str:
		return sha.using(rounds=1000, salt=SALT).hash(password).split("$")[-1]


class Validator:
	@staticmethod
	def username(username) -> bool:
		username = username.replace(" ", "").replace("\n", "")
		if match('^[a-zA-Z0-9._]*$', username) is None:
			return False
		return True
