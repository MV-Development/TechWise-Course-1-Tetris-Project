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
pygame.display.set_caption('Tetris')
programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)

#main loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit(0)



