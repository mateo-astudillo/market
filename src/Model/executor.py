from sqlite3 import connect
from os import getenv
from dotenv import load_dotenv

load_dotenv()
DATABASE = getenv("DATABASE")


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
	def execute_select(query:str, columns:tuple ,values:tuple) -> list:
		try:
			connection = connect(DATABASE)
			cursor = connection.cursor()
			cursor.execute(query % columns, values)
			result = cursor.fetchall()
			connection.commit()
		except Exception as ex:
			print(ex)
		finally:
			connection.close()
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


