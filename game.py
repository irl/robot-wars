
import pygame

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)

white = (255, 255, 255)

backdrop = pygame.image.load("/home/irl/game/backdrop.png") # 800x600 pixels

gunman = pygame.image.load("/home/irl/game/gunman.png") # 50x70 pixels
gunman_left = pygame.image.load("/home/irl/game/gunman-left.png") # 50x70 pixels

robot = pygame.image.load("/home/irl/game/robot.png") # 63x200 pixels

rocket = pygame.image.load("/home/irl/game/rocket.png") # 63x50 pixels

left = False

gx = 0 
gy = 300

w = False
a = False
s = False
d = False

rx = 700
ry = 0
rt = 0

# 25, 38-40

try:
	while True:

		#### Animation ###

		pygame.time.delay(5)

		screen.blit(backdrop, backdrop.get_rect())
		if left:
			screen.blit(gunman_left, pygame.rect.Rect(gx, gy, 63, 200))
		else:
			screen.blit(gunman, pygame.rect.Rect(gx, gy, 63, 200))
		screen.blit(robot, pygame.rect.Rect(rx, ry, 63, 200))
		if w:
			screen.blit(rocket, pygame.rect.Rect(gx, gy+200, 63, 200))
		pygame.display.flip()

		### Game Logic ###

		# Evil Robot AI

		if ry == 300 and rt == 0:
			rt = -1

		rx += rt

		if rx == 0:
			rt = 1
		if rx == 730:
			rt = -1

		# Gravity

		if ry < 300:
			ry += 1
		if gy < 300:
			gy += 1

		# Boundaries

		if gy > 300:
			gy = 300
		if gy < 0:
			gy = 0
		if gx > 750:
			gx = 750
		if gx < 0:
			gx = 0

		# Movement

		if w:
			gy -= 2
		if a:
			gx -= 2
		if s:
			gy += 2
		if d:
			gx += 2

		### Event Handling ###

		ev = pygame.event.poll()
		if ev.type == pygame.NOEVENT:
			continue
		if ev.type == pygame.QUIT:
			break
		if ev.type == pygame.KEYDOWN:
			if ev.scancode == 25: # It's a W
				w = True
			if ev.scancode == 38: # It's a A
				a = True
				left = True
			if ev.scancode == 39: # It's a S
				s = True
			if ev.scancode == 40: # It's a D
				left = False
				d = True
			continue
		if ev.type == pygame.KEYUP:
			if ev.scancode == 25: # It's a W
				w = False
			if ev.scancode == 38: # It's a A
				a = False
			if ev.scancode == 39: # It's a S
				s = False
			if ev.scancode == 40: # It's a D
				d = False
			continue

except KeyboardInterrupt:
	pass

