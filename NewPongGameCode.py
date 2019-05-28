import pygame, sys, BSL

pygame.font.init()
pygame.init()

display_width = 1520
display_height = 920
white = (255,255,255)
red = (255,0,0)
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width,display_height)) #use variables so we can reference
pygame.display.set_caption("Pong by Mackenna Greenberg (feat. Alex)")

buttons = []
labels = []
gameObjects = []
computerScore = 0
playerScore = 0

defaultState = {
    "buttons": [],
    "labels": [],
    "gameObjects": [],
    "computerScore": 0,
    "playerScore": 0
    }
homeState = {
    "buttons": [BSL.helpHomeScreenButton,
                BSL.difficultyHomeScreenButton],
    "labels": [BSL.homeScreenLabel],
    "gameObjects": [],
    "computerScore": 0,
    "playerScore": 0
    }

helpState = {
    "buttons": [BSL.backHelpScreenButton,
                BSL.difficultyHelpScreenButton],
    "labels": [BSL.helpHelpScreenLabel,
                BSL.instructionsHelpScreenLabel],
    "gameObjects": [],
    "computerScore": 0,
    "playerScore": 0
    }

difficultyState = {
    "buttons": [BSL.beginnerDifficultyScreenButton,
                BSL.intermediateDifficultyScreenButton,
                BSL.advancedDifficultyScreenButton,
                BSL.backDifficultyScreenButton],
    "labels": [BSL.difficultyScreenLabel],
    "gameObjects": [],
    "computerScore": 0,
    "playerScore": 0
    }

playState = {
    "buttons": [BSL.gameScreenButton,
                BSL.gameScreenHelpButton],
    "labels": [],
    "gameObjects": [BSL.gameScreenPaddleLeft,
                    BSL.beginnerGameScreenPaddleRight,
                    BSL.beginnerGameScreenBall],
    "computerScore": 0,
    "playerScore": 0,
    "mouseX": 0,
    "mouseY": 0
}

pauseState = {
    "buttons": [BSL.pauseScreenHomeButton,
                BSL.pauseScreenHelpButton,
                BSL.pauseScreenDifficultyButton,
                BSL.playButtonPauseScreen],
    "labels": [],
    "gameObjects": [],
    "computerScore": 0,
    "playerScore": 0
}

BSL.helpHomeScreenButton.nextState = helpState
BSL.difficultyHomeScreenButton.nextState = difficultyState

BSL.backHelpScreenButton.nextState = homeState
BSL.difficultyHelpScreenButton.nextState = difficultyState

BSL.beginnerDifficultyScreenButton.nextState = playState
BSL.intermediateDifficultyScreenButton.nextState = playState
BSL.advancedDifficultyScreenButton.nextState = playState
BSL.backDifficultyScreenButton.nextState = homeState

BSL.gameScreenButton.nextState = pauseState
BSL.gameScreenHelpButton.nextState = helpState

BSL.pauseScreenHomeButton.nextState = homeState
BSL.pauseScreenHelpButton.nextState = helpState
BSL.pauseScreenDifficultyButton.nextState = difficultyState
BSL.playButtonPauseScreen.nextState = playState




def resetState(gameState):
    gameState = {
        "buttons": [],
        "labels": [],
        "gameObjects": [],
        "computerScore": 0,
        "playerScore": 0
        }

def displayImages(gameWindow, gameState):
    for button in gameState["buttons"]:
        gameWindow.blit(button.image, (button.x1,button.y1))
    for label in gameState["labels"]:
        gameWindow.blit(label.image, (label.x1,label.y1))
    for gameObject in gameState["gameObjects"]:
        gameWindow.blit(gameObject.image, (gameObject.x1,gameObject.y1))

gameState = homeState

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();
    gameState["mouseX"] = pygame.mouse.get_pos()[0]
    gameState["mouseY"] = pygame.mouse.get_pos()[1]
    #(xPosition,yPosition) = pygame.mouse.get_pos()
    for button in gameState["buttons"]:
        nextState = button.checkClicked()
        if bool(nextState):
            gameState = nextState
            break #if there is a loop, stop running that loop
    for gameObject in gameState["gameObjects"]:
        gameObject.update(gameState)

    gameDisplay.fill(white)
    displayImages(gameDisplay, gameState)
    pygame.display.update()
    clock.tick(60)




#Buttons = [HelpButtonHomeScreen, ChooseDifficultyButtonHomeScreen,
#HomeButtonHelpScreen, ChooseDifficultyButtonHomeScreen, BeginnerDifficultyButton,
#IntermediateDifficultyButton, AdvancedDifficultyButton, PauseButtonGameScreen,
#PlayButtonPauseScreen, HomeButtonPauseScreen]

#GameObjects = [RightPaddle, LeftPaddle, Ball]

#Labels = [HomeScreenLabel, HelpScreenLabel, HelpScreenInstructions,
#DifficultyScreenLabel, PauseScreenLabel]

#Ball = some speed and direction
#LeftPaddle = some speed


#If Ball hits left wall:
#   ComputerScore += 1

#If Ball hits right wall:
#   PlayerScore += 1
