import pygame, sys
import cv2
import os
from Game import *

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

red=get_image('Pionek_czerwony.png')
green=get_image('Pionek_zielony.png')

def draw_pawns():

        for i in range(1,20,1):
            if game.board_state[i]==State.RED:
                screen.blit(red, (game.coordinates[i]))
            elif game.board_state[i]==State.GREEN:
                screen.blit(green, (game.coordinates[i]))

game=Game()
img = cv2.imread('PretwaBoard.png',0)
height, width = img.shape[:2]
resolution = (height,width)
screen = pygame.display.set_mode(resolution)  # Tutaj odpalamy okno
pygame.display.set_caption("Pretwa - The game")  # Ustalamy co wyświetli się na pasku
tps_clock = pygame.time.Clock()
tps_delta = 0.0
tps_max=40.0

#pozycje w których powinny być umieszczone pionki


while True:
    for event in pygame.event.get():  # przechwytuje jakieś zdarzenia, tylko trzeba rozróżnić że
                                         # np. każde kliknięcie to osobny event
                                            # ale kliknięcie i trzymanie to już tylko jeden event
        if event.type == pygame.QUIT:  # sprawdza, czy tym zdarzeniem było kliknięcie X
            sys.exit(0)                 # jeżeli tak, to wyłącza okienko
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
        # elif event.type == pygame.MOUSEBUTTONUP:
        #     pos = pygame.mouse.get_pos()
        elif event.type ==pygame.MOUSEBUTTONDOWN:
            print('Mouse position: {}'.format(event.pos))
            object_index = game.check_if_clickable(event.pos)
            if (object_index != None):
                print('Position on board: {}'.format(object_index))
                screen.blit(red, (game.coordinates[2]))

                game.add_to_interaction(object_index)
                print("Positions: {}".format(game.interaction))
                draw_pawns()

    background_image = pygame.image.load("PretwaBoard.png").convert()
    draw_pawns()

    pygame.display.flip()  # wyświetla to, co narysowaliśmy

    screen.blit(background_image, [0, 0])


