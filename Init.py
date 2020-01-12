import random
import pygame
# Import relevant libraries

#####
#
# Init.py holds a number of functions which are used to intialize various arrays of data and to begin the game before the
# user is allowed to interact with it. This includes gathering data from relevant text files, loading relevant images
# with the pygame library, and for iterating through arrays of data to generate random words
#
#####


def createHighScores():
    # This function opens the HighScore.txt text file and places the lines within it in an array to display high scores on
    # the main menu and to add new high scores if one is achieved

    highScores = [] # Initialize the final array
    highScoreFile = open("HighScore.txt") # Open the relevant file
    highScores = highScoreFile.readlines() # Convert contents of the file to an arary
    highScoreFile.close() # close the file
    for i in range(len(highScores)): # For each entry in this array
        highScores[i] = highScores[i].strip() # Strip away all white space

    # Return the final array
    return highScores

def addHighScores(listOfScores):
    # This function takes an argument of an array of scores, updated after the game has been played and a new high score
    # has been achieved, this will update the text file, so that the scores are stored between runs of the game.

    highScoreFile = open("HighScore.txt", "w") # Open the file in write mode
    for i in listOfScores: # For every entry in the relevant list
        highScoreFile.write(i) # Write the entry
        highScoreFile.write("\n") # Write a newline
    highScoreFile.close() # Close the file

def createData():
    # This function takes the text files of dictionary words, already separated by length, and converts them into an
    # array of arrays by size

    arrayOfOrderedWords = [] # Initialize the final array
    for name in range(3,9): # loop through the integers which are the names of the files
        filename = "WordLists/" + str(name) +".txt" # delcare the filename string based on those ints
        openedFile = open(filename) # Open the file
        arrayOfOrderedWords.append(openedFile.readlines()) # Append an array of that files' contents to the main array
        openedFile.close() # Close the file

    for list in arrayOfOrderedWords: # For each array in the main array
        for i in range(len(list)): # For each string in that list
            word = list[i].strip() # Strip whitespace
            word = word.upper() # Make all character uppercase
            list[i] = word # Store the value back into the array

    return arrayOfOrderedWords # Return the main array

def pickWord(arrayOfOrderedWords, length):
    # This function passes the ordered array and a given length value, and returns a random entry within the array of
    # given length within the ordered array

    if length > 8 : # Check if the length is given as greater than 8
        length = 8 # If so, set it to 8, which are the longest words available

    chosenListIndex = length - 3 # Decrement the length by 3, as the words are lengths 3-8, but are indexed at 0-5
    chosenWordIndex = random.randint(0,len(arrayOfOrderedWords[chosenListIndex])-1) # Select a random entry inside of the correct array

    chosenWord = arrayOfOrderedWords[chosenListIndex][chosenWordIndex] # Define a string of the chosen word

    return chosenWord # return the chosen word


def loadHeart():
    # This function loads the heart or life sprite used in the game

    filename = "Heart/heart.png" # Define the filepath of the image
    heartSprite = pygame.transform.scale(pygame.image.load(filename), (30, 30)) # Load the image with pygame

    return heartSprite # Return the loaded image

def loadImages():
    # This function loads the text sprites which fall from the top of the screen
    imagesDict = {} # Declare and empty dictionary
    textArray = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"] # Declare an array of the correct character

    for i in textArray: # For each character that maps to a file
        filename = "Sprites/" + i + ".png" # Find the name of that file
        imagesDict[i] = pygame.transform.scale(pygame.image.load(filename), (25, 25)) # load that file with pygame, and store the loaded image in the dictionary with the correct index

    return imagesDict # Return the relevant dictionary
