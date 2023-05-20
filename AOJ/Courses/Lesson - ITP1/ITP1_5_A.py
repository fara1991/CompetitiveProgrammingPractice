# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_5_A
# たてH cm よこ W cm の長方形を描くプログラムを作成して下さい。
# 1 cm × 1cm の長方形を '#'で表します。
while(True):
    height, width = input().split(" ")
    if height == "0" and width == "0":
        break

    height = int(height)
    width = int(width)
    for i in range(height):
        width_sharp = ""
        for j in range(width):
            width_sharp += "#"
        
        print(width_sharp)

    print("")

