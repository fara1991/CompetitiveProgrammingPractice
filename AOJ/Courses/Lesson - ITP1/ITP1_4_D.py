# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_4_D
# n個の整数 ai(i=1,2,...n)を入力し、それらの最小値、最大値、合計値を求めるプログラムを作成してください。
count = int(input())
numbers = sorted([int(i) for i in input().split(" ")])
min = numbers[0]
max = numbers[count - 1]
sum = sum(numbers)
print(str(min) + " " + str(max) + " " + str(sum))
