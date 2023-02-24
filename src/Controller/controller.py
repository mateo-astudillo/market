from Model import User


class Controller:
	def __init__(self, view, model):
		self.view = view
		self.model = model

		self.admin = False
		self.logged = False
		self.user_id = None

	def logged(self, username):
		self.logged = True
		self.user_id = User.get_id(username)
		self.view.go("shop")

	def go(self, page):
		if page in ["login", "register"]:
			self.view.go(page)
		elif self.logged and page in ["shop", "cart", "profile"]:
			self.view.go(page)
		elif self.admin and page in ["options", "add", "edit"]:
			self.view.go(page)

	def run(self):
		self.view.go("login")
