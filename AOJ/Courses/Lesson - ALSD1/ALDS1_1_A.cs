// https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_1_A
// N 個の要素を含む数列 A を昇順に並び替える挿入ソートのプログラムを作成してください。
using System;
using System.Linq;

public class InsertionSort{
    public static void Main(){
        // Insertion Sort
        var sequenceLength = int.Parse(Console.ReadLine().Trim());
        var numberListString = Console.ReadLine().Trim();
        Console.WriteLine(numberListString);
        var numberList = numberListString.Split(' ').Select(int.Parse).ToArray();

        for (var i = 1; i < sequenceLength; i++){
            // ソート前のi番目数値を保持
            var tempNumber = numberList[i];
            var j = i - 1;
            while(j >= 0 && numberList[j] > tempNumber) {
                // 左より右の数値が大きければ左の数値を上書き
                numberList[j + 1] = numberList[j];
                j--;
            }
            // 入れ替え終えたらソート済みの一番右を上書き
            numberList[j + 1] = tempNumber;
            // LINQ練習
            Console.WriteLine(String.Join(" ", numberList.Select(x => x.ToString()).ToArray()));
        }
    }
}
