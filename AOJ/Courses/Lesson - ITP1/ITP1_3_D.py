# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_3_D
# ３つの整数 a、b、c を読み込み、a から b までの整数の中に、c の約数がいくつあるかを求めるプログラムを作成してください。
a, b, c = [int(i) for i in input().split(" ")]
divisor_count = 0

for i in range(b - a + 1):
    j = a + i
    if c % j == 0:
        divisor_count += 1
    
print(divisor_count)
