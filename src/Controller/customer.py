from Model import User

class ShopController:
	pass


class CartController:
	@staticmethod
	def add(self, product_id:int):
		user_id = self.model.user.id
		if not self.model.sale.add(user_id, product_id):
			print("There are no products in the cart, crazy man")
			return False
		print("Product added")
		return True


class ProfileController:
	@staticmethod
	def remove(id):
		User.remove(id)

	@staticmethod
	def set_data(id, colunm, value):
		User.set_data(id, colunm, value)

	@staticmethod
	def change_username(id, username):
		if not User.exists(username):
			User.change_username(id, username)
			print("The username has succesfully changed")
		else:
			print("The user already exists")

	@staticmethod
	def change_password(id, password):
		User.change_password(id, password)

	@staticmethod
	def get_user(id) -> dict:
		username, name, surname, age = User.get_user(id)
		user = {
			"username": username,
			"name": name,
			"surname": surname,
			"age": age,
		}
		return user