# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_2_A
# �Q�̐��� a, b ��ǂݍ���ŁAa �� b �̑召�֌W���o�͂���v���O�������쐬���ĉ������B
input = input().split(" ")
a = int(input[0])
b = int(input[1])
if a < b:
    print("a < b")
elif a > b:
    print("a > b")
else:
    print("a == b")
