# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_6_B
# ���Y���Ԏq�ƈꏏ�Ƀg�����v�V�т����悤�Ƃ����Ƃ���A52������͂��̃J�[�h�� n ���̃J�[�h�����茳�ɂ���܂���B������ n ���̃J�[�h����͂Ƃ��āA����Ȃ��J�[�h���o�͂���v���O�������쐬���ĉ������B
# ���Y���ŏ��Ɏ����Ă����g�����v�̓W���[�J�[������52���̃J�[�h�ł��B
# 52���̃J�[�h�́A�X�y�[�h�A�n�[�g�A�N���u�A�_�C���̂S�̊G���ɕ�����Ă���A�e�G���ɂ�13�̃����N������܂��B
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

