import os
import fileinput
import pygame
import random

from Game.Bricks import *
from Game.Shared.GameConstants import *


class Level:
    """ Level handler class """

    def __init__(self, game):
        self.__game = game
        self.__bricks = []
        self.__amountOfBricksLeft = 0
        self.__currentLevel = 0

    def getBricks(self):
        return self.__bricks

    def getAmountOfBricksLeft(self):
        return self.__amountOfBricksLeft

    def brickHit(self):
        self.__amountOfBricksLeft -= 1

    def loadNextLevel(self):
        self.__currentLevel += 1
        filename = os.path.join("Assets", "Levels", "level" + str(self.__currentLevel) + ".dat")

        if not os.path.exists(filename):
            self.loadRandom()
        else:
            self.load(self.__currentLevel)

    def loadRandom(self):
        self.__bricks = []

        x, y = 0, 0
        amountOfSuperPowerBricks = 0

        maxBricks = int(GameConstants.SCREEN_SIZE[0] / GameConstants.BRICK_SIZE[0])
        rows = random.randint(2, 8)

        for row in range(0, rows):
            for brick in range(0, maxBricks):
                brickType = random.randint(0, 3)

                hasSuperPowerBrickNumberOverflown =\
                    (brickType == 2 or brickType == 3) and\
                    amountOfSuperPowerBricks >= 2

                if brickType == 1 or hasSuperPowerBrickNumberOverflown:
                    brick = Brick([x, y], pygame.image.load(GameConstants.SPRITE_BRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                elif brickType == 2:
                    brick = SpeedBrick([x, y], pygame.image.load(GameConstants.SPRITE_SPEEDBRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                    amountOfSuperPowerBricks += 1
                elif brickType == 3:
                    brick = LifeBrick([x, y], pygame.image.load(GameConstants.SPRITE_LIFEBRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                    amountOfSuperPowerBricks += 1

                x += GameConstants.BRICK_SIZE[0]

            x = 0
            y += GameConstants.BRICK_SIZE[1]


    def load(self, level):
        self.__currentLevel = level
        self.__bricks = []
        self.__amountOfBricksLeft = 0

        x, y = 0, 0

        for line in fileinput.input(os.path.join("Assets", "Levels", "level" + str(level) + ".dat")):
            for currentBrick in line:
                if currentBrick == "1":
                    brick = Brick([x, y], pygame.image.load(GameConstants.SPRITE_BRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                elif currentBrick == "2":
                    brick = SpeedBrick([x, y], pygame.image.load(GameConstants.SPRITE_SPEEDBRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                elif currentBrick == "3":
                    brick = LifeBrick([x, y], pygame.image.load(GameConstants.SPRITE_LIFEBRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                x += GameConstants.BRICK_SIZE[0]

            x = 0
            y += GameConstants.BRICK_SIZE[1]