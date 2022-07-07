import pygame
import random
import sys
import os

pygame.init()
#window variables
w_width = 800
w_height = 800

#screen initialization
screen = pygame.display.set_mode((w_width, w_height))
pygame.mouse.set_visible(0)

#main loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()




