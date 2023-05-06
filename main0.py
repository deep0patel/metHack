import pygame
import time
import random

pygame.font.init()
pygame.init()

WIDTH, HEIGHT = 700, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Waste Classification")

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

TRASH_WIDTH = 40
TRASH_HEIGHT = 60

PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

# Set up the object
OBJECT_SIZE = 50
OBJECT_HORIZONTAL_SPEED = 1
OBJECT_VERTICAL_SPEED = 10

FONT = pygame.font.SysFont("comicsans", 30)


def scale_image(img, factor):
    new_size = (int(img.get_width() * factor), int(img.get_height() * factor))
    return pygame.transform.scale(img, new_size)


def draw(player):
    WIN.blit(BG, (0, 0))
    #
    # time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    # WIN.blit(time_text, (10, 10))

    # pygame.draw.rect(WIN, "red", player)

    green_bin = scale_image(pygame.image.load("green_org.png"), 0.65)
    red_bin = scale_image(pygame.image.load("red_plastic.png"), 0.65)
    blue_bin = scale_image(pygame.image.load("blue_bottles_cans.png"), 0.65)
    yellow_bin = scale_image(pygame.image.load("yellow_mixed_Paper.png"), 0.65)

    # for star in stars:
    #     pygame.draw.rect(WIN, "white", star)

    WIN.blit(green_bin, (40, 478))
    WIN.blit(blue_bin, (205, 478))
    WIN.blit(red_bin, (370, 478))
    WIN.blit(yellow_bin, (535, 478))

    green_bin_rect = pygame.Rect(40, 478, green_bin.get_width(), green_bin.get_height())
    red_bin_rect = pygame.Rect(40, 478, red_bin.get_width(), red_bin.get_height())
    blue_bin_rect = pygame.Rect(40, 478, blue_bin.get_width(), blue_bin.get_height())
    yellow_bin_rect = pygame.Rect(40, 478, yellow_bin.get_width(), yellow_bin.get_height())

    pygame.display.update()



run = True

trash = pygame.Rect(200, HEIGHT - TRASH_HEIGHT,
                    TRASH_WIDTH, TRASH_HEIGHT)
CLOCK = pygame.time.Clock()
# start_time = time.time()
# elapsed_time = 0
#
# star_add_increment = 2000
# star_count = 0
#
# stars = []
# hit = False
# implement rendom function here to choose any png from the folder
IMAGE = pygame.image.load('green_org.png')
OBJECT_IMAGE = scale_image(IMAGE, 0.1)
WIN.blit(OBJECT_IMAGE,(0,0))
OBJECT_RECT = OBJECT_IMAGE.get_rect()
OBJECT_RECT.x = random.randint(0, WIDTH - OBJECT_SIZE)
OBJECT_RECT.y = 0

while run:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                OBJECT_RECT.move_ip(-OBJECT_VERTICAL_SPEED, 0)
            elif event.key == pygame.K_RIGHT:
                OBJECT_RECT.move_ip(OBJECT_VERTICAL_SPEED, 0)

    # Move the object downwards
    OBJECT_RECT.move_ip(0, OBJECT_HORIZONTAL_SPEED)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT] and trash.x - PLAYER_VEL >= 0:
    #     trash.x -= PLAYER_VEL
    # if keys[pygame.K_RIGHT] and trash.x + PLAYER_VEL + trash.width <= WIDTH:
    #     trash.x += PLAYER_VEL

    # for star in stars[:]:
    # star.y += STAR_VEL
    # if star.y > HEIGHT:
    #     stars.remove(star)
    # elif star.y + star.height >= player.y and star.colliderect(player):
    #     stars.remove(star)
    #     hit = True
    #     break
    #
    # if hit:
    #     lost_text = FONT.render("You Lost!", 1, "white")
    #     WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
    #     pygame.display.update()
    #     pygame.time.delay(4000)
    #     break


    CLOCK.tick(60)

    draw(trash)



pygame.quit()

