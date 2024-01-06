import sys     # imports the modules sys and pygame.
               # sys is for exiting game when done.
import pygame  # pygame is for functionality to build a game. 

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()  # this function initializes background settings for pygame.
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)) # creates display window assigned to self.screen
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        
        # Set the background color.
        self.bg_color = (255,182,193)
        
    def run_game(self):
        """Start the main loop for the game.""" # run_game is a method that controls the game.
        while True:                             # this is an event loop that listens for events to perform tasks.
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():  # returns list of events to cause for loop to run.
                if event.type == pygame.QUIT:  # click window close button game will quit.
                    sys.exit()
            
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
                    
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)
                
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()