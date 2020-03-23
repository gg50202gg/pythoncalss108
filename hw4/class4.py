import random

again = 'Y'
dict_go = {
    1: "剪刀",
    2: "石頭",
    3: "布",
}

dict_win = [None, 3, 1, 2]


def main():
    player = eval(input("請問你出什麼?\n1.剪刀\n2.石頭\n3.布\n... "))
    computer = random.randint(1, 3)
    print("隨機數: %d" % (computer))
    if player == computer:  # 平手
        go = dict_go[player]
        print("你出 %s ,電腦也出 %s ,平手" % (go, go))
    elif dict_win[computer] == player:  # 電腦win
        print("你出 %s ,電腦出 %s ,電腦贏" % (dict_go[player], dict_go[computer]))
    else:  # 玩家win
        print("你出 %s ,電腦出 %s ,玩家贏" % (dict_go[player], dict_go[computer]))


if __name__ == "__main__":
    while again == "Y" or again == 'y':
        main()
        again = input("Continue?(Y/N)")
    print("結束遊戲")
