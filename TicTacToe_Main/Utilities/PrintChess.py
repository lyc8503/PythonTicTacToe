from Game import StartGame


def printChess(chess):
    print("Chess:\n======")
    for x in range(0,3):
        for y in range(0,3):
            print(chess[x][y], end=" ")
        print("")
    print("======")
