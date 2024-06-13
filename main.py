import pygame
from screenManager import ScreenManager

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Galaga Refactorized - Revenge of Bombs")

screenManager = ScreenManager(screen)
screenManager.playGame()
