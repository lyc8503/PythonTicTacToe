def getWinner(chess):
    X = False
    O = False
    for x in range(0, 3):
        ifXSuccess = True
        ifOSuccess = True
        for y in range(0, 3):
            if chess[x][y] != "X":
                ifXSuccess = False
            if chess[x][y] != "O":
                ifOSuccess = False
        if ifXSuccess:
            X = True
        if ifOSuccess:
            O = True

    for y in range(0, 3):
        ifXSuccess = True
        ifOSuccess = True
        for x in range(0, 3):
            if chess[x][y] != "X":
                ifXSuccess = False
            if chess[x][y] != "O":
                ifOSuccess = False
        if ifXSuccess:
            X = True
        if ifOSuccess:
            O = True

    if (chess[0][0] == chess[1][1]) & (chess[1][1] == chess[2][2]) & (chess[0][0] == "X"):
        return "X"
    if (chess[0][0] == chess[1][1]) & (chess[1][1] == chess[2][2]) & (chess[0][0] == "O"):
        return "O"

    if (chess[0][2] == chess[1][1]) & (chess[1][1] == chess[2][0]) & (chess[1][1] == "X"):
        return "X"
    if (chess[0][2] == chess[1][1]) & (chess[1][1] == chess[2][0]) & (chess[1][1] == "O"):
        return "O"

    if X:
        return "X"
    if O:
        return "O"

    return "233"
