# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_3_B
# １つの整数 x を読み込み、それをそのまま出力するプログラムを作成して下さい。
for i in range(10000):
    data = input()
    if data == "0":
        break
    
    print("Case " + str(i + 1) + ": " + data)

