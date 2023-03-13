from Model import User, Product, Cart

class ShopController:
	pass


class CartController:
	@staticmethod
	def add(user_id:int, product_name:str, brand_name:str, amount:int):
		product_id = Product.get_id(product_name, brand_name)
		return Cart.add(user_id, product_id, amount)

	@staticmethod
	def remove(user_id:int, product_name:str, brand_name:str):
		product_id = Product.get_id(product_name, brand_name)
		return Cart.remove(user_id, product_id)

	@staticmethod
	def amount(user_id:int, product_name:str, brand_name:str, amount:int):
		product_id = Product.get_id(product_name, brand_name)
		return Cart.amount(user_id, product_id, amount)

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