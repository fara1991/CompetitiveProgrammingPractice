# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_1_C
# たて a cm よこ b cm の長方形の面積と周の長さを求めるプログラムを作成して下さい。
input_rectangle = input().split(" ")
v = int(input_rectangle[0])
h = int(input_rectangle[1])
print(str(v * h) + " " + str((v + h) * 2))
