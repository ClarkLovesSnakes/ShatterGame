import random
import pygame
# Initialize the functions of the game before the game loop begins
# This includes the previous high score and the lists of words

def createHighScores():
    # This will find the high score and keep it set
    highScores = []
    highScoreFile = open("HighScore.txt")
    highScores = highScoreFile.readlines()
    for i in range(len(highScores)):
        highScores[i] = highScores[i].strip()

    #for i in range(0, len(highScoresTemp), 2):
        #highScores.append([highScoresTemp[i], highScoresTemp[i + 1]])
    return highScores

def addHighScores(listOfScores):
    highScoreFile = open("HighScore.txt", "w")
    for i in listOfScores:
        highScoreFile.write(i)
        highScoreFile.write("\n")
    highScoreFile.close()

def createData():
    arrayOfOrderedWords = []
    for name in range(3,9):
        filename = "WordLists/" + str(name) +".txt"
        openedFile = open(filename)
        arrayOfOrderedWords.append(openedFile.readlines())
        openedFile.close()

    for list in arrayOfOrderedWords:
        for i in range(len(list)):
            word = list[i].strip()
            word = word.upper()
            list[i] = word

    return arrayOfOrderedWords

def pickWord(arrayOfOrderedWords, length):

    if length > 5 :
        length = 5

    chosenListIndex = length - 3
    chosenWordIndex = random.randint(0,len(arrayOfOrderedWords[chosenListIndex])-1)

    chosenWord = arrayOfOrderedWords[chosenListIndex][chosenWordIndex]

    return chosenWord


def loadHeart():
    filename = "Heart/heart.png"
    heartSprite = pygame.transform.scale(pygame.image.load(filename), (30, 30))

    return heartSprite

def loadImages():
    imagesDict = {}
    textArray = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"]

    for i in textArray:
        filename = "Sprites/" + i + ".png"
        imagesDict[i] = pygame.transform.scale(pygame.image.load(filename), (25, 25))

    return imagesDict