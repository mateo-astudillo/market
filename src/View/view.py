from Controller import Controllers
from .session import Login, Register
from .customer import Menu, Shop, Cart, Profile 
from .inventory import Options, Add, Edit

class View:
	def __init__(self, controller:Controllers):
		self.controller = controller

		self.session = {
			"login": Login( self.controller.session.get("login") ),
			"register": Register( self.controller.session.get("register") )
		}

		self.customer_menu = Menu( self.controller.customer.get("menu") )
		self.customer = {
			"shop": Shop( self.controller.customer.get("shop") ),
			"cart": Cart( self.controller.customer.get("cart") ),
			"profile": Profile( self.controller.customer.get("profile") )
		}

		self.inventory = {
			"options": Options( self.controller.inventory.get("options") ),
			"add": Add( self.controller.inventory.get("add") ),
			"edit": Edit( self.controller.inventory.get("edit") )
		}

	def go(self, page:str):
		if page in self.session.values():
			self.session.get(page)
		elif page in self.customer.values():
			self.customer.get(page)
		elif page in self.inventory.values():
			self.inventory.get(page)
		else:
			self.session.get("login")
