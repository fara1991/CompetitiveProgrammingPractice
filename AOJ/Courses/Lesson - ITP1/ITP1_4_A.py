# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_4_A
# �Q�̐��� a �� b ��ǂݍ���ŁA�ȉ��̒l���v�Z����v���O�������쐬���ĉ������F
# a �� b �F d (����)
# a �� b �̗]�� �F r (����)
# a �� b �F f (���������_��)
a, b = [int(i) for i in input().split(" ")]
d = a // b
r = a % b
f = a / b
print(str(d) + " " + str(r) + " " + str("{:.16f}".format(f)))

