import pygame


class Main:

    def __init__(self):

        pygame.init()

        self.window = pygame.display.set_mode([360, 640])
        self.title = pygame.display.set_caption("BeeHoney")

        self.loop = True

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False

    def draw(self):
        pass

    def updates(self):
        while self.loop:
            self.draw()
            self.events()
            pygame.display.update()


Main().updates()
