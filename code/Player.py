#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame.key

from code.Entity import Entity
from code.const import ENTITY_SPEED


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pressed_key = pygame.key.get_pressed() #vou fazer o personagem se mover
        if pressed_key[pygame.K_d] and self.rect.centerx >= 0: #se clicar "d" vai acontecer:
            self.rect.centerx += ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_a] and self.rect.centerx >= 0: #se clicar "a" vai acontecer:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        pass

