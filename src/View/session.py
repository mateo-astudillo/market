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

		self.entries.get("username").focus()
		self.entries.get("username").bind("<KeyRelease>", command=self.focus_password)
		self.entries.get("password").bind("<KeyRelease>", command=self.login_return)

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

	def focus_password(self, event):
		if event.keysym == "Return":
			self.entries.get("password").focus()

	def login_return(self, event):
		if event.keysym == "Return":
			self.login()

	def login(self):
		username = self.entries.get("username").get()
		password = self.entries.get("password").get()

		if LoginController.login(username, password):
			if username == "admin":
				self.view.go("options")
			else:
				self.view.logged(username)

	def register(self):
		self.view.go("register")

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

		self.entries.get("username").focus()
		self.entries.get("username").bind("<KeyRelease>", command=self.focus_password)
		self.entries.get("password").bind("<KeyRelease>", command=self.register_return)

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

	def focus_password(self, event):
		if event.keysym == "Return":
			self.entries.get("password").focus()

	def register_return(self, event):
		if event.keysym == "Return":
			self.register()

	def register(self):
		username = self.entries.get("username").get()
		password = self.entries.get("password").get()
		if RegisterController.register(username, password):
			self.view.go("login")

	def cancel(self):
		self.view.go("login")
