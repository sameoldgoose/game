import os
# Position the game window top left
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{0},{0}'

import pgzrun
from random import randint, choice

WIDTH = 800
HEIGHT = 480
TITLE = "Fruit Monkey!"
MONKEY_SPEED = 7
NUMBER_OF_FRUIT = 10
BORDER_OFFSET = 10

monkey = Actor("still")
fruit_images = ["fruit00", "fruit10", "fruit20"]
fruit_list = []
baddie = Actor("flame")    
game_ticks = 1

# PGZero engine calls this 60 times per second. Draw sprites and backgrounds here
def draw():
    
    


def display_text(text):
    

# PGZero engine calls this 60 times per second. Update game state here
def update():
    

def move_baddie():
    if baddie.dead:
        return

    # Baddie gets faster and jittery once he's near the monkey
    if baddie.distance_to(monkey) < 150:
    
    else:
    
    # Home in on the monkey's position
    dx = 0
    dy = 0
    if (baddie.x > monkey.x):
    
    elif (baddie.x < monkey.x):


    if (baddie.y > monkey.y):

    elif (baddie.y < monkey.y):


    if dx != 0 and dy != 0:
        

    baddie.x = baddie.x + (dx * baddie_speed)
    baddie.y = baddie.y + (dy * baddie_speed)


# colliderect gives monkey a generous chance to grab the fruit when he's near it
def check_monkey_fruit_collision():
    global fruit_list 
    for i in range(len(fruit_list)):
        

    # Use list comprehension to filter out the eaten fruit from the list
    fruit_list = ___

    if len(fruit_list) == 0:
        
        

# collidepoint gives monkey an easier time than if we use colliderect
def check_monkey_baddie_collision():
    if baddie.dead:
        return

    if monkey.collidepoint(baddie.pos):
        monkey.dead = True
        baddie.dead = True


def remove_fruit(fruit):
    fruit.state = "gone"


def move_monkey():
    global game_ticks

    if monkey.dead or monkey.won:
        if keyboard.RETURN:
            #reset the game

        return 

    dx = -1
    if keyboard.left:
        monkey.x -= MONKEY_SPEED
        dx = 0

    if keyboard.right:
        
    if keyboard.up:
        
    if keyboard.down:
        
    monkey.y = min(407, max(15, monkey.y))     
    monkey.x = min(755, max(40, monkey.x))  

    if (dx == -1):
        monkey.image = "still"
    else:
        monkey.image = "run" + str(dx) + str((game_ticks // 4) % 4)

def reset_game():
    global fruit_list 
    monkey.pos = WIDTH // 2, HEIGHT // 2
    monkey.dead = False
    monkey.won = False
    
    fruit_list = []
    for i in range(NUMBER_OF_FRUIT):
    

    baddie.topleft = BORDER_OFFSET, BORDER_OFFSET
    baddie.dead = False

reset_game()
pgzrun.go()