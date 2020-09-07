import pygame
import self as self


class Obj:

    def __init__(self, image, x, y):
        self.group = pygame.sprite.Group()
        self.spite = pygame.sprite.Sprite(self.group)

        self.sprite.image = pygame.image.load(image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y

    def draw(self, window):
        self.group.draw(window)
