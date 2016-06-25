# Import modules
from robot import Robot
from time import sleep
import sys
import pygame

# Set variables
robot = Robot(16,18,38,40)
speed = 100

# Initialize pygame
screen_width = 500
screen_height = 500
pygame.init()
pygame.display.set_mode([screen_width, screen_height])

while True:
    for event in pygame.event.get():
	if event.type == pygame.KEYDOWN:
	    if event.key == pygame.K_UP:
		print("Moving forward")
		robot.forward(speed)
	    if event.key == pygame.K_DOWN:
		print("Moving backward")
		robot.backward(speed)
	    if event.key == pygame.K_RIGHT:
		print("Moving right")
		robot.right(speed)
	    if event.key == pygame.K_LEFT:
		print("Moving left")
		robot.left(speed)

	if event.type == pygame.KEYUP:
	    if event.key == pygame.K_UP or event.key == pygame.K_DOWN or \
	       event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
		robot.stop()
	if event.type == pygame.QUIT:
	    robot.cleanup()
	    sys.exit()
	    
