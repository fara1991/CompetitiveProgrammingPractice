# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_4_B
# 半径 r の円の面積と円周の長さを求めるプログラムを作成して下さい。
pi = 3.14159265358979
radius = float(input())
print(str(radius * radius * pi) + " " + str(2 * radius * pi))
