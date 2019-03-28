import pygame, sys
import cv2


pygame.init()

img = cv2.imread('PretwaOpening.jpg',0)
height, width = img.shape[:2]
resolution = (height,width)
screen = pygame.display.set_mode(resolution)  # Tutaj odpalamy okno
pygame.display.set_caption("Pretwa - The game")  # Ustalamy co wyświetli się na pasku
tps_clock = pygame.time.Clock()
tps_delta = 0.0
tps_max=40.0

while True:
    for event in pygame.event.get():  # przechwytuje jakieś zdarzenia, tylko trzeba rozróżnić że
                                         # np. każde kliknięcie to osobny event
                                            # ale kliknięcie i trzymanie to już tylko jeden event
        if event.type == pygame.QUIT:  # sprawdza, czy tym zdarzeniem było kliknięcie X
            sys.exit(0)                 # jeżeli tak, to wyłącza okienko
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)

    background_image = pygame.image.load("PretwaOpening.jpg").convert()
    pygame.display.flip()  # wyświetla to, co narysowaliśmy
    screen.blit(background_image, [0, 0])
