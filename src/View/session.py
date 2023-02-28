from customtkinter import CTkFrame, CTkButton, CTkLabel, CTkEntry, CTkFrame
from Controller import LoginController, RegisterController


class Login(CTkFrame):
	def __init__(self, view):
		super().__init__(view)

		self.view = view

		self.entries = {
			"username": CTkEntry(self, placeholder_text="Username"),
			"password": CTkEntry(self, placeholder_text="Password", show="*")
		}

		self.buttons = {
			"login": CTkButton(self, text="Login", command=self.login),
			"register": CTkButton(self, text="Register", command=self.register)
		}

	def show(self):
		self.pack()
		self.pack_widgets()

	def hide(self):
		self.pack_forget()

	def pack_widgets(self):
		for entry in self.entries.values():
			entry.pack()

		for button in self.buttons.values():
			button.pack()

	def login(self):
		# username = self.entries.get("username").get()
		# password = self.entries.get("password").get()
		username = "juan"
		password = "hola"
		if LoginController.login(username, password):
			self.view.logged(username)

	def register(self):
		pass

class Register(CTkFrame):
	def __init__(self, view):
		super().__init__(view)

		self.view = view

		self.entries = {
			"username": CTkEntry(self, placeholder_text="Username"),
			"password": CTkEntry(self, placeholder_text="Password", show="*")
		}
		self.buttons = {
			"register": CTkButton(self, text="Register", command=self.register),
			"cancel": CTkButton(self, text="Cancel", command=self.cancel)
		}

	def show(self):
		self.pack()
		self.pack_widgets()

	def hide(self):
		self.pack_forget()

	def pack_widgets(self):
		for entry in self.entries.values():
			entry.pack()

		for button in self.buttons.values():
			button.pack()

	def register(self):
		username = self.entries.get("username").get()
		password = self.entries.get("password").get()
		if RegisterController.register(username, password):
			self.view.go("login")

	def cancel(self):
		pass
