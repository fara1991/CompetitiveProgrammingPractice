# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_6_C
# �`��w�͂P�t���A�P�O�����A�R�K���Ă̌��ɂS�����Ǘ����Ă��܂��B���ɂ̓����E�ދ��̏���ǂݍ��݁A�e�����̓����Ґ����o�͂���v���O�������쐬���ĉ������B
# n���̏�񂪗^�����܂��B�e���ł́A�S�̐���b, f, r, v���^�����܂��B����́Ab��f�K��r�Ԗڂ̕�����v�l���ǉ��œ����������Ƃ������܂��Bv�����̒l�̏ꍇ�A-v�l�ދ��������Ƃ������܂��B
# �ŏ��A�S�Ă̕����ɂ͒N���������Ă��Ȃ����̂Ƃ��܂��B
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

