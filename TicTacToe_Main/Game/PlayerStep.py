from Game.StartGame import chess
from Utilities.ConsleControl import clearScreen
from Utilities.PrintChess import printChess


def GetStep():
    x = -1
    y = -1
    try:
        x = int(input("请输入你想下棋的行数:"))
        y = int(input("请输入你想下棋的列数:"))
        global temp
        temp = chess[x - 1][y - 1]
    except Exception as e:
        print(e)
        print("输入有误!")
        clearScreen()
        printChess(chess)
        GetStep()
        return

    if temp != "*":
        print("输入有误!")
        clearScreen()
        printChess(chess)
        GetStep()
        return

    chess[x - 1][y - 1] = "X"
