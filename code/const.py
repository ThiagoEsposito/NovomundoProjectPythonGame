#C --> CORES
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_BLACK = (0, 0, 0)
COLOR_PINK = (200, 10, 100)
COLOR_WHITE = (255,255,255)
COLOR_YELLOW = (255,255,128)

#M -> MENU
MENU_OPTIONS = ("INICIO",
                "INICIO MULTIPLAYER",
                "ESCOLHER PERSONAGEM",
                "OPTIONS",
                "EXIT")

#E  -> ENTITY, EVENT_ENEMY
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {'florestalevel1part0': 0,
                'florestalevel1part1': 0,
                'florestalevel1part2': 10,
                'florestalevel1part3': 0,
                'florestalevel1part4': 0,
                'florestalevel1part5': 0,
                'florestalevel1part6': 0,
                'florestalevel1part7': 0,
                'player1': 20,
                'player2': 20,
                'Enemy1': 4,
                'Enemy2': 2
                }
PLAYER_KEY_JUMP = {'player1': pygame.K_w,
                   'player2': pygame.K_UP}

PLAYER_KEY_RIGHT = {'player1': pygame.K_d,
                   'player2': pygame.K_RIGHT}

PLAYER_KEY_LEFT = {'player1': pygame.K_a,
                    'player2': pygame.K_LEFT}


#W --> TAMANHOS (WIDTH e HEIGHT)
WIN_WIDTH = 1200
WIN_HEIGHT = 700
