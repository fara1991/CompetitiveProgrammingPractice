# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_5_A
# ����H cm �悱 W cm �̒����`��`���v���O�������쐬���ĉ������B
# 1 cm �~ 1cm �̒����`�� '#'�ŕ\���܂��B
while(True):
    height, width = input().split(" ")
    if height == "0" and width == "0":
        break

    height = int(height)
    width = int(width)
    for i in range(height):
        width_sharp = ""
        for j in range(width):
            width_sharp += "#"
        
        print(width_sharp)

    print("")

