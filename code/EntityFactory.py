#!/usr/bin/python
#-*- coding: utf-8 -*-
from code.background import background
from code.const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position: tuple):
        match entity_name:
            case 'florestalevel1part':
                list_bg = []
                for i in range(7):
                    list_bg.append(background(f'florestalevel1part{i}', (0,0)))
                    list_bg.append(background(f'florestalevel1part{i}', (WIN_WIDTH, 0)))
                return list_bg

