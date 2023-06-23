import pygame
from fox import Fox
from graph import plot


pygame.init()


ROAD = pygame.image.load("img/road.png")
BORDER = pygame.image.load("img/border.png")
BACKGROUND = pygame.image.load("img/background.png")
BORDER_MASK = pygame.mask.from_surface(BORDER)
HEIGHT, WIDTH = ROAD.get_height(), ROAD.get_width()
WINDOW = pygame.display.set_mode((HEIGHT, WIDTH))
BLACK = (0, 0, 0)
FPS = 60
fox = Fox()
images = [(BACKGROUND, (0, 0)), (ROAD, (0, 0)), (BORDER, (0, 0))]
clock = pygame.time.Clock()
run = True
steps = 0
steps_list = []
pygame.display.set_caption("The grass is lava")


def draw(WINDOW, images, fox):
    for img, pos in images:
        WINDOW.blit(img, pos)
        fox.draw(WINDOW)
    pygame.display.update()


while run:
    clock.tick(FPS)
    draw(WINDOW, images, fox)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    if steps < len(fox.learned_steps):
        fox.move_fox(fox.learned_steps[steps])
        fox.current_steps.append(fox.learned_steps[steps])
        steps += 1
    else:
        fox.generate_move()

    if fox.collide(BORDER_MASK):
        fox.start_position()
        fox.remember_steps()
        steps_list.append(steps)
        plot(steps_list)
        steps = 0


pygame.quit()
