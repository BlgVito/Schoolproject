import pygame
class Level:
    def __init__(self):
        
        #sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()