# powerup.py

import pygame
import random
from settings import POWERUP_SIZE, WIDTH, HEIGHT, POWERUP_COLOR

class PowerUp:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH - POWERUP_SIZE), random.randint(0, HEIGHT - POWERUP_SIZE), POWERUP_SIZE, POWERUP_SIZE)
        self.color = POWERUP_COLOR

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
