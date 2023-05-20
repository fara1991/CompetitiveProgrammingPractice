# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_6_A
# 与えられた数列を逆順に出力するプログラムを作成して下さい。
length = int(input())
array_i = input().split(" ")[::-1]
print(" ".join(array_i))
