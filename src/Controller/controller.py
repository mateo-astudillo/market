from Model import User, Database


class Controller:
	def __init__(self, view, model):
		self.view = view
		self.model = model

		self.admin = False
		self.user_logged = False
		self.user_id = None

		self.current = None

	def run(self):
		if not self.model.database:
			self.model.database = Database.create()
		self.go("login")

	def logged(self, username):
		self.user_logged = True
		self.user_id = User.get_id(username)
		# self.view.go("shop")

	def go(self, page):
		if page in ["login", "register"]:
			self.view.go(page)
		elif self.logged and page in ["shop", "cart", "profile"]:
			self.view.go(page)
		elif self.admin and page in ["options", "add", "edit"]:
			self.view.go(page)
		else:
			print("Page not exists")
