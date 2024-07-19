#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Entity import Entity
from code.const import WIN_WIDTH, ENTITY_SPEED, WIN_HEIGHT


class background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # Ajustar o tamanho da imagem de background para caber na tela
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH

