from .view import View
from customtkinter import CTkButton, CTkLabel, CTkEntry, CTkFrame

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

		self.entries = {
			"username": CTkEntry(self.frame),
			"password": CTkEntry(self.frame, show="*"),
			"name": CTkEntry(self.frame),
			"surname": CTkEntry(self.frame),
			"age": CTkEntry(self.frame)
		}
		self.set_state()

		self.btn_edit = CTkButton(self.frame, text="Edit", command=self.edit)
		self.btn_save = CTkButton(self.frame, text="Save", command=self.save)

	def show(self):
		self.frame.pack()
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


	def pack_widgets(self):
		for entry in self.entries.values():
			entry.pack()
		self.btn_edit.pack()