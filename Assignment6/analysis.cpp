#include "analysis.h"
#include <bits/stdc++.h>

using namespace std;

string clean_ciphertext(const string& ciphertext)
{
    string cleaned;

    for (char ch : ciphertext)
    {
        if (isalpha(ch))
        {
            cleaned += toupper(ch);
        }
    }

    return cleaned;
}

vector<pair<string, vector<int>>> find_repeated_patterns(const string& ciphertext)
{
    vector<pair<string, vector<int>>> patterns;

    int patternLength = 3;

    for (int i = 0; i <= ciphertext.length() - patternLength; i++)
    {
        string pattern = ciphertext.substr(i, patternLength);

        bool alreadyStored = false;

        for (auto& p : patterns)
        {
            if (p.first == pattern)
            {
                p.second.push_back(i);
                alreadyStored = true;
                break;
            }
        }

        if (!alreadyStored)
        {
            vector<int> positions;
            positions.push_back(i);
            patterns.push_back({pattern, positions});
        }
    }

    vector<pair<string, vector<int>>> repeated;

    for (auto& p : patterns)
    {
        if (p.second.size() > 1)
        {
            repeated.push_back(p);
        }
    }

    return repeated;
}

vector<pair<string, vector<int>>> calculate_distances(
    const vector<pair<string, vector<int>>>& patterns)
{
    vector<pair<string, vector<int>>> distances;

    for (auto& pattern : patterns)
    {
        vector<int> patternDistances;

        for (int i = 1; i < pattern.second.size(); i++)
        {
            int distance = pattern.second[i] - pattern.second[i - 1];
            patternDistances.push_back(distance);
        }

        distances.push_back({pattern.first, patternDistances});
    }

    return distances;
}


vector<pair<int, vector<int>>> find_factors(
    const vector<pair<string, vector<int>>>& distances)
{
    vector<pair<int, vector<int>>> factors;

    for (auto& pattern : distances)
    {
        for (int distance : pattern.second)
        {
            vector<int> currentFactors;

            for (int i = 2; i <= distance; i++)
            {
                if (distance % i == 0)
                {
                    currentFactors.push_back(i);
                }
            }

            factors.push_back({distance, currentFactors});
        }
    }

    return factors;
}

vector<int> kasiski_analysis(
    const vector<pair<int, vector<int>>>& factors)
{
    vector<pair<int, int>> factorCount;

    for (auto& entry : factors)
    {
        for (int factor : entry.second)
        {
            bool found = false;

            for (auto& count : factorCount)
            {
                if (count.first == factor)
                {
                    count.second++;
                    found = true;
                    break;
                }
            }

            if (!found)
            {
                factorCount.push_back({factor, 1});
            }
        }
    }

    for (auto& count : factorCount)
    {
        cout << "Factor " << count.first
             << " occurs " << count.second << " times" << endl;
    }

    int maxCount = 0;

    for (auto& count : factorCount)
    {
        if (count.second > maxCount)
        {
            maxCount = count.second;
        }
    }

    vector<int> candidates;

    for (auto& count : factorCount)
    {
        if (count.second == maxCount && count.first >= 2)
        {
            candidates.push_back(count.first);
        }
    }

    return candidates;
}

vector<string> split_into_groups(
    const string& ciphertext,
    int keyLength)
{
    vector<string> groups(keyLength);

    for (int i = 0; i < ciphertext.length(); i++)
    {
        groups[i % keyLength] += ciphertext[i];
    }

    return groups;
}

vector<vector<int>> frequency_analysis(
    const vector<string>& groups)
{
    vector<vector<int>> frequencies;

    for (string group : groups)
    {
        vector<int> count(26, 0);

        for (char ch : group)
        {
            count[ch - 'A']++;
        }

        frequencies.push_back(count);
    }

    return frequencies;
}

int find_shift(const vector<int>& frequency)
{
    double englishFrequency[26] =
    {
        8.17, 1.49, 2.78, 4.25, 12.70, 2.23,
        2.02, 6.09, 6.97, 0.15, 0.77, 4.03,
        2.41, 6.75, 7.51, 1.93, 0.10, 5.99,
        6.33, 9.06, 2.76, 0.98, 2.36, 0.15,
        1.97, 0.07
    };

    int total = 0;

    for (int count : frequency)
    {
        total += count;
    }

    if (total == 0)
    {
        return 0;
    }

    double bestScore = 1e18;
    int bestShift = 0;

    for (int shift = 0; shift < 26; shift++)
    {
        double chiSquare = 0;

        for (int i = 0; i < 26; i++)
        {
            int decryptedIndex = (i - shift + 26) % 26;

            double expected =
                total * englishFrequency[decryptedIndex] / 100.0;

            double observed = frequency[i];

            if (expected > 0)
            {
                chiSquare +=
                    (observed - expected) *
                    (observed - expected) /
                    expected;
            }
        }

        if (chiSquare < bestScore)
        {
            bestScore = chiSquare;
            bestShift = shift;
        }
    }

    return bestShift;
}