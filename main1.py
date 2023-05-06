import time

import pygame
import random

pygame.init()

# Set up the display
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the fonts
FONT_SMALL = pygame.font.Font(None, 24)
FONT_MEDIUM = pygame.font.Font(None, 36)
FONT_LARGE = pygame.font.Font(None, 48)


def scale_image(img, factor):
    new_size = (int(img.get_width() * factor), int(img.get_height() * factor))
    return pygame.transform.scale(img, new_size)


green_bin = scale_image(pygame.image.load("green_org.png"), 0.65)
red_bin = scale_image(pygame.image.load("red_plastic.png"), 0.65)
blue_bin = scale_image(pygame.image.load("blue_bottles_cans.png"), 0.65)
yellow_bin = scale_image(pygame.image.load("yellow_mixed_Paper.png"), 0.65)

# for star in stars:
#     pygame.draw.rect(WIN, "white", star)


# green_bin_rect = pygame.Rect(40, 478, green_bin.get_width(), green_bin.get_height())
# red_bin_rect = pygame.Rect(40, 478, red_bin.get_width(), red_bin.get_height())
# blue_bin_rect = pygame.Rect(40, 478, blue_bin.get_width(), blue_bin.get_height())
# yellow_bin_rect = pygame.Rect(40, 478, yellow_bin.get_width(), yellow_bin.get_height())

BIN_WIDTH = green_bin.get_width()
BIN_HEIGHT = green_bin.get_height()

GREEN_BIN_RECT = pygame.Rect(0, SCREEN_HEIGHT - BIN_HEIGHT, BIN_WIDTH, 50)
RED_BIN_RECT = pygame.Rect(BIN_WIDTH, SCREEN_HEIGHT - BIN_HEIGHT, BIN_WIDTH, 50)
BLUE_BIN_RECT = pygame.Rect(BIN_WIDTH * 2, SCREEN_HEIGHT - BIN_HEIGHT, BIN_WIDTH, 50)
YELLOW_BIN_RECT = pygame.Rect(BIN_WIDTH * 3, SCREEN_HEIGHT - BIN_HEIGHT, BIN_WIDTH, 50)

BINS = [
    GREEN_BIN_RECT, RED_BIN_RECT, BLUE_BIN_RECT, YELLOW_BIN_RECT
]

# Set up the object
OBJECT_SIZE = 50
OBJECT_HORIZONTAL_SPEED = 1
OBJECT_VERTICAL_SPEED = 10
IMAGE = pygame.image.load('green_org.png')
OBJECT_IMAGE = scale_image(IMAGE, 0.1)
OBJECT_RECT = OBJECT_IMAGE.get_rect()
OBJECT_RECT.x = random.randint(0, SCREEN_WIDTH - OBJECT_SIZE)
OBJECT_RECT.y = 0

# Defines general colours
SKY = (150, 240, 255)
GRASS = (126, 200, 80)
IVORY = (250, 250, 235)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Set up the game clock
CLOCK = pygame.time.Clock()

waste_list = []
remove_waste = []
waste_pool = [1, 2]  # List of waste items eligible to be spawned in the round
waste_randomizer = 0  # A random number drawn from waste_pool
waste_widths = [40, 50, 50, 50, 50, 40, 50, 30, 50, 50, 50, 48, 40, 40, 20, 20, 40, 23]
waste_heights = [40, 25, 25, 25, 31, 40, 25, 45, 25, 30, 40, 45, 40, 40, 40, 40, 40, 40]
waste_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
wasteGraphics = [pygame.transform.scale(pygame.image.load('waste/garb1.png'), (waste_widths[0], waste_heights[0])),
                 pygame.transform.scale(pygame.image.load('waste/garb2.png'), (waste_widths[1], waste_heights[1])),
                 pygame.transform.scale(pygame.image.load('waste/garb3.png'), (waste_widths[2], waste_heights[2])),
                 pygame.transform.scale(pygame.image.load('waste/garb4.png'), (waste_widths[3], waste_heights[3])),
                 pygame.transform.scale(pygame.image.load('waste/garb5.png'), (waste_widths[4], waste_heights[4])),
                 pygame.transform.scale(pygame.image.load('waste/garb6.png'), (waste_widths[5], waste_heights[5])),
                 pygame.transform.scale(pygame.image.load('waste/garb7.png'), (waste_widths[6], waste_heights[6])),
                 pygame.transform.scale(pygame.image.load('waste/garb8.png'), (waste_widths[7], waste_heights[7])),
                 pygame.transform.scale(pygame.image.load('waste/garb9.png'), (waste_widths[8], waste_heights[8])),
                 pygame.transform.scale(pygame.image.load('waste/garb10.png'), (waste_widths[9], waste_heights[9])),
                 pygame.transform.scale(pygame.image.load('waste/garb11.png'),
                                        (waste_widths[10], waste_heights[10])),
                 pygame.transform.scale(pygame.image.load('waste/garb12.png'),
                                        (waste_widths[11], waste_heights[11])),
                 pygame.transform.scale(pygame.image.load('waste/garb13.png'),
                                        (waste_widths[12], waste_heights[12])),
                 pygame.transform.scale(pygame.image.load('waste/garb14.png'),
                                        (waste_widths[13], waste_heights[13])),
                 pygame.transform.scale(pygame.image.load('waste/garb15.png'),
                                        (waste_widths[14], waste_heights[14])),
                 pygame.transform.scale(pygame.image.load('waste/garb16.png'),
                                        (waste_widths[15], waste_heights[15])),
                 pygame.transform.scale(pygame.image.load('waste/garb17.png'),
                                        (waste_widths[16], waste_heights[16])),
                 pygame.transform.scale(pygame.image.load('waste/garb18.png'),
                                        (waste_widths[17], waste_heights[17]))]


