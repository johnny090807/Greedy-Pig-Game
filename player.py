class Player:
    def __init__(self, name, savedPoints = 0, currentPoints = 0):
        self.__name = name
        self.__savedPoints = savedPoints
        self.__currentPoints = currentPoints

    def getPlayer(self):
        return [self.__name, self.__savedPoints, self.__currentPoints]

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSavedPoints(self, savedPoints):
        self.__savedPoints = savedPoints

    def getSavedPoints(self):
        return self.__savedPoints

    def setCurrentPoints(self, currentPoints):
        self.__currentPoints = currentPoints

    def getCurrentPoints(self):
        return self.__currentPoints
