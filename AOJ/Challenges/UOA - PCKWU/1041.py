# https://onlinejudge.u-aizu.ac.jp/challenges/sources/UOA/PCKWU/1041
while(True):
    total = int(int(input()) / 4)
    if total == 0:
        break

    count = 0
    for i in range(total):
        count += int(input())
    print(count)

