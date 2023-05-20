// https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_1_C
// n 個の整数を読み込み、それらに含まれる素数の数を出力するプログラムを作成してください。
using System;
using System.Linq;

public class PrimeNumber{
    public static void Main(){
        var primeCount = 0;
        string n;
        while((n = Console.ReadLine()) != null){
            var number = int.Parse(n.Trim());
            if (!IsPrime(number)) continue;

            primeCount++;
        }
        
        Console.WriteLine(primeCount);
    }
    
    static bool IsPrime(int number){
        if (number <= 1){
            return false;
        }

        if (number == 2){
            return true;
        }

        if (number % 2 == 0){
            return false;
        }

        for (int i = 3; i * i <= number; i += 2){
            if (number % i == 0){
                return false;
            }
        }

        return true;
    }
}
