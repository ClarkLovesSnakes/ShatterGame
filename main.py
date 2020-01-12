import pygame

from Game import Game

# initialize
# set screen size

pygame.init()
screen = pygame.display.set_mode((1000, 600))
done = False

clock = pygame.time.Clock()

gameState = 0
gameTime = 0
game = None

heart = pygame.transform.scale(pygame.image.load("Heart/heart.png"), (30, 30))

button1 = [66,133,0]
button2 = [382,133,1]
button3 = [66,366,2]
button4 = [382,366,3]
buttons = [button1,button2,button3,button4]

color = (255, 100, 0)
white = (255, 255, 255)
black = (0, 0, 0)

font = pygame.font.Font('freesansbold.ttf', 50)
text = font.render('SHATTER', True, white, black)
#textRect = text.get_rect()
textRect = [380,25]

text2 = [pygame.font.Font('freesansbold.ttf', 50).render('START', True, white), [110,185]]
text3 = [pygame.font.Font('freesansbold.ttf', 50).render('LEVEL', True, white), [426,185]]
text4 = [pygame.font.Font('freesansbold.ttf', 50).render('ABOUT', True, white), [100,421]]
text5 = [pygame.font.Font('freesansbold.ttf', 50).render('QUIT', True, white), [446,421]]
text6 = [pygame.font.Font('freesansbold.ttf', 35).render('HIGHSCORES', True, white, black), [700,130]]
text7 = [pygame.font.Font('freesansbold.ttf', 20).render('Elijah            5280', True, white, black), [700,200]]
text8 = [pygame.font.Font('freesansbold.ttf', 20).render('Elijah            5223', True, white, black), [700,230]]
text9 = [pygame.font.Font('freesansbold.ttf', 20).render('Elijah            5145', True, white, black), [700,260]]
text10 = [pygame.font.Font('freesansbold.ttf', 20).render('Elijah            4980', True, white, black), [700,290]]
text11 = [pygame.font.Font('freesansbold.ttf', 20).render('Josh              23', True, white, black), [700,320]]
texts = [text2,text3,text4,text5,text6,text7,text8,text9,text10,text11]



while not done:


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        if gameState == 0 :
            if event.type == pygame.MOUSEBUTTONUP:
                for i in buttons:
                    if (mousePos[0] > i[0] and mousePos[0] < i[0] + 250 and mousePos[1] > i[1] and mousePos[1] < i[1] + 150):
                        # start button pressed
                        if i[2] == 0 :
                            game = Game(1, screen, heart, 0, 0, 5)
                            gameState = 1

        if gameState == 1 :
            if event.type == pygame.KEYDOWN:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    game.inputStream = game.inputStream + chr(event.key).upper()
                elif event.key == pygame.K_RETURN:
                    game.selectedInput = game.inputStream
                    game.inputStream = ""
                elif event.key == pygame.K_BACKSPACE :
                    game.inputStream = game.inputStream[:len(game.inputStream) - 1]

    if gameState == 0 :

        gameTime += 1
        gameTime %= 60

        mousePos = pygame.mouse.get_pos()

        screen.fill((0, 0, 0))
        color = (255, 100, 0)

        for i in buttons:
            pygame.draw.rect(screen, color, pygame.Rect(i[0], i[1], 250, 150))
            if (mousePos[0] > i[0] and mousePos[0] < i[0]+250 and mousePos[1] > i[1] and mousePos[1] < i[1]+150) :
                #pygame.draw.rect(screen, [color[0],color[1]+80,color[2]+80], pygame.Rect(i[0], i[1], 250+30, 150+30))
                pygame.draw.rect(screen,[color[0],color[1]+80,color[2]+80], pygame.Rect(i[0], i[1], 250, 150))

        if gameTime < 30:
            screen.blit(text, textRect)
        for i in range(len(texts)):
                screen.blit(texts[i][0], texts[i][1])


    # run game loop
    elif gameState == 1 :

        game.loop_game()


    pygame.display.flip()
    clock.tick(60)
