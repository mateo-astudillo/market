from .session import Login, Register
from .customer import Shop, Cart, Profile
from .inventory import Options, Add, Edit


class View:
	def __init__(self):
		self.controller = None

		self.current_page = None

		self.pages = {
			"login": Login,
			"register": Register,
			"shop": Shop,
			"cart": Cart,
			"profile": Profile,
			"options": Options,
			"add": Add,
			"edit": Edit,
		}

	def set_controller(self, controller):
		self.controller = controller

	def go(self, page):
		if self.current_page is not None:
			self.current_page.hide()

		self.current_page = self.pages.get(page)(self)
		pages = {
			"login": Login,
			"register": Register,
			"menu": Menu,
			"shop": Shop,
			"cart": Cart,
			"profile": Profile,
			"options": Options,
			"add": Add,
			"edit": Edit,
		}
		self.current_page = pages.get(page)
		self.current_page = self.current_page(self)
		self.current_page.show()

	def logged(self, username):
		self.controller.logged(username)
