
from random import randint

class Word :

    def __init__(self, wordString, speed):

        self.wordString = wordString
        self.x = randint(0, 1000)
        self.y = 0
        self.dy = speed


    def update(self):
        self.y += self.dy
        if self.y > 600 :
            destroy()

