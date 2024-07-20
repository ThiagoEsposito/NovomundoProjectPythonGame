#!/usr/bin/python
#-*- coding: utf-8 -*-
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.const import WIN_WIDTH, ENTITY_SPEED


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        pass

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        return EnemyShot(f'{self.name}Shot', position=(self.rect.centerx - 30, self.rect.centery - 50))

