# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_2_A
# ２つの整数 a, b を読み込んで、a と b の大小関係を出力するプログラムを作成して下さい。
input = input().split(" ")
a = int(input[0])
b = int(input[1])
if a < b:
    print("a < b")
elif a > b:
    print("a > b")
else:
    print("a == b")
