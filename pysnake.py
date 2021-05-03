# classic snake game made with pygame module //haiq70
# pygame documentation: https://www.pygame.org/docs/
# references:
# https://www.youtube.com/watch?v=PHdZdrMCKuY

import pygame
import pygame_menu
import random
import tkinter as tk
from tkinter import messagebox

pygame.init()
pygame.display.init()
pygame.font.init()

# dimensions of the window
scr_width = 400
scr_height = 400

# size of the player
player_size = 10

# grid system for the checkerboard
tile_size = 40
grid_width = scr_width / tile_size  # place that many squares as the screen is wide
grid_height = scr_height / tile_size # /tall

# colors for the checkerboard background
color1 = (179, 179, 179)
color2 = (236, 255, 230)

# other colours
player_colour = (30, 128, 0)
fruit_colour = (255, 71, 26)
BLACK = (0, 0, 0)

# initialize font for the scoring system
score_font = pygame.font.SysFont('bahnschrift', 20)
score_font.set_bold(True)

# function to draw background checkerboard pattern
def draw_background(surface):
    for x in range(0, int(grid_height)):
        for y in range(0, int(grid_width)):
            # every second tile
            if (x + y) % 2 == 0:
                # Rect(left, top, width, height)
                tile = pygame.Rect(x*tile_size, y*tile_size, tile_size, tile_size)
                pygame.draw.rect(surface, color1, tile)
            else:
                tile1 = pygame.Rect(x*tile_size, y*tile_size, tile_size, tile_size)
                pygame.draw.rect(surface, color2, tile1)

# position of the player (initialized at around the centre of the board)
player_x_pos = 5*tile_size
player_y_pos = 4*tile_size

# vector velocities assure continuous movement
velocity_x = 0
velocity_y = 0

# draw player as a list of parts
def draw_player(player_size, player_parts):
    # for every part in the player model
    for part in player_parts:
        # rect(surface, colour, left, top, width, height)
        pygame.draw.rect(window, player_colour, [part[0], part[1], player_size, player_size])

# handle key input
def move_player():
    global velocity_x, velocity_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        velocity_y = -player_size
        velocity_x = 0
    if keys[pygame.K_DOWN]:
        velocity_y = player_size
        velocity_x = 0
    if keys[pygame.K_LEFT]:
        velocity_x = -player_size
        velocity_y = 0
    if keys[pygame.K_RIGHT]:
        velocity_x = player_size
        velocity_y = 0

# function to be called when losing conditions occur
def game_over(score):
    root = tk.Tk()
    root.wm_withdraw()
    # grammar
    if score == 1:
        tk.messagebox.showwarning("Game over!", "You lost... You scored " + str(score) + " point.")
    else:
        tk.messagebox.showwarning("Game over!", "You lost... You scored " + str(score) + " points.")
    root.destroy()

# function to display score on the board
def draw_score(score):
    message = score_font.render("Score: "+ str(score), True, BLACK)
    window.blit(message, (0,0))

# initialize window
window = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("PySnake!")

# initialize background
background = pygame.Surface(window.get_size())
draw_background(background)

# set difficulty of the game
difficulty = player_size

# main function of the game
def main():
    global player_x_pos, player_y_pos, velocity_x, velocity_y, difficulty
    isRunning = True # flag for the main loop

    player_parts=[]
    player_length = 1

    # position of fruit (interactive objects)
    random.seed()
    fruit_x_pos = round(random.randrange(0,scr_width-player_size)/10.0)*10.0
    fruit_y_pos = round(random.randrange(0,scr_height-player_size)/10.0)*10.0

    # setting game speed
    clock = pygame.time.Clock()

    # main game loop
    while isRunning:
        clock.tick(difficulty) # capping framerate at difficulty (initially size of the player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                root = tk.Tk()
                root.wm_withdraw()
                ans = tk.messagebox.askquestion("Warning", "Do you want to quit the game?")
                if ans == 'yes':
                    launch_menu()
                    root.destroy()
                else:
                    root.destroy()

            if event.type == pygame.KEYDOWN:
                move_player()
                if event.key == pygame.K_ESCAPE:
                    root = tk.Tk()
                    root.wm_withdraw()
                    ans = tk.messagebox.askquestion("Warning", "Do you want to quit the game?")
                    if ans == 'yes':
                        launch_menu()
                        root.destroy()
                    else:
                        root.destroy()

        # draw background onto window
        window.blit(background, (0,0))

        # add vector velocities to respective components
        player_x_pos += velocity_x
        player_y_pos += velocity_y

        # handling collisions with screen boundaries
        if player_y_pos < velocity_y or player_y_pos > scr_height - player_size:
            velocity_y = 0
            game_over(player_length)
            launch_menu()
        if player_x_pos < velocity_x or player_x_pos > scr_width - player_size:
            velocity_x = 0
            game_over(player_length)
            launch_menu()

        # draw fruit
        pygame.draw.rect(window, fruit_colour, [fruit_x_pos, fruit_y_pos, player_size, player_size])

        # add next parts to the player
        player_parts.append([player_x_pos, player_y_pos])
        # moving the player around; deleting the last part so as not to grow automatically
        if len(player_parts) > player_length:
            del player_parts[0]

        for part in player_parts[:-1]: # from 0 to the penultimate part of the player
            # if the player run into themselves - game over
            if part == [player_x_pos, player_y_pos]:
                game_over(player_length)
                launch_menu()


        draw_player(player_size, player_parts)
        draw_score(player_length)
        pygame.display.update()

        # handling colissions with fruit
        if player_x_pos == fruit_x_pos and player_y_pos == fruit_y_pos:
            # spawn next fruit
            fruit_x_pos = round(random.randrange(0,scr_width-player_size)/10.0)*10.0
            fruit_y_pos = round(random.randrange(0,scr_height-player_size)/10.0)*10.0
            # add a block to the player
            player_length = player_length + 1

    pygame.quit()


def set_difficulty(selected, value):
    global difficulty
    difficulty = player_size * value

def launch_menu():
    menu = pygame_menu.Menu(scr_width, scr_height, 'PySnake!', theme=pygame_menu.themes.THEME_GREEN)
    menu.add.selector('Difficulty: ', [('Easy',1), ('Medium',2), ('Hard',3)], onchange=set_difficulty)
    menu.add.button('Play', main)
    menu.add.button('Exit', pygame_menu.events.EXIT)
    menu.mainloop(window)

launch_menu()
