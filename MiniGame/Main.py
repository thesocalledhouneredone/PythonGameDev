import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Mini Game")
clock = pygame.time.Clock()
isRunning = True
test_font = pygame.font.Font(None, 50)

# Background surfaces
sky = pygame.Surface((1280, 500))
sky.fill("light blue")

ground = pygame.Surface((1280, 300))
ground.fill("dark green")

my_text = test_font.render("My Mini Game", False,"red")

main_char = pygame.Surface((100, 100))
main_char.fill("red")
x_pos_main = 300
y_in_general = 400

side_char = pygame.Surface((100, 100))
side_char.fill("yellow")
x_pos_side = 1100


while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            exit()

    screen.blit(sky, (0, 0))
    screen.blit(ground, (0, 500))
    screen.blit(my_text, (5, 10))

    x_pos_main += 7
    if x_pos_main >= 1280:
        x_pos_main = -100
    screen.blit(main_char, (x_pos_main, y_in_general))

    x_pos_side -= 7
    if x_pos_side <= -100:
        x_pos_side = 1280
    screen.blit(side_char, (x_pos_side, y_in_general))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
