from .controller import Controller


class OptionsController(Controller):
	def __init__(self):
		super().__init__()


class AddController(Controller):
	def __init__(self):
		super().__init__()

	def add_product(self, name:str, price:int, brand:int):
		self.model.product.add(name,price,brand)

	def remove_product(self, name:str):
		self.model.product.remove(name)

	def add_brand(self, name:str):
		self.model.brand.add(name)

	def remove_brand(self, name:str):
		self.model.brand.remove(name)


class EditController(Controller):
	def __init__(self):
		super().__init__()
