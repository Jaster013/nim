import random


class player:

    def __init__(self):
        self.__moves = 0

    def addMove(self):
        self.__moves += 1

    def getMoves(self):
        return self.__moves


class human(player):

    def __init__(self, name):
        player.__init__(self)
        self.__name = name

    def getName(self):
        return self.__name


class AI(player):

    def __init__(self):
        player.__init__(self)

        list = ['Hall', 'Genesis', 'Enigma', 'Machina', 'Jarvis']
        choice = random.randint(0, len(list) - 1)
        name = list[choice]
        self.__name = name

    def getName(self):
        return self.__name
