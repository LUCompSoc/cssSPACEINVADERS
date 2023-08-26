######################################################################################################################################################
################################################################ Game Setup ##########################################################################
######################################################################################################################################################
import pygame
import sys
import numpy as np
from pygame import mixer

pygame.init()

################################################################ Window Settings #####################################################################
width = 1920
height = 1080
screen = pygame.display.set_mode(
    (width, height), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)

################################################################ In Game #############################################################################
white = (255, 255, 255)
playerLives = 3
playerScore = 0
boomSound = mixer.Sound('Assets/Audio/SFX/boom.mp3')
bulletSound = mixer.Sound('Assets/Audio/SFX/laser.wav')
#  .----------------.
# | .--------------. |
# | |      _       | |
# | |     | |      | |
# | |     | |      | |
# | |     | |      | |
# | |     |_|      | |
# | |     (_)      | |
# | '--------------' |
#  '----------------'
# Letting the player know their score and remaining lives is important, but not as important as drawing the player to the screen. Figure out how to do that first, then come back to this later.#

# define font


# def showScore(score, x, y):
# define text
# print text to screen


# def showLives(playerLives, x, y):
# define text
# print text to screen

################################################################ Game Over ###########################################################################
overFont = pygame.font.Font(None, 72)


def gameOver(x, y):
    global gameStarted

    overText = overFont.render("Game Over", True, white)
    screen.blit(overText, (x, y))

    # Game over time check
    if not hasattr(gameOver, 'gameOverTime'):
        gameOver.gameOverTime = pygame.time.get_ticks()
    else:
        elapsed = pygame.time.get_ticks() - gameOver.gameOverTime
        if elapsed >= 10000:
            pygame.quit()
            sys.exit()


################################################################ Player ##############################################################################
#  .----------------.
# | .--------------. |
# | |      _       | |
# | |     | |      | |
# | |     | |      | |
# | |     | |      | |
# | |     |_|      | |
# | |     (_)      | |
# | '--------------' |
#  '----------------'
# One of the most important parts of the game, getting the player to the screen! Find an image online which you could use as a player and import is as the body.
# While you're online, be sure to look up how to import the image into pyGame, so that you can use it!

# playerBody = load player body
# playerX = player start location on the screen
# playerY = how far down the screen you want the player to be
# playerSpeed = do I need to elaborate what this means?
# playerStationary = We don't want the player to not be able to stop, this is basiacally how fast you want the player to move, when they stop moving.


# def player(x, y):
    # Hopefully you imported the player body earlier, now you can display it!


#  .----------------.
# | .--------------. |
# | |      _       | |
# | |     | |      | |
# | |     | |      | |
# | |     | |      | |
# | |     |_|      | |
# | |     (_)      | |
# | '--------------' |
#  '----------------'
# You may have the player on the screen, but do you have any enemies? If not, what's the point in shooting? Come back to me later!

# All sorted? Perfect! What did you do for drawing the player and enemies? Do the same here!

# Player Bullet
# bulletBody = load bullet body
# bulletX = how far away (x axis) do you want it to fire from the center of the player?
# bulletY = what height should the bullet originate from?
# bulletXchange = Will your bullet move sideways?
# bulletSpeed = How fast is your speeding bullet?
# bulletState = "ready"  # Keep as is. Uncomment when other variables have been entered.


# This function will work once the bullet variables have been implimented, you can just uncomment it.
# def fireBullet(x, y):
#     global bulletState
#     bulletState = "Fire"
#     screen.blit(bulletBody, (x + 16, y + 16))

# hitDistance = 27

