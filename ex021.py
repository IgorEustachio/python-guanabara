import pygame

print('hi hi hi ha')
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.mixer.wait()
