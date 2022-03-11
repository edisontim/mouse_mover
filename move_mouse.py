import time
import mouse
import AppKit
import random


screenWidth, screenHeight = pyautogui.size()
random.seed(1)


while 1:
	rand_width = random.randint(0, screenWidth)
	rand_height = random.randint(0, screenHeight)
	time.sleep(10)
	mouse.move(rand_width, rand_height)
