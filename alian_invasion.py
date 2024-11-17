import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
	"""Manage all game assests and resources"""

	def __init__(self):
		"""Initialize game"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption('Alien Invasion')

		self.ship = Ship(self)

	def run_game(self):
		"""Run game"""
		while True:
			self._check_events()
			self._update_screen()
			
	def _check_events(self):
		"""Watch for keyboard and mouse events"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		pygame.display.flip()
		

if __name__ == '__main__':
	# Create instance and run game
	ai = AlienInvasion()
	ai.run_game()