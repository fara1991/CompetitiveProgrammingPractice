// https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_1_B
// ２つの自然数 x, y を入力とし、それらの最大公約数を求めるプログラムを作成してください。
using System;

public class GreatestCommonDivisor{
    public static void Main(){
        // ユークリッドの互除法
        var list = Console.ReadLine().Trim().Split(' ');
        var x = int.Parse(list[0]);
        var y = int.Parse(list[1]);
        if (x < y) {
            var _x = x;
            x = y;
            y = _x;
        }
        while(y != 0) {
            var r = x % y;
            x = y;
            y = r;
        }
        
        Console.WriteLine(x);
    }
}
