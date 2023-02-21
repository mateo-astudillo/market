from re import match

def validate_username(username):
	username = username.replace(" ", "").replace("\n", "")
	if match('^[a-zA-Z0-9._]*$', username) is None:
		return False
	return True


class LoginController:
	def __init__(self, controller):
		self.controller = controller

	def login(self, username, password):
		if not validate_username(username):
			print("invalid username")
			return False
		if not self.controller.model.user.login(username, password):
			print("incorrect username or password")
			return False

		print(username, " ", password)
		return True

	def sign_up(self):
		self.controller.view.go("register")


class RegisterController:
	def __init__(self, controller):
		self.controller = controller

	def register(self, username, password):
		self.controller.model.user.register(username, password)

	def cancel(self):
		self.controller.view.go("login")
