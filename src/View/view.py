from .session import Login, Register


class View:
	def __init__(self):
		self.controller = None

		self.current_page = None


	def get_page(self, page, controller):
		pages = {
			"login": Login(controller),
			"register": Register(controller)
		}
		return pages.get(page)

	def set_controller(self, controller):
		self.controller = controller

	def go(self, page):
		self.get_page(page, self.controller)
		
