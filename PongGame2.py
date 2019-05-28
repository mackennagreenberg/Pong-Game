import pygame, sys, BSL

pygame.font.init()
pygame.init()
pygame.display.set_caption("Pong by Mackenna Greenberg (feat. Alex)")

display_width = 1520
display_height = 920
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width,display_height)) #use variables so we can reference

buttons = []
labels = []
gameObjects = []
computerScore = 0
playerScore = 0

gameState = {
    "buttons": [],
    "labels": [],
    "gameObjects": [],
    "computerScore": 0,
    "playerScore": 0
    }

def resetState(gameState):
    gameState = {
        "buttons": [],
        "labels": [],
        "gameObjects": [],
        "computerScore": 0,
        "playerScore": 0
        }

def homeState(gameState):
    resetState(gameState)
    gameState["buttons"] = [BSL.helpHomeScreenButton,
                            BSL.chooseDifficultyButtonHomeScreen]
    gameState["labels"] = [BSL.homeScreenLabel]

def displayImages(gameWindow, gameState):
        for button in gameState["buttons"]:
                gameWindow.blit(button.image, (button.x1,button.y1))
        for label in gameState["labels"]:
                gameWindow.blit(label.image, (label.x1,label.y1))

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

homeState(gameState)
while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit();
    (xPosition,yPosition) = pygame.mouse.get_pos()
    displayImages(gameDisplay, gameState)
    #currentScreen.displayImages(gameDisplay)
    pygame.display.update() #updates the screen
    clock.tick(60)
