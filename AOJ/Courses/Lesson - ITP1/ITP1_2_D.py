# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_2_D
# �����`�̒��ɉ~���܂܂�邩�𔻒肷��v���O�������쐬���Ă��������B���̂悤�ɁA�����`�͍����̒��_�����_�Ƃ��A�E��̒��_�̍��W (W,H) ���^�����܂��B�܂��A�~�͂��̒��S�̍��W (x,y) �Ɣ��a r �ŗ^�����܂��B
rectangle_width, rectangle_height, circle_center_x, circle_center_y, circle_radius = [int(i) for i in input().split(" ")]
if (
    circle_center_x - circle_radius < 0 or
    circle_center_x + circle_radius > rectangle_width or
    circle_center_y - circle_radius < 0 or
    circle_center_y + circle_radius > rectangle_height
):
    print("No")
else:
    print("Yes")
    
