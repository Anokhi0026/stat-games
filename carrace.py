# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 09:52:41 2025

@author: EIC
"""

import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 500
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Turbo Guess Race")

# Load assets
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 48)

# Player positions
car1_x, car1_y = 50, 160
car2_x, car2_y = 50, 260
finish_line = WIDTH - 100

# Generate secret numbers for each player
secret_number_p1 = random.randint(1, 50)
secret_number_p2 = random.randint(1, 50)

input_text = ""
current_player = 1
winner = None
hint_p1 = ""
hint_p2 = ""

def draw_racetrack():
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, (0, 140, WIDTH, 100))  # Track for Player 1
    pygame.draw.rect(screen, GRAY, (0, 240, WIDTH, 100))  # Track for Player 2
    pygame.draw.line(screen, BLACK, (finish_line, 140), (finish_line, 340), 5)  # Finish line

def draw_car(x, y, color):
    pygame.draw.rect(screen, color, (x, y, 70, 40), border_radius=10)
    pygame.draw.circle(screen, BLACK, (x + 15, y + 40), 8)
    pygame.draw.circle(screen, BLACK, (x + 55, y + 40), 8)
    pygame.draw.circle(screen, BLACK, (x + 15, y), 8)
    pygame.draw.circle(screen, BLACK, (x + 55, y), 8)
    pygame.draw.polygon(screen, BLACK, [(x + 20, y), (x + 50, y), (x + 45, y - 10), (x + 25, y - 10)])

def display_hint(guess, secret):
    if guess < secret:
        return "Too Low! 🔽"
    elif guess > secret:
        return "Too High! 🔼"
    return "Correct! 🎉"

# Game loop
running = True
while running:
    draw_racetrack()
    draw_car(car1_x, car1_y, RED)
    draw_car(car2_x, car2_y, BLUE)
    
    # Display instructions
    text = font.render(f"Player {current_player}'s turn - Enter a guess (1-50)", True, BLACK)
    screen.blit(text, (20, 20))
    
    # Input box
    pygame.draw.rect(screen, GREEN, (20, 50, 150, 40))
    input_surface = font.render(input_text, True, BLACK)
    screen.blit(input_surface, (30, 60))
    
    # Display hint for each player
    hint_surface_p1 = large_font.render(f"P1: {hint_p1}", True, YELLOW)
    screen.blit(hint_surface_p1, (200, 60))
    hint_surface_p2 = large_font.render(f"P2: {hint_p2}", True, YELLOW)
    screen.blit(hint_surface_p2, (200, 90))
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if input_text.isdigit():
                    guess = int(input_text)
                    if current_player == 1:
                        hint_p1 = display_hint(guess, secret_number_p1)
                        if guess == secret_number_p1:
                            car1_x = finish_line  # Instantly reach finish line
                            winner = "Player 1 Wins!"
                            running = False
                        else:
                            move = max(10, 50 - abs(secret_number_p1 - guess))
                            car1_x = min(car1_x + move, finish_line)
                    else:
                        hint_p2 = display_hint(guess, secret_number_p2)
                        if guess == secret_number_p2:
                            car2_x = finish_line  # Instantly reach finish line
                            winner = "Player 2 Wins!"
                            running = False
                        else:
                            move = max(10, 50 - abs(secret_number_p2 - guess))
                            car2_x = min(car2_x + move, finish_line)
                    input_text = ""
                    current_player = 2 if current_player == 1 else 1
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.unicode.isdigit():
                input_text += event.unicode
    
    pygame.display.flip()
    
# Show winner and correct numbers
screen.fill(WHITE)
winner_text = font.render(winner, True, RED)
number_text_p1 = font.render(f"Player 1's number: {secret_number_p1}", True, BLACK)
number_text_p2 = font.render(f"Player 2's number: {secret_number_p2}", True, BLACK)
screen.blit(winner_text, (WIDTH // 2 - 100, HEIGHT // 2 - 60))
screen.blit(number_text_p1, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
screen.blit(number_text_p2, (WIDTH // 2 - 100, HEIGHT // 2 + 20))
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()
sys.exit()
