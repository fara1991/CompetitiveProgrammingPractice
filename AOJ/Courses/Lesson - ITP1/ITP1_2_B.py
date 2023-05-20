# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_2_B
# ３つの整数a, b, cを読み込み、それらが a < b < cの条件を満たすならば"Yes"を、満たさないならば"No"を出力するプログラムを作成して下さい。
input = input().split(" ")
a = input[0]
b = input[1]
c = input[2]
if a < b and b < c:
    print("Yes")
else:
    print("No")
