#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame.key

from code.Entity import Entity
from code.PlayerShot import PlayerShot
from code.const import ENTITY_SPEED, WIN_WIDTH, PLAYER_KEY_JUMP, PLAYER_KEY_RIGHT, PLAYER_KEY_LEFT, PLAYER_KEY_SHOOT


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # Adicionando atributos para o pulo
        self.jump_speed = 42  # altura pulo
        self.gravity = 10  # velocidade da descida (gravidade)
        self.vel_y = 0  # Velocidade vertical
        self.on_ground = True  # Verificação se o player está no chão

    def move(self):
        pressed_key = pygame.key.get_pressed() #vou fazer o personagem se mover
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.centerx >= 0: #se clicar "d" vai acontecer:
            self.rect.centerx += ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.centerx >= 0: #se clicar "a" vai acontecer:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_JUMP[self.name]] and self.on_ground: #vou fazer o personagem pular
            self.vel_y = -self.jump_speed               #quando eu apertar "w"
            self.on_ground = False

            # Aplicar a gravidade
        self.vel_y += self.gravity
        self.rect.top += self.vel_y

        # Verificar se o player está no chão
        if self.rect.bottom >= 630:  # Assumindo que o chão está na parte inferior da tela (y = 700)
            self.rect.bottom = 630
            self.vel_y = 0
            self.on_ground = True

    def shoot(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
            return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
        else:
            return None


        pass

