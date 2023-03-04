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
			result = True
		except Exception as ex:
			print(ex)
			result = False
		finally:
			connection.close()
		return result

	@staticmethod
	def execute_select(query:str, columns:tuple ,values:tuple = None) -> list:
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
		finally:
			connection.close()
			# print(result)
		return result

	@staticmethod
	def execute_delete(query:str, values:tuple) -> bool:
		try:
			connection = connect(DATABASE)
			cursor = connection.cursor()
			cursor.execute(query, values)
			result = cursor.fetchall()
			connection.commit()
			result = True
		except Exception as ex:
			print(ex)
			result = False
		finally:
			connection.close()
		return result

	@staticmethod
	def exists(table:str, column:str, value:str) -> bool:
		query = "SELECT * FROM %s WHERE %s = ?;"
		data = Executor.execute_select( query, (table, column), (value, ) )
		return bool(data)


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