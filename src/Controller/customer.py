from Model import User, Product, Cart, Brand


class ShopController:
	pass


class CartController:
	@staticmethod
	def add(user_id:int, product_name:str, brand_name:str, amount:int):
		brand_id = Brand.get_id(brand_name)
		product_id = Product.get_id(product_name, brand_id)
		return Cart.add(user_id, product_id, amount)

	@staticmethod
	def remove(user_id:int, product_name:str, brand_name:str):
		brand_id = Brand.get_id(brand_name)
		product_id = Product.get_id(product_name, brand_id)
		return Cart.remove(user_id, product_id)

	@staticmethod
	def amount(user_id:int, product_name:str, brand_name:str, amount:int):
		brand_id = Brand.get_id(brand_name)
		product_id = Product.get_id(product_name, brand_id)
		cart_id = Cart.get_id(user_id, product_id)
		return Cart.update(cart_id, "amount", amount)


class ProfileController:
	@staticmethod
	def remove(id):
		User.remove(id)

	@staticmethod
	def set_data(id, colunm, value):
		User.update(id, colunm, value)

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