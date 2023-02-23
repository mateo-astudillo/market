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

	def create_sale(self, product_id:int, price:int, date):
		user_id = self.model.user.id[0]
		self.model.sale.create(user_id, product_id, price, date)


class ProfileController(Controller):
	def __init__(self):
		super().__init__()

	def remove(self):
		id = self.model.user.id
		self.model.user.remove(id)

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

	def change_password(self, password):
		id = self.model.user.id
		self.model.user.change_password(id, password)
