# enemy.py

import pygame
import random
import math
from settings import ENEMY_SIZE, WIDTH, HEIGHT, MIN_ENEMY_SPEED, MAX_ENEMY_SPEED, ATTRACT_RADIUS

# Colors
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
DARK = (50, 50, 50)
STAR_YELLOW = (255, 255, 0)

class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), 0, ENEMY_SIZE, ENEMY_SIZE)
        self.speed = random.randint(MIN_ENEMY_SPEED, MAX_ENEMY_SPEED)
        self.color = self.get_color_by_speed(self.speed)

    def get_color_by_speed(self, speed):
        if speed <= 5:
            return RED
        elif speed <= 10:
            return YELLOW
        else:
            return DARK

    def move(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - ENEMY_SIZE)
            self.rect.y = 0
            self.speed = random.randint(MIN_ENEMY_SPEED, MAX_ENEMY_SPEED)
            self.color = self.get_color_by_speed(self.speed)
            return True
        return False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.speed > 10:
            self.draw_star(screen)

    def draw_star(self, screen):
        center = (self.rect.x + ENEMY_SIZE // 2, self.rect.y + ENEMY_SIZE // 2)
        pygame.draw.polygon(screen, STAR_YELLOW, [
            (center[0], center[1] - 10), 
            (center[0] + 3, center[1] - 3), 
            (center[0] + 10, center[1]), 
            (center[0] + 3, center[1] + 3), 
            (center[0], center[1] + 10),
            (center[0] - 3, center[1] + 3), 
            (center[0] - 10, center[1]), 
            (center[0] - 3, center[1] - 3)
        ])

    def attract_to_player(self, player_rect):
        distance_x = player_rect.centerx - self.rect.centerx
        distance_y = player_rect.centery - self.rect.centery
        distance = math.hypot(distance_x, distance_y)

        if distance < ATTRACT_RADIUS and self.rect.y < player_rect.y:
            attraction_strength = 0.05  # Adjust this value to change the strength of attraction
            self.rect.x += attraction_strength * distance_x
            self.rect.y += attraction_strength * distance_y
