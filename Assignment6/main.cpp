#include <iostream>
#include <vector>
#include "analysis.h"
#include "vigenere.h"

using namespace std;

int main()
{
    string ciphertext =
        "DAZFI SFSPA VQLSN PXYSZ WXALC DAFGQ UISMT PHZGA "
        "MKTTF TCCFX KFCRG GLPFE TZMMM ZOZDE ADWVZ WMWKV "
        "GQSOH QSVHP WFKLS LEASE PWHMJ EGKPU RVSXJ XVBWV "
        "POSDE TEQTX OBZIK WCXLW NUOVJ MJCLL OEOFA ZENVM "
        "JILOW ZEKAZ EJAQD ILSWW ESGUG KTZGQ ZVRMN WTQSE "
        "OTKTK PBSTA MQVER MJEGL JQRTL GFJYG SPTZP GTACM "
        "OECBX SESCI YGUFP KVILL TWDKS ZODFW FWEAA PQTFS "
        "TQIRG MPMEL RYELH QSVWB AWMOS DELHM UZGPG YEKZU "
        "KWTAM ZJMLS EVJQT GLAWV OVVXH KWQIL IEUYS ZWXAH "
        "HUSZO GMUZQ CIMVZ UVWIF JJHPW VXFSE TZEDF";

    // Step 1: Clean ciphertext
    string cleaned = clean_ciphertext(ciphertext);

    cout << "========================================" << endl;
    cout << "   VIGENERE CIPHER CRYPTANALYSIS" << endl;
    cout << "========================================" << endl;

    cout << "\nCleaned ciphertext length: "
         << cleaned.length() << endl;

    // Step 2: Find repeated patterns
    vector<pair<string, vector<int>>> patterns =
        find_repeated_patterns(cleaned);

    cout << "\n--- Repeated Patterns ---" << endl;

    for (auto& pattern : patterns)
    {
        cout << pattern.first << " : ";

        for (int position : pattern.second)
        {
            cout << position << " ";
        }

        cout << endl;
    }

    // Step 3: Calculate distances
    vector<pair<string, vector<int>>> distances =
        calculate_distances(patterns);

    cout << "\n--- Distances ---" << endl;

    for (auto& entry : distances)
    {
        cout << entry.first << " : ";

        for (int distance : entry.second)
        {
            cout << distance << " ";
        }

        cout << endl;
    }

    // Step 4: Find factors
    vector<pair<int, vector<int>>> factors =
        find_factors(distances);

    cout << "\n--- Factors ---" << endl;

    for (auto& entry : factors)
    {
        cout << "Distance " << entry.first << " : ";

        for (int factor : entry.second)
        {
            cout << factor << " ";
        }

        cout << endl;
    }

    // Step 5: Kasiski analysis
    vector<int> keyLengthCandidates =
        kasiski_analysis(factors);

    cout << "\n--- Kasiski Analysis ---" << endl;

    cout << "Possible key lengths: ";

    for (int length : keyLengthCandidates)
    {
        cout << length << " ";
    }

    cout << endl;

    if (keyLengthCandidates.empty())
    {
        cout << "Could not determine key length." << endl;
        return 1;
    }
    cout << "\n--- Index of Coincidence Analysis (Bonus) ---\n";

for (int length = 1; length <= 15; length++)
{
    vector<string> groups =
        split_into_groups(cleaned, length);

    double totalIC = 0.0;

    for (const string& group : groups)
    {
        totalIC += calculate_ic(group);
    }

    double averageIC =
        totalIC / groups.size();

    cout << "Key Length "
         << length
         << " -> Average IC = "
         << averageIC
         << endl;
}
    // Use the most probable Kasiski candidate
    int keyLength = keyLengthCandidates[0];

    cout << "Selected key length: "
         << keyLength << endl;

    // Step 6: Split ciphertext into groups
    vector<string> groups =
        split_into_groups(cleaned, keyLength);

    cout << "\n--- Ciphertext Groups ---" << endl;

    for (int i = 0; i < groups.size(); i++)
    {
        cout << "Group " << i + 1 << ": "
             << groups[i] << endl;
    }

    // Step 7: Frequency analysis
    vector<vector<int>> frequencies =
        frequency_analysis(groups);

    cout << "\n--- Frequency Analysis ---" << endl;

    for (int i = 0; i < frequencies.size(); i++)
    {
        cout << "\nGroup " << i + 1 << ":" << endl;

        for (int j = 0; j < 26; j++)
        {
            cout << char('A' + j)
                 << " : "
                 << frequencies[i][j]
                 << endl;
        }
    }

    // Step 8 & 9: Find shifts and recover key
    cout << "\n--- Shift Analysis ---" << endl;

    for (int i = 0; i < frequencies.size(); i++)
    {
        int shift = find_shift(frequencies[i]);

        cout << "Group " << i + 1
             << " -> Shift: " << shift
             << " -> Key letter: "
             << char('A' + shift)
             << endl;
    }

    string key = find_key(frequencies);

    cout << "\nRecovered key: "
         << key << endl;

    // Step 10: Decrypt
    string plaintext =
        vigenere_decrypt(cleaned, key);

    cout << "\n--- Recovered Plaintext ---" << endl;
    cout << plaintext << endl;

    // Step 11: Verify
    bool verified =
        verify(cleaned, plaintext, key);

    cout << "\n--- Verification ---" << endl;

    if (verified)
    {
        cout << "SUCCESS: Re-encrypted ciphertext "
             << "matches original ciphertext." << endl;
    }
    else
    {
        cout << "FAILED: Re-encrypted ciphertext "
             << "does not match original ciphertext." << endl;
    }

    cout << "\n========================================" << endl;

    return 0;
}