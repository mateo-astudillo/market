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

	def set_data(self, colunm, value):
		id = self.model.user.id
		self.model.user.set_data(id, colunm, value)

	def change_username(self, username):
		id = self.model.user.id
		if not self.model.user.exists(username):
			self.model.user.change_username(id, username)
			print("The username has succesfully changed")
		else:
			print("The user already exists")

	def change_password(self, id, password):
		self.model.user.change_password(id, password)
