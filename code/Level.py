#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame.display
from pygame import Surface

from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.const import COLOR_WHITE, MENU_OPTIONS, EVENT_ENEMY, WIN_HEIGHT, POSITION_INICIO_PLAYER1, \
    POSITION_INICIO_PLAYER2


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.window = pygame.display.set_mode((1200, 700))
        self.entity_list: list[Entity] = []
        self.name = name
        self.mode = menu_option  # opção do meu (mode)
        self.Entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('florestalevel1part', (0, 0)))
        # Definir novas posições para os players
        player1_position = (5, WIN_HEIGHT - 215)
        player2_position = (50, WIN_HEIGHT - 215)

        self.entity_list.append(EntityFactory.get_entity('player1', (POSITION_INICIO_PLAYER1)))
        if menu_option in [MENU_OPTIONS[1], MENU_OPTIONS[2]]:
            self.entity_list.append(EntityFactory.get_entity('player2', (POSITION_INICIO_PLAYER2)))
        pygame.time.set_timer(EVENT_ENEMY, 15000)#tempo em que vai acontecer o evento de criar o enemy
                                                    #em milisegundos
        # Carregar a música fora do loop principal
        pygame.mixer_music.load(f'asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)

    def run(self):

        clock = pygame.time.Clock()  # vou criar o clock para definir o fps
        while True:
            clock.tick(60)  # defini o tempo de rodagem (FPS) em clock.tick{x}, para não passar disso

            #for para desenhar todas as entidades (cuidado para não colocar o que não deve e ficar lento)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf,
                                 dest=ent.rect)  # aqui eu desenho as entidades ex: background, imagens em geral
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
            #texto para ser printado na tela
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10, 10)) #colocar o cpf na tela do jogo.

            #atualizar na tela
            pygame.display.flip()
            #VERIFICAR RELACIONAMENTOS DE ENTIDADES (CONTATO):
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            #conferir eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice, [0,0]))


        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
