import random
import tkinter as tk


class player:

    def __init__(self):
        self.__moves = 0

    def setMoves(self, moves):
        self.__moves = moves

    def addMove(self):
        self.__moves += 1

    def getMoves(self):
        return self.__moves


class Human(player):

    def __init__(self, name):
        player.__init__(self)
        self.__name = name

    def setName(self, name):
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


class Stack:

    def __init__(self):
        self.__stack = tk.IntVar(random.randint(1, 10))

    def setStack(self):
        self.__stack.set(random.randint(1, 10))

    def getStack(self):
        return self.__stack

    def takeBalls(self, balls):
        if self.__stack < balls:
            print("Error, you can can't take this many")
        else:
            self.__stack -= balls

    def aiMove(self):
        take = random.randint(1, self.__stack)
        self.__stack -= take
