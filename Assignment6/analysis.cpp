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