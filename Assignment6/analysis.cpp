#include "analysis.h"
#include <cctype>

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

