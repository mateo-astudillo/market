from Controller.customer import MenuController, ShopController, CartController, ProfileController


class Menu:
	def __init__(self, controller: MenuController):
		self.controller = controller


class Shop:
	def __init__(self, controller: ShopController):
		self.controller = controller


class Cart:
	def __init__(self, controller: CartController):
		self.controller = controller


class Profile:
	def __init__(self, controller: ProfileController):
		self.controller = controller
