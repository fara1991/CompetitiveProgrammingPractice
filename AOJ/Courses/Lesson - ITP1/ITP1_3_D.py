# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_3_D
# �R�̐��� a�Ab�Ac ��ǂݍ��݁Aa ���� b �܂ł̐����̒��ɁAc �̖񐔂��������邩�����߂�v���O�������쐬���Ă��������B
a, b, c = [int(i) for i in input().split(" ")]
divisor_count = 0

for i in range(b - a + 1):
    j = a + i
    if c % j == 0:
        divisor_count += 1
    
print(divisor_count)
