# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_5_D
# 次のC++言語のプログラムと同じ動作をするプログラムを作成してください。ただし、goto 文は使わないで実装してみましょう。

# void call(int n){
#   int i = 1;
#  CHECK_NUM:
#   int x = i;
#   if ( x % 3 == 0 ){
#     cout << " " << i;
#     goto END_CHECK_NUM;
#   }
#  INCLUDE3:
#   if ( x % 10 == 3 ){
#     cout << " " << i;
#     goto END_CHECK_NUM;
#   }
#   x /= 10;
#   if ( x ) goto INCLUDE3;
#  END_CHECK_NUM:
#   if ( ++i <= n ) goto CHECK_NUM;
# 
#   cout << endl;
# }
# 3 <= number <= 10000

number = int(input())
output = ""
for i in range(number):
    j = i + 1
    if j % 3 == 0 or "3" in str(j):
        output += str(j) + " "

print(output)

