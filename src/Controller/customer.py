from Model import User, Product, Cart, Brand


class ShopController:
	@staticmethod
	def get_products():
		products = []
		for product in Product.get_all():
			name, brand, stock, price = product
			p = {
				"name": name.capitalize(),
				"brand": brand.capitalize(),
				"stock": int(stock),
				"price": float(price),
			}
			products.append(p)
		return products

	@staticmethod
	def add_to_cart(user_id:int, product_name:str, brand_name:str, amount:int) -> bool:
		product_name = product_name.upper()
		brand_name = brand_name.upper()
		brand_id = Brand.get_id(brand_name)
		product_id = Product.get_id(product_name, brand_id)
		stock = Product.get_value(product_id, "stock")
		stock = int(stock[0]) - 1
		Product.update(product_id, "stock", stock)
		if Cart.exists(user_id, product_id):
			id = Cart.get_id(user_id, product_id)
			amount_db = Cart.get_amount(user_id, product_id)[0]
			amount += amount_db
			return Cart.update(id, "amount", amount)
		return Cart.add(user_id, product_id, amount)


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

	@staticmethod
	def get_products(user_id:int) -> list:
		products_cart = Cart.get_products(user_id)
		products = []
		for id, amount in products_cart:
			name, brand, stock, price = Product.get_one(id)
			p = {
				"name": name.capitalize(),
				"brand": brand.capitalize(),
				"amount": amount,
				"price": float(price)
			}
			products.append(p)
		return products


class ProfileController:
	@staticmethod
	def remove(id:int):
		User.remove(id)

	@staticmethod
	def set_data(id:int, colunm:str, value):
		User.update(id, colunm, value)

	@staticmethod
	def change_username(id:int, username:str):
		if not User.exists(username):
			User.change_username(id, username)
			print("The username has succesfully changed")
		else:
			print("The user already exists")

	@staticmethod
	def change_password(id:int, password:str):
		User.change_password(id, password)

	@staticmethod
	def get_user(id:int) -> dict:
		username, name, surname, age = User.get_user(id)
		user = {
			"username": username,
			"name": name,
			"surname": surname,
			"age": age,
		}
		return user