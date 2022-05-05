import pygame

import ui

objects = []

def add_obj(obj):
	objects.append(obj)

class Obj:
	def __init__(self, x, y, type):
		self.x, self.y = x, y
		self.size_x, self.size_y = 25, 25
		self.type = type

		if self.type == "gate":
			self.color = (100, 255, 100)
		else:
			self.color = (100, 100, 255)

		self.old_mouse_pos = (-1, -1)

		self.context_menu_opened = False

		self.buttons = []

	def render(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, 16, 16))

		for but in self.buttons:
			but.render(win)

	def tick(self):
		x, y = self.x, self.y
		sx, sy = self.size_x, self.size_y
		mp = pygame.mouse.get_pos()

		if self.old_mouse_pos == (-1, -1):
			self.old_mouse_pos = mp

		if mp[0] >= x and mp[0] <= x + sx and mp[1] >= y and mp[1] <= y + sy:
			pressed = pygame.mouse.get_pressed()
			if pressed[0]:
				self.x += mp[0] - self.old_mouse_pos[0]
				self.y += mp[1] - self.old_mouse_pos[1]

				self.context_menu_opened = False
			if pressed[2] and not self.context_menu_opened:
				inc_size = ui.Button(x + 25 // 2, y + 25 // 2, 75, 25, (170, 170, 170))

				self.buttons.append(inc_size)

				self.context_menu_opened = True
		
		self.old_mouse_pos = mp

		# Update buttons
		for but in self.buttons:
			but.tick()
