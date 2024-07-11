#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from code.const import WIN_WIDTH


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('../Model/backgroundmenu1.png').convert_alpha()
        self.rect: Rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", (255, 128, 0), (WIN_WIDTH / 2, 70))
            pygame.display.flip()

            for event in pygame.event.get():  # quando receber um evento(quando houver ->get<-)
                if event.type == pygame.QUIT:  # se o tipo do evento for quit (sair) vai acontecer:
                    pygame.quit()  # vai fechar a tela e finalizar o jogo também
                    quit()  # a tela não fecha sozinha e se fechar não finaliza. # Vou criar um evento para quando eu fechar a tela, finalize o game.
                pressed_key = pygame.key.get_pressed()
        pass

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

