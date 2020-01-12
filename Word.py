
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

        if self.active :
            self.y += self.dy
            if self.y > 530 :
                self.offScreen = True

    def draw(self, screen, images):

        if self.active :
            characters = self.scrambledWord
            for i in range(len(characters)):
                screen.blit(images[characters[i]], (self.x + 30 * i, self.y))