# https://onlinejudge.u-aizu.ac.jp/challenges/sources/UOA/PCKWU/1041
while(True):
    input_word = input()
    if input_word == "END OF INPUT":
        break

    word_list = input_word.split(" ")
    word_count = ""
    for i in range(len(word_list)):
        word_count += str(len(word_list[i]))
    print(word_count)

