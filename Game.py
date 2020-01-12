import pygame
import random
from Word import Word
import Init
import math

pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
scoreNameString = ""


class Game:

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


    def setLevel(self,newLevel):
        self.level = newLevel

    def incrementLevel(self):
        self.level += 1
        self.levelUpSound.play()

    def incrementWordsCleared(self):
        self.wordsCleared += 1
        if self.wordsCleared >= 20:

            self.incrementLevel()
            self.wordsCleared = 0

    def decrementLives(self):
        self.hurt = True
        self.lives -= 1
        self.loseLifeSound.play()

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

    def toggleEnter(self):
        if self.gameState == 1 or self.gameState == 2:
            self.enterPressed = True


    def loop_game(self):
        global scoreNameString
        screen.fill((0, 0, 0))

        # normal game loop

        if self.gameState == 0:

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
                        self.shatterSound.play()
                        self.words[i].shatter()

                if self.words[i].offScreen or not (self.words[i].active):
                    if self.words[i].offScreen:
                        self.decrementLives()
                    if not (self.words[i].active):
                        self.incrementWordsCleared()
                        self.incrementScore(
                            10 * len(self.words[i].originalWord) + 5 * self.words[i].swaps + 15 * self.words[i].deletions)
                    del self.words[i]

            # draw images
            for currWord in self.words:
                currWord.draw(screen, self.images)

            # refresh selected input
            self.selectedInput = ""

            # draw hurt animation
            if self.hurt:

                if self.hurtFrameCount >= 8:
                    self.hurtAlpha -= 20
                else:
                    self.hurtAlpha += 20

                hurtSurface = pygame.Surface((1000, 530))
                hurtSurface.set_alpha(self.hurtAlpha)
                hurtSurface.fill((255, 0, 0))
                screen.blit(hurtSurface, (0, 0))
                self.hurtFrameCount += 1
                if self.hurtFrameCount > 15:

                    self.hurt = False
                    self.hurtFrameCount = 0
                    self.hurtAlpha = 0

                    if self.lives <= 0:
                        self.gameState = 1

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

        elif self.gameState == 1:

            # game over screen
            screen.fill((0, 0, 0))

            gameOverText = pygame.font.Font('freesansbold.ttf', 70).render('GAME OVER', True, (255, 255, 255), (0, 0, 0))
            levelText = pygame.font.Font('freesansbold.ttf', 50).render("LEVEL " + str(self.level), True, (255, 255, 255), (0, 0, 0))
            scoreText = pygame.font.Font('freesansbold.ttf', 50).render("YOUR SCORE: " + str(self.score), True, (255, 255, 255), (0, 0, 0))
            finalText = pygame.font.Font('freesansbold.ttf', 50).render("PRESS ENTER TO CONTINUE", True, (255, 255, 255), (0, 0, 0))
            self.screen.blit(gameOverText, ((500 - ((gameOverText.get_rect().width) / 2)), 130))
            self.screen.blit(levelText, ((500 - ((levelText.get_rect().width) / 2)), 340))
            self.screen.blit(scoreText, ((500 - ((scoreText.get_rect().width) / 2)), 400))
            self.screen.blit(finalText, ((500 - ((finalText.get_rect().width) / 2)), 550))

            if self.enterPressed:
                if self.score > int(self.highScores[9]):
                    self.gameState = 2
                else:
                    self.running = False

            self.enterPressed = False

        elif self.gameState == 2:

            # score screen

            scoreAdd = str(self.score)

            while len(scoreAdd) < 5:
                scoreAdd = "0" + scoreAdd

            screen.fill((0, 0, 0))


            finalInstruction = pygame.font.Font("freesansbold.ttf", 70).render("YOU GOT A HIGH SCORE! ENTER YOUR NAME!", True, (255, 255, 255), (0,0,0))
            finalDisplay = pygame.font.Font("freesansbold.ttf", 60).render(self.inputStream, True, (127, 255, 127), (0, 0, 0))
            screen.blit(finalInstruction, ((500 - ((finalInstruction.get_rect().width) / 2)), 300))
            screen.blit(finalDisplay, ((500 - ((finalDisplay.get_rect().width) / 2)), 540))

            if self.enterPressed:

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

                del self.highScores[11]
                del self.highScores[10]

                Init.addHighScores(self.highScores)

                self.running = False





