from .controller import Controller


class OptionsController(Controller):
	def __init__(self):
		super().__init__()


class AddController(Controller):
	def __init__(self):
		super().__init__()

	def add_product(self, name:str, price:float, brand:str):
		price = float(price)
		self.model.product.add(name, price, brand)

	def add_brand(self, name:str):
		self.model.brand.add(name)



class EditController(Controller):
	def __init__(self):
		super().__init__()

	def remove_product(self, name:str, brand:str):
		self.model.product.remove(name, brand)

	def edit_product(self, id:str, column:str, value):
		self.model.product.edit(id, column, value)

	def remove_brand(self, name:str):
		self.model.brand.remove(name)

	def edit_brand(self, id:str, column:str, value):
		self.model.brand.edit(id, column, value)
