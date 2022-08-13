import pygame
import time
import sys
import random

class Main:
    def __init__(self,screen, difficult):
        pygame.init()
        self.difficult = difficult
        self.screen =screen
        self.score = 1

        head = pygame.image.load('date/head.png').convert_alpha()
        self.head = pygame.transform.scale(head, (50, 50))

        body = pygame.image.load('date/body.png').convert_alpha()
        self.body = pygame.transform.scale(body, (50, 50))

        back = pygame.image.load('date/back.png').convert_alpha()
        self.back = pygame.transform.scale(back, (50, 50))

        apple = pygame.image.load('date/apple.png').convert_alpha()
        self.apple = pygame.transform.scale(apple, (50, 50)) 

        esc = pygame.image.load('date/esc.png').convert_alpha()
        self.esc = pygame.transform.scale(esc, (75, 75)) 

        self.length = [(6,9,0),(6,10, 270 ),(5,10,270)]
        self.corg_apple = (6,6)
        self.x_cord = 14
        self.y_cord = 14
        self.pause_status = False
        self.side = 0



    def pause(self):
        if self.pause_status == False:
            self.pause_status = True

            self.screen.fill(( 0 ,68, 0 ))

            font = pygame.font.SysFont('ariel', 60)
            text = font.render('ПАУЗА', True , 'white')

            self.screen.blit(text, (65, 170))
            pygame.display.flip()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                    elif event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_ESCAPE:
                            self.pause_status = False
                            return
                    pygame.display.flip()

    
    def tab(self):
        r = pygame.Rect(0, 0, 800, 100)
        pygame.draw.rect(self.screen, (0, 0, 0), r, 0)
        
        font = pygame.font.SysFont('ariel', 59)
        text = font.render('СЧЕТ: '+str(self.score), True , 'white')
        self.screen.blit(text, (500, 50))

        self.screen.blit(self.esc , (25, 15))

        font = pygame.font.SysFont('ariel', 59)
        text = font.render('ПАУЗА', True , 'white')
        self.screen.blit(text, (125, 50))


    def graund(self):
        for x in range(self.x_cord):
            for y in range(self.y_cord):
                r = pygame.Rect(2*(y* 50),2*(x *50) +100, 50, 50)
                pygame.draw.rect(self.screen, (72, 230, 0), r, 0)

                r = pygame.Rect( 2 * (y * 50)+  50, 2 * (x * 50) + 50 +100, 50, 50)
                pygame.draw.rect(self.screen, (72, 230, 0), r, 0)

    def refresh(self):
        self.screen.fill((55,178,0))
        self.graund()
        self.tab()
        for i in range(len(self.length)):
            if i == 0 :
                image = self.head
            elif i == len(self.length)-1:
                image =self.back
            else:
                image = self.body
            
            if self.length[i][2] == 0:
                image = pygame.transform.rotate(image, 0)
            
            elif self.length[i][2] == 270:
                image = pygame.transform.rotate(image, 270)
            
            elif self.length[i][2] == 90:
                image = pygame.transform.rotate(image, 90)
            
            elif self.length[i][2] == 180:
                image = pygame.transform.rotate(image, 180)

            self.screen.blit(image,(self.length[i][0] * 50 ,self.length[i][1] * 50 + 100))
            self.screen.blit(self.apple,(self.corg_apple[0] * 50 ,self.corg_apple[1] * 50 + 100))

        pygame.display.flip()
        return

    def movement(self):
        sleep = 0
        clock = pygame.time.Clock()
        self.refresh()
        
        while True:
            
            for event in pygame.event.get():
                    
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.side = 0
                            
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.side = 90

                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.side = 180

                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.side = 270
                        
                    elif event.key == pygame.K_ESCAPE:
                        self.pause()
                        sleep = 1

                else:
                    break
            if sleep == 0:
                self.chanchess()
            self.refresh()
            sleep = 0
            clock.tick(self.difficult)



                            
    def chanchess(self):

        move = self.length
        if self.length[0][2] - self.side != 180 and self.length[0][2] - self.side != -180:
            for i in reversed(range(len(self.length))):
                if i == 0:
                    if self.side == 0 :
                        new = ( self.length[0][0] , self.length[0][1] - 1 , self.side)
                    elif self.side == 180 :
                        new = ( self.length[0][0] , self.length[0][1] + 1 , self.side)
                    elif self.side == 90 :
                        new = ( self.length[0][0] - 1 , self.length[0][1] , self.side)
                    else:
                        new = ( self.length[0][0] + 1 , self.length[0][1] , self.side)
            self.length = move
            self.length.insert(0, new)

            if self.corg_apple == (self.length[0][0] , self.length[0][1]):
                self.score +=1
                self.spawn_apple()
            else:
                self.length.pop(len(self.length)-1)
            self.proverka()


    def proverka(self):
        if self.length[0][0] >= 14 :
            self.lose()
        elif self.length[0][0] < 0:
            self.lose()
        elif self.length[0][1] >= 14 :
            self.lose()
        elif self.length[0][1] < 0:
            self.lose()
        else:
            for index in reversed(range(1 , len(self.length))):
                if (self.length[0][0], self.length[0][1]) == (self.length[index][0], self.length[index][1]):
                    self.lose()



    def spawn_apple(self):
        all_free =[]
        for x in range(14):
            for y in range(14):
                for i in range(len(self.length)):
                    if (x , y) != ( self.length[0], self.length[1]):
                        all_free.append((x,y))
        self.corg_apple = all_free[random.randint(0 , len(all_free)-1)]

        
                                    
                        

    def lose(self):
        while True:
            self.screen.fill(( 224, 0 , 0 ))

            font = pygame.font.SysFont('ariel', 60)
            text = font.render('ПРОИГРЫШ', True , 'white')
            self.screen.blit(text, (65, 170))

            font = pygame.font.SysFont('ariel', 60)
            text = font.render('СЧЁТ: '+ str(self.score), True , 'white')
            self.screen.blit(text, (65, 220))
            pygame.display.flip()
        





        