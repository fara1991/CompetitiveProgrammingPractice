# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_2_C
# ３つの整数を読み込み、それらを値が小さい順に並べて出力するプログラムを作成して下さい。
input = input().split(" ")
sorted_input = sorted(input)
a = sorted_input[0]
b = sorted_input[1]
c = sorted_input[2]
print(str(a) + " " + str(b) + " " + str(c))
