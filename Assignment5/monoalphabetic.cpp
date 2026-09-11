#include "monoalphabetic.h"

#include <iostream>
#include <iomanip>
#include <cctype>

using namespace std;

void encryptText(const string& plaintext,
                 const string& key,
                 string& ciphertext)
{
    ciphertext = "";

    for (int i = 0; i < (int)plaintext.length(); i++)
    {
        char ch = plaintext[i];

        if (ch >= 'A' && ch <= 'Z')
        {
            ciphertext += key[ch - 'A'];
        }
        else if (ch >= 'a' && ch <= 'z')
        {
            char upper = ch - 'a' + 'A';
            char encrypted = key[upper - 'A'];

            ciphertext += encrypted + ('a' - 'A');
        }
        else
        {
            ciphertext += ch;
        }
    }
}

void frequency_analysis(const string& ciphertext)
{
    int frequency[26] = {0};
    int total = 0;

    for (int i = 0; i < (int)ciphertext.length(); i++)
    {
        char ch = ciphertext[i];

        if (ch >= 'a' && ch <= 'z')
            ch = ch - 'a' + 'A';

        if (ch >= 'A' && ch <= 'Z')
        {
            frequency[ch - 'A']++;
            total++;
        }
    }

    vector<pair<char, int>> freq;

    for (int i = 0; i < 26; i++)
        freq.push_back({char('A' + i), frequency[i]});

    // Manual sorting in descending order
    for (int i = 0; i < 26; i++)
    {
        for (int j = i + 1; j < 26; j++)
        {
            if (freq[j].second > freq[i].second)
            {
                pair<char, int> temp = freq[i];
                freq[i] = freq[j];
                freq[j] = temp;
            }
        }
    }

    cout << "\n===== FREQUENCY ANALYSIS =====\n";
    cout << "Letter\tCount\tPercentage\n";

    for (int i = 0; i < 26; i++)
    {
        double percentage = 0;

        if (total != 0)
            percentage = (freq[i].second * 100.0) / total;

        cout << freq[i].first << "\t"
             << freq[i].second << "\t"
             << fixed << setprecision(2)
             << percentage << "%\n";
    }

    cout << "\nMost frequent letters:\n";

    for (int i = 0; i < 5; i++)
    {
        if (freq[i].second > 0)
            cout << freq[i].first << " ";
    }

    cout << "\n";
}

void word_frequency_analysis(const string& ciphertext)
{
    map<string, int> wordCount;
    string word = "";

    for (int i = 0; i <= (int)ciphertext.length(); i++)
    {
        char ch = (i < (int)ciphertext.length())
                    ? ciphertext[i]
                    : ' ';

        if (isalpha(ch))
        {
            if (ch >= 'a' && ch <= 'z')
                ch = ch - 'a' + 'A';

            word += ch;
        }
        else
        {
            if (!word.empty())
            {
                wordCount[word]++;
                word = "";
            }
        }
    }

    cout << "\n===== WORD FREQUENCY ANALYSIS =====\n";

    for (auto entry : wordCount)
    {
        if (entry.second > 1)
        {
            cout << entry.first
                 << " -> "
                 << entry.second
                 << "\n";
        }
    }

    cout << "\n===== SHORT WORDS =====\n";

    for (auto entry : wordCount)
    {
        int len = entry.first.length();

        if (len >= 1 && len <= 3)
        {
            cout << entry.first
                 << " -> "
                 << entry.second
                 << "\n";
        }
    }
}

string getPattern(const string& word)
{
    map<char, int> patternMap;
    string pattern = "";
    int nextNumber = 1;

    for (int i = 0; i < (int)word.length(); i++)
    {
        char ch = word[i];

        if (patternMap.find(ch) == patternMap.end())
        {
            patternMap[ch] = nextNumber;
            nextNumber++;
        }

        pattern += char('0' + patternMap[ch]);
    }

    return pattern;
}

void pattern_analysis(const string& ciphertext)
{
    cout << "\n===== PATTERN ANALYSIS =====\n";

    string word = "";

    for (int i = 0; i <= (int)ciphertext.length(); i++)
    {
        char ch = (i < (int)ciphertext.length())
                    ? ciphertext[i]
                    : ' ';

        if (isalpha(ch))
        {
            if (ch >= 'a' && ch <= 'z')
                ch = ch - 'a' + 'A';

            word += ch;
        }
        else
        {
            if (!word.empty())
            {
                cout << word
                     << " -> "
                     << getPattern(word)
                     << "\n";

                word = "";
            }
        }
    }
}

string apply_substitution(const string& ciphertext,
                          const map<char, char>& substitution)
{
    string result = "";

    for (int i = 0; i < (int)ciphertext.length(); i++)
    {
        char ch = ciphertext[i];
        char upper = ch;

        if (ch >= 'a' && ch <= 'z')
            upper = ch - 'a' + 'A';

        if (upper >= 'A' && upper <= 'Z')
        {
            if (substitution.find(upper) != substitution.end())
            {
                char replacement = substitution.at(upper);

                if (ch >= 'a' && ch <= 'z')
                    replacement = replacement - 'A' + 'a';

                result += replacement;
            }
            else
            {
                result += '_';
            }
        }
        else
        {
            result += ch;
        }
    }

    return result;
}

void display_partial_plaintext(
    const string& ciphertext,
    const map<char, char>& substitution)
{
    cout << "\n===== PARTIAL PLAINTEXT =====\n";

    string result = apply_substitution(ciphertext, substitution);

    cout << result << "\n";
}

bool verify_solution(const string& plaintext,
                     const string& ciphertext,
                     const string& key)
{
    string generatedCiphertext;

    encryptText(plaintext, key, generatedCiphertext);

    if (generatedCiphertext == ciphertext)
    {
        cout << "\nVerification successful!\n";
        cout << "Re-encrypted ciphertext matches the original ciphertext.\n";
        return true;
    }

    cout << "\nVerification failed!\n";
    cout << "Re-encrypted ciphertext does not match.\n";

    return false;
}