# -----EVERYTHING CLOUDS-----
class Cloud:
    def __init__(self, cloudID, cloudX, cloudY, cloudSpeed):
        self.ID = cloudID
        self.x = cloudX
        self.y = cloudY
        self.speed = cloudSpeed

    def draw(self):
        SCREEN.blit(cloudGraphics[self.ID], (int(self.x), int(self.y)))


cloud_list = []
cloud_widths = [70, 90, 120, 150]
cloud_heights = [70, 80, 100, 160]
remove_cloud = []
cloud_randomizer = 0  # A random number drawn from cloud pool
cloudGraphics = [pygame.transform.scale(pygame.image.load('cloud.png'), (cloud_widths[0], cloud_heights[0])),
                 pygame.transform.scale(pygame.image.load('cloud.png'), (cloud_widths[1], cloud_heights[1])),
                 pygame.transform.scale(pygame.image.load('cloud.png'), (cloud_widths[2], cloud_heights[2])),
                 pygame.transform.scale(pygame.image.load('cloud.png'), (cloud_widths[3], cloud_heights[3]))]

# Set up the game variables
score = 0
game_over = False

# Game loop
while not game_over:

    SCREEN.blit(BG, (0, 0))

    SCREEN.blit(green_bin, (40, 478))
    SCREEN.blit(blue_bin, (205, 478))
    SCREEN.blit(red_bin, (370, 478))
    SCREEN.blit(yellow_bin, (535, 478))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                OBJECT_RECT.move_ip(-OBJECT_VERTICAL_SPEED, 0)
            elif event.key == pygame.K_RIGHT:
                OBJECT_RECT.move_ip(OBJECT_VERTICAL_SPEED, 0)

    # Move the object downwards
    OBJECT_RECT.move_ip(0, OBJECT_HORIZONTAL_SPEED)

    # Check if the object intersects with a bin
    for bin_rect in BINS:
        if OBJECT_RECT.colliderect(bin_rect):
            score += 1
            OBJECT_RECT.move_ip(0, 0)
            if OBJECT_RECT.centerx < bin_rect.centerx:
                OBJECT_RECT.centerx = bin_rect.centerx - BIN_WIDTH // 2
            else:
                # score += 1
                OBJECT_RECT.centerx = bin_rect.centerx + BIN_WIDTH // 2
        else:
            # Draw the object
            SCREEN.blit(OBJECT_IMAGE, OBJECT_RECT)

    # Check if the object is out of bounds
    if OBJECT_RECT.bottom >= SCREEN_HEIGHT:
        game_over = True

    # Clear the screen
    # SCREEN.fill(BLACK)

    # Draw the bins
    # for bin_rect in BINS:
    #     pygame.draw.rect(SCREEN, GREEN, bin_rect)

    # Draw the score
    score_text = FONT_MEDIUM.render(f'Score: {score}', True, BLACK)
    SCREEN.blit(score_text, (10, 10))

    if game_over:
        esc = True
        while esc:
            # Game over screen
            # SCREEN.fill(BLACK)
            game_over_text = FONT_LARGE.render('Game Over', True, BLACK)
            SCREEN.blit(game_over_text, (
                SCREEN_WIDTH // 2 - game_over_text.get_width() // 2,
                SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
            score_text = FONT_MEDIUM.render(f'Final Score: {score}', True, BLACK)
            SCREEN.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2,
                                     SCREEN_HEIGHT // 2 - score_text.get_height() // 2 + game_over_text.get_height()))

            # Update the display
            pygame.display.flip()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    esc = False
    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    CLOCK.tick(60)
