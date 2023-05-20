# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_3_C
# ２つの整数 x, y を読み込み、それらを値が小さい順に出力するプログラムを作成して下さい。
# ただし、この問題は以下に示すようにいくつかのデータセットが与えられることに注意して下さい。
for i in range(10000):
    x, y = sorted([int(j) for j in input().split(" ")])
    if x == 0 and y == 0:
        break
    
    print(str(x) + " " + str(y))
    
