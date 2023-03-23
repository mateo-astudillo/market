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
		self.view.mainloop()


if __name__  == "__main__":
	# from Controller import *
	# from Model import *
	print("Start")
	app = App()
	app.run()
	# print(
	# 	CartController.get_products(2)
	# )
