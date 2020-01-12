import pygame
from Game import Game
import Init
# Import libraries and other relevant files

#####
#
# Main file which governs the Scatter game. This file runs the main game loop, instantiates the game class from Game.py,
# and takes user input
#
#####

# Initialize the pygame library
pygame.init()
# Change the name of the game window
pygame.display.set_caption("SHATTER")
# Load pygame font library
pygame.font.get_fonts()
# Declare a pygame display variable named screen of the desired size
screen = pygame.display.set_mode((1000, 600))
# Initialize the done Boolean, which will govern the main game loop
done = False

# Initialize a clock which will be used to update the game on a framerule
clock = pygame.time.Clock()

# Initialize a number of flags which will be used later
gameState = 0
gameTime = 0
game = None

# Find the current list of high scores from the createHighScores() function in Init
highScores = Init.createHighScores()

# Load the heart image so that it can be initalized before the loadHeart() function in Init is relevant
heart = pygame.transform.scale(pygame.image.load("Heart/heart.png"), (30, 30))

# Delcare a set of buttons, with relevant coordinates and data values, and place them in an array
button1 = [66,133,0]
button2 = [382,133,1]
button3 = [66,366,2]
button4 = [382,366,3]
buttons = [button1,button2,button3,button4]


# Declare the flag of whether the mouse has been clicked, beginning at False
mouseClick = False


# Declare some rgb colors used regularly for images in the file
color = (255, 100, 0)
white = (255, 255, 255)
black = (0, 0, 0)

# Using the same method of instantiating a font of the proper size, and then using pygame.font.Font.render, create objects
# with text to be displayed, and add them to an array with a smaller array of their eventual coordinates
text = [pygame.font.Font('freesansbold.ttf', 50).render('SHATTER', True, white, black), [380, 25]]
text2 = [pygame.font.Font('freesansbold.ttf', 50).render('START', True, white), [110,185]]
text3 = [pygame.font.Font('freesansbold.ttf', 50).render('LEVEL', True, white), [426,185]]
text4 = [pygame.font.Font('freesansbold.ttf', 50).render('ABOUT', True, white), [100,421]]
text5 = [pygame.font.Font('freesansbold.ttf', 50).render('QUIT', True, white), [446,421]]
text6 = [pygame.font.Font('freesansbold.ttf', 35).render('HIGHSCORES', True, white, black), [700,130]]

def highScoreList(highScores):
    # This function takes the argument of the array of highSores, and create the arrays with relevant text and coordinates as mentioned above
    # This is functional because these high scores may need to be updated after every session of the game, so they are checked regularly
    text7 = [pygame.font.SysFont("freesansbold.ttf", 30).render(highScores[0], True, white, black), [700,200]]
    text8 = [pygame.font.SysFont("freesansbold.ttf", 30).render(highScores[2], True, white, black), [700,230]]
    text9 = [pygame.font.SysFont("freesansbold.ttf", 30).render(highScores[4], True, white, black), [700,260]]
    text10 = [pygame.font.SysFont("freesansbold.ttf", 30).render(highScores[6], True, white, black), [700,290]]
    text11 = [pygame.font.SysFont("freesansbold.ttf", 30).render(highScores[8], True, white, black), [700,320]]
    text12 = [pygame.font.SysFont("freesansbold.ttf", 30).render(highScores[1], True, white, black), [900,200]]
    text13 = [pygame.font.SysFont("freesansbold.ttf", 30).render(highScores[3], True, white, black), [900,230]]
    text14 = [pygame.font.SysFont("freesansbold.ttf", 30).render(highScores[5], True, white, black), [900,260]]
    text15 = [pygame.font.SysFont("freesansbold.ttf", 30).render(highScores[7], True, white, black), [900,290]]
    text16 = [pygame.font.SysFont("freesansbold.ttf", 30).render(highScores[9], True, white, black), [900,320]]

    # Return the created text arrays
    return text7, text8, text9, text10, text11, text12, text13, text14, text15, text16

# Call the above function once to initialize the variable
text7, text8, text9, text10, text11, text12, text13, text14, text15, text16 = highScoreList(highScores)

# Place all of the texts (apart from the title text) into an array to be looped through
texts = [text2,text3,text4,text5,text6,text7,text8,text9,text10,text11, text12, text13, text14, text15, text16]

