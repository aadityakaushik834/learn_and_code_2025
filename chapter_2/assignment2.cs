using System;
using System.Numerics;

class MyClass
{
    static void Main()
    {
        // Read N and Q
        int[] input = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
        int n = input[0];
        int q = input[1];

        // Read array
        long[] arr = Array.ConvertAll(Console.ReadLine().Split(), long.Parse);

        // Build prefix sum array
        long[] prefixSum = new long[n + 1];
        for (int i = 1; i <= n; i++)
        {
            prefixSum[i] = prefixSum[i - 1] + arr[i - 1];
        }

        // Process queries
        for (int i = 0; i < q; i++)
        {
            int[] query = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int l = query[0];
            int r = query[1];

            long subArraySum = prefixSum[r] - prefixSum[l - 1];
            long length = r - l + 1;

            Console.WriteLine(subArraySum / length); // floor of mean
        }
    }
}
