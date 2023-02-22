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

	def set_data(self, id, colunm, value):
		self.model.user.set_data(id, colunm, value)

	def change_username(self, id, username):
		self.model.user.change_username(id, username)

	def change_password(self, id, password):
		self.model.user.change_password(id, password)
