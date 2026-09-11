#include <iostream>
#include "analysis.h"

using namespace std;

int main()
{
    string ciphertext = "ABCXYZABCDEFXYZ";

    string cleaned = clean_ciphertext(ciphertext);

    vector<pair<string, vector<int>>> patterns =
        find_repeated_patterns(cleaned);

    vector<pair<string, vector<int>>> distances =
        calculate_distances(patterns);

    vector<pair<int, vector<int>>> factors =
        find_factors(distances);

    vector<int> candidates =
        kasiski_analysis(factors);

    cout << "\nCandidate Key Lengths:\n";

    for (int length : candidates)
    {
        cout << length << " ";
    }

    cout << endl;

    return 0;
}