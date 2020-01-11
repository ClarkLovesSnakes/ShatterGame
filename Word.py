
from random import randint


class Word :

    # initialize object
    # set x and y positions, set word, set speed
    def __init__(self, wordString, speed):

        self.wordString = wordString
        self.x = randint(0, 1000)
        self.y = 0
        self.dy = speed
        self.active = True

    # should be called every frame before render
    # updates y position, if off sreen, sets active to "false"
    def update(self):

        self.y += self.dy
        if self.y > 600 :
            self.active = False
