#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame.display
from pygame import Surface

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.entity_list: list[Entity] = []
        self.name = name
        self.mode = menu_option #opção do meu (mode)
        self.Entity_list: list[Entity] = []
        self.entity_list.append(EntityFactory.get_entity('estrelafloresta', (0,0)))

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
            pygame.display.flip()
        pass

