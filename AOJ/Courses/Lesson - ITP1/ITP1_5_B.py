# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_5_B
# �ȉ��̂悤�ȁA����H cm �悱 W cm �̘g��`���v���O�������쐬���ĉ������B
while(True):
    height, width = input().split(" ")
    if height == "0" and width == "0":
        break

    height = int(height)
    width = int(width)
    for i in range(height):
        width_sharp = ""
        for j in range(width):
            if i != 0 and i != height - 1 and j != 0 and j != width - 1:
                width_sharp += "."
            else:
                width_sharp += "#"
        
        print(width_sharp)

    print("")

