# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_4_D
# n�̐��� ai(i=1,2,...n)����͂��A�����̍ŏ��l�A�ő�l�A���v�l�����߂�v���O�������쐬���Ă��������B
count = int(input())
numbers = sorted([int(i) for i in input().split(" ")])
min = numbers[0]
max = numbers[count - 1]
sum = sum(numbers)
print(str(min) + " " + str(max) + " " + str(sum))
