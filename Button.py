import pygame
class Button: #names the class
	def __init__(self,image,x1,y1,x2,y2,whatItDoes): #initializes the class; defines the button with the characteristics
		self.image = image #sets the color I have defined to the self object (button) 
		self.x1 = x1 #sets a coordinate I have defined to the self object (button)
		self.y1 = y1 #sets a coordinate I have defined to the self object (button)
		self.x2 = x2#sets a coordinate I have defined to the self object (button)
		self.y2 = y2
		self.whatItDoes = whatItDoes #variable for what the object does and defines it to the self (button)
		self.clicked = False 
	def checkClicked(self): #creates a method to tell the computer when the button is clicked
						#three paremeters: self, mousButtonState and the coordinates of the cursor
		pygame.event.get()
		if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[0] and (self.x2>pygame.mouse.get_pos()[0]) and (pygame.mouse.get_pos()[0]>self.x1) and (self.y1<pygame.mouse.get_pos()[1]) and (pygame.mouse.get_pos()[1]<self.y2): #if the mouse is the first in the list (the mouse on the mac)
			 # and if it is inside the button
		
			self.clicked = True #do what the button does
		else:
			self.clicked = False
