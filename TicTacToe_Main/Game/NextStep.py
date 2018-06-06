from Game import StartGame
from Utilities.GameJudge import getWinner
from Utilities.ConsleControl import clearScreen
import copy


firstChessStr = ""
allPossibilities = []
losePossibilities = []
# num = 0


class Step:
    def __init__(self):
        self.Loc = []
        self.chess = ""


class Possibility:
    def __init__(self):
        self.steps = []
        self.finalChess = []
        self.stepsToWin = -1
        self.loseStep = 0


def checkTwoPoss(check_chess):
    poss_to_win = 0
    emptySlots = []
    for x in range(0, 3):
        for y in range(0, 3):
            if StartGame.chess[x][y] == "*":
                Loc = [x, y]
                emptySlots.append(Loc)

    for test in emptySlots:
        backup = copy.deepcopy(check_chess)
        backup[test[0]][test[1]] = "X"
        if getWinner(backup) == "X":
            poss_to_win += 1

    if poss_to_win >= 2:
        return True
    else:
        return False



def nextStep():
    clearScreen()
    allPossibilities.clear()
    losePossibilities.clear()
    empty = StartGame.chess[1][1] == "*"
    if empty:
        StartGame.chess[1][1] = "O"
        print("处理完成!")
        print("下棋位置 [2, 2]")
        input("Enter to Continue")
        return
    # num = 0

    emptySlots = []
    for x in range(0, 3):
        for y in range(0, 3):
            if StartGame.chess[x][y] == "*":
                Loc = [x, y]
                emptySlots.append(Loc)

    two_poss = False
    bad_locations = []

    if len(emptySlots) > 2:
        for emptyLoc in emptySlots:
            backup = copy.deepcopy(StartGame.chess)
            backup[emptyLoc[0]][emptyLoc[1]] = "O"
            emptySlots_1 = []
            for x in range(0, 3):
                for y in range(0, 3):
                    if backup[x][y] == "*":
                        Loc_1 = [x, y]
                        emptySlots_1.append(Loc_1)
            for emptyLoc_1 in emptySlots_1:
                backup1 = copy.deepcopy(backup)
                backup1[emptyLoc_1[0]][emptyLoc_1[1]] = "X"
                if checkTwoPoss(backup1):
                    print("!!!TWO POSSIBILITIES FOUND!!!")
                    bad_locations.append(emptyLoc)
                    two_poss = True

    print(bad_locations)
    print("正在遍历所有可能性...请稍候.依据你的电脑配置第一次可能30秒左右的处理时间 :P")
    poss = Possibility()
    poss.finalChess = copy.deepcopy(StartGame.chess)
    getAllPossibilities(poss)
    # print(firstChessStr)
    print("遍历完成!")
    win_steps = 666
    num_draw = 0
    num_win = 0
    num_lose = 0
    for possible in allPossibilities:
        if possible.stepsToWin == 9999:
            print("Draw " + str(possible.finalChess))
            num_draw += 1
        elif possible.stepsToWin == -1:
            print("Error " + str(possible.finalChess))
        else:
            print("Win Steps" + str(possible.stepsToWin) + " " + str(possible.finalChess))
            num_win += 1
            if possible.steps[0].Loc not in bad_locations:
                if possible.stepsToWin < win_steps:
                    win_steps = possible.stepsToWin
                    final_poss = possible

    lose_steps = 666
    for lose_possible in losePossibilities:
        print("Lose Steps" + str(lose_possible.loseStep) + str(lose_possible.finalChess))
        num_lose += 1
        if lose_possible.loseStep < lose_steps:
            lose_steps = lose_possible.loseStep
    print("处理完成!")
    print("Win_Num " + str(num_win) + " Lose_Num " + str(num_lose) + " Draw_Num " + str(num_draw))
    print("WinStep " + str(win_steps) + " LoseSteps " + str(lose_steps))

    try:
        final_loc = final_poss.steps[0].Loc
        final_chess = final_poss.steps[0].chess
    except :
        print("Can't Win")
    # if (win_steps != 1) & (num_lose != 0):
    #     if win_steps >= lose_steps:
    #         print("!!!MAY LOSE!!!")
    if lose_steps == 1:
        breakFlag = False
        for lose_poss in losePossibilities:
            if lose_poss.loseStep == 1:
                for temp in lose_poss.steps:
                    if temp.chess == "X":
                        final_loc = temp.Loc
                        final_chess = "O"
                if StartGame.chess[final_loc[0]][final_loc[1]] == "*":
                    breakFlag = True
                if breakFlag:
                    break
            if breakFlag:
                break
    try:
        final_loc[0] += 1
        final_loc[1] += 1
        print("下棋位置 " + str(final_loc))
        final_loc[0] -= 1
        final_loc[1] -= 1
        StartGame.chess[final_loc[0]][final_loc[1]] = final_chess
    except Exception:
        final_poss = allPossibilities[0]
        final_loc = final_poss.steps[0].Loc
        final_chess = final_poss.steps[0].chess
        final_loc[0] += 1
        final_loc[1] += 1
        print("下棋位置 " + str(final_loc))
        final_loc[0] -= 1
        final_loc[1] -= 1
        StartGame.chess[final_loc[0]][final_loc[1]] = final_chess

    input("Enter to Continue")


def getAllPossibilities(startPossibility):
    # print("正在计算...请稍候", end="" )
    # print(startPossibility.finalChess)
    winner = getWinner(startPossibility.finalChess)
    # print(winner)
    if winner == "O":
        allPossibilities.append(startPossibility)
        # print("Win" + str(startPossibility.finalChess))
        return
    elif winner == "X":
        # print("Lose" + str(startPossibility.finalChess))
        startPossibility.stepsToWin = -233
        losePossibilities.append(startPossibility)
        return
    # print("TEST")
    emptySlotLoc = []
    ifFull = True
    numO = 0
    numX = 0
    chess = startPossibility.finalChess
    for x in range(0, 3):
        for y in range(0, 3):
            if chess[x][y] == "*":
                Loc = [x, y]
                ifFull = False
                emptySlotLoc.append(Loc)
            if chess[x][y] == "X":
                numX += 1
            if chess[x][y] == "O":
                numO += 1

    if ifFull:
        # print("Draw " + str(startPossibility.finalChess))
        temp = copy.deepcopy(startPossibility)
        temp.stepsToWin = 9999
        allPossibilities.append(temp)

    if numO == numX:
        executedChess = firstChessStr
    elif numO > numX:
        executedChess = "X"
    else:
        executedChess = "O"
    for loc in emptySlotLoc:
        newPoss = copy.deepcopy(startPossibility)
        curStep = Step()
        curStep.Loc = loc
        curStep.chess = executedChess
        newPoss.finalChess[loc[0]][loc[1]] = executedChess
        if executedChess == "O":
            newPoss.stepsToWin += 1
        if executedChess == "X":
            newPoss.loseStep += 1
        newPoss.steps.append(curStep)
        getAllPossibilities(newPoss)
