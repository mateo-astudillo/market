from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkScrollableFrame, CTkEntry, StringVar
from tkinter import END
from Controller import AddController, EditController

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
		self.search.bind("<KeyRelease>", self.get_product_to_search)
		self.btn_search = CTkButton(self.top, text="Search", command=self.search_product)
		self.table = CTkScrollableFrame(self)
		self.back_btn = CTkButton(self, text="Back", command=lambda:self.view.go("options"))
		self.show_all_products()

	def show(self):
		self.pack()
		self.top.pack(side="top")
		self.title.pack()
		self.search.pack(side="left")
		self.table.pack()

	def hide(self):
		self.pack_forget()

	def get_product_to_search(self,event):
		if not event.keysym == "Caps_Lock":
			product = self.search.get()
			if product == "":
				self.hide_list()
				self.show_all_products()
			else:
				self.search_product(product)

	def search_product(self, product):
		products = EditController.get_all()
		products_founded = []

		for p in products:
			if product in p[0] or product in p[1]:
				products_founded.append(p)

		self.hide_list()
		self.show_all_products(products_founded)

	def show_all_products(self, products = None):

		if products == None:
			products = EditController.get_all()

		self.back_btn.pack(side="bottom")

		for p in products:
			f = CTkFrame(self.table)
			name = CTkLabel(f, text=p[0])
			brand = CTkLabel(f, text=p[1])
			price = CTkLabel(f, text=p[2])
			f.pack()
			name.pack(side="left", ipadx=5)
			brand.pack(side="left", ipadx=5)
			price.pack(side="left", ipadx=5)

	def hide_list(self):
		for w in self.table.winfo_children():
			w.pack_forget()
		self.back_btn.pack_forget()