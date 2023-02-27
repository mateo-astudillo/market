from customtkinter import CTkFrame, CTkButton, CTkLabel, CTkEntry, CTkFrame, StringVar


class Menu:
	def __init__(self, view):
		self.view = view

	def show(self):
		pass

	def hide(self):
		pass


class Shop:
	def __init__(self, view):
		self.view = view

	def show(self):
		pass

	def hide(self):
		pass


class Cart:
	def __init__(self, view):
		self.view = view

	def show(self):
		pass

	def hide(self):
		pass


class Profile(CTkFrame):
	def __init__(self, view):
		super().__init__(view)

		self.view = view

		self.variables = {
			"username": StringVar(),
			"name": StringVar(),
			"surname": StringVar(),
			"age": StringVar(),
		}
		self.entries = {
			"username": CTkEntry(self, textvariable=self.variables.get("username")),
			"password": CTkEntry(self, show="*"),
			"name": CTkEntry(self, textvariable=self.variables.get("name")),
			"surname": CTkEntry(self, textvariable=self.variables.get("surname")),
			"age": CTkEntry(self, textvariable=self.variables.get("age"))
		}
		self.set_state()

		self.btn_edit = CTkButton(self, text="Edit", command=self.edit)
		self.btn_save = CTkButton(self, text="Save", command=self.save)

	def show(self):
		self.pack()
		self.set_placeholder()
		self.pack_widgets()

	def hide(self):
		self.pack_forget()

	def set_state(self):
		if self.state:
			for entry in self.entries.values():
				entry.configure(state="normal")
		else:
			for entry in self.entries.values():
				entry.configure(state="disabled")
		self.state = not self.state

	def edit(self):
		self.set_state()
		self.btn_edit.pack_forget()
		self.btn_save.pack()

	def save(self):
		self.set_state()
		self.btn_save.pack_forget()
		self.btn_edit.pack()

	def set_placeholder(self):
		user = self.controller.get_user()
		for key,var in self.variables.items():
			var.set(user.get(key))

	def pack_widgets(self):
		for entry in self.entries.values():
			entry.pack()
		self.btn_edit.pack()
