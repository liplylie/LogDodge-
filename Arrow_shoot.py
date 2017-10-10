import pygame
import random 

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
brown = (165,42,42)
gray = (211,211,211)
light_gray =(225,225,225)
green = (0,255,0)
light_blue = (73,216,230)


gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Log Dodge')

font = pygame.font.SysFont(None, 25)


pygame.display.update()

clock = pygame.time.Clock()


def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [800/2,600/2])

def gameLoop():
    gameExit = False
    gameOver = False 

    #arrow loop count
    arrow_count = 0
    arrow_h_count = 0
    #user sprite default position
    lead_x = 400
    lead_y = 550
    lead_x_change = 0
    lead_y_change = 0
    #arrow 1
    arrow_x = random.randrange(0,800,100)
    arrow_y = -110
    arrow_y_change = 10
    #arrow 2
    arrow_x_2 = random.randrange(0,800,100)
    arrow_y_2 = -110
    arrow_y_change_2 = 10
    #arrow 3 horizontal (h)

    arrow_x_h = -100
    arrow_y_h = random.randrange(0,600,100)
    arrow_x_change_h = 10


    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit.", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit= True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -10
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = 10
                elif event.key == pygame.K_DOWN:
                    lead_y_change = -10
                elif event.key == pygame.K_UP:
                    lead_y_change = 10
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    lead_y_change = 0
            #arrow reset and speed up 
        if arrow_y >= 600:
            arrow_y = -110
            arrow_x = random.randrange(1,800,100)
            arrow_y_change += .5
            arrow_count +=1
            #add arrow v 2
        if arrow_count > 3:
            arrow_y_2 += arrow_y_change_2
        #arrow v 2 reset
        if arrow_y_2 >= 600:
            arrow_y_2 = -110
            arrow_x_2 = random.randrange(1,800,100)
            arrow_y_change_2 += .5
            arrow_h_count += 1
        #add arrow h sprite
        if arrow_h_count > 3:
            arrow_x_h += arrow_x_change_h
        #arrow h reset
        if arrow_x_h >= 800:
            arrow_x_h = -10
            arrow_y_h = random.randrange(1,600,100)
            arrow_x_change_h += .5
            #arrow_h_count += 1
        
            
         
            
        #user boundaries
        if lead_x >=760:
            lead_x = 760
        elif lead_x <= 10:
            lead_x = 10
        elif lead_y >=560:
            lead_y = 560
        elif lead_y <= 20:
            lead_y = 20
            

        lead_x += lead_x_change
        lead_y -= lead_y_change
        print(arrow_x, 'arrow_x')
        print (lead_x, 'lead_x')
        print(arrow_y, 'arrow_y')
        print(lead_y, 'lead_y')
        arrow_y += arrow_y_change
        gameDisplay.fill(light_blue)
        #user sprite
        pygame.draw.rect(gameDisplay, brown, [lead_x,lead_y,30,30])
        pygame.draw.rect(gameDisplay, green, [(lead_x) + 10,(lead_y) - 10,10,10])
        #arrow v sprite
        pygame.draw.rect(gameDisplay, brown, [arrow_x, arrow_y, 20, 100])
        pygame.draw.rect(gameDisplay, gray, [arrow_x, (arrow_y) + 100,20,10])
            # arrow tip. not needed. pygame.draw.rect(gameDisplay, light_gray, [(arrow_x) + 5, (arrow_y) + 110,10,5])
        #arrow v 2 sprite
        pygame.draw.rect(gameDisplay, brown, [arrow_x_2, arrow_y_2, 20, 100])
        pygame.draw.rect(gameDisplay, gray, [arrow_x_2, (arrow_y_2) + 100,20,10])
            #pygame.draw.rect(gameDisplay, light_gray, [(arrow_x_2) + 5, (arrow_y_2) + 110,10,5])
        #arrow h sprite
        pygame.draw.rect(gameDisplay, brown, [arrow_x_h, arrow_y_h, 100, 20])
        pygame.draw.rect(gameDisplay, gray, [(arrow_x_h), (arrow_y_h),10,20])
            #pygame.draw.rect(gameDisplay, light_gray, [(arrow_x_h) - 5, (arrow_y_h) +5,5,10])

        pygame.display.update()

        
        #collision
        if lead_x > arrow_x - 30 and lead_x < arrow_x + 20 and lead_y > arrow_y - 110 and not lead_y > arrow_y + 111:
            gameOver = True
        if lead_x >= arrow_x_2 - 30 and lead_x < arrow_x_2 + 20 and lead_y >= arrow_y_2 - 110 and not lead_y > arrow_y_2 + 111:
            gameOver = True
        if lead_x >= arrow_x_h - 30 and not lead_x < arrow_x_h + 200 and lead_y >= arrow_y_h - 110 and not lead_y > arrow_y_h + 111:
            gameOver = True

         
        clock.tick(15)
    


    pygame.quit()
    quit()

gameLoop()
