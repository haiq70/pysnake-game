# classic snake game made with pygame module //haiq70
# pygame documentation: https://www.pygame.org/docs/
import pygame
import random
import tkinter as tk
from tkinter import messagebox

pygame.display.init()


# dimensions of the window
scr_width = 800
scr_height = 800

# grid system for the checkerboard
tile_size = 50      # 16 x 16 board
grid_width = scr_width / tile_size  # place that many squares as the screen is wide
grid_height = scr_height / tile_size # /tall

# colors for the checkerboard background
color1 = (66, 132, 245)
color2 = (0, 65, 179)

# initialize assets
snake_head = pygame.image.load("assets/snake_head.png")
snake_head = pygame.transform.scale(snake_head, (40, 40))
apple = pygame.image.load("assets/apple.png")
apple = pygame.transform.scale(apple, (50, 50))

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
player_x_pos = 8 * tile_size
player_y_pos = 7 * tile_size

# position of fruit (interactive objects)
fruit_x_pos =  tile_size
fruit_y_pos = tile_size

# vector velocities assure continuous movement
velocity_x = 0
velocity_y = 0


def draw_player():
    window.blit(snake_head, (player_x_pos, player_y_pos))

def draw_fruit():
    random.seed()
    x = random.randint(0, grid_width)
    y = random.randint(0, grid_height)
    window.blit(apple, (x*fruit_x_pos, y*fruit_y_pos))


# TODO: include wall collisions
def move_player():
    global velocity_x, velocity_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        velocity_y = -2
        velocity_x = 0
    if keys[pygame.K_DOWN]:
        velocity_y = 2
        velocity_x = 0
    if keys[pygame.K_LEFT]:
        velocity_x = -2
        velocity_y = 0
    if keys[pygame.K_RIGHT]:
        velocity_x = 2
        velocity_y = 0


# initialize window
window = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("PySnake!")

# initialize background
background = pygame.Surface(window.get_size())
draw_background(background)

# main function of the game
def main():
    global player_x_pos, player_y_pos
    isRunning = True # flag for the main loop
    fps = 60
    clock = pygame.time.Clock()
    # main game loop
    while isRunning:
        clock.tick(fps) # capping framerate at 60

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                root = tk.Tk()
                root.wm_withdraw()
                ans = tk.messagebox.askquestion("Warning", "Do you want to quit the game?")
                if ans == 'yes':
                    isRunning = False
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
                        isRunning = False
                        root.destroy()
                    else:
                        root.destroy()

        # draw background onto window
        window.blit(background, (0,0))
        # add vector velocities to respective components
        player_x_pos += velocity_x
        player_y_pos += velocity_y
        draw_player()
        pygame.display.update()
    pygame.quit()


main()
