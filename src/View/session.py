from .view import View
from customtkinter import CTkButton, CTkLabel, CTkEntry, CTkFrame


class Login(View):
	def __init__(self, root):
		super().__init__()
		self.frame = CTkFrame(master=root)

		self.entries = {
			"username": CTkEntry(self.frame, placeholder_text="Username"),
			"password": CTkEntry(self.frame, placeholder_text="Password", show="*")
		}

		self.buttons = {
			"login": CTkButton(self.frame, text="Login", command=self.login),
			"register": CTkButton(self.frame, text="Register", command=self.register)
		}

	def show(self):
		self.frame.pack()
		self.pack_widgets()

	def pack_widgets(self):
		for entry in self.entries.values():
			entry.pack()

		for button in self.buttons.values():
			button.pack()

	def login(self):
		username = self.entries.get("username").get()
		password = self.entries.get("password").get()
		self.controller.login(username, password)

	def register(self):
		pass

class Register(View):
	def __init__(self, root):
		super().__init__()
		self.frame = CTkFrame(master=root)

		self.entries = {
			"username": CTkEntry(self.frame, placeholder_text="Username"),
			"password": CTkEntry(self.frame, placeholder_text="Password", show="*")
		}
		self.buttons = {
			"register": CTkButton(self.frame, text="Register", command=self.register),
			"cancel": CTkButton(self.frame, text="Cancel", command=self.cancel)
		}

	def show(self):
		self.frame.pack()
		self.pack_widgets()

	def pack_widgets(self):
		for entry in self.entries.values():
			entry.pack()

		for button in self.buttons.values():
			button.pack()

	def register(self):
		username = self.entries.get("username").get()
		password = self.entries.get("password").get()
		self.controller.register(username, password)

	def cancel(self):
		pass