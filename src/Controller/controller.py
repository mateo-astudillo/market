from .session import LoginController, RegisterController
from .customer import MenuController, ShopController, CartController, ProfileController
from .inventory import OptionsController, AddController, EditController


class Controller:
	def __init__(self):
		self.view = None
		self.model = None

		self.session = {
			"login": LoginController(self),
			"register": RegisterController(self),
		}

		self.customer = {
			"menu": MenuController(self),
			"shop": ShopController(self),
			"cart": CartController(self),
			"profile": ProfileController(self),
		}
		self.inventory = {
			"options": OptionsController(self),
			"add": AddController(self),
			"edit": EditController(self),
		}

	def set_view(self, view):
		self.view = view

	def set_model(self, model):
		self.model = model

	def run(self):
		pass
