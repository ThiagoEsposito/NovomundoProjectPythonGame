#!/usr/bin/python
#-*- coding: utf-8 -*-
from code.Player import Player
from code.background import background
from code.const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position: tuple):
        match entity_name:
            case 'florestalevel1part': #esse case é para o background do level 1
                list_bg = []
                for i in range(7):
                    list_bg.append(background(f'florestalevel1part{i}', (0,0)))
                    list_bg.append(background(f'florestalevel1part{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'player1': #esse case é do personagem
                return Player('player1', (5, 550))

