from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkScrollableFrame, CTkEntry, StringVar
from tkinter import END
from Controller import AddController

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
		self.add = CTkButton(self, text="Add", command=self.add)

		self.entries = {
			"name": CTkEntry(self, placeholder_text="name"),
			"brand": CTkEntry(self,placeholder_text="brand"),
			"stock": CTkEntry(self, placeholder_text="stock"),
			"price": CTkEntry(self, placeholder_text="price")
		}

	def show(self):
		self.pack()
		self.title.pack()
		self.pack_widgets()
		self.back.pack(side="left")
		self.add.pack(side="right")

	def hide(self):
		self.pack_forget()

	def pack_widgets(self):
		for entry in self.entries.values():
			entry.pack()

	def add(self):
		name = self.entries.get("name").get()
		brand = self.entries.get("brand").get()
		stock = int(self.entries.get("stock").get())
		price = int(self.entries.get("price").get())
		AddController.add_product(name,brand,stock,price)
		self.reset_entry()


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
		self.btn_search = CTkButton(self.top, text="Search")
		self.table = CTkScrollableFrame(self)
		self.add_product()
		self.back = CTkButton(self, text="Back", command=lambda:self.view.go("options"))


	def show(self):
		self.pack()
		self.top.pack()
		self.title.pack()
		self.search.pack(side="left")
		self.btn_search.pack(side="right")
		self.table.pack()
		self.back.pack()

	def hide(self):
		self.pack_forget()

	def add_product(self):
		pr = [
			{"name":"Aceite", "brand":"Natura", "price":340},
			{"name":"Atun", "brand":"Carrefour", "price":200},
			{"name":"Autito", "brand":"Hot Wheels", "price":600},
			{"name":"Aceite", "brand":"Natura", "price":340},
			{"name":"Atun", "brand":"Carrefour", "price":200},
			{"name":"Autito", "brand":"Hot Wheels", "price":600},
			{"name":"Aceite", "brand":"Natura", "price":340},
			{"name":"Atun", "brand":"Carrefour", "price":200},
			{"name":"Autito", "brand":"Hot Wheels", "price":600},
			{"name":"Aceite", "brand":"Natura", "price":340},
			{"name":"Atun", "brand":"Carrefour", "price":200},
			{"name":"Autito", "brand":"Hot Wheels", "price":600}
		]
		for p in pr:
			f = CTkFrame(self.table)
			name = CTkLabel(f, text=p.get("name"))
			brand = CTkLabel(f, text=p.get("brand"))
			price = CTkLabel(f, text=p.get("price"))
			f.pack()
			name.pack(side="left", ipadx=5)
			brand.pack(side="left", ipadx=5)
			price.pack(side="left", ipadx=5)