# Bullet collision detection, but how? Why does this work?
# def isCollision(enemyX, enemyY, bulletX, bulletY):
    # distance_squared = (enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2
    # return distance_squared < hitDistance ** 2

    ################################################################ Enemies #############################################################################
    #  .----------------.
    # | .--------------. |
    # | |      _       | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     |_|      | |
    # | |     (_)      | |
    # | '--------------' |
    #  '----------------'
    # Time to add enemies into the game! Go online and get another appropriate image for an enemie, keeping in mind the effects the picture size may have when displaying the enemy, which you may have encountered when loading in the player.

    # enemyBody = You know the drill
    # enemySpeed = ???
    # enemyValue = ???
    # enemyJump = How far down the page the enemies will go, once they reach the edge of the screen.
    # multiplier = 1 #This will be kept as is. But why? Where else is it used in the program? Why?

    # def generateEnemies(): Everything here can be uncommented and will work fine.......but hang on, why are global variables being declared here? Bit odd init? Why are they not declared elsewhere?
    #     global enemyBody, enemyX, enemyY, enemyXchange, enemyYchange, numOfEnemies

    #     # Clear previous enemies
    #     enemyX = []
    #     enemyY = []
    #     enemyXchange = []
    #     enemyYchange = []
    #     numOfEnemies = 1 * multiplier

    #     for i in range(numOfEnemies):
    #         # Calculate enemy position based on row and column
    #         row = i // 10
    #         col = i % 10
    #         enemyX.append(col * 100)
    #         enemyY.append(80 + row * 80)
    #         enemyXchange.append(enemySpeed)
    #         enemyYchange.append(enemyJump)

    # def enemy(x, y):
        # all you need to do here is draw the enemy to the screen

    ######################################################################################################################################################
    ################################################################ Game Start###########################################################################
    ######################################################################################################################################################
    # generateEnemies()
    # gameStarted = True
    # while gameStarted:
    #     for event in pygame.event.get():
    #         ################################################################ Safe Exit Mechanic ##################################################################
    #         if event.type == pygame.QUIT:
    #             gameStarted = False
    ################################################################ Player Controls #####################################################################
    #  .----------------.
    # | .--------------. |
    # | |      _       | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     |_|      | |
    # | |     (_)      | |
    # | '--------------' |
    #  '----------------'
    # Time to give the player controls. You want to be able to move left and right, as well as stop moving once the movement keys are released.
    # You also want to be able to shoot and have sound play when the bullet is fired.

    ################################################################ Screen Colour #####################################################################
    #  .----------------.
    # | .--------------. |
    # | |      _       | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     |_|      | |
    # | |     (_)      | |
    # | '--------------' |
    #  '----------------'
    # Add a background. Could be a solid colour, a gradient effect, a picture, or something else that I had no idea you could do. Go crazy!

    ################################################################ Emeny Movement ######################################################################
    #  .----------------.
    # | .--------------. |
    # | |      _       | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     |_|      | |
    # | |     (_)      | |
    # | '--------------' |
    #  '----------------'
    # Everything here works fine, just uncomment it when the players, enemies and bullets are ready!

    # enemyY = np.array(enemyY)
    # playerY = float(playerY)

    # Game over when enemy is too close
    # for y in enemyY:
    #     if y > playerY - 50:
    #         gameOver((width // 2) - 75, (height // 2) -
    #                  75)
    #         break

    # else:
    #     # Enemy movement and collision detection
    #     for i in range(numOfEnemies):
    #         # Enemy Right
    #         if enemyX[i] <= 0:
    #             enemyXchange[i] = enemySpeed
    #             if enemyX[i] <= 0.1:
    #                 enemyY[i] += enemyYchange[i]
    #         # Enemy Left
    #         elif enemyX[i] >= width * 0.96:
    #             enemyXchange[i] = -enemySpeed
    #             if enemyX[i] >= (width * 0.96) - 0.1:
    #                 enemyY[i] += enemyYchange[i]
    #         enemyX[i] += enemyXchange[i]

    # Player bullet collision
    # if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
    #     boomSound.play()
    #     bulletY = playerY
    #     bulletState = "ready"
    #     playerScore += enemyValue

    # Remove the enemy from the list
    # enemyX.pop(i)
    # enemyY = np.delete(enemyY, i)
    # enemyXchange.pop(i)
    # enemyYchange.pop(i)
    # numOfEnemies -= 1
    # break  # Exit the loop

    # Generates new, more and faster enemies when all have been destroyed.
    # if len(enemyX) == 0:
    #     multiplier += 2
    #     enemySpeed *= 1.1
    #     generateEnemies()

    # Resets the bullet functionality once it exits the screen.
    # if bulletY <= 0:
    #     bulletY = playerY
    #     bulletState = "ready"
    # elif bulletState == "Fire":
    #     fireBullet(bulletX, bulletY)
    #     bulletY -= bulletSpeed

    ################################################################ Final Draw to Screen ################################################################
    #  .----------------.
    # | .--------------. |
    # | |      _       | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     |_|      | |
    # | |     (_)      | |
    # | '--------------' |
    #  '----------------'
    # Time to draw everything to the screen! Your game will look great by the end of this!

    # call player function
    # Draw each enemy on the screen
    # display the player score
    # display the players remaining lives

    pygame.display.update()  # Tells pyGame to update the display.
