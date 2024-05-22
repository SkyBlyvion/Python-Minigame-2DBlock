# player.py

import pygame
from settings import PLAYER_COLOR, PLAYER_SIZE, PLAYER_SPEED

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.color = PLAYER_COLOR

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_d]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_z]:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_s]:
            self.rect.y += PLAYER_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
