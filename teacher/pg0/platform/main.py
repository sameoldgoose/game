import random
import pgzrun

# Set up the screen dimensions
WIDTH = 800
HEIGHT = 600

# Player properties
player_radius = 20
player_pos = [WIDTH / 2, HEIGHT / 2]
player_speed = 5

# Star properties
star_radius = 10
stars = []
star_speed = 4

# Enemy properties
enemy_radius = 15
enemies = []
enemy_speed = 10

# Game state
score = 0
game_over = False

def draw():
    screen.clear()
    screen.blit("background", (0, 0))
    screen.draw.text("Score: " + str(score), topleft=(10, 10), fontsize=30, color="white")

    if not game_over:
        screen.draw.filled_circle(player_pos, player_radius, "white")

        for star in stars:
            screen.draw.filled_circle(star, star_radius, "yellow")

        for enemy in enemies:
            screen.draw.filled_circle(enemy, enemy_radius, "red")
    else:
        screen.draw.text("Game Over", center=(WIDTH/2, HEIGHT/2), fontsize=60, color="red")
        screen.draw.text("Press SPACE to play again", center=(WIDTH/2, HEIGHT/2 + 50), fontsize=30, color="red")

def update():
    global score, game_over

    if not game_over:
        # Move the player
        if keyboard.left:
            player_pos[0] -= player_speed
        elif keyboard.right:
            player_pos[0] += player_speed
        elif keyboard.up:
            player_pos[1] -= player_speed
        elif keyboard.down:
            player_pos[1] += player_speed

        # Update star positions and check for collisions
        for star in stars:
            star[1] += star_speed

            if collision(player_pos, player_radius, star, star_radius):
                score += 1
                stars.remove(star)

            if star[1] > HEIGHT + star_radius:
                stars.remove(star)

        # Update enemy positions and check for collisions
        for enemy in enemies:
            enemy[1] += enemy_speed

            if collision(player_pos, player_radius, enemy, enemy_radius):
                game_over = True

            if enemy[1] > HEIGHT + enemy_radius:
                enemies.remove(enemy)

        # Add new stars and enemies randomly
        if random.randint(1, 75) == 1:
            star_x = random.randint(star_radius, WIDTH - star_radius)
            star_y = -star_radius
            stars.append([star_x, star_y])

        if random.randint(1, 150) == 1:
            enemy_x = random.randint(enemy_radius, WIDTH - enemy_radius)
            enemy_y = -enemy_radius
            enemies.append([enemy_x, enemy_y])

def on_key_down(key):
    global score, game_over

    if game_over and key == keys.SPACE:
        score = 0
        game_over = False
        player_pos[0] = WIDTH / 2
        player_pos[1] = HEIGHT / 2
        stars.clear()
        enemies.clear()

def collision(pos1, radius1, pos2, radius2):
    distance = ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5
    return distance < radius1 + radius2

pgzrun.go()
