import pygame

class Ship:
    # A class o manage the ship.

    def __init__(self, ai_game):
        #initialize the ship and set its starting position.
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image an get its rect.
        self.image = pygame.image.load('/home/sara-rzen/Projects/CrashCoursePython/alien_invasion/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # Draw the ship at its current location.
        self.screen.blit(self.image, self.rect)
