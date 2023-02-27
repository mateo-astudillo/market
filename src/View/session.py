from Controller import LoginController, RegisterController

class Login:
	def __init__(self, view):
		self.view = view

	def show(self):
		pass

	def hide(self):
		pass

	def login(self):
		username = "juan"
		password = "hola"
		if LoginController.login(username, password):
			self.view.logged(username)

	def register(self):
		self.controller.go("register")


class Register:
	def __init__(self):
		pass

	def show(self):
		pass

	def hide(self):
		pass

	def register(self):
		username = "juan"
		password = "hola"
		if RegisterController.register(username, password):
			self.controller.go("login")
