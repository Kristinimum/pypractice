import pygame  # pygame is for functionality to build a game. 
from pygame.sprite import Group 

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Intitialize pygame, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Kristin's Alien Invasion")

    # Set background color.
    bg_color = (255, 182, 193)

    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()