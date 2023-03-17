from Controller import Controller
from View import View
from Model import Model


class App:
	def __init__(self):
		self.view =  View()
		self.model = Model()
		self.controller = Controller(self.view, self.model)

		self.view.set_controller(self.controller)
		self.model.set_controller(self.controller)

	def run(self):
		self.controller.run()


if __name__  == "__main__":
	from Controller import ShopController
	from Model import *
	print("Start")
	app = App()
	app.run()
	# print(Product.get_id("MOCHILA", 1))
	# print(Brand.get_id("EVERLAST"))
	ShopController.add_to_cart(1, "MOCHILA", "EVERLAST", 1)
