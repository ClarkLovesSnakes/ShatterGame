import random
import pygame
# Initialize the functions of the game before the game loop begins
# This includes the previous high score and the lists of words

def createHighScores():
    # This will find the high score and keep it set
    highScoreFile = open("HighScore.txt")
    highScores = highScoreFile.readlines()
    return highScores

def createData():
    arrayOfOrderedWords = []
    for name in range(3,6):
        filename = "WordLists/" + str(name) +".txt"
        openedFile = open(filename)
        arrayOfOrderedWords.append(openedFile.readlines())
        openedFile.close()

    for list in arrayOfOrderedWords:
        for i in range(len(list)):
            word = list[i].strip()
            list[i] = word

    return arrayOfOrderedWords

def pickWord(arrayOfOrderedWords, length):
    chosenListIndex = length - 3
    chosenWordIndex = random.randint(0,len(arrayOfOrderedWords[chosenListIndex])-1)

    chosenWord = arrayOfOrderedWords[chosenListIndex][chosenWordIndex]

    return chosenWord


def loadImages():
    imagesDict = {}
    textArray = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"]

    for i in textArray:
        filename = "Sprites/" + i + ".png"
        imagesDict[i] = pygame.transform.scale(pygame.image.load(filename), (25, 25))

    return imagesDict