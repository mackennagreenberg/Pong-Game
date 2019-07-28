import pygame
pygame.font.init()
import BSL
import sys
pygame.init()
display_width = 1520
display_height = 920
gameDisplay = pygame.display.set_mode((display_width,display_height)) #use variables so we can reference
pygame.display.set_caption("Pong by Mackenna Greenberg (feat. Alex)")


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
currentScreen = BSL.HomeScreen



x = (display_width * 0.45)
y = (display_height * 0.8)
clock = pygame.time.Clock()


currentComputerScore = 0
currentPlayerScore = 0

newPlayerScore = 0
newComputerScore = 0




currentDifficulty = None



font = pygame.font.SysFont('Comic Sans MS',25)
computerScoreText = font.render("Opponent's Score: "+str(newComputerScore), True, black)
playerScoreText = font.render("Your Score: "+str(newPlayerScore), True, black)

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit(); sys.exit();
        (xPosition,yPosition) = pygame.mouse.get_pos()
        print(BSL.GameScreen.difficulty, currentDifficulty)

        if BSL.GameScreen.difficulty == "Beginner":
                currentDifficulty = "Beginner"
                BSL.BeginnerGameScreenBall.active = True
                BSL.BeginnerGameScreenPaddleRight.active = True
                BSL.IntermediateGameScreenBall.active = False
                BSL.IntermediateGameScreenPaddleRight.active = False
                BSL.AdvancedGameScreenBall.active = False
                BSL.AdvancedGameScreenPaddleRight.active = False

        if BSL.GameScreen.difficulty == "Intermediate":
                currentDifficulty = "Intermediate"
                BSL.BeginnerGameScreenBall.active = False
                BSL.BeginnerGameScreenPaddleRight.active = False
                BSL.IntermediateGameScreenBall.active = True
                BSL.IntermediateGameScreenPaddleRight.active = True
                BSL.AdvancedGameScreenBall.active = False
                BSL.AdvancedGameScreenPaddleRight.active = False

        if BSL.GameScreen.difficulty == "Advanced":
                currentDifficulty = "Advanced"
                BSL.BeginnerGameScreenBall.active = False
                BSL.BeginnerGameScreenPaddleRight.active = False
                BSL.IntermediateGameScreenBall.active = False
                BSL.IntermediateGameScreenPaddleRight.active = False
                BSL.AdvancedGameScreenBall.active = True
                BSL.AdvancedGameScreenPaddleRight.active = True

        if BSL.GameScreen.difficulty == None:
    #	currentDifficulty = None
                BSL.BeginnerGameScreenBall.active = False
                BSL.BeginnerGameScreenPaddleRight.active = False
                BSL.IntermediateGameScreenBall.active = False
                BSL.IntermediateGameScreenPaddleRight.active = False
                BSL.AdvancedGameScreenBall.active = False
                BSL.AdvancedGameScreenPaddleRight.active = False

        BSL.GameScreenPaddleLeft.active = True


        BSL.GameScreenPaddleLeft.y1 = yPosition
        BSL.GameScreenPaddleLeft.y2 = yPosition + 200


        BSL.Paddle.RightPaddlePosition(BSL.BeginnerGameScreenPaddleRight,BSL.BeginnerGameScreenBall)
        BSL.Paddle.RightPaddlePosition(BSL.IntermediateGameScreenPaddleRight,BSL.IntermediateGameScreenBall)

        BSL.Paddle.RightPaddlePosition(BSL.AdvancedGameScreenPaddleRight,BSL.AdvancedGameScreenBall)





        if (BSL.BeginnerGameScreenBall.active == True) and (BSL.BeginnerGameScreenPaddleRight.active == True):
            BSL.Ball.collisionCheckPaddle(BSL.BeginnerGameScreenBall,BSL.GameScreenPaddleLeft)
            BSL.Ball.collisionCheckPaddle(BSL.BeginnerGameScreenBall,BSL.BeginnerGameScreenPaddleRight)
            BSL.Ball.collisionCheckWall(BSL.BeginnerGameScreenBall,display_width,display_height)
            BSL.BeginnerGameScreenBall.updateBallPosition()

        if (BSL.IntermediateGameScreenBall.active == True) and (BSL.IntermediateGameScreenPaddleRight.active == True):
            BSL.Ball.collisionCheckPaddle(BSL.IntermediateGameScreenBall,BSL.GameScreenPaddleLeft)
            BSL.Ball.collisionCheckPaddle(BSL.IntermediateGameScreenBall,BSL.IntermediateGameScreenPaddleRight)
            BSL.Ball.collisionCheckWall(BSL.IntermediateGameScreenBall,display_width,display_height)
            BSL.IntermediateGameScreenBall.updateBallPosition()

        if (BSL.AdvancedGameScreenBall.active == True) and (BSL.AdvancedGameScreenPaddleRight.active == True):
            BSL.Ball.collisionCheckPaddle(BSL.AdvancedGameScreenBall,BSL.GameScreenPaddleLeft)
            BSL.Ball.collisionCheckPaddle(BSL.AdvancedGameScreenBall,BSL.AdvancedGameScreenPaddleRight)
            BSL.Ball.collisionCheckWall(BSL.AdvancedGameScreenBall,display_width,display_height)
            BSL.AdvancedGameScreenBall.updateBallPosition()

        gameDisplay.fill(white)

        if BSL.BeginnerGameScreenBall.active == True:
            if currentScreen == BSL.GameScreen:
                if ((BSL.BeginnerGameScreenBall.x1 <= 0) and
            	   (BSL.BeginnerGameScreenBall.y1 >= 0) and
            	   (BSL.BeginnerGameScreenBall.y1 <= display_height)):
                        currentComputerScore += 1
                        newComputerScore = currentComputerScore
                        computerScoreText = font.render("Opponent's Score: "+str(newComputerScore), True, black)
                        print(newPlayerScore,newComputerScore)

                        if newComputerScore == 8:
                            newComputerScore = 0
                            currentComputerScore = 0
                            gameDisplay.blit(computerScoreText,(1350,0))


        if ((BSL.BeginnerGameScreenBall.x2 >= display_width) and
            (BSL.BeginnerGameScreenBall.y1 >= 0) and
            (BSL.BeginnerGameScreenBall.y1 <= display_height)):
                currentPlayerScore += 1
                newPlayerScore = currentPlayerScore
                playerScoreText = font.render("Your Score: "+str(newPlayerScore), True, black)
                if newPlayerScore == 8:
                    newPlayerScore = 0
                    currentPlayerScore = 0
                gameDisplay.blit(playerScoreText,(0,0))





        if BSL.IntermediateGameScreenBall.active == True:
            if currentScreen == BSL.GameScreen:
                if ((BSL.IntermediateGameScreenBall.x1 <= 0) and
                    (BSL.IntermediateGameScreenBall.y1 >= 0) and
                    (BSL.IntermediateGameScreenBall.y1 <= display_height)):
                        currentComputerScore += 1
                        newComputerScore = currentComputerScore
                        computerScoreText = font.render("Opponent's Score: "+str(newComputerScore), True, black)


                        if newComputerScore == 8:
                            newComputerScore = 0
                            currentComputerScore = 0
                        gameDisplay.blit(computerScoreText,(1350,0))


            if ((BSL.IntermediateGameScreenBall.x2 >= display_width) and
                (BSL.IntermediateGameScreenBall.y1 >= 0) and
                (BSL.IntermediateGameScreenBall.y1 <= display_height)):
                    currentPlayerScore += 1
                    newPlayerScore = currentPlayerScore
                    playerScoreText = font.render("Your Score: "+str(newPlayerScore), True, black)


                    if newPlayerScore == 8:
                        newPlayerScore = 0
                        currentPlayerScore = 0
                    gameDisplay.blit(playerScoreText,(0,0))


        if BSL.AdvancedGameScreenBall.active == True:
            if currentScreen == BSL.GameScreen:
                if ((BSL.AdvancedGameScreenBall.x1 <=0) and
                    (BSL.AdvancedGameScreenBall.y1 >= 0) and
                    (BSL.AdvancedGameScreenBall.y1 <= display_height)):
                        currentComputerScore += 1
                        newComputerScore = currentComputerScore
                        computerScoreText = font.render("Opponent's Score: "+str(newComputerScore), True, black)
                        print(newPlayerScore,newComputerScore)

                        if newComputerScore == 8:
                            newComputerScore = 0
                            currentComputerScore = 0
                        gameDisplay.blit(computerScoreText,(1350,0))


                if ((BSL.AdvancedGameScreenBall.x2 >= display_width) and
                    (BSL.AdvancedGameScreenBall.y1 >= 0) and
                    (BSL.AdvancedGameScreenBall.y1 <= display_height)):
                        currentPlayerScore += 1
                        newPlayerScore = currentPlayerScore
                        playerScoreText = font.render("Your Score: "+str(newPlayerScore), True, black)



                        if newPlayerScore == 8:
                            newPlayerScore = 0
                            currentPlayerScore = 0
                        gameDisplay.blit(playerScoreText,(0,0))


        currentScreen.displayImages(gameDisplay)

        newScreen = currentScreen.checkClicked()
        if newScreen:

                if BSL.BeginnerDifficultyScreenButton.clicked == True:
                    BSL.GameScreen.difficulty = "Beginner"

                elif BSL.IntermediateDifficultyScreenButton.clicked == True:
                    BSL.GameScreen.difficulty = "Intermediate"

                elif BSL.AdvancedDifficultyScreenButton.clicked == True:
                    BSL.GameScreen.difficulty = "Advanced"
                else:
                    BSL.GameScreen.difficulty = None


        if BSL.PlayButtonPauseScreen.clicked == True:

            BSL.GameScreen.difficulty = currentDifficulty


        currentScreen.unload()
        currentScreen = newScreen

        pygame.display.update() #updates the screen
        clock.tick(60)
