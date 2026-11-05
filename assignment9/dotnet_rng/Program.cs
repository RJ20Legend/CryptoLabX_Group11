using System.Security.Cryptography;

byte[] randomBytes = new byte[1024 * 1024];

RandomNumberGenerator.Fill(randomBytes);

string outputPath = "../generated_data/dotnet_rng.bin";

File.WriteAllBytes(outputPath, randomBytes);

Console.WriteLine($"Generated {randomBytes.Length} random bytes.");
Console.WriteLine($"Saved to: {outputPath}");