# main.py

import pygame
import sys
import random
from settings import WIDTH, HEIGHT, BLACK, FUNNY_PHRASES
from player import Player
from enemy import Enemy
from powerup import PowerUp
from highscores import load_high_scores, save_high_score

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Minigame")

font = pygame.font.Font(None, 74)
message_font = pygame.font.Font(None, 50)

def main_menu():
    play_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 100)
    scores = load_high_scores()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return  # Start the game

        screen.fill(BLACK)
        pygame.draw.rect(screen, (0, 128, 0), play_button)
        play_text = font.render("Play", True, (255, 255, 255))
        screen.blit(play_text, (play_button.x + 50, play_button.y + 20))

        score_text = message_font.render("Top 5 Scores", True, (255, 255, 255))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + 80))
        for i, score in enumerate(scores):
            score_line = message_font.render(f"{i + 1}. {score}", True, (255, 255, 255))
            screen.blit(score_line, (WIDTH // 2 - score_line.get_width() // 2, HEIGHT // 2 + 120 + i * 40))

        pygame.display.flip()

def main_game():
    player = Player(WIDTH // 2, HEIGHT // 2)
    
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
    message = ""
    message_timer = 0
    message_duration = 1000  # message display duration in milliseconds

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current_time = pygame.time.get_ticks()
        if current_time - last_spawn_time > spawn_delay and current_enemy_count < max_enemies:
            enemies.append(Enemy())
            last_spawn_time = current_time
            current_enemy_count += 1

        if current_time - last_powerup_spawn_time > powerup_spawn_delay and len(powerups) < max_powerups:
            powerups.append(PowerUp())
            last_powerup_spawn_time = current_time

        player.handle_keys()

        for enemy in enemies:
            if enemy.move():
                score += 1
            enemy.attract_to_player(player.rect)

        for enemy in enemies:
            if player.rect.colliderect(enemy.rect):
                running = False

        for powerup in powerups[:]:
            if player.rect.colliderect(powerup.rect):
                powerups.remove(powerup)
                score += 5  # Example: Increase score by 5 for collecting a power-up
                message = random.choice(FUNNY_PHRASES)
                message_timer = pygame.time.get_ticks()

        screen.fill(BLACK)
        player.draw(screen)
        
        for enemy in enemies:
            enemy.draw(screen)

        for powerup in powerups:
            powerup.draw(screen)

        score_text = font.render(str(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        if message and current_time - message_timer < message_duration:
            message_text = message_font.render(message, True, (255, 255, 255))
            screen.blit(message_text, (WIDTH // 2 - message_text.get_width() // 2, HEIGHT // 2 - message_text.get_height() // 2))
        else:
            message = ""

        pygame.display.flip()
        clock.tick(30)

    save_high_score(score)
    main_menu()

if __name__ == "__main__":
    while True:
        main_menu()
        main_game()
