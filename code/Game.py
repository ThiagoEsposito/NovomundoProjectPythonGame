#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame as pygame
from pygame.ftfont import Font

from code.Menu import Menu
from code.const import WIN_HEIGHT, WIN_WIDTH


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))


    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()

            for event in pygame.event.get():  # quando receber um evento(quando houver ->get<-)
                if event.type == pygame.QUIT:  # se o tipo do evento for quit (sair) vai acontecer:
                    pygame.quit()  # vai fechar a tela e finalizar o jogo também
                    quit()  # a tela não fecha sozinha e se fechar não finaliza. # Vou criar um evento para quando eu fechar a tela, finalize o game.
                pressed_key = pygame.key.get_pressed()
            pass


