#!/usr/bin/python
#-*- coding: utf-8 -*-
from code.background import background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position: tuple):
        match entity_name:
            case 'estrelafloresta':
                return background(f'estrelafloresta', position)

