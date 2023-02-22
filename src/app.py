from Controller import Controllers
from View import View
from Model import Model


class App:
	def __init__(self):
		self.controller = Controllers()
		self.view = View(self.controller)
		self.model = Model(self.controller)

		self.controller.set_view(self.view)
		self.controller.set_model(self.model)

		self.controller.set_views()
		self.controller.set_models()
		self.controller.run()


if __name__  == "__main__":
	app = App()
	print("Start")
	app.controller.session.get("login").login("juan123", "holacomoestas")

