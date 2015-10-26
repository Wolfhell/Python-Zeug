import os, sys

import pygame

from pygame.base import *

if not pygame.font: print ("Warning, fonts disabled")
if not pygame.mixer: print ("Warning, sound disabled")

class PyManMain:
    """The Main PyMan Class - This class handles the main  initialization and creating of the Game."""
    def __init__(self, width=640, height=480):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width, self.height))


    def MainLoop(self):
        """This is the Main Loop of the Game"""
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    if __name__ == "__main__":
        MainWindow = PyManMain()
        MainWindow.MainLoop()

class Snake(pygame.sprite.Sprite):
    """This is our snake that will move around the screen"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("snake.png",-1)
        self.pellets = 0
