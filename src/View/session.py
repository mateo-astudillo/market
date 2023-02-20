from Controller.session import LoginController, RegisterController


class Login:
	def __init__(self, controller: LoginController):
		self.controller = controller


class Register:
	def __init__(self, controller: RegisterController):
		self.controller = controller
