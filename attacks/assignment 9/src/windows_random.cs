using System;
using System.IO;
using System.Security.Cryptography;

class RandomGenerator
{
    static void Main()
    {
        byte[] data = new byte[1024 * 1024];

        RandomNumberGenerator.Fill(data);

        Directory.CreateDirectory("outputs");

        File.WriteAllBytes("outputs/windows_cng.bin", data);

        Console.WriteLine("Generated 1 MB using Windows CNG/.NET");
    }
}
