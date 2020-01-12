import pygame

#TODO
screen = pygame.display.set_mode((1000, 600))


class Game:

    def __init__(self, level, screen, wordsCleared = 0):
        self.level = level
        self.wordsCleared = wordsCleared
        self.screen = screen


    def setLevel(self,newLevel):
        self.level = newLevel

    def incrementLevel(self):
        self.level += 1

    def incrementWordsCleared(self):
        self.wordsCleared += 1
        if self.wordsCleared >= 20:

            self.incrementLevel()
            self.wordsCleared = 0



    def draw(self, varString = "", score = 0):
        fontDisp = pygame.font.Font("freesansbold.ttf", 25)
        fontType = pygame.font.Font("freesansbold.ttf", 35)
        currentLevelDisplay = fontDisp.render("LEVEL " + str(self.level), True, (255, 255, 255), (255, 100, 0))
        typingDisplay = fontType.render(varString, True, (127, 255, 127), (255, 100,0))
        scoreDisplay = fontDisp.render("SCORE: " + str(score), True, (255,255,255), (255,100,0))

        self.screen.blit(currentLevelDisplay, (10,565))

game = Game(1, screen, 0)

game.draw()
