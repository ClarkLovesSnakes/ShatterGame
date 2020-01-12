from random import randint
# Import relevant library

#####
#
# Word.py holds the data behind the word objects, such as how they are scrambled, have their letters deleted, and how they move
#
#####

# Create a Word class
class Word :

    # Initialize the Word object, with the unscrambled word, its speed, the number of swaps it will recieve, and the number of deletions
    def __init__(self, originalWord, speed, swaps, deletions):

        # inintialize variables
        self.originalWord = list(originalWord)
        self.scrambledWord = list(originalWord)
        self.swaps = swaps
        self.deletions = deletions
        # Define the starting x as some point on screen, but randomly horizontal
        self.x = randint(0, 1000 - (30 * len(originalWord)))
        # Define the starting y as a point slighlty above the screen
        self.y = -25
        # Define the speed value as dy
        self.dy = speed
        self.active = True
        self.offScreen = False

        # shatter animation variables
        self.shatterFrameCount = 0
        self.shattering = False
        self.shatterAngles = []

        length = len(originalWord)

        # execute swaps
        for i in range(swaps): # For the number of swaps
            swapPos1 = randint(0, length - 1) # Choose one position in the word
            swapPos2 = randint(0, length - 1) # Choose a second position
            temp = self.scrambledWord[swapPos1] # Store the first scrambled character
            self.scrambledWord[swapPos1] = self.scrambledWord[swapPos2] # Set the first scrambled character to the second
            self.scrambledWord[swapPos2] = temp # Set the second scrambled character to the first

        # execute deletions
        for i in range(deletions): # For the number of deltions
            deletePos = randint(0, length - 1) # Find a random position in the word
            self.scrambledWord[deletePos] = "_" # Change that position to an underscore


    def update(self):
        # This function checks if the word is allowed to move (active and not in the process of dying)

        if self.active and not(self.shattering): # If the word is still allowed to move
            self.y += self.dy # Add the sped to the y position
            if self.y > 530 : # If the word is now offscreen
                self.offScreen = True # Set the offScreen flag to True

    def shatter(self):
        # This function prepares the data to allow for the word object to undergo the shatter animation
        characters = self.scrambledWord # Get the length of the words
        for i in range(len(characters)): # For each character
            self.shatterAngles.append([randint(-5, 5), randint(-5, 5)]) # Choose a random vector for the character
        self.shattering = True # Set the shattering flag to True

    def draw(self, screen, images):
        #This function governs the overall animation of the word

        # If the word is active and not animating
        if self.active and not (self.shattering):
            characters = self.scrambledWord # Get all the characters
            for i in range(len(characters)): # For each character
                screen.blit(images[characters[i]], (self.x + 30 * i, self.y)) # Put the characters on the screen in the proper order in the right places

        if self.shattering: # If the shattering animation is running
            if self.shatterFrameCount <= 10: # If the word has been shattering for 10 or fewer frames
                characters = self.scrambledWord
                for i in range(len(self.shatterAngles)): # For each character
                    screen.blit(images[characters[i]], (
                    self.x + 30 * i + self.shatterAngles[i][0] * self.shatterFrameCount * 10, # Place the characters on the screen moving at various directions governened by shatterAngles
                    self.y + self.shatterAngles[i][1] * self.shatterFrameCount * 10))
                self.shatterFrameCount += 1 # Increment the frame count
            else: # If the word has been shattering for more than 10 frames
                self.shattering = False # Set the shattering flag to False
                self.active = False # Set the active flag to salve