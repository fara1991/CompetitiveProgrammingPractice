# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_6_B
# 太郎が花子と一緒にトランプ遊びをしようとしたところ、52枚あるはずのカードが n 枚のカードしか手元にありません。これらの n 枚のカードを入力として、足りないカードを出力するプログラムを作成して下さい。
# 太郎が最初に持っていたトランプはジョーカーを除く52枚のカードです。
# 52枚のカードは、スペード、ハート、クラブ、ダイヤの４つの絵柄に分かれており、各絵柄には13のランクがあります。
number = int(input())
spade_cards = list(range(1,14))
heart_cards = list(range(1,14))
club_cards = list(range(1,14))
diamond_cards = list(range(1,14))
for i in range(number):
    card, card_number = input().split(" ")
    if card == "S":
        spade_cards.remove(int(card_number))
    elif card == "H":
        heart_cards.remove(int(card_number))
    elif card == "C":
        club_cards.remove(int(card_number))
    elif card == "D":
        diamond_cards.remove(int(card_number))

for i in range(len(spade_cards)):
    print("S " + str(spade_cards[i]))
for i in range(len(heart_cards)):
    print("H " + str(heart_cards[i]))
for i in range(len(club_cards)):
    print("C " + str(club_cards[i]))
for i in range(len(diamond_cards)):
    print("D " + str(diamond_cards[i]))

