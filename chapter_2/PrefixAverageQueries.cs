using System;
using System.Numerics;

class MyClass
{
    static void Main()
    {
        // Read N and totalQueries
        int[] input = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
        int totalCount = input[0];
        int totalQueries = input[1];

        // Read array
        long[] arr = Array.ConvertAll(Console.ReadLine().Split(), long.Parse);

        // Build prefix sum array
        long[] prefixSum = new long[n + 1];
        for (int i = 1; i <= totalCount; i++)
        {
            prefixSum[i] = prefixSum[i - 1] + arr[i - 1];
        }

        // Process queries
        for (int i = 0; i < totalQueries; i++)
        {
            int[] query = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int left = query[0];
            int right = query[1];

            long subArraySum = prefixSum[right] - prefixSum[left - 1];
            long length = right - left + 1;

            Console.WriteLine(subArraySum / length); // floor of mean
        }
    }
}
