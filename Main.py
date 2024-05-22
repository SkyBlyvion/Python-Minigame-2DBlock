# main.py

import pygame
import sys
from settings import WIDTH, HEIGHT, BLACK
from player import Player
from enemy import Enemy
from powerup import PowerUp

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Minigame")

    player = Player(WIDTH // 2, HEIGHT // 2)
    
    # Initialize variables for enemy spawning and power-ups
    enemies = []
    powerups = []
    spawn_delay = 1000  # delay in milliseconds
    powerup_spawn_delay = 5000  # delay in milliseconds
    last_spawn_time = pygame.time.get_ticks()
    last_powerup_spawn_time = pygame.time.get_ticks()
    max_enemies = 5
    max_powerups = 3
    current_enemy_count = 0

    clock = pygame.time.Clock()
    score = 0
    font = pygame.font.Font(None, 74)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Spawn enemies at intervals
        current_time = pygame.time.get_ticks()
        if current_time - last_spawn_time > spawn_delay and current_enemy_count < max_enemies:
            enemies.append(Enemy())
            last_spawn_time = current_time
            current_enemy_count += 1

        # Spawn power-ups at intervals
        if current_time - last_powerup_spawn_time > powerup_spawn_delay and len(powerups) < max_powerups:
            powerups.append(PowerUp())
            last_powerup_spawn_time = current_time

        player.handle_keys()

        # Move enemies, check for off-screen, and attract them to the player
        for enemy in enemies:
            if enemy.move():
                score += 1
            enemy.attract_to_player(player.rect)

        # Check for collisions
        for enemy in enemies:
            if player.rect.colliderect(enemy.rect):
                running = False

        # Check for power-up collection
        for powerup in powerups[:]:
            if player.rect.colliderect(powerup.rect):
                powerups.remove(powerup)
                score += 50  # Example: Increase score by 5 for collecting a power-up

        screen.fill(BLACK)
        player.draw(screen)
        
        for enemy in enemies:
            enemy.draw(screen)

        for powerup in powerups:
            powerup.draw(screen)

        score_text = font.render(str(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
