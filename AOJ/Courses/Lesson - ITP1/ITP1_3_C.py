# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_3_C
# �Q�̐��� x, y ��ǂݍ��݁A������l�����������ɏo�͂���v���O�������쐬���ĉ������B
# �������A���̖��͈ȉ��Ɏ����悤�ɂ������̃f�[�^�Z�b�g���^�����邱�Ƃɒ��ӂ��ĉ������B
for i in range(10000):
    x, y = sorted([int(j) for j in input().split(" ")])
    if x == 0 and y == 0:
        break
    
    print(str(x) + " " + str(y))
    
