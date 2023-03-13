from Model import Product, Brand


class OptionsController:
	pass


class AddController:
	@staticmethod
	def add_product(name:str, brand:str, stock:int, price:float):
		if not Brand.exists(brand):
			Brand.add(brand)

		if Product.exists(name, brand):
			return False
		Product.add(name, brand, stock, price)
		return True

	@staticmethod
	def add_brand(name:str):
		Brand.add(name)


class EditController:
	@staticmethod
	def remove_product(name:str, brand:str):
		Product.remove(name, brand)

	@staticmethod
	def edit_product(id:str, column:str, value):
		Product.edit(id, column, value)

	@staticmethod
	def remove_brand(name:str):
		Brand.remove(name)

	@staticmethod
	def edit_brand(id:str, column:str, value):
		Brand.edit(id, column, value)
