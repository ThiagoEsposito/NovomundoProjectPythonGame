#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import os
print(os.getcwd())

import pygame

from code.const import ENTITY_HEALTH


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png')

        #  self.surf = pygame.image.load('asset/' + name + '.png')
        #self.rect = self.surf.get_rect(topleft=position)  # Usar 'topleft' para definir a posição inicial
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]

    @abstractmethod
    def move (self):
        pass

    def name(self, ):
        pass

    def surf(self, ):
        pass

    def rect(self, ):
        pass

