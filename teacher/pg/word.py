import pygame
import random

# Initialize Pygame
pygame.init()

# Game window dimensions
WIDTH = 800
HEIGHT = 600

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (176, 224, 230)  # Light Blue

# Set up the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Word Scramble")

# Font for displaying text
font = pygame.font.Font("freesansbold.ttf", 48)

# List of words to scramble
words = ["python", "game", "scramble", "word", "pygame"]

# Select a random word from the list
word = random.choice(words)
scrambled_word = ''.join(random.sample(word, len(word)))

# Game variables
score = 0
guess = ""

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                guess = guess[:-1]
            elif event.key == pygame.K_RETURN:
                if guess.lower() == word:
                    score += 1
                word = random.choice(words)
                scrambled_word = ''.join(random.sample(word, len(word)))
                guess = ""
            else:
                guess += event.unicode

    # Clear the screen
    window.fill(BACKGROUND_COLOR)

    # Display the scrambled word
    text = font.render(scrambled_word, True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    window.blit(text, text_rect)

    # Display the player's guess
    guess_text = font.render(guess, True, BLACK)
    guess_rect = guess_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    window.blit(guess_text, guess_rect)

    # Display the score
    score_text = font.render("Score: " + str(score), True, BLACK)
    score_rect = score_text.get_rect(topright=(WIDTH - 20, 20))
    window.blit(score_text, score_rect)

    pygame.display.flip()

# Quit the game
pygame.quit()
