# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_4_A
# ２つの整数 a と b を読み込んで、以下の値を計算するプログラムを作成して下さい：
# a ÷ b ： d (整数)
# a ÷ b の余り ： r (整数)
# a ÷ b ： f (浮動小数点数)
a, b = [int(i) for i in input().split(" ")]
d = a // b
r = a % b
f = a / b
print(str(d) + " " + str(r) + " " + str("{:.16f}".format(f)))

