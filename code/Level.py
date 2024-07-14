#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

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
        self.mode = menu_option  # opção do meu (mode)
        self.Entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('florestalevel1part', (0, 0)))
        self.entity_list.append(EntityFactory.get_entity('player1', (0,0)))

    def run(self):
        pygame.mixer_music.load(f'asset/{self.name}.mp3')  # musica da fase1
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()  # vou criar o clock para definir o fps
        while True:
            clock.tick(60)  # defini o tempo de rodagem (FPS) em clock.tick{x}, para não passar disso
            for ent in self.entity_list:
                self.window.blit(source=ent.surf,
                                 dest=ent.rect)  # aqui eu desenho as entidades ex: background, imagens em geral
                # self.level_text(14, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10, 10)) #colocar o cpf na tela do jogo.
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
