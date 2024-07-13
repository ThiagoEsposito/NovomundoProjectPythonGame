#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame.display
from pygame import Surface

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.window = pygame.display.set_mode((1200, 700))
        self.entity_list: list[Entity] = []
        self.name = name
        self.mode = menu_option #opção do meu (mode)
        self.Entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('florestalevel1part', (0, 0)))
    def run(self):
        pygame.mixer_music.load(f'asset/{self.name}.mp3') #musica da fase1
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock() #vou criar o clock para definir o fps
        while True:
            clock.tick(60) #defini o tempo de rodagem (FPS) em clock.tick{x}, para não passar disso
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass

