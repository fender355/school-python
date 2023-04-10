import curses
import time
import random
import pygame

# set the dimensions of the screen
width = 800
height = 600

# initialize the screen
screen = curses.initscr()
curses.curs_set(0)
board_size = screen.getmaxyx()

# generate the initial snake position and direction
snake_pos = [(board_size[0] // 2, board_size[1] // 2)]
direction = (0, 1)

# generate the initial food position
def generate_food_position(snake_pos):
    food_pos = None
    while food_pos is None:
        # generate a random position on the board
        food_pos = (random.randint(0, board_size[0]-1), random.randint(0, board_size[1]-1))
        # check if the food position is not on the snake
        if food_pos in snake_pos:
            food_pos = None
    return food_pos

food_pos = generate_food_position(snake_pos)

# initialize the score
score = 0

# initialize the change_to variable
change_to = None

# initialize the game_over variable
game_over = False

# main game loop
while not game_over:
    # get the user input
    event = screen.getch()
    if event == curses.KEY_UP:
        change_to = (-1, 0)
    elif event == curses.KEY_DOWN:
        change_to = (1, 0)
    elif event == curses.KEY_LEFT:
        change_to = (0, -1)
    elif event == curses.KEY_RIGHT:
        change_to = (0, 1)
        
    # check if the snake ate the food
    if snake_pos[0] == food_pos:
        # if the snake ate the food, add a new head and generate a new food position
        snake_pos.insert(0, (snake_pos[0][0] + direction[0], snake_pos[0][1] + direction[1]))
        
        # update the score
        score += 1
        
        # generate a new food position
        food_pos = generate_food_position(snake_pos)
        
    else:
        # if the snake did not eat the food, remove the tail
        snake_pos.pop()
        
    # update the snake direction based on the user input
    if change_to:
        direction = change_to
        change_to = None
    
    # move the snake by adding a new head in the direction of the current direction
    new_head = (snake_pos[0][0] + direction[0], snake_pos[0][1] + direction[1])
    snake_pos.insert(0, new_head)
    
    # check if the snake collided with the boundary or with itself
    if (new_head[0] < 0 or new_head[0] >= board_size[0] or
        new_head[1] < 0 or new_head[1] >= board_size[1] or
        new_head in snake_pos[1:]):
        game_over = True
    
    # clear the screen and draw the snake and food
    screen.clear()
    screen.addstr(food_pos[0], food_pos[1], '🍎')
    for pos in snake_pos:
        screen.addstr(pos[0], pos[1], '🟢')
    
    # display the score
    screen.addstr(board_size[0], 0, f'Score: {score}')
    
    # refresh the screen
    screen.refresh()
    
    # wait for a short amount of time before moving the snake again
    time.sleep(0.1)
    
# game over, display the final score
    screen.fill(0,0,0)
    font = pygame.font.SysFont('Arial', 30)
    text = font.render('Game Over! Your score is: ' + str(score), True, 255,255,255)
    text_rect = text.get_rect()
    text_rect.center = (width // 2, height // 2)
    screen.blit(text, text_rect)
    pygame.display.update()
 
    # wait for 3 seconds before quitting the game
    pygame.time.wait(3000)
 
    # quit pygame and the program
    pygame.quit()
    quit()

