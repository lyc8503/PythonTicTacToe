def printMain():
    print("Python井字棋 By lyc8503")
    print("=======================")
    print("1.Start New Game")
    print("2.Help & About")
    print("3.Clear Screen")
    print("4.Exit")
    print("=======================")
    try:
        return int(input("Choose an index:"))
    except Exception as e:
        print(e)
        return 666

def clearScreen():
    print("\n" * 100)

def printAbout():
    print("Hi...这是我写的井字棋算法测试 :)\nBug Report:lyc8503@gmail.com")
    input("按回车键以继续")

