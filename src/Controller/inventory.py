from Model import Product, Brand


class OptionsController:
	pass


class AddController:
	@staticmethod
	def add_product(name:str, brand:str, stock:int, price:float):
		if not Brand.exists(brand):
			Brand.add(brand)
		brand_id = Brand.get_id(brand)
		if Product.exists(name, brand_id):
			return False
		return Product.add(name, brand_id, stock, price)


class EditController:
	@staticmethod
	def remove_product(name:str, brand:str):
		brand_id = Brand.get_id(brand)
		Product.remove(name, brand_id)

	@staticmethod
	def edit_product(id:str, column:str, value):
		Product.update(id, column, value)

	@staticmethod
	def remove_brand(name:str):
		# First check product
		Brand.remove(name)

	@staticmethod
	def edit_brand(id:str, column:str, value):
		Brand.update(id, column, value)

	@staticmethod
	def get_all():
		return Product.get_all()
