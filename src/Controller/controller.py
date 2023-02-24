

class Controller:
	def __init__(self, view, model):
		self.view = view
		self.model = model

		self.admin = False
		self.user_id = None

	def run(self):
		self.view.go("login")
