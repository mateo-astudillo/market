from .controller import Controller


class OptionsController(Controller):
	def __init__(self):
		super().__init__()


class AddController(Controller):
	def __init__(self):
		super().__init__()

	def add_brand(self, name:str):
		self.model.product.add_brand(name)

	def add_product(self, name, price, brand):
		self.model.product.add_product(name,price,brand)


class EditController(Controller):
	def __init__(self):
		super().__init__()
