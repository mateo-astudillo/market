from .session import LoginController, RegisterController
from .customer import MenuController, ShopController, CartController, ProfileController
from .inventory import OptionsController, AddController, EditController
from .interface import Controller


class Controllers(Controller):
	def __init__(self):
		super().__init__()

		self.session = {
			"login": LoginController(),
			"register": RegisterController(),
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

	def set_views(self):
		for controller in self.session.values():
			controller.set_view(self.view)

	def set_models(self):
		for controller in self.session.values():
			controller.set_model(self.model)

	def run(self):
		if not self.model.init_database():
			return False
		self.view.go("login")
		return True
