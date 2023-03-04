from Controller import Controller
from View import View
from Model import Model, Product


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
	print("Start")
	app = App()
	app.run()
	Product.add("Aceite", "Natura", 20, 500)
	Product.add("Jugo", "Marolio", 60, 400)
	Product.add("Atun", "Del Sur", 489, 30)




