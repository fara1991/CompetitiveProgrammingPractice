# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_1_C
# ���� a cm �悱 b cm �̒����`�̖ʐςƎ��̒��������߂�v���O�������쐬���ĉ������B
input_rectangle = input().split(" ")
v = int(input_rectangle[0])
h = int(input_rectangle[1])
print(str(v * h) + " " + str((v + h) * 2))
