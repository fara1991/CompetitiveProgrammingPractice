# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_1_D
# �b�P�ʂ̎��� S���^������̂ŁAh:m:s �̌`���֕ϊ����ďo�͂��Ă��������B
# �����ŁAh�͎��ԁAm��60�����̕��As��60�����̕b�Ƃ��܂��B
second = int(input())
h, h_mod = divmod(second, 60 * 60)
m, m_mod = divmod(h_mod, 60)
s = m_mod
print(str(h) + ":" + str(m) + ":" + str(s))
