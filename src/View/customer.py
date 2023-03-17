from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkScrollableFrame, CTkEntry, StringVar
from Controller import ProfileController, ShopController


class Product(CTkFrame):
	def __init__(self, master, name:str, brand:str, stock:int, price:float):
		super().__init__(master)

		self.stock = stock
		self.stock_var = StringVar( value=str(stock) )

		self.labels = {
			"name": CTkLabel(self, text=name),
			"brand": CTkLabel(self, text=brand),
			"stock": CTkEntry(self, textvariable=self.stock_var, state="disable"),
			"price": CTkLabel( self, text=str(price) )
		}

		self.add_btn = CTkButton(self, text="Add", command=self.add)

	def show(self):
		self.pack()
		for l in self.labels.values():
			l.pack(side="left", padx=4)
		self.add_btn.pack(side="right", expand=True)
		
	def add(self):
		self.stock -= 1
		self.stock_var.set( value=str(self.stock) )
		if self.stock == 0:
			self.pack_forget()
		# ShopController.add_to_cart(self)


class Shop(CTkFrame):
	def __init__(self, view):
		super().__init__(view)
		self.view = view

		#TOP
		self.top = CTkFrame(self)
		self.profile = CTkButton(self.top, text="Profile", command=lambda: self.view.go("profile"))
		self.cart = CTkButton(self.top, text="Cart", command=lambda: self.view.go("cart"))
		self.credit = CTkLabel(self.top, text="Credit $500")

		#TABLE
		self.table = CTkScrollableFrame(self, width=700)
		self.products = []
		self.load_products()

	def show(self):
		self.pack()
		self.top.pack(side="top")
		self.profile.pack(side="left")
		self.credit.pack(side="left")
		self.cart.pack(side="right")
		self.show_products()
		self.table.pack()

	def hide(self):
		self.pack_forget()

	def show_products(self):
		for p in self.products:
			p.show()

	def load_products(self):
		for p in ShopController.get_products():
			name, brand, stock, price = p.values()
			product = Product(self.table, name, brand, stock, price)
			self.products.append(product)


class Cart(CTkFrame):
	def __init__(self, view):
		super().__init__(view)
		self.view = view
		self.table = CTkScrollableFrame(self)
		self.btn_buy = CTkButton(self, text="Buy")
		self.btn_back = CTkButton(self, text="Back", command= lambda: self.view.go("shop"))
		self.add_product()

	def show(self):
		self.pack()
		self.table.pack()
		self.btn_buy.pack(side="right")
		self.btn_back.pack(side="left")

	def hide(self):
		self.pack_forget()

	def add_product(self):
		pr = [
			{"name":"Aceite", "brand":"Natura", "price":340, "icon":"🗑️"},
			{"name":"Atun", "brand":"Carrefour", "price":200,"icon":"🗑️"},
			{"name":"Autito", "brand":"Hot Wheels", "price":600,"icon":"🗑️"},
			{"name":"Aceite", "brand":"Natura", "price":340,"icon":"🗑️"},
			{"name":"Atun", "brand":"Carrefour", "price":200,"icon":"🗑️"},
			{"name":"Autito", "brand":"Hot Wheels", "price":600,"icon":"🗑️"},
			{"name":"Aceite", "brand":"Natura", "price":340,"icon":"🗑️"},
			{"name":"Atun", "brand":"Carrefour", "price":200,"icon":"🗑️"}
		]
		for p in pr:
			f = CTkFrame(self.table)
			name = CTkLabel(f, text=p.get("name"))
			brand = CTkLabel(f, text=p.get("brand"))
			price = CTkLabel(f, text=p.get("price"))
			remove = CTkButton(f, text=p.get("icon"))
			f.pack()
			name.pack(side="left", ipadx=5)
			brand.pack(side="left", ipadx=5)
			price.pack(side="left", ipadx=5)
			remove.pack(side="left", ipadx=5)


class Profile(CTkFrame):
	def __init__(self, view):
		super().__init__(view)
		self.view = view
		self.state = False

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

		self.btn_edit = CTkButton(self, text="Edit", command=self.show_save)
		self.btn_save = CTkButton(self, text="Save", command=self.save)
		self.btn_cancel = CTkButton(self, text="Cancel", command=self.show_edit)
		self.btn_back = CTkButton(self, text="Back", command= lambda: self.view.go("shop"))

	def show(self):
		self.pack()
		self.set_placeholder()
		self.pack_widgets()
		self.show_edit()

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

	def show_edit(self):
		self.set_state()
		self.btn_edit.pack(side="right")
		self.btn_back.pack(side="left")
		self.btn_cancel.pack_forget()
		self.btn_save.pack_forget()

	def show_save(self):
		self.set_state()
		self.btn_save.pack(side="right")
		self.btn_cancel.pack(side="left")
		self.btn_back.pack_forget()
		self.btn_edit.pack_forget()

	def save(self):
		self.show_edit()

	def set_placeholder(self):
		user = ProfileController.get_user(self.view.controller.user_id)
		for key,var in self.variables.items():
			var.set(user.get(key))

	def pack_widgets(self):
		for entry in self.entries.values():
			entry.pack()
