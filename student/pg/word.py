# This is a simple word scramble game implemented using Pygame. The game displays a scrambled word, and the player needs to guess the original word by entering their guess using the keyboard. If the guess is correct, the player earns a point, and a new word is presented. The game continues until the player decides to quit.

# Algorithm:
# Initialize the Pygame library and set up the game window.
# Define the game window dimensions and color constants.
# Load the font for displaying text.
# Create a list of words to be scrambled.
# Select a random word from the list and scramble its letters to create a new word.
# Set up game variables, including the score and the player's guess.
# Start the game loop, which continues until the player decides to quit.
# Handle events, such as quitting the game or processing keyboard input.
# If the player presses the Enter key, check if the guess matches the original word.
# If the guess is correct, increment the score, select a new word, and scramble it.
# Reset the player's guess.
# If the player presses the Backspace key, remove the last character from the guess.
# For any other key pressed, add the corresponding character to the guess.
# Clear the screen and update the display.
# Render and display the scrambled word, the player's guess, and the score.
# Update the game display.
# Once the game loop ends, quit the game.

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


# Font for displaying text
font = pygame.font.Font("freesansbold.ttf", 48)

# List of words to scramble

# Select a random word from the list and scramble the word

# Game variables
score = 0
guess = ""

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              # Quit the game if the window is closed

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Check if the player's guess is correct
                if guess == word:
                    #increment score
                    # Select a new word and scramble it
                    
            elif event.key == pygame.K_BACKSPACE:
                # Remove the last character from the player's guess
                
            else:
                guess += event.unicode

    # Clear the screen
    window.fill(BACKGROUND_COLOR)

    # Display the scrambled word
    
    # Display the player's guess
    

    # Display the score
    

    pygame.display.flip()

# Quit the game
pygame.quit()
