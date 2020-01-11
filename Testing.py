import pygame
#import pygame.sprite.Sprite as Sprite

class Game:
    def __init__(self):
        pass





def main():

    pygame.init()
    pygame.display.set_caption("test")
    screen = pygame.display.set_mode((1920,1080))
    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False

main()


for i in range(10):
    print(i)

print("Elijah's Test")
