# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_6_D
# n�~m�̍s��A�ƁAm�~1�̗�x�N�g��b��ǂݍ��݁AA��b�̐ς��o�͂���v���O�������쐬���Ă��������B
n, m = [int(i) for i in input().split(" ")]
an = []
bn = []

for i in range(n):
    ai = [int(i) for i in input().split(" ")]
    an.append(ai)

for i in range(m):
    b1 = int(input())
    bn.append(b1)

for i in range(len(an)):
    cn = 0
    for j in range(len(bn)):
        cn += an[i][j] * bn[j]
    print(cn)

