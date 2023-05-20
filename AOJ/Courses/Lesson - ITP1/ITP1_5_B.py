# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_5_B
# 以下のような、たてH cm よこ W cm の枠を描くプログラムを作成して下さい。
while(True):
    height, width = input().split(" ")
    if height == "0" and width == "0":
        break

    height = int(height)
    width = int(width)
    for i in range(height):
        width_sharp = ""
        for j in range(width):
            if i != 0 and i != height - 1 and j != 0 and j != width - 1:
                width_sharp += "."
            else:
                width_sharp += "#"
        
        print(width_sharp)

    print("")

