# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_4_A
# n個の整数を含む数列Sと、q個の異なる整数を含む数列Tを読み込み、Tに含まれる整数の中でSに含まれるものの個数Cを出力するプログラムを作成してください。
n = int(input())
S = input().split(" ")
m = int(input())
T = input().split(" ")

counter = 0
for i in range(m):
    if T[i] in S:
        counter += 1

print(counter)
