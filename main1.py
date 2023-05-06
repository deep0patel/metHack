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
# Sets general variables
key = 0
start = 0
level = 1
paused = 0
wasteSpawnTimer = 0
cloudSpawnTimer = 0
score = 0
score_threshold = 15
font = pygame.font.SysFont('Arial', 22)

TRASH_TYPES = ["blue", "black", "green"]

TRASH_IMAGES = {
    "blue": [pygame.image.load("park/plastic.png"), pygame.image.load("park/juice_box.png"),
             pygame.image.load("park/magazine.png"),
             pygame.image.load("park/newspaper.png")],
    "black": [pygame.image.load("park/paper_nap.png")],
    "green": [pygame.image.load("park/paper_nap.png"), pygame.image.load("park/broken_rose.png")
        , pygame.image.load("park/banana_Peel.png"), pygame.image.load("park/animal_waste.png"),
              pygame.image.load("park/apple.png"), ]
}


def scale_image(img, factor):
    new_size = (int(img.get_width() * factor), int(img.get_height() * factor))
    return pygame.transform.scale(img, new_size)


# Set up trash object
class Trash:
    def __init__(self):
        self.trash_type = random.choice(TRASH_TYPES)
        self.image_list = TRASH_IMAGES[self.trash_type]
        self.image = scale_image(random.choice(self.image_list), 0.1)
        self.width, self.height = self.image.get_size()
        self.x = random.randint(0, SCREEN_WIDTH - self.width)
        self.y = random.randint(-SCREEN_HEIGHT, -self.height)

    def move_vertical(self, v_speed):
        self.y += v_speed

    def move_horizontal(self, h_speed):
        self.y += h_speed

    def draw(self):
        SCREEN.blit(self.image, (self.x, self.y))



    def intersects(self, bin_rect):
        return bin_rect.colliderect(pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height()))

    def in_bin(self, bin_rect):
        if self.intersects(bin_rect):
            if self.trash_type == "paper" and bin_rect == BINS[3]:
                return True
            elif self.trash_type == "plastic" and bin_rect == BINS[1]:
                return True
            elif self.trash_type == "organic" and bin_rect == BINS[0]:
                return True
            else:
                return False


green_bin = scale_image(pygame.image.load("green.png"), 0.65)
black_bin = scale_image(pygame.image.load("black.png"), 0.65)
blue_bin = scale_image(pygame.image.load("blue.png"), 0.65)

BIN_WIDTH = green_bin.get_width()
BIN_HEIGHT = green_bin.get_height()

GREEN_BIN_RECT = pygame.Rect(0, SCREEN_HEIGHT - BIN_HEIGHT, BIN_WIDTH, 50)
BLACK_BIN_RECT = pygame.Rect(BIN_WIDTH, SCREEN_HEIGHT - BIN_HEIGHT, BIN_WIDTH, 50)
BLUE_BIN_RECT = pygame.Rect(BIN_WIDTH * 2, SCREEN_HEIGHT - BIN_HEIGHT, BIN_WIDTH, 50)

BINS = [
    GREEN_BIN_RECT, BLACK_BIN_RECT, BLUE_BIN_RECT
]





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

# Set up the game variables
score = 0
game_over = False

# Game loop
while not game_over:
    # SCREEN.blit(BG, (0, 0))

    SCREEN.fill(SKY)
    pygame.draw.rect(SCREEN, GRASS, (0, 490, 960, 50), 0)
    SCREEN.blit(green_bin, (69, 478))
    SCREEN.blit(blue_bin, (269, 478))
    SCREEN.blit(black_bin, (469, 478))

    image = Trash().image
    image_rect = image.get_rect()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                image_rect.move_ip(-5, 0)
            elif event.key == pygame.K_RIGHT:
                image_rect.move_ip(5, 0)


    # Move the object downwards
    image_rect.move_ip(0, 2)

    SCREEN.blit(image, image_rect)



    # Check if the object intersects with a bin
    # for bin_rect in BINS:
    #     if OBJECT_RECT.colliderect(bin_rect):
    #         score += 1
    #         OBJECT_RECT.move_ip(0, 0)
    #         if OBJECT_RECT.centerx < bin_rect.centerx:
    #             OBJECT_RECT.centerx = bin_rect.centerx - BIN_WIDTH // 2
    #         else:
    #             # score += 1
    #             OBJECT_RECT.centerx = bin_rect.centerx + BIN_WIDTH // 2
    #     else:
    #         # Draw the object
    #         SCREEN.blit(OBJECT_IMAGE, OBJECT_RECT)

    # Check if the object is out of bounds
    # if OBJECT_RECT.bottom >= SCREEN_HEIGHT:
    #     game_over = True



    # if trash.y > SCREEN_HEIGHT:
    #     if not game_over:
    #         global SCORE
    #         SCORE -= 10

    # Draw the score
    score_text = FONT_MEDIUM.render(f'Score: {score}', True, BLACK)
    SCREEN.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    CLOCK.tick(60)

if game_over:
    while game_over:
        # game_over = True
        game_over_text = FONT_LARGE.render('Game Over', True, BLACK)
        SCREEN.blit(game_over_text, (
            SCREEN_WIDTH // 2 - game_over_text.get_width() // 2,
            SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
        score_text = FONT_MEDIUM.render(f'Final Score: {score}', True, BLACK)
        SCREEN.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2,
                                 SCREEN_HEIGHT // 2 - score_text.get_height() // 2 + game_over_text.get_height()))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Quit
                    game_over = False
                    pygame.quit()

        # Update the display
        pygame.display.flip()
