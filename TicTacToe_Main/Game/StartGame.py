from Utilities import ConsleControl
chess = []


def start():
    chess.clear()
    for i in range(0, 3):
        temp = ["*", "*", "*"]
        chess.append(temp)
    from Game import GameLoop
    ConsleControl.clearScreen()
    print("游戏开始!")
    print("在棋盘中, '*'代表空格, 请依据提示输入下棋的位置")
    temp = input("玩家是否先手(玩家使用'X',计算机使用'O')?(Y/N)")
    import Game.NextStep
    if (temp == "Y") | (temp == "y"):
        Game.NextStep.firstChessStr = "X"
        GameLoop.startLoop(True)
    elif (temp == "N") | (temp == "n"):
        Game.NextStep.firstChessStr = "O"
        GameLoop.startLoop(False)
    else :
        print("输入错误!")
    input("按回车返回主菜单")
