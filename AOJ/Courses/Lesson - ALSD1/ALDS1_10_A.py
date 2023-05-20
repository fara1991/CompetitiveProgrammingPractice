# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_10_A
# フィボナッチ数列の第n項の値を出力するプログラムを作成してください。
n = int(input())
an = [1, 1]
for i in range(43):
    an.append(an[i] + an[i + 1])

print(an[n])

