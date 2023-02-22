from .controller import Controller

class MenuController(Controller):
	def __init__(self):
		super().__init__()


class ShopController(Controller):
	def __init__(self):
		super().__init__()


class CartController(Controller):
	def __init__(self):
		super().__init__()


class ProfileController(Controller):
	def __init__(self):
		super().__init__()

	def remove(self, username):
		self.model.user.remove(username)

	def change_username(self, username, new_usarname):
		self.model.user.change_username(username, new_usarname)
