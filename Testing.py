import pygame

<<<<<<< HEAD
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
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    screen.fill((0, 0, 0))
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

    pygame.display.flip()
    clock.tick(60)
>>>>>>> a101cc1292000df6dc2cc878495ded60d6e4600a
