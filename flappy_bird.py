# /////////// INSTRUCTIONS /////////////////
# 👾 Let's make the Flappy Bird!
# 
# 1️⃣ Run the file & install
#    - in the Terminal run the command: pip3 install pgzero
#    - play the game
#
# 2️⃣ Add in your own charachter & background sprite!
# 
# 3️⃣ Add these features in the game
#     - increase the space between obstacles
#     - end the game if a player hits an obstacle
#     - randomally space the obstacle
#     - random size obstacles 
#     - end the game if the player goes off the screen
#     - draw the score on the screen
#     - increase the score each second 
# 
# 4️⃣ extension feature ideas
#     - gems : user can collect gems for jump boost and extra coins
#     - obstacles: spawn at random distances
#     - restart: click R to restart the game 
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# import required libraries
import pgzrun
from helpers import *
from random import randint
import sys 

# SETUP GAME WINDOW
WIDTH = 300
HEIGHT = 600


# SETUP BACKGROUND
background = Actor('background_blue.png', anchor=('center', 'middle'))

# SETUP PLAYER
player = Actor('alien.png', anchor=('center', 'center'))
player.scale = .5         # scales the sprite image
player.x = 30            # sets the X position
player.y = HEIGHT/2      # sets the Y position
player.speed = 0
player.gravity = .1 
player.jump_height = 2

# SETUP OBSTACLE
OBSTARCLE_FILE = "cactus.png"
top_obstacle_list = []
bottom_obstacle_list = []
total_spawn_interval = 50
current_spawn_interval = 0

# SETUP GAME SETTINGS
game_running = True

def draw():

  # if the game is running, draw the game
    if game_running == True:


        background.draw()


        player.draw()

        for obstacle in top_obstacle_list:
          obstacle.draw()

        for obstacle in bottom_obstacle_list:
          obstacle.draw()


    # else, the game is not running, draw 'Game Over' 
    else:
        screen.draw.filled_rect(Rect((0, 0), (WIDTH, HEIGHT)), (0, 0, 0))
        screen.draw.text(f"Game Over", centerx=WIDTH/2, centery=HEIGHT/2, fontsize= 50)


def key_presses():
    global game_running

    # if the player is on the floor, they can jump
    if keyboard[keys.SPACE]:
        player.speed = -player.jump_height

    elif keyboard[keys.ESCAPE]:
        sys.exit()

def move_player():
    global game_running
    # move the player

    player.y += player.speed
    player.speed += player.gravity

    if player.top <= 0 or player.bottom >= HEIGHT:
        game_running = False

def obstacle_spawn():
    global current_spawn_interval, top_obstacle_list, bottom_obstacle_list

    current_spawn_interval += 1

    # if the total spawn interval time has passed, create new obstacle
    if current_spawn_interval > total_spawn_interval:
    
        # creates a top bottom obstacle
        top_obstacle = Actor(OBSTARCLE_FILE, anchor=('center', 'top'))
        top_obstacle.scale = 2
        top_obstacle.x = WIDTH
        top_obstacle.y = 0
        top_obstacle.flip_y = False
        top_obstacle_list.append(top_obstacle)

         # creates a new bottom obstacle
        bottom_obstacle = Actor(OBSTARCLE_FILE, anchor=('center', 'bottom'))
        bottom_obstacle.scale = 2
        bottom_obstacle.x = WIDTH
        bottom_obstacle.y = HEIGHT
        bottom_obstacle.flip_y = True
        bottom_obstacle_list.append(bottom_obstacle)


        current_spawn_interval = 0

def obstacle_movement():
    global game_running, top_obstacle_list, bottom_obstacle_list

    # move each obstacle to the left
    for obstacle in top_obstacle_list:
        obstacle.x -= 1

        # if the obstacle is off the screen, remove it
        if obstacle.x < 0:
            top_obstacle_list.remove(obstacle)

    for obstacle in bottom_obstacle_list:
        obstacle.x -= 1

        # if the obstacle is off the screen, remove it
        if obstacle.x < 0:
            bottom_obstacle_list.remove(obstacle)

    ### if player hits a obstacle, end the game
    if player.collidelist(top_obstacle_list) != -1 or player.collidelist(bottom_obstacle_list) != -1:
        game_running = True 

def update():
    global game_running

    if game_running == True:
        key_presses()
        move_player()
        obstacle_spawn()
        obstacle_movement()

pgzrun.go()