# Another set of text images for the CHOOSE LEVEL screen instead of the main menu. Exactly the same as above
chlt1 = [pygame.font.Font('freesansbold.ttf', 50).render('CHOOSE LEVEL', True, white), [500-pygame.font.Font('freesansbold.ttf', 50).render('CHOOSE LEVEL', True, white).get_rect().width/2,75]]
chlt2 = [pygame.font.Font('freesansbold.ttf', 50).render('1', True, white), [100-pygame.font.Font('freesansbold.ttf', 50).render('1', True, white).get_rect().width/2,250]]
chlt3 = [pygame.font.Font('freesansbold.ttf', 50).render('2', True, white), [200-pygame.font.Font('freesansbold.ttf', 50).render('2', True, white).get_rect().width/2,250]]
chlt4 = [pygame.font.Font('freesansbold.ttf', 50).render('3', True, white), [300-pygame.font.Font('freesansbold.ttf', 50).render('3', True, white).get_rect().width/2,250]]
chlt5 = [pygame.font.Font('freesansbold.ttf', 50).render('4', True, white), [400-pygame.font.Font('freesansbold.ttf', 50).render('4', True, white).get_rect().width/2,250]]
chlt6 = [pygame.font.Font('freesansbold.ttf', 50).render('5', True, white), [500-pygame.font.Font('freesansbold.ttf', 50).render('5', True, white).get_rect().width/2,250]]
chlt7 = [pygame.font.Font('freesansbold.ttf', 50).render('6', True, white), [600-pygame.font.Font('freesansbold.ttf', 50).render('6', True, white).get_rect().width/2,250]]
chlt8 = [pygame.font.Font('freesansbold.ttf', 50).render('7', True, white), [700-pygame.font.Font('freesansbold.ttf', 50).render('7', True, white).get_rect().width/2,250]]
chlt9 = [pygame.font.Font('freesansbold.ttf', 50).render('8', True, white), [800-pygame.font.Font('freesansbold.ttf', 50).render('8', True, white).get_rect().width/2,250]]
chlt10 = [pygame.font.Font('freesansbold.ttf', 50).render('9', True, white), [900-pygame.font.Font('freesansbold.ttf', 50).render('9', True, white).get_rect().width/2,250]]

# Place all of the CHOOSE LEVEL texts into an array for looping
chooseLevelTexts = [chlt1,chlt2,chlt3,chlt4,chlt5,chlt6,chlt7,chlt8,chlt9,chlt10]

# More text variables, these for the ABOUT screen
abt1 = [pygame.font.Font('freesansbold.ttf', 20).render('SHATTER WAS WRITTEN BY', True, white), [500-pygame.font.Font('freesansbold.ttf', 20).render('SHATTER WAS WRITTEN BY', True, white).get_rect().width/2,75]]
abt2 = [pygame.font.Font('freesansbold.ttf', 20).render('JOSHUA GIBBONS', True, white), [500-pygame.font.Font('freesansbold.ttf', 20).render('JOSHUA GIBBONS', True, white).get_rect().width/2,150]]
abt3 = [pygame.font.Font('freesansbold.ttf', 20).render('CLARK HENSLEY', True, white), [500-pygame.font.Font('freesansbold.ttf', 20).render('CLARK HENSLEY', True, white).get_rect().width/2,225]]
abt4 = [pygame.font.Font('freesansbold.ttf', 20).render('ELIJAH MAGEE', True, white), [500-pygame.font.Font('freesansbold.ttf', 20).render('ELIJAH MAGEE', True, white).get_rect().width/2,300]]

# The ABOUT text placed into an array
aboutTexts = [abt1,abt2,abt3,abt4]





def dist(p1,p2):
    # This funtion finds the distance between two points by Pythagorean theorem
    return ( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )** .5


