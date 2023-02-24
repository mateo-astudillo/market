from .session import Login, Register


class View:
	def __init__(self):
		self.controller = None

		self.pages = {
			"login": Login(),
			"register": Register()
		}

	def set_controller(self, controller):
		self.controller = controller

	def go(self, page):
		self.pages.get(page).show()
		
