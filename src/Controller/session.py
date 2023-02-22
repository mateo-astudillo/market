from re import match
from .controller import Controller

def validate_username(username) -> bool:
	username = username.replace(" ", "").replace("\n", "")
	if match('^[a-zA-Z0-9._]*$', username) is None:
		return False
	return True


class LoginController(Controller):
	def __init__(self):
		super().__init__()

	def login(self, username, password):
		if not validate_username(username):
			print("invalid username")
			return False
		if not self.model.user.login(username, password):
			print("incorrect username or password")
			return False

		print("logged: ", username, " ", password)
		return True

	def sign_up(self):
		self.view.go("register")


class RegisterController(Controller):
	def __init__(self):
		super().__init__()

	def register(self, username, password):
		if not validate_username(username):
			print("invalid username")
			return False
		if self.model.user.exists(username):
			print("username already exists")
			return False
		if not self.model.user.register(username, password):
			print("Error in database")
			return False
		print("register with exit")
		return True

	def cancel(self):
		self.view.go("login")
