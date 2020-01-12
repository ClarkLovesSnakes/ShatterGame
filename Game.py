import pygame
import random
from Word import Word
import Init
import math
# Import relevant libraries and files

#####
#
# This file holds the Game class, which governs much of the data about the game, some elements of user input, and calls
# The Word.py file for its contents.
#
######

# Initialize Pygame
pygame.init()

# Create a Game class
class Game:

    # The class is initialized with the following variables, and below has a number of other self attributes
    def __init__(self, level, screen, heartSprite, wordsCleared, score, lives, gameState, highScores):

        self.level = level
        self.wordsCleared = wordsCleared
        self.screen = screen
        self.heartSprite = heartSprite
        self.score = score
        self.lives = lives
        self.gameState = gameState
        self.highScores = highScores

        # sound objects
        self.shatterSound = pygame.mixer.Sound("Sounds/correct.wav")
        self.levelUpSound = pygame.mixer.Sound("Sounds/levelUp.wav")
        self.loseLifeSound = pygame.mixer.Sound("Sounds/loseLife.wav")

        # game state variables
        self.dictionary = Init.createData()
        self.images = Init.loadImages()
        self.words = []
        self.inputStream = ""
        self.selectedInput = ""
        self.framesSinceLastWord = 0
        self.enterPressed = False
        self.running = True

        # hurt animation variables
        self.hurt = False
        self.hurtFrameCount = 0
        self.hurtAlpha = 0


    # This Function is used to increase level by 1, it calls the IncrementLives() function, and plays the LevelUpSound
    def incrementLevel(self):
        self.level += 1
        self.incrementLives()
        self.levelUpSound.play()

    # This function increments self.lives if self.lives is less than 5
    def incrementLives(self):
        if self.lives < 5 :
            self.lives += 1

    # This function increases the count of the number of words cleared on the current level, and calls for the level to
    # be incremented if the number of words cleared is high enough, 15 in this case. In such a case, wordsCleared is also
    # reset to 0
    def incrementWordsCleared(self):
        self.wordsCleared += 1
        if self.wordsCleared >= 15:

            self.incrementLevel()
            self.wordsCleared = 0

    # This function decreases the number of self.lives. It declares self.hurt as True, so that the hurt animation plays,
    # decrements the self.lives counter, and plays the loseLifeSound.
    def decrementLives(self):
        self.hurt = True
        self.lives -= 1
        self.loseLifeSound.play()

    # This function increases the score by amount, an int passed through it, defined by the length and complexity of the word
    def incrementScore(self, amount):
        self.score += amount

    # This function gets the length of a word from between 3 and 8, based on the current level. (Level 1 and 2 only have
    # words of length 3, levels 3 and 4 have words of lengths 3 and 4, etc.)
    def defineWordLength(self):
        length = math.floor((3 + (self.level - 1) * 0.5))
        return random.randint(3, length)

    # This function determines what will happen to the next word to appear, prepares the data for this word, and passes this
    # data to Word.py, eventually returning the Word object
    def getWord(self):

        # Define the three possibilities as zero
        length = 0
        swaps = 0
        deletions = 0

        # Assume, at first, that neither one nor two deletions will occur
        isDeletingOne = False
        isDeletingTwo = False

        # If the level is 10 or above
        if self.level >= 10:
            # Generate a random integer between 1 and 10
            randDelete = random.randint(1,10)
            # If that integer is 10
            if randDelete == 10:
                isDeletingOne = True # Declare that one character will be deleted
            # If that integer is 9
            elif randDelete == 9:
                isDeletingTwo = True # Declare that two characters will be delted
        # If the level is not 10 or above, but is 5 or above
        elif self.level >= 5:
            # Generate a random integer between 1 and 10
            randDelete = random.randint(1,10)
            # If that integer is 10
            if randDelete == 10:
                isDeletingOne = True # Declare that one character will be deleted

        if isDeletingTwo: # If two characters will be deleted
            deletions = 2 # Set deletions to two
        elif isDeletingOne: # If one character will be deleted
            deletions = 1 # set deletions to one
        else: # If no deletions are occuring
            swaps = random.randint(0, self.level) # Set swap to some number between 0 and the current level

        length = self.defineWordLength() # Declare length based on defineWordLength()
        speedFactor = 0.4 # Set what the speed will be multiplied by to 0.4
        if length > 4 : # If the word is longer than 4 characters
            speedFactor = 0.1 # Slow the word to a factor of 0.1
        elif length > 3 : # If the word is 4 characters (shorter than 5, longer than 3)
            speedFactor = 0.2 # Slow the word to factor of 0.2
        speed = speedFactor * random.randint(1, self.level) # Define speed by speed factor times some integer between 1 and the level

        # Return a word object with an original word for init.Pickword based on the base data and the defined length, and the created speed, swaps, and deletions
        return Word(Init.pickWord(self.dictionary, self.defineWordLength()), speed, swaps, deletions)

    def toggleEnter(self):
        # This function checks if the enter key is pressed on relevant screens
        if self.gameState == 1 or self.gameState == 2:
            self.enterPressed = True


    def loop_game(self):
        # This function is the main loop of the game

        # Clear the screen briefly
        self.screen.fill((0, 0, 0))

        # If the gameState is 0
        if self.gameState == 0:

            # Increase the count of framesSinceLastWord
            self.framesSinceLastWord += 1

            # If there are fewer than 5 words, and there have been 30 or more frames since the last word was instantiated
            if len(self.words) < 5 and self.framesSinceLastWord >= 30:
                self.words.append(self.getWord()) # Add a new word
                self.framesSinceLastWord = 0 # Note that it's now 0 frames since the last word

            for i in range(len(self.words) - 1, -1, -1): # For each word, going from the first first

                # update word states
                self.words[i].update() # Update each word

                # check user input
                if self.selectedInput != "": # If the user has not entered nothing
                    if self.selectedInput == "".join(self.words[i].originalWord): # If the user has entered the correct original word
                        self.shatterSound.play() # Play the shatter sound
                        self.words[i].shatter() # Call for the "correct" word to be shattered, and move offscreen

                if self.words[i].offScreen or not (self.words[i].active): # If words go offsreen or are not active
                    if self.words[i].offScreen: # If they are offscreen
                        self.decrementLives() # Decrement lives
                    if not (self.words[i].active): # If they are inactive ("cleared")
                        self.incrementWordsCleared() # Increment wordsClaered
                        self.incrementScore(
                            10 * len(self.words[i].originalWord) + 5 * self.words[i].swaps + 15 * self.words[i].deletions) # Increment score by 10 fore each letter, 5 for each swap, an 15 for each deletion
                    del self.words[i] # Delete the now inactive words

            # draw images
            for currWord in self.words: # For each current word
                currWord.draw(self.screen, self.images) # Draw the word on the screen using the correct sprites

            # refresh selected input
            self.selectedInput = ""

            if self.hurt: # If a word gets to the bottom (self is hurt)

                if self.hurtFrameCount >= 8: # If It's been hurting for 8 or mor frames
                    self.hurtAlpha -= 20 # Decrease the hurt Alpha
                else: # Otherwise
                    self.hurtAlpha += 20 # Increase the hurt alpha

                hurtSurface = pygame.Surface((1000, 530)) # Instantiate the hurtSurface
                hurtSurface.set_alpha(self.hurtAlpha) # Set the surface's Alpha
                hurtSurface.fill((255, 0, 0)) # Color red
                self.screen.blit(hurtSurface, (0, 0)) # Flash red
                self.hurtFrameCount += 1 # Increase count of frames
                if self.hurtFrameCount > 15: # After 15 frames

                    self.hurt = False # End the hurt flag
                    self.hurtFrameCount = 0 # Return hurtFrameCount to default 0
                    self.hurtAlpha = 0 # Return urtAlpha to default 0

                    if self.lives <= 0: # If the player is now out of lives
                        self.gameState = 1 # Set the game state to 1 (game over)


            # The following is text relevant to the display for the user

            # Fill in the bottom in black
            pygame.draw.rect(self.screen, (0, 0, 0), (0, 530, 1000, 70))

            # Draw a white line above this black bottom
            pygame.draw.rect(self.screen, (255, 255, 255), (0,530, 1000, 2))

            # Instantiate some of the correct font in relevant sizes
            fontDisp = pygame.font.Font('freesansbold.ttf', 25)
            fontType = pygame.font.Font("freesansbold.ttf", 60)

            # Create text to be placed in the display
            currentLevelDisplay = fontDisp.render("LEVEL " + str(self.level), True, (255, 255, 255), (0, 0, 0))
            typingDisplay = fontType.render(self.inputStream, True, (127, 255, 127), (0, 0,0))
            scoreDisplay = fontDisp.render("SCORE: " + str(self.score), True, (255,255,255), (0,0,0))

            # Display the created text
            self.screen.blit(currentLevelDisplay, (10,540))
            self.screen.blit(scoreDisplay, (10, 570))
            self.screen.blit(typingDisplay, ((500-((typingDisplay.get_rect().width)/2)), 540))

            # For each life that the user currently has
            for i in range(self.lives):
                self.screen.blit(self.heartSprite, (820 + 34*i, 552)) # Place the heart sprites in the correct places

        elif self.gameState == 1: # If the gameState is game over

            # game over screen
            self.screen.fill((0, 0, 0)) # Clear the screen

            # Create game over text
            gameOverText = pygame.font.Font('freesansbold.ttf', 70).render('GAME OVER', True, (255, 255, 255), (0, 0, 0))
            levelText = pygame.font.Font('freesansbold.ttf', 50).render("LEVEL " + str(self.level), True, (255, 255, 255), (0, 0, 0))
            scoreText = pygame.font.Font('freesansbold.ttf', 50).render("YOUR SCORE: " + str(self.score), True, (255, 255, 255), (0, 0, 0))
            finalText = pygame.font.Font('freesansbold.ttf', 50).render("PRESS ENTER TO CONTINUE", True, (255, 255, 255), (0, 0, 0))

            # Impose game over text
            self.screen.blit(gameOverText, ((500 - ((gameOverText.get_rect().width) / 2)), 100))
            self.screen.blit(levelText, ((500 - ((levelText.get_rect().width) / 2)), 290))
            self.screen.blit(scoreText, ((500 - ((scoreText.get_rect().width) / 2)), 350))
            self.screen.blit(finalText, ((500 - ((finalText.get_rect().width) / 2)), 500))

            # If enter is pressed
            if self.enterPressed:
                if self.score > int(self.highScores[9]): # Check if there is a new high score
                    self.gameState = 2 # If there is a new high score, go to the highScore screen
                else: # If there is no high score
                    self.running = False # Set the running flag to False, returning to main menu

            self.enterPressed = False # Reset the enterPressed flag

        elif self.gameState == 2: # If gameState is 2, that is 'High Score"

            # Copy the current score to a string
            scoreAdd = str(self.score)

            # Format the string so that it is 5 digits or more
            while len(scoreAdd) < 5:
                scoreAdd = "0" + scoreAdd

            # Clear the screen
            self.screen.fill((0, 0, 0))

            # Instantiate final instructions, both High Score and input
            finalInstruction = pygame.font.Font("freesansbold.ttf", 35).render("YOU GOT A HIGH SCORE! ENTER YOUR NAME!", True, (255, 255, 255), (0,0,0))
            finalDisplay = pygame.font.Font("freesansbold.ttf", 60).render(self.inputStream, True, (127, 255, 127), (0, 0, 0))

            # Place final texts on the screen
            self.screen.blit(finalInstruction, ((500 - ((finalInstruction.get_rect().width) / 2)), 300))
            self.screen.blit(finalDisplay, ((500 - ((finalDisplay.get_rect().width) / 2)), 540))

            # Once enter is pressed (When the user is done with their name)
            if self.enterPressed:

                # Check which score the player has beat, put their score in that place


                if self.score > int(self.highScores[1]):
                    self.highScores.insert(0, self.selectedInput)
                    self.highScores.insert(1, scoreAdd)

                elif self.score > int(self.highScores[3]):
                    self.highScores.insert(2, self.selectedInput)
                    self.highScores.insert(3, scoreAdd)

                elif self.score > int(self.highScores[5]):
                    self.highScores.insert(4, self.selectedInput)
                    self.highScores.insert(5, scoreAdd)

                elif self.score > int(self.highScores[7]):
                    self.highScores.insert(6, self.selectedInput)
                    self.highScores.insert(7, scoreAdd)

                elif self.score > int(self.highScores[9]):
                    self.highScores.insert(8, self.selectedInput)
                    self.highScores.insert(9, scoreAdd)


                # Delete the lowest score, which is now # 6
                del self.highScores[11]
                del self.highScores[10]

                # Add these scores to the text document to store them
                Init.addHighScores(self.highScores)

                # Set the running flag to false, returning to the main menu
                self.running = False
