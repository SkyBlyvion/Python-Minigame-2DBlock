# enemy.py

import pygame
import random
from Settings import ENEMY_COLOR, ENEMY_SIZE, MIN_ENEMY_SPEED, MAX_ENEMY_SPEED, WIDTH, HEIGHT

class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), 0, ENEMY_SIZE, ENEMY_SIZE)
        self.color = ENEMY_COLOR
        self.speed = random.randint(MIN_ENEMY_SPEED, MAX_ENEMY_SPEED)

    def move(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - ENEMY_SIZE)
            self.rect.y = 0
            self.speed = random.randint(MIN_ENEMY_SPEED, MAX_ENEMY_SPEED)
            return True
        return False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
