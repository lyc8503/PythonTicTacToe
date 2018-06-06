from Game import NextStep
from Game import PlayerStep
from Utilities import PrintChess
from Utilities import ConsleControl
from Utilities import GameJudge
from Game.StartGame import chess


def startLoop(ifPlayer):
    for i in range(0, 9):
        ConsleControl.clearScreen()
        PrintChess.printChess(chess)
        if GameJudge.getWinner(chess) == "X":
            ConsleControl.clearScreen()
            PrintChess.printChess(chess)
            print("X(玩家)赢得了游戏!")
            return
        if GameJudge.getWinner(chess) == "O":
            ConsleControl.clearScreen()
            PrintChess.printChess(chess)
            print("O(计算机)赢得了游戏!")
            return
        if ifPlayer:
            PlayerStep.GetStep()
            ifPlayer = False
        else:
            NextStep.nextStep()
            ifPlayer = True

    if GameJudge.getWinner(chess) == "X":
        ConsleControl.clearScreen()
        PrintChess.printChess(chess)
        print("X(玩家)赢得了游戏!")
        return
    if GameJudge.getWinner(chess) == "O":
        ConsleControl.clearScreen()
        PrintChess.printChess(chess)
        print("O(计算机)赢得了游戏!")
        return
    ConsleControl.clearScreen()
    PrintChess.printChess(chess)
    print("游戏平局!")
