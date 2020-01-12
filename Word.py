
from random import randint


class Word :

    # initialize object
    # set x and y positions, set word, set speed
    def __init__(self, originalWord, speed, swaps, deletions):

        # inintialize variables
        self.originalWord = list(originalWord)
        self.scrambledWord = list(originalWord)
        self.swaps = swaps
        self.deletions = deletions
        self.x = randint(0, 1000 - (30 * len(originalWord)))
        self.y = -25
        self.dy = speed
        self.active = True
        self.offScreen = False

        # shatter animation variables
        self.shatterFrameCount = 0
        self.shattering = False
        self.shatterAngles = []

        length = len(originalWord)

        # execute swaps
        for i in range(swaps) :
            swapPos1 = randint(0, length - 1)
            swapPos2 = randint(0, length - 1)
            temp = self.scrambledWord[swapPos1]
            self.scrambledWord[swapPos1] = self.scrambledWord[swapPos2]
            self.scrambledWord[swapPos2] = temp

        # execute deletions
        for i in range(deletions) :
            deletePos = randint(0, length - 1)
            self.scrambledWord[deletePos] = "_"


    # should be called every frame before render
    # updates y position, if off sreen, sets active to "false"
    def update(self):

        if self.active and not(self.shattering):
            self.y += self.dy
            if self.y > 530 :
                self.offScreen = True

    def shatter(self):
        characters = self.scrambledWord
        for i in range(len(characters)):
            self.shatterAngles.append([randint(-5, 5), randint(-5, 5)])
        self.shattering = True

    def draw(self, screen, images):

        if self.active and not (self.shattering):
            characters = self.scrambledWord
            for i in range(len(characters)):
                screen.blit(images[characters[i]], (self.x + 30 * i, self.y))

        if self.shattering:
            if self.shatterFrameCount <= 10:
                characters = self.scrambledWord
                for i in range(len(self.shatterAngles)):
                    screen.blit(images[characters[i]], (
                    self.x + 30 * i + self.shatterAngles[i][0] * self.shatterFrameCount * 10,
                    self.y + self.shatterAngles[i][1] * self.shatterFrameCount * 10))
                self.shatterFrameCount += 1
            else:
                self.shattering = False
                self.active = False