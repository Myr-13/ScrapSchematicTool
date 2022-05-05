import pygame

import configuration as config

class ScrapSchematic:
	def __init__(self):
		self.config = config.Config()
		self.settings = {}

		self.running = True

	def run(self):
		self.config.load()
		self.settings = self.config.settings

		# Pygame
		self.win = pygame.display.set_mode((self.settings["window"]["width"], self.settings["window"]["height"]))
		self.clock = pygame.time.Clock()

		# Main cycle
		while self.running:
			self.clock.tick(self.settings["window"]["fps"])

			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					self.on_close()
					self.running = False
					
			self.win.fill((0, 0, 0))
			self.on_render()
			pygame.display.update()

	def on_render(self):
		pass

	def on_close(self):
		self.config.save()

if __name__ == '__main__':
	main = ScrapSchematic()
	main.run()
