from Controller import Controller, AddController
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
	print("Start")
	app = App()
	app.run()
	AddController.add_product("Galletitas", "Toddy", 20, 500)
	AddController.add_product("Galletitas", "Toddy", 20, 300)
	AddController.add_product("Galletitas", "Oreo", 60, 400)
	AddController.add_product("Alfajor", "Oreo", 489, 30)





