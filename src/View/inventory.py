from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkScrollableFrame, CTkEntry, StringVar


class Options(CTkFrame):
	def __init__(self, view):
		super().__init__(view)

		self.view = view
		self.btn_add = CTkButton(self, text="Add Product",command=lambda: self.view.go("add"))
		self.btn_edit = CTkButton(self, text="Edit Product", command=lambda: self.view.go("edit"))
		self.btn_exit = CTkButton(self, text="Exit", command=lambda: self.view.go("login"))

	def show(self):
		self.pack()
		self.btn_add.pack()
		self.btn_edit.pack()
		self.btn_exit.pack()

	def hide(self):
		self.pack_forget()


class Add(CTkFrame):
	def __init__(self, view):
		super().__init__(view)

		self.view = view
		self.title = CTkLabel(self, text="ADD :D")
		self.back = CTkButton(self, text="Back", command=lambda:self.view.go("options"))

	def show(self):
		self.pack()
		self.title.pack()
		self.back.pack()

	def hide(self):
		self.pack_forget()


class Edit(CTkFrame):
	def __init__(self, view):
		super().__init__(view)

		self.view = view
		self.title = CTkLabel(self, text="EDIT :D")
		self.back = CTkButton(self, text="Back", command=lambda:self.view.go("options"))


	def show(self):
		self.pack()
		self.title.pack()
		self.back.pack()

	def hide(self):
		self.pack_forget()
