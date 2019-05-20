import pygame, sys
import cv2
import os
from Game import *
from Game_with_computer import *

pygame.init()
_image_library = {}


def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image

    return image


red = get_image('Pionek_czerwony.png')
green = get_image('Pionek_zielony.png')

def draw_pawns():

        for i in range(1, 20, 1):
            if game.board_state[i] == State.RED:
                screen.blit(red, (game.coordinates[i]))
            elif game.board_state[i] == State.GREEN:
                screen.blit(green, (game.coordinates[i]))


def draw_pawns_pvc():
    for i in range(1, 20, 1):
        if game_with_computer.board_state[i] == State.RED:
            screen.blit(red, (game_with_computer.coordinates[i]))
        elif game_with_computer.board_state[i] == State.GREEN:
            screen.blit(green, (game_with_computer.coordinates[i]))

game_with_computer = Game_with_computer()
game = Game()

img = cv2.imread('Pretwa_menu.png', 0)
in_menu = True
with_player=True
height, width = img.shape[:2]
resolution = (width, height)
screen = pygame.display.set_mode(resolution)  # Tutaj odpalamy okno
pygame.display.set_caption("Pretwa - The game")  # Ustalamy co wyświetli się na pasku
tps_clock = pygame.time.Clock()
tps_delta = 0.0
tps_max = 40.0

while True:
    if in_menu:
        background_image = pygame.image.load("Pretwa_menu.png").convert()
        for event in pygame.event.get():  # przechwytuje jakieś zdarzenia, tylko trzeba rozróżnić że
                                            # np. każde kliknięcie to osobny event
                                            # ale kliknięcie i trzymanie to już tylko jeden event

            if event.type == pygame.QUIT:  # sprawdza, czy tym zdarzeniem było kliknięcie X
                sys.exit(0)  # jeżeli tak, to wyłącza okienko
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('Mouse position: {}'.format(event.pos))
                if (event.pos[0] >= 100)\
                        and (event.pos[0] <= 500)\
                        and (event.pos[1] >= 250)\
                        and (event.pos[1] <= 350):
                   in_menu = False
                   background_image = pygame.image.load("PretwaBoard.png").convert()

                elif (event.pos[0] >= 100)\
                        and (event.pos[0] <= 500)\
                        and (event.pos[1] >= 400)\
                        and (event.pos[1] <= 500):
                    in_menu = False
                    background_image = pygame.image.load("PretwaBoard.png").convert()
                    with_player=False

    elif (in_menu == False) and (game.red_wins == False and game.green_wins ==False) and (with_player == True) :
        for event in pygame.event.get():  # przechwytuje jakieś zdarzenia, tylko trzeba rozróżnić że
                                             # np. każde kliknięcie to osobny event
                                                # ale kliknięcie i trzymanie to już tylko jeden event
            if event.type == pygame.QUIT:  # sprawdza, czy tym zdarzeniem było kliknięcie X
                sys.exit(0)                 # jeżeli tak, to wyłącza okienko

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

            elif event.type ==pygame.MOUSEBUTTONDOWN:
                print('Mouse position: {}'.format(event.pos))
                object_index = game.check_if_clickable(event.pos)

                if object_index != None:
                    print('Position on board: {}'.format(object_index))
                    screen.blit(red, (game.coordinates[2]))

                    game.add_to_interaction(object_index)
                    print("Positions: {}".format(game.interaction))
                    draw_pawns()

        if game.red_turn:
            background_image = pygame.image.load("Pretwa_red_turn.png").convert()
            draw_pawns()

        elif not game.red_turn:
            background_image = pygame.image.load("Pretwa_green_turn.png").convert()
            draw_pawns()
    elif (in_menu == False)\
            and (game_with_computer.red_wins == False)\
            and (game_with_computer.green_wins == False)\
            and (with_player == False):
        for event in pygame.event.get():  # przechwytuje jakieś zdarzenia, tylko trzeba rozróżnić że
            # np. każde kliknięcie to osobny event
            # ale kliknięcie i trzymanie to już tylko jeden event
            if event.type == pygame.QUIT:  # sprawdza, czy tym zdarzeniem było kliknięcie X
                sys.exit(0)  # jeżeli tak, to wyłącza okienko

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('Mouse position: {}'.format(event.pos))
                object_index = game_with_computer.check_if_clickable(event.pos)

                if object_index != None:
                    print('Position on board: {}'.format(object_index))
                    screen.blit(red, (game_with_computer.coordinates[2]))

                    game_with_computer.add_to_interaction(object_index)
                    print("Positions: {}".format(game_with_computer.interaction))
                    draw_pawns_pvc()

        if game_with_computer.red_turn:
            background_image = pygame.image.load("Pretwa_red_turn.png").convert()
            draw_pawns_pvc()

        elif not game_with_computer.red_turn:
            background_image = pygame.image.load("Pretwa_green_turn.png").convert()
            draw_pawns_pvc()
    else:

        if game.green_wins or game_with_computer.green_wins:
            background_image = pygame.image.load("Pretwa_green_wins.png").convert()
            for event in pygame.event.get():  # przechwytuje jakieś zdarzenia, tylko trzeba rozróżnić że
                # np. każde kliknięcie to osobny event
                # ale kliknięcie i trzymanie to już tylko jeden event

                if event.type == pygame.QUIT:  # sprawdza, czy tym zdarzeniem było kliknięcie X
                    sys.exit(0)  # jeżeli tak, to wyłącza okienko
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

        if game.red_wins or game_with_computer.red_wins:
            background_image = pygame.image.load("Pretwa_red_wins.png").convert()
            for event in pygame.event.get():  # przechwytuje jakieś zdarzenia, tylko trzeba rozróżnić że
                # np. każde kliknięcie to osobny event
                # ale kliknięcie i trzymanie to już tylko jeden event

                if event.type == pygame.QUIT:  # sprawdza, czy tym zdarzeniem było kliknięcie X
                    sys.exit(0)  # jeżeli tak, to wyłącza okienko
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)


    pygame.display.flip()  # wyświetla to, co narysowaliśmy

    screen.blit(background_image, [0, 0])


