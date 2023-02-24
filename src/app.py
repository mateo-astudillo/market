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
	app = App()
	app.run()
	print("Start")



