# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_2_B
# �R�̐���a, b, c��ǂݍ��݁A����炪 a < b < c�̏����𖞂����Ȃ��"Yes"���A�������Ȃ��Ȃ��"No"���o�͂���v���O�������쐬���ĉ������B
input = input().split(" ")
a = input[0]
b = input[1]
c = input[2]
if a < b and b < c:
    print("Yes")
else:
    print("No")
