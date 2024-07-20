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
                'player1Shot': 100,
                'player2': 20,
                'player2Shot': 100,
                'Enemy1': 4,
                'Enemy1Shot': 20,
                'Enemy2': 2,
                'Enemy2Shot': 20
                }
#VIDA = HEALTH

ENTITY_HEALTH = {'florestalevel1part0': 999,
                'florestalevel1part1': 999,
                'florestalevel1part2': 999,
                'florestalevel1part3': 999,
                'florestalevel1part4': 999,
                'florestalevel1part5': 999,
                'florestalevel1part6': 999,
                'florestalevel1part7': 999,
                'player1': 100,
                'player1Shot': 1,
                'player2': 100,
                'player2Shot': 3,
                'Enemy1': 50,
                'Enemy1Shot': 1,
                'Enemy2': 50,
                'Enemy2Shot': 1
                }
#intervalo de criação de tiro, PARA PODER ATIRAR (USAR PODER)
ENTITY_SHOT_DELAY = {'player1': 2,
                     'player2': 2
                        }

PLAYER_KEY_JUMP = {'player1': pygame.K_w,
                   'player2': pygame.K_UP}

PLAYER_KEY_RIGHT = {'player1': pygame.K_d,
                   'player2': pygame.K_RIGHT}

PLAYER_KEY_LEFT = {'player1': pygame.K_a,
                    'player2': pygame.K_LEFT}

PLAYER_KEY_SHOOT = {'player1': pygame.K_SPACE,
                    'player2': pygame.K_0}

POSITION_INICIO_PLAYER1 = (5, 700 - 215)
POSITION_INICIO_PLAYER2 = (50, 700 - 215)

#W --> TAMANHOS (WIDTH e HEIGHT)
WIN_WIDTH = 1200
WIN_HEIGHT = 700
