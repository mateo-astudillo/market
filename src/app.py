from Controller import *
from View import *
from Model import Model
from customtkinter import CTk

class App:
	def __init__(self, root):
		self.model = Model()

		self.views = {
			"login": Login(root),
			"register": Register(root),
			"menu": Menu(),
			"shop": Shop(),
			"cart": Cart(),
			"profile": Profile(root),
			"options": Options(),
			"add": Add(),
			"edit": Edit(),
		}

		self.controllers = {
			"login": LoginController(),
			"register": RegisterController(),
			"menu": MenuController(),
			"shop": ShopController(),
			"cart": CartController(),
			"profile": ProfileController(),
			"options": OptionsController(),
			"add": AddController(),
			"edit": EditController(),
		}

		for view, controller in self.controllers.items():
			controller.set_view(self.views.get(view))
			controller.set_model(self.model)

		for controller, view in self.views.items():
			view.set_controller(self.controllers.get(controller))

if __name__  == "__main__":
	root = CTk()
	app = App(root)
	app.views.get("profile").show()
	app.model.init_database()
	root.mainloop()


