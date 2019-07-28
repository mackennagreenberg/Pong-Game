import pygame, sys, BSL

pygame.font.init()
pygame.init()

display_width = 1520
display_height = 920
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
clock = pygame.time.Clock()


gameDisplay = pygame.display.set_mode((display_width,display_height)) #use variables so we can reference
pygame.display.set_caption("Pong by Mackenna Greenberg (feat. Alex)")

buttons = []
labels = []
gameObjects = []
score = [0,0]

defaultState = {
    "buttons": [],
    "labels": [],
    "gameObjects": [],
    "score": [0,0],
    "display_width": display_width,
    "display_height": display_height,
    "difficulty": 0,
    "win": None

    }

homeState = {
    "buttons": [BSL.helpHomeScreenButton,
                BSL.difficultyHomeScreenButton],
    "labels": [BSL.homeScreenLabel],
    "gameObjects": [],
    "score": [0,0],
    "display_width": display_width,
    "display_height": display_height,
    "difficulty": 0,
    "win": None
    }

helpState = {
    "buttons": [BSL.backHelpScreenButton,
                BSL.difficultyHelpScreenButton],
    "labels": [BSL.helpHelpScreenLabel,
                BSL.instructionsHelpScreenLabel],
    "gameObjects": [],
    "score": [0,0],
    "display_width": display_width,
    "display_height": display_height,
    "difficulty": 0,
    "win": None
    }

difficultyState = {
    "buttons": [BSL.beginnerDifficultyScreenButton,
                BSL.intermediateDifficultyScreenButton,
                BSL.advancedDifficultyScreenButton,
                BSL.backDifficultyScreenButton],
    "labels": [BSL.difficultyScreenLabel],
    "gameObjects": [],
    "score": [0,0],
    "display_width": display_width,
    "display_height": display_height,
    "difficulty": 0,
    "win": None
    }

playState = {
    "buttons": [BSL.gameScreenButton,
                BSL.gameScreenHelpButton],
    "labels": [],
    "gameObjects": [BSL.gameScreenPaddleLeft,
                    BSL.beginnerGameScreenPaddleRight,
                    BSL.beginnerGameScreenBall],
    "score": [0,0],
    "mouseX": 0,
    "mouseY": 0,
    "display_width": display_width,
    "display_height": display_height,
    "difficulty": 0,
    "AIdifficulty": 0,
    "win": None,
}

beginnerState = playState.copy()
beginnerState["difficulty"] = 13
beginnerState["AIdifficulty"] = beginnerState["difficulty"] - 3

intermediateState = playState.copy()
intermediateState["difficulty"] = 16
intermediateState["AIdifficulty"] = intermediateState["difficulty"] - 2

advancedState = playState.copy()
advancedState["difficulty"] = 25
advancedState["AIdifficulty"] = advancedState["difficulty"] - 2

pauseState = {
    "buttons": [BSL.pauseScreenHomeButton,
                BSL.pauseScreenHelpButton,
                BSL.pauseScreenDifficultyButton,
                BSL.playButtonPauseScreen],
    "labels": [],
    "gameObjects": [],
    "score": [0,0],
    "display_width": display_width,
    "display_height": display_height,
    "difficulty": 0,
    "win": None
}

winState = {
    "buttons": [BSL.playAgainButton, BSL.changeDifficultyWinButton, BSL.homeWinButton],
    "labels": [BSL.winnerLabel],
    "gameObjects": [],
    "score": [0,0],
    "display_width": display_width,
    "display_height": display_height,
    "difficulty": 0,
    "win": None
}

loseState = winState.copy()
loseState["labels"] = [BSL.loserLabel]


BSL.helpHomeScreenButton.nextState = helpState
BSL.difficultyHomeScreenButton.nextState = difficultyState

BSL.backHelpScreenButton.nextState = homeState
BSL.difficultyHelpScreenButton.nextState = difficultyState

BSL.beginnerDifficultyScreenButton.nextState = beginnerState
BSL.intermediateDifficultyScreenButton.nextState = intermediateState
BSL.advancedDifficultyScreenButton.nextState = advancedState
BSL.backDifficultyScreenButton.nextState = homeState

BSL.gameScreenButton.nextState = pauseState
BSL.gameScreenHelpButton.nextState = helpState

BSL.pauseScreenHomeButton.nextState = homeState
BSL.pauseScreenHelpButton.nextState = helpState
BSL.pauseScreenDifficultyButton.nextState = difficultyState
BSL.playButtonPauseScreen.nextState = playState

BSL.changeDifficultyWinButton.nextState = difficultyState
BSL.homeWinButton.nextState = homeState
BSL.playAgainButton.nextState = homeState


font = pygame.font.SysFont('Comic Sans MS',25)

def resetState(gameState):
    gameState = {
        "buttons": [],
        "labels": [],
        "gameObjects": [],
        "score": [0,0]
        }

gameState = homeState

def displayImages(gameWindow, gameState):
    for button in gameState["buttons"]:
        gameWindow.blit(button.image, (button.x1,button.y1))
    for label in gameState["labels"]:
        gameWindow.blit(label.image, (label.x1,label.y1))
    for gameObject in gameState["gameObjects"]:
        gameWindow.blit(gameObject.image, (gameObject.x1,gameObject.y1))
#    for score in gameState["score"]:
    #    print(gameState["score"])
#    gameWindow.blit(computerScoreText,(1278,0))
    #    gameWindow.blit(playerScoreText, (5,0))

def displayText(gameWindow, gameState):
    computerScoreText = font.render("Opponent's Score: "+str(gameState["score"][1]), True, black)
    playerScoreText = font.render("Your Score: "+str(gameState["score"][0]), True, black)
    print(gameState["score"])
    gameWindow.blit(computerScoreText,(1278,0))
    gameWindow.blit(playerScoreText, (5,0))


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
            gameState["score"] = [0,0]
            break
    if gameState == beginnerState:
        BSL.playButtonPauseScreen.nextState = beginnerState
        BSL.playAgainButton.nextState = beginnerState
        BSL.beginnerGameScreenPaddleRight.dy = beginnerState["difficulty"]
    elif gameState == intermediateState:
        BSL.playButtonPauseScreen.nextState = intermediateState
        BSL.playAgainButton.nextState = intermediateState
            #gameState["currentDifficulty"] == intermediate
    elif gameState == advancedState:
        BSL.playButtonPauseScreen.nextState = advancedState
        BSL.playAgainButton.nextState = advancedState
            #gameState["currentDifficulty"] == advanced





     #if there is a loop, stop running that loop
    for gameObject in gameState["gameObjects"]:
        gameObject.update(gameState)

    gameDisplay.fill(white)

    if gameState["win"] == True:
        gameState["win"] = None
        gameState = winState
    elif gameState["win"] == False:
        gameState["win"] = None
        gameState = loseState
    if (gameState == beginnerState) or (gameState == intermediateState) or (gameState == advancedState):
        displayText(gameDisplay, gameState)
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
