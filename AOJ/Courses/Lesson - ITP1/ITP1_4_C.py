# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_4_C
# ２つの整数 a, b と１つの演算子 op を読み込んで、a op b を計算するプログラムを作成して下さい。ただし、演算子 op は、"+"(和)、"-"(差)、"*"(積)、"/"(商)、のみとし、割り算で割り切れない場合は、小数点以下を切り捨てたものを計算結果とします。
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

