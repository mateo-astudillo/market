

class LoginController:
	def __init__(self, controller):
		self.controller = controller

	def login(self, username, password):
		if self.controller.model.user.login(username, password):
			self.controller.view.go("shop")

	def sign_up(self):
		self.controller.view.go("register")


class RegisterController:
	def __init__(self, controller):
		self.controller = controller

	def register(self):
		pass

	def cancel(self):
		self.controller.view.go("login")
