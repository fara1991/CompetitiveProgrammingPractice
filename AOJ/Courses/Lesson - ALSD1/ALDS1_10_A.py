# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_10_A
# �t�B�{�i�b�`����̑�n���̒l���o�͂���v���O�������쐬���Ă��������B
n = int(input())
an = [1, 1]
for i in range(43):
    an.append(an[i] + an[i + 1])

print(an[n])

