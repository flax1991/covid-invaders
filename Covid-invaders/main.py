import pygame
import random

# intialize pygame
pygame.init()

# create the screen width:800 heigth:600
screen = pygame.display.set_mode((800, 600))

# insert background img
background = pygame.image.load('player/earth.jpg')

# change the window name and icon
icon = pygame.image.load('player/alien-2.png')
pygame.display.set_caption('COVID-19 invaders')
pygame.display.set_icon(icon)

# player
# player cordinate
playerimg = pygame.image.load('player/space-ship.png')
playerX = 370
playerY = 480

# create a variable for player move
playerX_changed = 0

# TODO planet img and coordinate
planet_image1 = pygame.image.load('player/saturn.png')
planetX = 600
planetY = 200

# TODO planet.png
planet_image2 = pygame.image.load('player/planet.png')
planetX2 = 50
planetY2 = 40

# enemy coordinate random
enemy_img = pygame.image.load('player/virus.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
# speed
enemyX_changed = 2.0
enemyY_changed = 40  # move 40px down

# Ready - you can't see the bullet on the screen
# Fire - The bullet is currently moving
# Bullet coordinate
bullet_img = pygame.image.load('player/laser.png')
bulletX = 0
bulletY = 480
# speed
bulletX_changed = 0
# move 10px down
bulletY_changed = 10
bullet_state = "ready"


# create a method player
def player(x, y):
    # a blit() method draw the img on the screen
    screen.blit(playerimg, (round(x), round(y)))


# TODO create a method for planet.png
def planet2(x, y):
    screen.blit(planet_image2, (round(x), round(y)))


# TODO create a method for saturn.png
def planet(x, y):
    screen.blit(planet_image1, (round(x), round(y)))


# create a method for enemy
def enemy(x, y):
    screen.blit(enemy_img, (round(x), round(y)))


# create a method for bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (round(x + 16), round(y + 10)))


# GAME LOOP, ensures that the game always work
# EXECUTE the game always inside the loop

running = True
while running:
    # Change background color RGB - red, green, blue
    screen.fill((0, 0, 0))

    # Background img
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if keystroke is pressed check whether it's right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_changed = -3.0

        if event.key == pygame.K_RIGHT:
            playerX_changed = 3.0

        if event.key == pygame.K_SPACE:
            fire_bullet(playerX, bulletY)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            # object stop
            playerX_changed = 0



    # increase and decrease the value
    playerX += playerX_changed

    # object stop at the border
    # checking for boundaries of spaceship so it doesn't go out of bounds
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    # enemy move
    enemyX += enemyX_changed
    if enemyX <= 0:
        enemyX_changed = 2.0
        enemyY += enemyY_changed  # when it gets to the edge go down
    elif enemyX >= 736:
        enemyX_changed = -2.0
        enemyY += enemyY_changed  # when it gets to the edge go down

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_changed

    # Recall method
    player(playerX, playerY)
    planet(planetX, planetY)
    planet2(planetX2, planetY2)
    enemy(enemyX, enemyY)
    fire_bullet(playerX, bulletY)
    pygame.display.update()
