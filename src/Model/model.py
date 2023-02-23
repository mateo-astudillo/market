from sqlite3 import connect
from os import getenv
from dotenv import load_dotenv

from .entities import User, Sale, Product, Brand

load_dotenv()
DATABASE = getenv("DATABASE")

class Model:
	def __init__(self):

		self.user = User()
		self.sale = Sale()
		self.product = Product()
		self.brand = Brand()

	def init_database(self):
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
				name varchar NOT NULL UNIQUE,
				price float DEFAULT 0 NOT NULL,
				brand_id integer NOT NULL
			);
			""",

			"""
			CREATE TABLE IF NOT EXISTS Sale (
				id integer PRIMARY KEY NOT NULL,
				user_id integer NOT NULL,
				product_id integer NOT NULL,
				date datetime,
				price float DEFAULT 0
			);
			""",

			"""
			CREATE TABLE IF NOT EXISTS Brand (
				id integer PRIMARY KEY NOT NULL,
				name varchar NOT NULL UNIQUE
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
