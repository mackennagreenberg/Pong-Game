import pygame


class Button: #names the class
        def __init__(self,path,x1,y1,x2,y2,whereItGoes): #initializes the class; defines the button with the characteristics
                self.image = pygame.image.load(path) #sets the color I have defined to the self object (button)
                self.x1 = x1 #sets a coordinate I have defined to the self object (button)
                self.y1 = y1 #sets a coordinate I have defined to the self object (button)
                self.x2 = x2#sets a coordinate I have defined to the self object (button)
                self.y2 = y2
                self.whereItGoes = whereItGoes #variable for what the object does and defines it to the self (button)
                self.clicked = False
        def checkClicked(self): #creates a method to tell the computer when the button is clicked
                                                #three paremeters: self, mousButtonState and the coordinates of the cursor
                pygame.event.get()
                if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[0] and (self.x2>pygame.mouse.get_pos()[0]) and (pygame.mouse.get_pos()[0]>self.x1) and (self.y1<pygame.mouse.get_pos()[1]) and (pygame.mouse.get_pos()[1]<self.y2):
                         # and if it is inside the button

                        self.clicked = True #do what the button does
                        return self.whereItGoes
                else:
                        self.clicked = False
                        return None


class Paddle:
        def __init__(self,path,x1,y1,x2,y2,dy):
                self.image = pygame.image.load(path)
                self.x1 = x1
                self.y1 = y1
                self.x2 = x2
                self.y2 = y2
        self.dy = dy
    self.active = False

    self.horizontalPosition = False
                self.verticalPosition = False
                self.previousHorizontalPosition = False
                self.previousVerticalPosition = False



    def RightPaddlePosition(self,Ball):
    paddleMidline = (self.y1+self.y2)*0.5
    if Ball.y2 < paddleMidline:
    self.y1 = self.y1 - self.dy
    self.y2 = self.y2 - self.dy

    if Ball.y1 > paddleMidline:
    self.y1 = self.y1 + self.dy
    self.y2 = self.y2 + self.dy






class Screen:
        def __init__(self,buttonList,labelList,uniqueObjects,difficulty = None):

    self.buttonList = buttonList
                self.labelList = labelList
    self.uniqueObjects = uniqueObjects
    self.difficulty = difficulty
        def addButtons(self,buttonList):
                self.buttonList = buttonList

        def addLabels(self,labelList):
                self.labelList = labelList

    def addUniqueObjects(self,uniqueObjects):
    self.uniqueObjects = uniqueObjects


    def displayImages(self,gameWindow):
            for button in self.buttonList:
               		gameWindow.blit(button.image, (button.x1,button.y1))
          	for label in self.labelList:
                	gameWindow.blit(label.image, (label.x1,label.y1))
    for uniqueObject in self.uniqueObjects:
    if uniqueObject.active == True:
    gameWindow.blit(uniqueObject.image, (uniqueObject.x1,uniqueObject.y1))

    def checkClicked(self):
    newScreen = []
    for button in self.buttonList:
    if button.checkClicked():
    return button.checkClicked()
    def unload(self):
    for button in self.buttonList:
    button.clicked = False




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

HomeScreenLabel = Label("PONGhomescreen.png",400,0,1080,200)
DifficultyScreenLabel = Label("SelectDifficultyLabel.png",440,0,1080,200)
HelpHelpScreenLabel = Label("HelpHelpScreenLabel.png",440,0,1080,200)
InstructionsHelpScreenLabel = Label("HelpScreenLabel.png",160,400,1360,800)

GameScreenPaddleLeft = Paddle("Paddle.png",40,360,120,560,20)
BeginnerGameScreenPaddleRight = Paddle("Paddle.png",1400,360,1480,560,30)
IntermediateGameScreenPaddleRight = Paddle("Paddle.png",1400,360,1480,560,45)
AdvancedGameScreenPaddleRight = Paddle("Paddle.png",1400,360,1480,560,52)


YouWinLabel = Label("YouWinLabel.png",280,0,1240,240)

BeginnerGameScreenBall = Ball("Ball.png",560,440,600,480,-39,40)
IntermediateGameScreenBall = Ball("Ball.png",560,440,600,480,-50,55)
AdvancedGameScreenBall = Ball("Ball.png",560,440,600,480,-50,62)

HomeScreen = Screen(None,[HomeScreenLabel],[])
DifficultyScreen = Screen(None,[DifficultyScreenLabel],[])
HelpScreen = Screen(None,[HelpHelpScreenLabel,InstructionsHelpScreenLabel],[])
GameScreen = Screen(None,[],[GameScreenPaddleLeft,BeginnerGameScreenPaddleRight,IntermediateGameScreenPaddleRight,AdvancedGameScreenPaddleRight,BeginnerGameScreenBall,IntermediateGameScreenBall,AdvancedGameScreenBall])
PauseScreen = Screen(None,[],[])
WinScreen = Screen(None,[YouWinLabel],[])
PauseGameScreenButton = Button("PauseGameScreenButton.png",680,0,800,120,PauseScreen)


PlayAgainWinLoseButton = Button("SelectDifficultyAndPlayAgainButton.png",200,360,320,520,GameScreen)
HomeWinLoseButton = Button("HomeWinLoseScreenButton.png",880,360,1320,520,HomeScreen)

DifficultyHomeScreenButton = Button("DifficultyButton.png",240,440,640,640,DifficultyScreen)
HelpHomeScreenButton = Button("HelpButton.png",880,440,1280,640,HelpScreen)
GameScreenHomeButton = Button("GameScreenHomeButton.png",360,0,600,120,HomeScreen)

BeginnerDifficultyScreenButton = Button("BeginnerButton.png",80,400,480,600,GameScreen)
IntermediateDifficultyScreenButton = Button("IntermediateButton.png",560,400,960,600,GameScreen)
AdvancedDifficultyScreenButton = Button("AdvancedButton.png",1040,400,1440,600,GameScreen)
BackDifficultyScreenButton = Button("BackDifficultyScreenButton.png",80,40,360,160,HomeScreen)





BackHelpScreenButton = Button("BackHelpScreenButton.png",80,40,360,160,HomeScreen)
DifficultyHelpScreenButton = Button("DifficultyHelpScreenButton.png",1160,40,1440,160,DifficultyScreen)
GameScreenHelpButton = Button("GameScreenHelpButton.png",880,0,1120,120,HelpScreen)

PauseScreenHomeButton = Button("HomePauseScreenButton.png",80,40,360,160,HomeScreen)
PauseScreenHelpButton = Button("HelpPauseScreenButton.png",600,40,920,160,HelpScreen)
PauseScreenDifficultyButton = Button("DifficultyPauseScreenButton.png",1160,40,1440,160,DifficultyScreen)

PlayButtonPauseScreen = Button("PlayButton.png",520,280,800,640,GameScreen)

HomeScreen.addButtons([DifficultyHomeScreenButton,HelpHomeScreenButton])

DifficultyScreen.addButtons([BeginnerDifficultyScreenButton,IntermediateDifficultyScreenButton,AdvancedDifficultyScreenButton,BackDifficultyScreenButton])

HelpScreen.addButtons([BackHelpScreenButton,DifficultyHelpScreenButton])

GameScreen.addButtons([PauseGameScreenButton,GameScreenHomeButton,GameScreenHelpButton])

PauseScreen.addButtons([PlayButtonPauseScreen,PauseScreenHomeButton,PauseScreenHelpButton,PauseScreenDifficultyButton])

WinScreen.addButtons([PlayAgainWinLoseButton,HomeWinLoseButton])