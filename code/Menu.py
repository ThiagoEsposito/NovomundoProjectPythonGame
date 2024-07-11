#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from code.const import WIN_WIDTH, COLOR_ORANGE, COLOR_PINK, MENU_OPTIONS, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('../Model/backgroundmenu1.png').convert_alpha()
        self.rect: Rect = self.surf.get_rect(left=0, top=0)
        self.menu_option=0
    def run(self):
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(75, "NOVO", (COLOR_ORANGE), (WIN_WIDTH / 2, 190))
            self.menu_text(75, "MUNDO", (COLOR_ORANGE), (WIN_WIDTH / 2, 250))


            for i in range(len(MENU_OPTIONS)):
                if i == self.menu_option:
                    self.menu_text(40, MENU_OPTIONS[i], COLOR_YELLOW, (WIN_WIDTH / 2, 350 + 60 * i))
                else:
                    self.menu_text(40, MENU_OPTIONS[i], COLOR_PINK, (WIN_WIDTH / 2, 350 + 60 * i))

            pygame.display.flip()
            #Abaixo serve para conseguir fechar o jogo...
            for event in pygame.event.get():  # quando receber um evento(quando houver ->get<-)
                if event.type == pygame.QUIT:  # se o tipo do evento for quit (sair) vai acontecer:
                    pygame.quit()  # vai fechar a tela e finalizar o jogo também
                    sys.exit()
                    #quit()  # a tela não fecha sozinha e se fechar não finaliza. # Vou criar um evento para quando eu fechar a tela, finalize o game.
                #pressed_key = pygame.key.get_pressed()

                #para rolar no menu
                if event.type == pygame.KEYDOWN: #Testar se alguma tecla foi pressionada
                    if event.key == pygame.K_DOWN: #Se a tecla que for pressionada for set para baixo
                        if self.menu_option < len(MENU_OPTIONS) - 1:
                            self.menu_option += 1
                        else:
                            self.menu_option = 0
                    if event.key == pygame.K_UP: #Se a tecla que for pressionada for a seta para cima
                        if self.menu_option > 0:
                            self.menu_option -= 1
                        else:
                            self.menu_option = len(MENU_OPTIONS) - 1


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

