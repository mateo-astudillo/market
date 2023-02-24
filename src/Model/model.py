from sqlite3 import connect
from os import getenv
from dotenv import load_dotenv


load_dotenv()
DATABASE = getenv("DATABASE")

class Model:
	def __init__(self):
		self.controller = None

	def set_controller(self, controller):
		self.controller = controller

	@staticmethod
	def init_database():
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
		connection = connect(DATABASE)
		cursor = connection.cursor()
		for query in queries:
			query = query.replace("\t", "").replace("\n", " ")
			cursor.execute(query)
		connection.commit()
		connection.close()