while not done:
    # BEGIN the main while loop governing the game


    for event in pygame.event.get(): # For every event which the pygame library registers

        if event.type == pygame.QUIT: # If the event is quitting the game,
            done = True # Set the done boolean to True, ending the loop

        if gameState == 0 : # If gameState is 0, that is, if the Menu is expected
            if event.type == pygame.MOUSEBUTTONUP: # If the mouse is released
                for i in buttons: # For every button on the main menu
                    if (mousePos[0] > i[0] and mousePos[0] < i[0] + 250 and mousePos[1] > i[1] and mousePos[1] < i[1] + 150): # Check if the mouse position is within the button
                        # If the mouse is released on the button with data 0, that is "Start"
                        if i[2] == 0 :
                            game = Game(1, screen, heart, 0, 0, 5, 0, Init.createHighScores()) # Instantiate a game object at level 1, with
                            # the screen and hearts, no score, no words cleared, 5 lives a game state of 0, and the highScoresList
                            gameState = 1 # Set gameState to 1

                        # If the mouse is released on the button with data 1, that is, "Levels"
                        if i[2] == 1:
                            gameState = 2 # Set gameState to 2

                        # If the mouse is released on the button with data 2, that is "About"
                        if i[2] == 2:
                            gameState = 3 # Set gameState to 3

                        if i[2] == 3: # If the mosue is released on button with data 3, that is "Quit"
                            done = True # Set done Flag to True, ending the loop

        if gameState == 1 : # If gameState is 1
            if event.type == pygame.KEYDOWN: # Check if KEYDOWN event occurs
                if event.key >= pygame.K_a and event.key <= pygame.K_z and len(game.inputStream) < 12: # Check if the key pressed is a letter, and if the inputStream is not too long
                    game.inputStream = game.inputStream + chr(event.key).upper() # Add that letter to the inputSTream
                elif event.key == pygame.K_RETURN: # If the key is enter
                    game.selectedInput = game.inputStream # Store the inputStream as selectedInput
                    game.inputStream = "" # Clear inputStream
                    game.toggleEnter() # Note that enter was pressed
                elif event.key == pygame.K_BACKSPACE: # If the key pressed is delete
                    game.inputStream = game.inputStream[:len(game.inputStream) - 1] # Delete the last character of the string

        if gameState == 2: # If gamestate is 2
            if event.type == pygame.MOUSEBUTTONDOWN: # Check where the mouse is pressed
                mouseClick = True # Set mouseClick bool to True
            if event.type == pygame.MOUSEBUTTONUP and mouseClick: # If the mouse has been pressed and clicked
                mouseClick = False # Set the mouseClick bool to False
                for i in range(len(chooseLevelTexts)): # Check each level selection button
                    if dist(mousePos, chooseLevelTexts[i][1]) < 40: # Find the correct position of the click
                        game = Game(i, screen, heart, 0, 0, 5, 0, Init.createHighScores()) # Instantiate a game at the desired level, with other parameters default
                        gameState = 1 # set gameState to 1

        if gameState == 3: # If gameState is 3
            if event.type == pygame.MOUSEBUTTONDOWN: # Check when the mouse is pressed
                mouseClick = True # Set the flag to True
            if event.type == pygame.MOUSEBUTTONUP and mouseClick: # If mouse is clicked and flag is True
                mouseClick = False # Set the flag to false
                gameState = 0 # Return to the main emnu

    gameTime += 1 # Increase the time each loop
    gameTime %= 60 # Modulo the time, so that it does not increase exponentially


    if gameState == 0: # If gameState is 0

        text7, text8, text9, text10, text11, text12, text13, text14, text15, text16 = highScoreList(highScores) # Reset the dispalyed highScore list

        texts = [text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13, text14, text15, text16] # Reset the texts array

        mousePos = pygame.mouse.get_pos() # Find the position of the mouse

        screen.fill((0, 0, 0)) # Clear the screen
        color = (255, 100, 0) # Define the button color

        for i in buttons: # For each button
            pygame.draw.rect(screen, color, pygame.Rect(i[0], i[1], 250, 150)) # Draw a button rectangle
            if (mousePos[0] > i[0] and mousePos[0] < i[0]+250 and mousePos[1] > i[1] and mousePos[1] < i[1]+150): # If the mouse is on the button
                pygame.draw.rect(screen,[color[0],color[1]+80,color[2]+80], pygame.Rect(i[0], i[1], 250, 150)) # Brighten the color of the button

        if gameTime < 30: # For the first 30 frames every second
            screen.blit(text[0], text[1]) # Display the title
        for i in range(len(texts)): # For all the other text
                screen.blit(texts[i][0], texts[i][1]) # Display all the other text


    # run game loop
    elif gameState == 1 : # If the gameState is 1
        if game.running == True: # So long as the running flag is True
            game.loop_game() # Call loop_game()
        else: # Otherwise
            highScores = Init.createHighScores() # Get the highScores to be put up
            gameState = 0 # Go to the main menu

    elif gameState == 2: # If the gameState is 2
        mousePos = pygame.mouse.get_pos() # Find the mouse position
        screen.fill((0, 0, 0)) # Clear the screen
        for i in range(len(chooseLevelTexts)): # Show the level section buttons
                if dist(mousePos, chooseLevelTexts[i][1]) < 40: # If a selection button is hovered over
                    if gameTime//10 % 2 == 0: # Every 20 frames
                        screen.blit(chooseLevelTexts[i][0], chooseLevelTexts[i][1]) # Flash the button
                else: # Otherwise
                    screen.blit(chooseLevelTexts[i][0], chooseLevelTexts[i][1]) # Show the texts normally

    elif gameState == 3: # If the gameState is 3
        screen.fill((0, 0, 0)) # Clear the screen
        for i in range(len(aboutTexts)): # For each about Test
                screen.blit(aboutTexts[i][0], aboutTexts[i][1]) # Display the about text

    pygame.display.flip() # update the screen each loop
    clock.tick(60) # Set the framerate
