from Controller import *
from View import *
from Model import Model


class App:
	def __init__(self):
		self.model = Model()

		self.views = {
			"login": Login(),
			"register": Register(),
			"menu": Menu(),
			"shop": Shop(),
			"cart": Cart(),
			"profile": Profile(),
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
	app = App()
	print("Start")
	app.model.init_database()
	app.controllers.get("register").register("pepito","pass")
	# app.controllers.get("profile").set_data("1","surname","alfonso")
	# app.controllers.get("profile").set_data("1","age","32")
	app.controllers.get("login").login("pepito", "pass")
	# app.controllers.get("profile").change_password("pass")
	# app.controllers.get("profile").remove()
	# app.controllers.get("profile").set_data("surname","alfonsin")
	# app.controllers.get("profile").change_username("prueba")

