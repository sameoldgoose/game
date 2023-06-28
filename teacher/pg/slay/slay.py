import pygame
from sys import exit
'''
    A list of all the constatns that will be used and
    accessed throughout the program
'''

SCREEN_SIZE = (550, 750)
STATUSBAR_SIZE = (SCREEN_SIZE[0], SCREEN_SIZE[1]//15)
FPS = 60
GAME_NAME = 'Boom'
TARGET_SIZE = (100, 130)
SIGN_SIZE = (110, 160)
SELF_DESTRUCTION = 2000
SIGN_SELF_DESTRUCTION = 300
SPAWN_TIME = 1000
SCORE_INCREASE, SCORE_DECREASE = 1, 2

xCo, yCo = SCREEN_SIZE[0]//8, (SCREEN_SIZE[1]-STATUSBAR_SIZE[1])//8

TARGET_SPAWN = (
    (xCo, 87), (3*xCo, 87), (5*xCo, 87), (7*xCo, 87),
    (xCo, 262), (3*xCo, 262), (5*xCo, 262), (7*xCo, 262),
    (xCo, 437), (3*xCo, 437), (5*xCo, 437), (7*xCo, 437),
    (xCo, 612), (3*xCo, 612), (5*xCo, 612), (7*xCo, 612)
)


'''
    controls the program flow
'''
import pygame

class ProgramController():
    def __init__(self, screen, gametimer, sign_group, score=None) -> None:
        self.screen = screen
        self.state = 'menu'
        self.score = score

        # Font
        self.font = pygame.font.Font(None, 40)

        # Surfaces and Rects
        self.message_su = self.font.render(
            "press SPACE to play", False, 'Black')
        self.message_rect = self.message_su.get_rect(
            center=(SCREEN_SIZE[0]//2, 425))

        game_background_pic = pygame.image.load('assets/background.jpeg')
        self.game_background = pygame.transform.scale(
            game_background_pic, (SCREEN_SIZE[0], SCREEN_SIZE[1]-STATUSBAR_SIZE[1]))

        gameover_background_pic = pygame.image.load(
            'assets/gameover_background.jpg')
        self.gameover_background = pygame.transform.scale(
            gameover_background_pic, SCREEN_SIZE)

        status_bar_pic = pygame.image.load('assets/status_bar.jpg')
        # self.status_bar = pygame.transform.scale(status_bar_pic, (500, 50))
        self.status_bar = pygame.transform.scale(status_bar_pic, STATUSBAR_SIZE)

        # Groups
        self.target_group = pygame.sprite.Group()
        self.game_timer = pygame.sprite.GroupSingle()
        self.game_timer.add(gametimer)
        self.sign_group = sign_group

    # Check for current state
    def run(self) -> None:
        if self.state == 'game':
            self.run_game()
        elif self.state == 'menu':
            self.run_menu()
        elif self.state == 'gameover':
            self.run_gameover()

    def set_state(self, state) -> None:
        self.sign_group.empty()
        self.target_group.empty()
        self.state = state

    def get_state(self) -> str:
        return self.state

    # main game meterial in the main loop
    def run_game(self) -> None:
        self.screen.blit(self.game_background, (0, 0))
        self.screen.blit(self.status_bar, (0, SCREEN_SIZE[1] - STATUSBAR_SIZE[1]))
        self.target_group.draw(self.screen)
        self.target_group.update()
        self.game_timer.draw(self.screen)
        self.game_timer.update()
        self.sign_group.draw(self.screen)
        self.sign_group.update()

        if self.score is not None:
            self.score.set_pos((10, SCREEN_SIZE[1] - STATUSBAR_SIZE[1] + 10))
            self.score.show()
            if self.score.get_score() < 0 or self.game_timer.sprite.get_time() <= 0:
                self.set_state('gameover')
                self.game_timer.sprite.set_time(60)

    # menu material in the main loop
    def run_menu(self) -> None:
        keys = pygame.key.get_pressed()
        self.screen.blit(self.gameover_background, (0, 0))
        self.screen.blit(self.message_su, self.message_rect)
        if keys[pygame.K_SPACE]:
            self.set_state("game")
            self.score.set_zero()

    # gameover surface material in the main loop
    def run_gameover(self) -> None:
        keys = pygame.key.get_pressed()
        self.screen.blit(self.gameover_background, (0, 0))
        self.screen.blit(self.message_su, self.message_rect)

        if self.score is not None:
            self.score.set_pos((140, 300))
            self.score.show()

        if keys[pygame.K_SPACE]:
            self.set_state("game")
            self.score.set_zero()

    # Add target to the target Group
    def add_target(self, target) -> None:
        self.target_group.add(target)

    def get_target_group(self) -> None:
        return self.target_group
    
'''
    a class that manages the score system of the game
'''
import pygame


class ScoreManager():
    def __init__(self, x: int = 10, y: int = SCREEN_SIZE[1] - STATUSBAR_SIZE[1] + 10) -> None:
        self.score = 0
        self.screen = pygame.display.get_surface()
        self.x, self.y = x, y
        self.font = pygame.font.Font(None, 60)

    def increase(self) -> None:
        self.score += SCORE_INCREASE

    def decrease(self) -> None:
        self.score -= SCORE_DECREASE

    def set_pos(self, pos) -> None:
        self.x, self.y = pos[0], pos[1]

    def set_zero(self) -> None:
        self.score = 0

    def get_score(self) -> int:
        return self.score

    def show(self) -> None:
        score_su = self.font.render(
            f"SCORE: {str(self.score)}", False, 'Black')
        score_rect = score_su.get_rect(topleft=(self.x, self.y))
        self.screen.blit(score_su, score_rect)

'''
    a sprite for 'signs' with its features which consists of 
    two signs : Green number one, Red number two
'''

import pygame

class Sign(pygame.sprite.Sprite):
    def __init__(self, spawn_time, pos, type):
        super().__init__()

        self.pos = pos
        self.spawn_time = spawn_time
        one_pic = pygame.image.load('assets/one.png')
        one = pygame.transform.scale(one_pic, SIGN_SIZE)
        two_pic = pygame.image.load('assets/two.png')
        two = pygame.transform.scale(two_pic, SIGN_SIZE)
        if type == 'one':
            self.image = one
            self.rect = one.get_rect(center=pos)
        elif type == 'two':
            self.image = two
            self.rect = two.get_rect(center=pos)

    # self destruction after a said time
    def self_destruct(self):
        if (pygame.time.get_ticks() - self.spawn_time) > SIGN_SELF_DESTRUCTION:
            self.kill()

    def update(self):
        self.self_destruct()

from random import choice
# a spawn algorithms which will spawn the targets
# randomally in the 4x4 grid each time.
# no target will be spawned in a currently
# occupied tile
def spawn_target(target_group):
    while len(target_group) < 12:
        switch = True
        pos = choice(TARGET_SPAWN)
        for target in target_group:
            if pos == target.get_pos():
                switch = False
                break
        if switch:
            return pos
    return (0, 0)

'''
    contains the 'target' sprite and its features
'''

import pygame


class Target(pygame.sprite.Sprite):
    def __init__(self, pos, spawn_time, score, sign_group) -> None:
        super().__init__()

        self.sign_event = pygame.event.Event(pygame.USEREVENT + 3)
        target_surface = pygame.image.load(
            'assets/enemy.png').convert_alpha()
        target = pygame.transform.scale(target_surface, TARGET_SIZE)

        self.pos = pos
        self.image = target
        self.rect = target.get_rect(center=self.pos)
        self.spawn_time = spawn_time
        self.score = score
        self.sign_group = sign_group

        self.kill_sound = pygame.mixer.Sound('assets/kill_sound.mp3')

    # target gets destroyed after clicking on it.
    # meaning: detecting collision with the target sprtie
    def destroy(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicks = pygame.mouse.get_pressed()
        if self.rect.collidepoint(mouse_pos) and mouse_clicks[0]:
            self.sign_group.add(
                Sign(pygame.time.get_ticks(), self.get_pos(), 'one'))
            self.score.increase()
            self.kill_sound.play()
            self.kill()

    def get_pos(self):
        return self.pos

    # self destruction after a said time
    def self_destruct(self):
        if (pygame.time.get_ticks() - self.spawn_time) > SELF_DESTRUCTION:
            self.sign_group.add(
                Sign(pygame.time.get_ticks(), self.get_pos(), 'two'))
            self.score.decrease()
            self.kill()

    def update(self):
        self.destroy()
        self.self_destruct()

'''
    contains the 'Timer' sprite and its features
    which will be shown in the game as a 60 secons timer
'''

import pygame
class GameTimer(pygame.sprite.Sprite):
    def __init__(self, time=60) -> None:
        super().__init__()

        x, y = SCREEN_SIZE[0] - 180, SCREEN_SIZE[1] - STATUSBAR_SIZE[1] + 10

        self.time = time
        self.font = pygame.font.Font(None, 60)
        self.image = self.font.render(f"Time: {self.time}", False, 'Black')
        self.rect = self.image.get_rect(topleft=(x, y))

    def tick(self):
        self.time -= 1
        self.image = self.font.render(f"Time: {self.time}", False, 'Black')

    def set_time(self, time):
        self.time = time
        self.image = self.font.render(f"Time: {self.time}", False, 'Black')

    def get_time(self):
        return self.time

def main_loop() -> None:
    target_spawn = SPAWN_TIME
    while True:
        # a list of target sprites
        target_group = controller.get_target_group().sprites()

        # handling events in the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Handling Spawn based on the custom event timer
            if event.type == target_spawn_timer:
                valid_pos = spawn_target(target_group)
                if valid_pos != (0, 0):
                    controller.add_target(
                        Target(valid_pos, pygame.time.get_ticks(), score, sign_group))

            # Event for the 60 second timer
            if event.type == count_down and controller.get_state() == 'game':
                game_timer.tick()

                # increasing the spawn speed each second by reducing the delay
                # for target_spawn_timer
                pygame.time.set_timer(target_spawn_timer, target_spawn)
                if target_spawn > 300:
                    target_spawn -= 50

        # Reset spawn time after gameover
        if controller.get_state() == 'gameover':
            target_spawn = SPAWN_TIME

        controller.run()
        clock.tick(FPS)
        pygame.display.update()


if __name__ == '__main__':
    # Initializing basic stuff for the program
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    score = ScoreManager()
    game_timer = GameTimer()
    sign_group = pygame.sprite.Group()
    controller = ProgramController(screen, game_timer, sign_group, score)
    pygame.display.set_caption('Boom')
    target_spawn_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(target_spawn_timer, SPAWN_TIME)
    count_down = pygame.USEREVENT + 2
    pygame.time.set_timer(count_down, 1000)
    clock = pygame.time.Clock()
    main_loop()