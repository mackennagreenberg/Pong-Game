import pygame

class Button: #names the class
        def __init__(self, path, x1, y1, x2, y2, nextState={}): #initializes the class; defines the button with the characteristics
                self.image = pygame.image.load(path) #sets the color I have defined to the self object (button)
                self.x1 = x1 #sets a coordinate I have defined to the self object (button)
                self.y1 = y1 #sets a coordinate I have defined to the self object (button)
                self.x2 = x2#sets a coordinate I have defined to the self object (button)
                self.y2 = y2
                self.nextState = nextState

        def checkClicked(self): #creates a method to tell the computer when the button is clicked
                                            #three paremeters: self, mousButtonState and the coordinates of the cursor
                pygame.event.get()
                if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[0] and (self.x2>pygame.mouse.get_pos()[0]) and (pygame.mouse.get_pos()[0]>self.x1) and (self.y1<pygame.mouse.get_pos()[1]) and (pygame.mouse.get_pos()[1]<self.y2):
                         # and if it is inside the button

                    return self.nextState

class Paddle:
        def __init__(self,path,x1,y1,x2,y2,dy):
                self.image = pygame.image.load(path)
                self.x1 = x1
                self.y1 = y1
                self.x2 = x2
                self.y2 = y2
                self.dy = dy
                self.height = y2 - y1

                self.horizontalPosition = False
                self.verticalPosition = False
                self.previousHorizontalPosition = False
                self.previousVerticalPosition = False

class AIPaddle(Paddle):
    #def __init__(...) - may want to implement own init later for difficulty purposes

    def update(self,gameState):
        paddleMidline = (self.y1+self.y2)*0.5
        ball = gameState["gameObjects"][2]
        if ball.y2 < paddleMidline:
            self.y1 = self.y1 - self.dy
            self.y2 = self.y2 - self.dy

        if ball.y1 > paddleMidline:
            self.y1 = self.y1 + self.dy
            self.y2 = self.y2 + self.dy


class PlayerPaddle(Paddle):
    #def __init__(...) - again may want to implement playButtonPauseScreen

    def update(self,gameState):
        self.y1 = gameState["mouseY"]
        self.y2 = gameState["mouseY"] + self.height

class Label:
        def __init__(self,path,x1,y1,x2,y2):
                self.image = pygame.image.load(path)
                self.x1 = x1
                self.y1 = y1
                self.x2 = x2
                self.y2 = y2

class Ball:
    def __init__(self,path,x1,y1,x2,y2,dx,dy):
        self.image = pygame.image.load(path)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.dx = dx
        self.dy = dy
        self.active = False

    def update(self,gameState):
        self.y1 = self.y1 - 1
        self.y2 = self.y2 - 1

    def collisionCheckPaddle(self,gameObject):
        effect = pygame.mixer.Sound('BOOP.wav')
        gameObject.previousHorizontalPosition = gameObject.horizontalPosition
        gameObject.previousVerticalPosition = gameObject.verticalPosition

        if (((self.x1 <= gameObject.x2) and (self.x1 >= gameObject.x1)) or
            ((self.x2 >= gameObject.x1) and (self.x2 <= gameObject.x2))):
            gameObject.horizontalPosition = True
        else:
            gameObject.horizontalPosition = False

        if (((self.y1 >= gameObject.y1) and (self.y1 <= gameObject.y2)) or
            ((self.y2 >= gameObject.y1) and (self.y2 <= gameObject.y2))):
            gameObject.verticalPosition = True
        else:
            gameObject.verticalPosition = False

        if (gameObject.horizontalPosition == True) and (gameObject.verticalPosition == True):
            if (gameObject.verticalPosition != gameObject.previousVerticalPosition) and (gameObject.horizontalPosition != gameObject.previousHorizontalPosition):
                self.dy = -1*self.dy
                self.dx = -1*self.dx
                effect.play()

            else:
                if (gameObject.verticalPosition != gameObject.previousVerticalPosition):
                    self.dy = -1*self.dy
                    effect.play()

            if (gameObject.horizontalPosition != gameObject.previousHorizontalPosition):
                self.dx = -1*self.dx
                effect.play()

    def collisionCheckWall(self,display_width,display_height):
        effect = pygame.mixer.Sound('BOOP.wav')
        if (self.y2>=display_height):
            self.dy = -1*self.dy
            self.y2 = display_height
            self.y1 = display_height - 40
            effect.play()

        if (self.y1<=0):
            self.dy = -1*self.dy
            self.y1 = 0
            self.y2 = 40
            effect.play()

        if ((self.x1<=0) or
            (self.x2>=display_width)):
            self.x1=560
            self.x2=600
            self.y1=440
            self.y2=480

    def updateBallPosition(self):
        self.x1 = self.x1 + self.dx
        self.y1 = self.y1 + self.dy
        self.x2 = self.x2 + self.dx
        self.y2 = self.y2 + self.dy

homeScreenLabel = Label("PONGhomescreen.png",400,0,1080,200)
difficultyScreenLabel = Label("SelectDifficultyLabel.png",440,0,1080,200)
helpHelpScreenLabel = Label("HelpHelpScreenLabel.png",440,0,1080,200)
instructionsHelpScreenLabel = Label("HelpScreenLabel.png",160,400,1360,800)
#youWinLabel = Label("YouWinLabel.png",280,0,1240,240)

gameScreenPaddleLeft = PlayerPaddle("Paddle.png",40,360,120,560,20)
beginnerGameScreenPaddleRight = AIPaddle("Paddle.png",1400,360,1480,560,30)

beginnerGameScreenBall = Ball("Ball.png",560,440,600,480,-39,40)

gameScreenButton = Button("PauseGameScreenButton.png",680,0,800,120)
playAgainWinLoseButton = Button("SelectDifficultyAndPlayAgainButton.png",200,360,320,520)
homeWinLoseButton = Button("HomeWinLoseScreenButton.png",880,360,1320,520)
difficultyHomeScreenButton = Button("DifficultyButton.png",240,440,640,640)
helpHomeScreenButton = Button("HelpButton.png",880,440,1280,640)
gameScreenHomeButton = Button("GameScreenHomeButton.png",360,0,600,120)
beginnerDifficultyScreenButton = Button("BeginnerButton.png",80,400,480,600)
intermediateDifficultyScreenButton = Button("IntermediateButton.png",560,400,960,600)
advancedDifficultyScreenButton = Button("AdvancedButton.png",1040,400,1440,600)
backDifficultyScreenButton = Button("BackDifficultyScreenButton.png",80,40,360,160)
backHelpScreenButton = Button("BackHelpScreenButton.png",80,40,360,160)
difficultyHelpScreenButton = Button("DifficultyHelpScreenButton.png",1160,40,1440,160)
gameScreenHelpButton = Button("GameScreenHelpButton.png",880,0,1120,120)
pauseScreenHomeButton = Button("HomePauseScreenButton.png",80,40,360,160)
pauseScreenHelpButton = Button("HelpPauseScreenButton.png",600,40,920,160)
pauseScreenDifficultyButton = Button("DifficultyPauseScreenButton.png",1160,40,1440,160)
playButtonPauseScreen = Button("PlayButton.png",520,280,800,640)
