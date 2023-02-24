from .view import View
from customtkinter import CTkButton, CTkLabel, CTkEntry, CTkFrame, StringVar

class Menu(View):
	def __init__(self):
		super().__init__()


class Shop(View):
	def __init__(self):
		super().__init__()


class Cart(View):
	def __init__(self):
		super().__init__()


class Profile(View):
	def __init__(self, root):
		super().__init__()
		self.frame = CTkFrame(master=root)
		self.edit_fr = CTkFrame(master=root)
		self.state = False

		self.variables = {
			"username": StringVar(),
			"name": StringVar(),
			"surname": StringVar(),
			"age": StringVar(),
		}
		self.entries = {
			"username": CTkEntry(self.frame, textvariable=self.variables.get("username")),
			"password": CTkEntry(self.frame, show="*"),
			"name": CTkEntry(self.frame, textvariable=self.variables.get("name")),
			"surname": CTkEntry(self.frame, textvariable=self.variables.get("surname")),
			"age": CTkEntry(self.frame, textvariable=self.variables.get("age"))
		}
		self.set_state()

		self.btn_edit = CTkButton(self.frame, text="Edit", command=self.edit)
		self.btn_save = CTkButton(self.frame, text="Save", command=self.save)

	def show(self):
		self.frame.pack()
		self.set_placeholder()
		self.pack_widgets()

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