import pygame
from obj import Obj
from menu import Menu


class Main:

    def __init__(self):

        pygame.init()

        self.window = pygame.display.set_mode([360, 640])
        self.title = pygame.display.set_caption("BeeHoney")

        self.loop = True

        self.star_screen = Menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False

            self.star_screen.event(event)

    def draw(self):
        self.window.fill([0, 0, 0])
        if not self.star_screen.change_scene:
            self.star_screen.draw(self.window)

    def updates(self):
        while self.loop:
            self.draw()
            self.events()
            pygame.display.update()


Main().updates()
