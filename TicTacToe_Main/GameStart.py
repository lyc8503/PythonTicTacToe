from Utilities import  ConsleControl
from Game import StartGame
import os


while True:
    i = ConsleControl.printMain()
    if i == 1:
        StartGame.start()
    elif i == 2:
        ConsleControl.printAbout()
    elif i == 3:
        ConsleControl.clearScreen()
    elif i == 4:
        os._exit(0)
    else:
        print("Wrong Input!")
