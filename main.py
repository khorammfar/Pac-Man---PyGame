import pygame
from maps import MAP
import math

pygame.init()

# Display
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT + 20])
pygame.display.set_caption('pacman')

# Map
def draw_map():
    for index_line, line in enumerate(MAP):
        for index_column, column in enumerate(line):
            width = WIDTH // len(line)
            height = HEIGHT // len(MAP)
            if   column == 1:
                pygame.draw.circle(
                    surface=screen,
                    color="white",
                    center=(
                        (index_column * width) + (width * .5),
                        (index_line * height) + (height * .5)
                    ),
                    radius=2
                )
            elif column == 2:
                pygame.draw.circle(
                    surface=screen,
                    color="white",
                    center=(
                        (index_column * width) + (width * .5),
                        (index_line * height) + (height * .5)
                    ),
                    radius=5
                )
            elif column == 3:
                pygame.draw.line(
                    surface=screen,
                    color="blue",
                    start_pos=(
                        (index_column*width) + (width * .5),
                        index_line * height
                    ),
                    end_pos=(
                        (index_column*width) + (width * .5),
                        index_line*height+ height
                    ),
                    width=3
                )
            elif column == 4:
                pygame.draw.line(
                    surface=screen,
                    color="blue",
                    start_pos=(
                        index_column*width,
                        (index_line * height) + (height * .5)
                    ),
                    end_pos=(
                        (index_column*width) + width,
                        (index_line*height) + (height * .5)
                    ),
                    width=3
                )
            elif column == 5:
                pygame.draw.arc(
                    surface=screen,
                    color="blue",
                    rect=[
                        (index_column*width-(width*.4)) - 2,
                        (index_line*height+(.5 * height)),
                        width,
                        height
                    ],
                    start_angle=0,
                    stop_angle=math.pi/2,
                    width=3
                )
            elif column == 6:
                pygame.draw.arc(
                    surface=screen,
                    color="blue",
                    rect=[
                        index_column * width + (width*.5),
                        index_line * height + (height * .5),
                        width,
                        height
                    ],
                    start_angle=math.pi / 2,
                    stop_angle=math.pi,
                    width=3
                )
            elif column == 7:
                pygame.draw.arc(
                    surface=screen,
                    color="blue",
                    rect=[
                        (index_column*width+(width*.5)),
                        (index_line*height-(.4 * height)),
                        width,
                        height
                    ],
                    start_angle=math.pi,
                    stop_angle=3 * math.pi / 2,
                    width=3
                )
            elif column == 8:
                pygame.draw.arc(
                    surface=screen,
                    color="blue",
                    rect=[
                        (index_column*width-(width*.4)) -2,
                        (index_line*height-(.4 * height)),
                        width,
                        height
                    ],
                    start_angle=3 * math.pi / 2,
                    stop_angle=2 * math.pi,
                    width=3
                )
            elif column == 9:
                pygame.draw.line(
                    surface=screen,
                    color="white",
                    start_pos=(
                        index_column*width,
                        (index_line * height) + (height * .5)
                    ),
                    end_pos=(
                        (index_column*width) + width,
                        (index_line*height) + (height * .5)
                    ),
                    width=3
                )
                

# Game Loop

is_closed = False

while not is_closed:
    
    draw_map()
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            is_closed = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                is_closed = True
    # apply changes
    pygame.display.update()

pygame.quit()
