#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame as pygame
from pygame.ftfont import Font

from code.Menu import Menu
from code.const import WIN_HEIGHT, WIN_WIDHT


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDHT, WIN_HEIGHT))


    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass


