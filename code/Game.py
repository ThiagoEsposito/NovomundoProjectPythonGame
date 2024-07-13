#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys

import pygame as pygame
from pygame.ftfont import Font

from code.Level import Level
from code.Menu import Menu
from code.const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTIONS


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))


    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            if menu_return in [MENU_OPTIONS[0], MENU_OPTIONS[1],MENU_OPTIONS[2], MENU_OPTIONS[3]]:
                level = Level(self.window, "florestalevel1part", menu_return)
                level_return = level.run()
                pass
            else:
                pygame.quit()
                sys.exit()


