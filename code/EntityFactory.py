#!/usr/bin/python
#-*- coding: utf-8 -*-
import random

from code.Enemy import Enemy
from code.Player import Player
from code.background import background
from code.const import WIN_WIDTH, WIN_HEIGHT, POSITION_INICIO_PLAYER2, POSITION_INICIO_PLAYER1


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position: tuple):
        match entity_name:
            case 'florestalevel1part': #esse case é para o background do level 1

                list_bg = []
                for i in range(8):
                    list_bg.append(background(f'florestalevel1part{i}', (0,0)))
                    list_bg.append(background(f'florestalevel1part{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'player1': #esse case é do personagem
               return Player('player1', (5, 550 - 100))
            case 'player2':  # esse case é do personagem
                return Player('player2', (55, 550 - 100))
            #case 'player1':  # Esse case é do personagem
                #return Player('player1', position)  # Usar a posição passada como argumento
            case 'Enemy1':#criando o inimigo 1 e sua posição
                return Enemy('Enemy1', (WIN_WIDTH + 5, WIN_HEIGHT - 230))

            case 'Enemy2':# criando o inimigo 2 e sua posição
                return Enemy('Enemy2', (WIN_WIDTH + 5, WIN_HEIGHT - 230))
