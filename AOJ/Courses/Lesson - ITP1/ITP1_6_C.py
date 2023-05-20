# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_6_C
# Ａ大学は１フロア１０部屋、３階建ての公舎４棟を管理しています。公舎の入居・退去の情報を読み込み、各部屋の入居者数を出力するプログラムを作成して下さい。
# n件の情報が与えられます。各情報では、４つの整数b, f, r, vが与えられます。これは、b棟f階のr番目の部屋にv人が追加で入居したことを示します。vが負の値の場合、-v人退去したことを示します。
# 最初、全ての部屋には誰も入居していないものとします。
number = int(input())
residence_1 = [[0] * 10, [0] * 10, [0] * 10]
residence_2 = [[0] * 10, [0] * 10, [0] * 10]
residence_3 = [[0] * 10, [0] * 10, [0] * 10]
residence_4 = [[0] * 10, [0] * 10, [0] * 10]
residence = [residence_1, residence_2, residence_3, residence_4]

for i in range(number):
    b, f, r, v = [int(i) for i in input().split(" ")]
    residence[b - 1][f - 1][r - 1] += v


prev_i = 0
for i in range(4):
    if prev_i != i:
        prev_i = i
        print("####################")
    for j in range(3):
        members = ""
        for k in range(10):
            members += " " + str(residence[i][j][k])
        print(members)

