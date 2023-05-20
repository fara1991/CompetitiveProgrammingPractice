# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_5_C
# �ȉ��̂悤�ȁA����H cm �悱 W cm �̃`�F�b�N���̒����`��`���v���O�������쐬���ĉ������B

#	 #.#.#.#.#.
#	 .#.#.#.#.#
#	 #.#.#.#.#.
#	 .#.#.#.#.#
#	 #.#.#.#.#.
#	 .#.#.#.#.#

# ��}�́A���� 6 cm �悱 10 cm �̒����`��\���Ă��܂��B
# �����`�̍��オ "#" �ƂȂ�悤�ɕ`���ĉ������B
while(True):
    height, width = input().split(" ")
    if height == "0" and width == "0":
        break

    height = int(height)
    width = int(width)
    is_sharp_text = True
    for i in range(height):
        width_sharp = ""
        for j in range(width):
            if is_sharp_text:
                width_sharp += "#"
            else:
                width_sharp += "."
            is_sharp_text = not is_sharp_text

        if width % 2 == 0:
            is_sharp_text = not is_sharp_text
        print(width_sharp)

    print("")

