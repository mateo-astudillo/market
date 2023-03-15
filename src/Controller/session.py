from Model import User
from .validator import Validator


class LoginController:
	@staticmethod
	def login(username:str, password:str) -> bool:
		if not Validator.username(username):
			print("invalid username")
			return False
		if not User.login(username, password):
			print("incorrect username or password")
			return False
		print(f"Logged: {username}")
		return True


class RegisterController:
	@staticmethod
	def register(username:str, password:str) -> bool:
		if not Validator.username(username):
			print("invalid username")
			return False
		if User.exists(username):
			print("Username already exists")
			return False
		if not User.add(username, password):
			print("Error in database")
			return False
		print("register with exit")
		return True
