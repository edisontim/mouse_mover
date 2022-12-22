import time
import random
# py -m pip install mouse
import mouse
# py -m pip install pyautogui
import pyautogui

# AppKit does not appear to be needed
# wheels?
# py -m pip install --upgrade pip setuptools wheel
# error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
# py -m pip install pycairo
# https://www.msys2.org/ msys2-x86_64-20221216.exe
# https://github.com/msys2/msys2-installer/releases/download/2022-12-16/msys2-x86_64-20221216.exe
# pacman -Suy
# pacman -S mingw-w64-x86_64-gtk3 mingw-w64-x86_64-python3 mingw-w64-x86_64-python3-gobject
# import AppKit

screenWidth, screenHeight = pyautogui.size()
random.seed(1)

class move_mouse:
    def __init__(self):
        # pause between movements (secs)
        self.pause = 10
        # duration to run (secs)
        self.duration = 15 * 60
        self.debug = True

    def start(self):
        if self.debug :
           print('screen ' + str(screenWidth) + ', ' + str(screenHeight) )
        while self.duration > 0:
            rand_width = random.randint(0, screenWidth)
            rand_height = random.randint(0, screenHeight)
            mouse.move(rand_width, rand_height)
            if self.debug :
               print('moved to ' + str(rand_width) + ',' + str(rand_height) )
            # wait pause seconds
            # print('waiting ' + str(self.pause) )
            time.sleep(self.pause)
            self.duration -= self.pause
            # remaining duration
            if self.debug :
               print('remaining ' + str(self.duration) )

if __name__ == "__main__":
    t = move_mouse()
    t.start()
