import pygame

import obj

class Button:
	def __init__(self, x : int, y : int, size_x : int, size_y : int, color : tuple):
		self.x = x
		self.y = y
		self.size_x = size_x
		self.size_y = size_y
		self.color = color
		self.true_color = color

		self.old_pressed = (0, 0, 0)

	def render(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.size_x, self.size_y))

	def tick(self):
		x, y = self.x, self.y
		sx, sy = self.size_x, self.size_y
		mp = pygame.mouse.get_pos()

		if mp[0] >= x and mp[0] <= x + sx and mp[1] >= y and mp[1] <= y + sy:
			r, g, b = self.true_color
			self.color = (min(r + 50, 255), min(g + 50, 255), min(b + 50, 255))

			pressed = pygame.mouse.get_pressed()
			if pressed[0] and not self.old_pressed[0]:
				self.on_click(0)
			if pressed[1] and not self.old_pressed[1]:
				self.on_click(1)
			if pressed[2] and not self.old_pressed[2]:
				self.on_click(2)
			self.old_pressed = pressed
		else:
			self.color = self.true_color

	def on_click(self, button): # 0 - left | 2 - right | 1 - middle
		pass

class CreateObjectButton(Button):
	def __init__(self, x : int, y : int, size_x : int, size_y : int, color : tuple, window_size : tuple):
		super().__init__(x, y, size_x, size_y, color)

		self.window_size = window_size

	def on_click(self, button):
		obj.add_obj(obj.Obj(self.window_size[0] // 2, self.window_size[1] // 2, "gate"))

class ObjectContextButton(Button):
	def __init__(self, x : int, y : int, size_x : int, size_y : int, color : tuple, window_size : tuple):
		super().__init__(x, y, size_x, size_y, color)

		self.window_size = window_size

	def on_click(self, button):
		obj.add_obj(obj.Obj(self.window_size[0] // 2, self.window_size[1] // 2, "gate"))
