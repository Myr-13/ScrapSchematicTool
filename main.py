import pygame

import configuration as config
import obj
import ui

class ScrapSchematic:
	def __init__(self):
		self.config = config.Config()
		self.settings = {}

		self.running = True

		self.buttons = []

	def run(self):
		self.config.load()
		self.settings = self.config.settings

		# Pygame
		self.win = pygame.display.set_mode((self.settings["window"]["width"], self.settings["window"]["height"]), pygame.RESIZABLE)
		self.clock = pygame.time.Clock()

		# Create tool bar buttons
		self.buttons.append(ui.Button(0, 0, 40, 25, (100, 100, 100)))

		# Create objects buttons
		self.buttons.append(ui.CreateObjectButton(self.win.get_width() - 100, 25, 50, 50, (100, 100, 100), (self.win.get_width(), self.win.get_height())))

		# Main cycle
		while self.running:
			self.clock.tick(self.settings["window"]["fps"])

			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					self.on_close()
					self.running = False

			# Update work space
			for o in obj.objects:
				o.tick()

			# Update ui
			for but in self.buttons:
				but.tick()
			
			self.win.fill((0, 0, 0))
			self.on_render()
			pygame.display.update()

	def on_render(self):
		# Render work space
		for o in obj.objects:
			o.render(self.win)

		# Render ui
		for but in self.buttons:
			but.render(self.win)

	def on_close(self):
		self.config.save()

if __name__ == '__main__':
	main = ScrapSchematic()
	main.run()
