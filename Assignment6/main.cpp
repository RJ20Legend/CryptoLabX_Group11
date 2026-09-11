#include <iostream>
#include "analysis.h"

using namespace std;

int main()
{
    string ciphertext = "ABCXYZABCDEFXYZ";

    string cleaned = clean_ciphertext(ciphertext);

    vector<pair<string, vector<int>>> patterns =
        find_repeated_patterns(cleaned);

    cout << "Repeated Patterns:\n";

    for (auto& p : patterns)
    {
        cout << p.first << " -> ";

        for (int pos : p.second)
        {
            cout << pos << " ";
        }

        cout << endl;
    }

    return 0;
}