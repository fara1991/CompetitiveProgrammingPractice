# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_2_D
# 長方形の中に円が含まれるかを判定するプログラムを作成してください。次のように、長方形は左下の頂点を原点とし、右上の頂点の座標 (W,H) が与えられます。また、円はその中心の座標 (x,y) と半径 r で与えられます。
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
    
