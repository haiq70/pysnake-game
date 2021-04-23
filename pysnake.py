# classic snake game made with pygame module //haiq70
# pygame documentation: https://www.pygame.org/docs/
import pygame
import time

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
snake_head = pygame.image.load("assets\snake_head.png")

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


x_pos = 8 * tile_size
y_pos = 7 * tile_size


def draw_player():
    global x_pos, y_pos
    window.blit(snake_head, (x_pos, y_pos))

# TODO: implement continuous movement
# TODO: include wall collisions
def move_player():
    global x_pos, y_pos
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y_pos -= tile_size
        time.sleep(0.2)
    if keys[pygame.K_DOWN]:
        y_pos += tile_size
        time.sleep(0.2)
    if keys[pygame.K_LEFT]:
        x_pos -= tile_size
        time.sleep(0.2)
    if keys[pygame.K_RIGHT]:
        x_pos += tile_size
        time.sleep(0.2)



# initialize window
window = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("PySnake!")

# initialize background
background = pygame.Surface(window.get_size())
draw_background(background)

# main function of the game
def main():
    isRunning = True # flag for the main loop
    fps = 60
    clock = pygame.time.Clock()
    # main game loop
    while isRunning:
        clock.tick(fps) # capping framerate at 60
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            if event.type == pygame.KEYDOWN:
                move_player()
                if event.key == pygame.K_ESCAPE:
                    #TODO: add a warning message
                    isRunning = False
        # draw background onto window
        window.blit(background, (0,0))
        draw_player()
        pygame.display.update()
    pygame.quit()


main()
