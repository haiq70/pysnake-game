# classic snake game made with pygame module //haiq70
# pygame documentation: https://www.pygame.org/docs/
import pygame
pygame.display.init()


# dimensions of the window
scr_width = 800
scr_height = 800
# grid system for the checkerboard
tile_size = 50      # 16 x 16 board
grid_width = scr_width / tile_size  # place that many squares as the screen is wide
grid_height = scr_height / tile_size # /tall

# flag for the main loop
isRunning = True

# colors for the checkerboard background
color1 = (66, 132, 245)
color2 = (0, 65, 179)

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


# initialize window
window = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("PySnake!")

# initialize background
background = pygame.Surface(window.get_size())
draw_background(background)

# main game loop
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    # draw background onto window
    window.blit(background, (0,0))
    pygame.display.update()
pygame.quit()
