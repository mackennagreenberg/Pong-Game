import pygame
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




x = (display_width * 0.45)
y = (display_height * 0.8)
clock = pygame.time.Clock()

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit(); sys.exit();
	"""gameDisplay.fill(white)"""

	pygame.display.update() #updates the screen
        clock.tick(60)
