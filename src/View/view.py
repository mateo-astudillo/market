from .session import Login, Register
from .customer import Shop, Cart, Profile, Menu
from .inventory import Options, Add, Edit


class View:
	def __init__(self):
		self.controller = None

		self.current_page = None

		self.pages = {
			"login": self.login,
			"register": self.register,
			"menu": self.menu,
			"shop": self.shop,
			"cart": self.cart,
			"profile": self.profile,
			"options": self.options,
			"add": self.add,
			"edit": self.edit,
		}

	def set_controller(self, controller):
		self.controller = controller

	def go(self, page):
		if self.current_page is not None:
			self.current_page.hide()

		self.current_page = self.pages.get(page)(self)
		self.current_page.show()

	def logged(self, username):
		self.controller.logged(username)

