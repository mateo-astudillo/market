from .session import Login, Register
from .customer import Shop, Cart, Profile, Menu
from .inventory import Options, Add, Edit


class View:
	def __init__(self):
		self.controller = None

		self.current_page = None

	def set_controller(self, controller):
		self.controller = controller

	def go(self, page):
		if self.current_page is not None:
			self.current_page.hide()
		pages = {
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
		self.current_page = pages.get(page)
		self.current_page = self.current_page()
		self.current_page.show()

	def logged(self, username):
		self.controller.logged(username)
		
	# Session
	def login(self):
		return Login(self)

	def register(self):
		return Register(self)

	# Customer
	def menu(self):
		return Menu(self)

	def shop(self):
		return Shop(self)

	def cart(self):
		return Cart(self)

	def profile(self):
		return Profile(self)

	# Inventory
	def options(self):
		return Options(self)

	def add(self):
		return Add(self)

	def edit(self):
		return Edit(self)
