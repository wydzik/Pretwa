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

def draw_pawns():
        red=get_image('Pionek_czerwony.png')
        green=get_image('Pionek_zielony.png')
        screen.blit(red, (game.coordinates[1]))
        screen.blit(red, (game.coordinates[2]))
        screen.blit(red, (game.coordinates[3]))
        screen.blit(red, (game.coordinates[7]))
        screen.blit(red, (game.coordinates[8]))
        screen.blit(red, (game.coordinates[9]))
        screen.blit(red, (game.coordinates[13]))
        screen.blit(red, (game.coordinates[14]))
        screen.blit(red, (game.coordinates[15]))
        screen.blit(green, (game.coordinates[4]))
        screen.blit(green, (game.coordinates[5]))
        screen.blit(green, (game.coordinates[6]))
        screen.blit(green, (game.coordinates[10]))
        screen.blit(green, (game.coordinates[11]))
        screen.blit(green, (game.coordinates[12]))
        screen.blit(green, (game.coordinates[16]))
        screen.blit(green, (game.coordinates[17]))
        screen.blit(green, (game.coordinates[18]))

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
            print('Position on board: {}'.format(game.check_if_clickable(event.pos)))
    background_image = pygame.image.load("PretwaBoard.png").convert()
    draw_pawns()

    pygame.display.flip()  # wyświetla to, co narysowaliśmy

    screen.blit(background_image, [0, 0])


