from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkScrollableFrame, CTkEntry, StringVar
from tkinter import END
from Controller import AddController, EditController, Validator

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
		self.add_btn = CTkButton(self, text="Add", command=self.add)

		self.entries = {
			"name": CTkEntry(self, placeholder_text="name"),
			"brand": CTkEntry(self, placeholder_text="brand"),
			"stock": CTkEntry(self, placeholder_text="stock"),
			"price": CTkEntry(self, placeholder_text="price")
		}

	def show(self):
		self.pack()
		self.title.pack()
		self.pack_widgets()
		self.back.pack(side="left")
		self.add_btn.pack(side="right")

	def hide(self):
		self.pack_forget()

	def pack_widgets(self):
		for entry in self.entries.values():
			entry.pack()

	def add(self):
		name,brand,stock,price = self.get_data()
		if AddController.add_product(name, brand, stock, price):
			self.title.configure(fg_color="green")
		else:
			self.title.configure(fg_color="red")
		self.reset_entry()

	def get_data(self):
		data = (
			self.entries.get("name").get(),
			self.entries.get("brand").get(),
			int(self.entries.get("stock").get()),
			int(self.entries.get("price").get())
		)
		return data

	def reset_entry(self):
		for entry in self.entries.values():
			entry.delete(0,END)
		self.focus()

class Edit(CTkFrame):
	def __init__(self, view):
		super().__init__(view)
		self.view = view

		self.top = CTkFrame(self)
		self.title = CTkLabel(self.top, text="EDIT :D")
		self.search = CTkEntry(self.top, placeholder_text="Search")
		self.table = CTkScrollableFrame(self)
		self.back_btn = CTkButton(self, text="Back", command=lambda:self.view.go("options"))

		self.search.bind("<KeyRelease>", self.search_keyrelease)

		self.products = []
		self.load_products()

	def show(self):
		self.pack()
		self.top.pack(side="top")
		self.title.pack()
		self.search.pack(side="left")
		self.table.pack()
		self.show_products()
		self.back_btn.pack(side="bottom")

	def hide(self):
		self.pack_forget()

	def show_products(self):
		for p in self.products:
			if p.get("status"):
				p.get("frame").pack()
			else:
				p.get("frame").pack_forget()

	def load_products(self):
		for p in EditController.get_all():
			frame = CTkFrame(self.table)
			labels = []
			for value in p.values():
				l = CTkLabel(frame, text=value)
				l.pack(side="left", padx=5)
				labels.append(l)
			p["frame"] = frame
			p["status"] = True
			p["labels"] = labels
			self.products.append(p)

	def search_keyrelease(self, event):
		if not bool(self.products):
			print("error load products")
			return
		if not Validator.key_press(str(event.char)):
			print("Not valid key")
			return
		product = self.search.get()
		if product == "":
			for p in self.products:
				p["status"] = True
			self.show_products()
		else:
			self.search_product(product)

	def search_product(self, product):
		for p in self.products:
			if product in p.get("name") or product in p.get("brand"):
				p["status"] = True
			else:
				p["status"] = False
				p.get("frame").pack_forget()
