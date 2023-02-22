from sqlite3 import connect
from os import getenv
from dotenv import load_dotenv

from .entities import User, Sale, Product

load_dotenv()
DATABASE = getenv("DATABASE")

class Model:
	def __init__(self):

		self.user = User()
		self.sale = Sale()
		self.product = Product()

	def init_database(self):
		queries = [
			"""
			CREATE TABLE IF NOT EXISTS User (
				id integer PRIMARY KEY NOT NULL,
				username varchar,
				password varchar,
				name varchar,
				surname varchar,
				age integer,
				credit float
			);
			""",

			"""
			CREATE TABLE IF NOT EXISTS Product (
				id integer PRIMARY KEY NOT NULL,
				name varchar,
				price float,
				brand_id integer
			);
			""",

			"""
			CREATE TABLE IF NOT EXISTS Sale (
				id integer PRIMARY KEY NOT NULL,
				user_id integer,
				product_id integer,
				date datetime, 
				price float
			);
			""",

			"""
			CREATE TABLE IF NOT EXISTS Brand (
				id integer PRIMARY KEY NOT NULL,
				name varchar
			);
			"""
		]
		connection = connect(DATABASE)
		cursor = connection.cursor()
		for query in queries:
			query = query.replace("\t", "").replace("\n", " ")
			cursor.execute(query)
		connection.commit()
		connection.close()
