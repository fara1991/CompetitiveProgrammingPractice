# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_1_D
# 秒単位の時間 Sが与えられるので、h:m:s の形式へ変換して出力してください。
# ここで、hは時間、mは60未満の分、sは60未満の秒とします。
second = int(input())
h, h_mod = divmod(second, 60 * 60)
m, m_mod = divmod(h_mod, 60)
s = m_mod
print(str(h) + ":" + str(m) + ":" + str(s))
