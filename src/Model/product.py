

class Product:
	def __init__(self, name:str, price:int, brand:str):
		self.name = name
		self.price = price
		self.brand = brand

		self.id: int = None
