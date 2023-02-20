from Controller import Controller
from View import View
from Model import Model


class App:
	def __init__(self):
		self.controller = Controller()
		self.view = View(self.controller)
		self.model = Model(self.controller)

		self.controller.set_view(self.view)
		self.controller.set_model(self.model)

		self.controller.run()


if __name__  == "__main__":
	app = App()
	print("Start")
