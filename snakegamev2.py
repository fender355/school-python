import pygame
import random

# initialize pygame
pygame.init()

# create screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# set colors
green = (0, 255, 0)
red = (255, 0, 0)

# set font for displaying score
font = pygame.font.Font(None, 36)

# set initial position of the snake
snake_block_size = 10
snake_speed = 15
x_change = 0
y_change = 0
snake_list = []
snake_length = 1

# set initial position of food
food_block_size = 10
food_x = round(random.randrange(0, screen_width - food_block_size) / 10.0) * 10.0
food_y = round(random.randrange(0, screen_height - food_block_size) / 10.0) * 10.0

# set initial score
score = 0

# function to display score on the screen
def display_score(score):
    score_text = font.render("Score: " + str(score), True, green)
    screen.blit(score_text, [10, 10])

# game loop
game_over = False
while not game_over:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_block_size
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_block_size
                y_change = 0
            elif event.key == pygame.K_UP:
                x_change = 0
                y_change = -snake_block_size
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = snake_block_size
    
    # move the snake
    snake_head = []
    snake_head.append(round(snake_block_size + x_change, 1))
    snake_head.append(round(snake_block_size + y_change, 1))
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]
    
    # check if snake hit the boundary or itself
    for block in snake_list[:-1]:
        if block == snake_head:
            game_over = True
    if snake_head[0] < 0 or snake_head[0] >= screen_width or snake_head[1] < 0 or snake_head[1] >= screen_height:
        game_over = True
    
    # check if snake eats the food
    if snake_head[0] == food_x and snake_head[1] == food_y:
        food_x = round(random.randrange(0, screen_width - food_block_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, screen_height - food_block_size) / 10.0) * 10.0
        snake_length += 1
        score += 10
    
    # draw the snake and the food on the screen
    screen.fill((0, 0, 0))
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], snake_block_size, snake_block_size])
    pygame.draw.rect(screen, red, [food_x, food_y, food_block_size, food_block_size])
    display_score(score)
    pygame.display.update()
