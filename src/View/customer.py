from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkScrollableFrame

class Menu:
	def __init__(self, view):
		self.view = view

	def show(self):
		pass

	def hide(self):
		pass


class Shop(CTkFrame):
	def __init__(self, view):
		super().__init__(view)
		self.view = view
		#TOP
		self.top = CTkFrame(self)
		self.credit = CTkLabel(self.top, text="Credit $500")
		self.cart = CTkButton(self.top, text="Cart")
		#TABLE
		self.table = CTkScrollableFrame(self)
		self.add_product()

	def show(self):
		self.pack()
		self.top.pack(side="top")
		self.credit.pack(side="left")
		self.cart.pack(side="right")
		self.table.pack()

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


class Cart:
	def __init__(self, view):
		self.view = view

	def show(self):
		pass

	def hide(self):
		pass


class Profile:
	def __init__(self, view):
		self.view = view

	def show(self):
		pass

	def hide(self):
		pass
