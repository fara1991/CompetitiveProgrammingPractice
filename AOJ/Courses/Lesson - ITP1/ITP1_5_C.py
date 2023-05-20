# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_5_C
# 以下のような、たてH cm よこ W cm のチェック柄の長方形を描くプログラムを作成して下さい。

#	 #.#.#.#.#.
#	 .#.#.#.#.#
#	 #.#.#.#.#.
#	 .#.#.#.#.#
#	 #.#.#.#.#.
#	 .#.#.#.#.#

# 上図は、たて 6 cm よこ 10 cm の長方形を表しています。
# 長方形の左上が "#" となるように描いて下さい。
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

