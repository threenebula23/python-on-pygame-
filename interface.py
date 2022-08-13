import instruments as ins
import pygame
import time
import sys

def difficult():
    pygame.init()

    easy = 1.5 
    normal =1 
    hard =0.75

    screen = pygame.display.set_mode((400, 320))
    screen.fill((0,157,204))

    font = pygame.font.SysFont('ariel', 60)
    text = font.render('СЛОЖНОСТЬ:', True , 'white')
    screen.blit(text, (50, 20))

    r = pygame.Rect(50, 80, 300, 60)
    pygame.draw.rect(screen, (72, 209, 0), r, 0)

    font = pygame.font.SysFont('ariel', 60)
    text = font.render('ЛЕГКО', True , 'white')
    screen.blit(text, (120, 90))

    r = pygame.Rect(50, 160, 300, 60)
    pygame.draw.rect(screen, (200, 209, 0), r, 0)

    font = pygame.font.SysFont('ariel', 59)
    text = font.render('НОРМАЛЬНО', True , 'white')
    screen.blit(text, (65, 170))

    r = pygame.Rect(50, 240, 300, 60)
    pygame.draw.rect(screen, (242, 0, 0), r, 0)

    font = pygame.font.SysFont('ariel', 59)
    text = font.render('СЛОЖНО', True , 'white')
    screen.blit(text, (105, 250))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if event.button == 1:
                    x_click = event.pos[0]
                    y_click = event.pos[1]
                    
                    if x_click >= 50 and x_click <= 350:

                        if y_click >= 80 and y_click <= 140:
                            pygame.quit()
                            game(easy)

                        elif y_click >= 160 and y_click <= 220:
                            pygame.quit()
                            game(normal)

                        elif y_click >= 240 and y_click <= 300:
                            pygame.quit()
                            game(hard)

        pygame.display.flip()

def game(difficult):
    screen = pygame.display.set_mode((700, 800))
    worker = ins.Main(screen,difficult)
    worker.refresh()
    pause_status = False

    worker.movement()
            

    pygame.display.flip()
