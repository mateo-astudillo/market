from Controller import LoginController, RegisterController

class Login:
	def __init__(self):
		self.controller = LoginController
		pass

	def show(self):
		pass

	def login(self):
		LoginController.login()


class Register:
	def __init__(self):
		pass

	def show(self):
		pass
