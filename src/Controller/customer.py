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

	def add(self, product_id:int):
		user_id = self.model.user.id
		if not self.model.sale.add(user_id, product_id):
			print("There are no products in the cart, crazy man")
			return False
		print("Product added")
		return True


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

	def get_user(self) -> dict:
		id = self.model.user.id
		username, name, surname, age = self.model.user.get_user(id)
		user = {
			"username": username,
			"name": name,
			"surname": surname,
			"age": age,
		}
		return user