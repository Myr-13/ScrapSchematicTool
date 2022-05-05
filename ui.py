class Panel:
	def __init__(self, x : int, y : int, size_x : int, size_y : int, color : tuple):
		self.x = x
		self.y = y
		self.size_x = size_x
		self.size_y = size_y
		self.color = color

		self.objects = []

	def add_object(self, object):
		self.objects.append(object)

screen_panel = Panel()

class UIObject:
	"""
	Common class of object for UI

	x : int
	y : int
	size_x : int
	size_y : int
	color : tuple(r, g, b)
	"""
	def __init__(self, x : int, y : int, size_x : int, size_y : int, color : tuple, panel = screen_panel):
		self.x = x
		self.y = y
		self.size_x = size_x
		self.size_y = size_y
		self.color = color
		self.panel = panel

	def render(self, win):
		pass

class Button(UIObject):
	def __init__(self, x : int, y : int, size_x : int, size_y : int, color : tuple, panel = screen_panel):
		super().__init__(x, y, size_x, size_y, color, panel)

		panel.add_object(self)
