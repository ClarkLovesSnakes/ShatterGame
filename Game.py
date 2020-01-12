import pygame
import random
from Word import Word
import Init
import math

#TODO
pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()


class Game:

    def __init__(self, level, screen, heartSprite, wordsCleared, score, lives):

        self.level = level
        self.wordsCleared = wordsCleared
        self.screen = screen
        self.heartSprite = heartSprite
        self.score = score
        self.lives = lives

        # game state variables
        self.dictionary = Init.createData()
        self.images = Init.loadImages()
        self.words = []
        self.inputStream = ""
        self.selectedInput = ""
        self.framesSinceLastWord = 0


    def setLevel(self,newLevel):
        self.level = newLevel

    def incrementLevel(self):
        self.level += 1

    def incrementWordsCleared(self):
        self.wordsCleared += 1
        if self.wordsCleared >= 20:

            self.incrementLevel()
            self.wordsCleared = 0

    def decrementLives(self):
        self.lives -= 1
        if self.lives <= 0:
            print("Dead")

    def incrementScore(self, amount):
        self.score += amount

    def defineWordLength(self):
        length = math.floor((3 + (self.level - 1) * 0.5))
        return random.randint(3, length)

    def getWord(self):
        speed = 0.5 * random.randint(1, self.level)
        swaps = 0
        deletions = 0

        isDeletingOne = False
        isDeletingTwo = False

        if self.level >= 10:
            randDelete = random.randint(1,10)
            if randDelete == 10:
                isDeletingOne = True
            elif randDelete == 9:
                isDeletingTwo = True
        elif self.level >= 5:
            randDelete = random.randint(1,10)
            if randDelete == 10:
                isDeletingOne = True

        if isDeletingTwo:
            deletions = 2
        elif isDeletingOne:
            deletions = 1
        else:
            swaps = random.randint(0, self.level)

        return Word(Init.pickWord(self.dictionary, self.defineWordLength()), speed, swaps, deletions)


    def loop_game(self):

        screen.fill((0, 0, 0))

        # update game state

        self.framesSinceLastWord += 1

        if len(self.words) < 5 and self.framesSinceLastWord >= 30:
            self.words.append(self.getWord())
            # self.words.append(Word(Init.pickWord(self.dictionary, 4), 2, 0, 0))
            self.framesSinceLastWord = 0

        for i in range(len(self.words) - 1, -1, -1):

            # update word states
            self.words[i].update()

            # check user input
            if self.selectedInput != "":
                if self.selectedInput == "".join(self.words[i].originalWord):
                    self.words[i].active = False

            if self.words[i].offScreen or not (self.words[i].active):
                if self.words[i].offScreen :
                    self.decrementLives()
                if not (self.words[i].active) :
                    self.incrementWordsCleared()
                    self.incrementScore(10 * len(self.words[i].originalWord) + 5 * self.words[i].swaps + 15 * self.words[i].deletions)
                del self.words[i]

        # draw images
        for currWord in self.words:
            currWord.draw(screen, self.images)

        # refresh selected input
        self.selectedInput = ""


        # conrol panel

        # draw black rectangle
        pygame.draw.rect(screen, (0, 0, 0), (0, 530, 1000, 70))

        pygame.draw.rect(screen, (255, 255, 255), (0,530, 1000, 2))

        fontDisp = pygame.font.Font('freesansbold.ttf', 25)
        fontType = pygame.font.Font("freesansbold.ttf", 60)
        currentLevelDisplay = fontDisp.render("LEVEL " + str(self.level), True, (255, 255, 255), (0, 0, 0))
        typingDisplay = fontType.render(self.inputStream, True, (127, 255, 127), (0, 0,0))
        scoreDisplay = fontDisp.render("SCORE: " + str(self.score), True, (255,255,255), (0,0,0))

        self.screen.blit(currentLevelDisplay, (10,540))
        self.screen.blit(scoreDisplay, (10, 570))
        self.screen.blit(typingDisplay, ((500-((typingDisplay.get_rect().width)/2)), 540))

        for i in range(self.lives):
            self.screen.blit(self.heartSprite, (820 + 34*i, 552))

