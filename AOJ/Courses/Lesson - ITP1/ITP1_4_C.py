# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_4_C
# �Q�̐��� a, b �ƂP�̉��Z�q op ��ǂݍ���ŁAa op b ���v�Z����v���O�������쐬���ĉ������B�������A���Z�q op �́A"+"(�a)�A"-"(��)�A"*"(��)�A"/"(��)�A�݂̂Ƃ��A����Z�Ŋ���؂�Ȃ��ꍇ�́A�����_�ȉ���؂�̂Ă����̂��v�Z���ʂƂ��܂��B
while(True):
    a, op, b = input().split(" ")
    if op == "+":
        print(str(int(a) + int(b)))
    elif op == "-":
        print(str(int(a) - int(b)))
    elif op == "*":
        print(str(int(a) * int(b)))
    elif op == "/":
        print(str(int(a) // int(b)))
    elif op == "?":
        break

