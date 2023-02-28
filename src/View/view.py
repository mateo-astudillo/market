from customtkinter import CTk
from .session import Login, Register
from .customer import Shop, Cart, Profile, Menu
from .inventory import Options, Add, Edit


class View(CTk):
	def __init__(self):
		super().__init__()

		self.controller = None

		self.current_page = None

	def set_controller(self, controller):
		self.controller = controller

	def go(self, page):
		if self.current_page is not None:
			self.current_page.hide()
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
