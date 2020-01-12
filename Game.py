import pygame

#TODO
pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()


class Game:

    def __init__(self, level, screen, heartSprite, wordsCleared, score, entry, lives):
        self.level = level
        self.wordsCleared = wordsCleared
        self.screen = screen
        self.heartSprite = heartSprite
        self.score = score
        self.entry = entry
        self.lives = lives


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

    def draw(self):

        pygame.draw.rect(screen, (255, 255, 255), (0,530, 1000, 2))

        fontDisp = pygame.font.Font('freesansbold.ttf', 25)
        fontType = pygame.font.Font("freesansbold.ttf", 60)
        currentLevelDisplay = fontDisp.render("LEVEL " + str(self.level), True, (255, 255, 255), (0, 0, 0))
        typingDisplay = fontType.render(self.entry, True, (127, 255, 127), (0, 0,0))
        scoreDisplay = fontDisp.render("SCORE: " + str(self.score), True, (255,255,255), (0,0,0))

        self.screen.blit(currentLevelDisplay, (10,540))
        self.screen.blit(scoreDisplay, (10, 570))
        self.screen.blit(typingDisplay, ((500-((typingDisplay.get_rect().width)/2)), 540))

        for i in range(self.lives):
            self.screen.blit(self.heartSprite, (820 + 34*i, 552))



filename = "Heart/heart.png"
heart = pygame.transform.scale(pygame.image.load(filename), (30, 30))
game = Game(1, screen, heart, 0, 99999, "I TYPED THIS", 5)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    game.draw()
    pygame.display.flip()
    clock.tick(60)