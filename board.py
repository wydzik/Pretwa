import pygame, sys
import cv2
import os

pygame.init()
_image_library = {}

pos_1 = (275,-25)
pos_2 = (20,125)
pos_3 = (530,125)
pos_4 = (275,575)
pos_5 = (20,425)
pos_6 = (530,425)
pos_11 = (275,75)
pos_12 = (105,175)
pos_13 = (445,175)
pos_14 = (275,475)
pos_15 = (105,375)
pos_16 = (445,375)
pos_21 = (275,175)
pos_22 = (190,225)
pos_23 = (355,225)
pos_24 = (275,375)
pos_25 = (190,325)
pos_26 = (355,325)
pos_31 = (275,275)

def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

def draw_pawns():
    pionek_1 = screen.blit(get_image('Pionek_czerwony.png'),(pos_1))
    pionek_2 = screen.blit(get_image('Pionek_czerwony.png'), (pos_2))
    pionek_3 = screen.blit(get_image('Pionek_czerwony.png'),(pos_3))
    pionek_11 = screen.blit(get_image('Pionek_czerwony.png'), (pos_11))
    pionek_12 = screen.blit(get_image('Pionek_czerwony.png'),(pos_12))
    pionek_13 = screen.blit(get_image('Pionek_czerwony.png'), (pos_13))
    pionek_21 = screen.blit(get_image('Pionek_czerwony.png'),(pos_21))
    pionek_22 = screen.blit(get_image('Pionek_czerwony.png'),(pos_22))
    pionek_23 = screen.blit(get_image('Pionek_czerwony.png'),(pos_23))
    pionek_4 = screen.blit(get_image('Pionek_zielony.png'),(pos_4))
    pionek_5 = screen.blit(get_image('Pionek_zielony.png'),(pos_5))
    pionek_6 = screen.blit(get_image('Pionek_zielony.png'),(pos_6))
    pionek_14 = screen.blit(get_image('Pionek_zielony.png'),(pos_14))
    pionek_15 = screen.blit(get_image('Pionek_zielony.png'),(pos_15))
    pionek_16 = screen.blit(get_image('Pionek_zielony.png'),(pos_16))
    pionek_24 = screen.blit(get_image('Pionek_zielony.png'),(pos_24))
    pionek_25 = screen.blit(get_image('Pionek_zielony.png'),(pos_25))
    pionek_26 = screen.blit(get_image('Pionek_zielony.png'),(pos_26))
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
        elif event.type ==pygame.MOUSEBUTTONDOWN:
            print(event.pos)
    background_image = pygame.image.load("PretwaBoard.png").convert()

    draw_pawns()
    pygame.display.flip()  # wyświetla to, co narysowaliśmy
    screen.blit(background_image, [0, 0])
