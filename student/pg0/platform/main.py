# Game Description:
# The game is a simple dodge-and-collect game where the player controls a character represented by a white circle. The objective is to collect yellow stars while avoiding red enemies. The stars and enemies fall from the top of the screen, and the player can move left, right, up, and down using the arrow keys. Each time the player collects a star, their score increases. If the player collides with an enemy, the game ends. The player can restart the game by pressing the spacebar.

# Algorithm:

# Set up the screen dimensions and initialize the player, star, and enemy properties.
# Draw the game elements on the screen, including the player, stars, enemies, and the score display.
# Update the game state in the update() function:
# Move the player based on keyboard input.
# Update the positions of stars and enemies, and check for collisions with the player.
# Remove stars and enemies that have fallen off the screen.
# Randomly add new stars and enemies at the top of the screen.
# Define a collision function that checks whether two objects (e.g., player and star) have collided based on their positions and radii.
# Handle the spacebar key press in the on_key_down() function to restart the game if it is over.
# Start the game using the pgzrun.go() function.
# The game loop continuously updates the game state, redraws the screen, and handles player input, creating the interactive gameplay experience.

import random
import pgzrun

# Set up the screen dimensions
WIDTH = 
HEIGHT = 

# Player properties
player_radius = 
player_pos = [WIDTH / 2, HEIGHT / 2]
player_speed = 5

# Star properties
star_radius = 20
stars = []
star_speed = 10

# Enemy properties
enemy_radius = 15
enemies = []
enemy_speed = 10

# Game state
score = 0
game_over = False

def draw():
    # setup a clear screen, set background to background in images
    

    if not game_over:
        

        for star in stars:
            

        for enemy in enemies:
            
    else:
        
def update():
    global score, game_over

    if not game_over:
        # Move the player
        if keyboard.left:
            
        elif keyboard.right:
            
        elif keyboard.up:
            
        elif keyboard.down:
            
        # Update star positions and check for collisions
        for star in stars:
            
            if collision(player_pos, player_radius, star, star_radius):
                

            if star[1] > HEIGHT + star_radius:
                
        # Update enemy positions and check for collisions
        for enemy in enemies:
            enemy[1] += enemy_speed

            if collision(player_pos, player_radius, enemy, enemy_radius):
                # end the game

            if enemy[1] > HEIGHT + enemy_radius:

        # Add new stars and enemies randomly
        if random.randint(1, 75) == 1:
            

        if random.randint(1, 150) == 1:
        

def on_key_down(key):
    global score, game_over

    if game_over and key == keys.SPACE:
        

def collision(pos1, radius1, pos2, radius2):
    
    return distance < radius1 + radius2

pgzrun.go()
