# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_4_A
# n�̐������܂ސ���S�ƁAq�̈قȂ鐮�����܂ސ���T��ǂݍ��݁AT�Ɋ܂܂�鐮���̒���S�Ɋ܂܂����̂̌�C���o�͂���v���O�������쐬���Ă��������B
n = int(input())
S = input().split(" ")
m = int(input())
T = input().split(" ")

counter = 0
for i in range(m):
    if T[i] in S:
        counter += 1

print(counter)
