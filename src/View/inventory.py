from Controller.inventory import OptionsController, AddController, EditController


class Options:
	def __init__(self, controller: OptionsController):
		self.controller = controller


class Add:
	def __init__(self, controller: AddController):
		self.controller = controller


class Edit:
	def __init__(self, controller: EditController):
		self.controller = controller
