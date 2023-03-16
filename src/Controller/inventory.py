from Model import Product, Brand


class OptionsController:
	pass


class AddController:
	@staticmethod
	def add_product(name:str, brand:str, stock:int, price:float):
		brand = brand.upper()
		name = name.upper()
		if not Brand.exists(brand):
			Brand.add(brand)
		brand_id = Brand.get_id(brand)
		if Product.exists(name, brand_id):
			return False
		return Product.add(name, brand_id, stock, price)


class EditController:
	@staticmethod
	def remove_product(name:str, brand:str):
		brand_id = Brand.get_id(brand.upper())
		Product.remove(name.upper(), brand_id)

	@staticmethod
	def edit_product(id:str, column:str, value):
		if type(value) is str:
			value = value.upper()
		Product.update(id, column, value)

	@staticmethod
	def remove_brand(name:str):
		# First check product
		Brand.remove(name.upper())

	@staticmethod
	def edit_brand(id:str, column:str, value):
		if type(value) is str:
			value = value.upper()
		Brand.update(id, column, value)

	@staticmethod
	def get_all() -> list:
		products = []
		for product in Product.get_all():
			name, brand, stock, price = product
			p = {
				"name": name,
				"brand": brand,
				"stock": int(stock),
				"price": float(price),
			}
			products.append(p)
		return products
