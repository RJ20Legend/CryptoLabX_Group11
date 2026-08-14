#include <iostream>
#include <string>

using namespace std;

struct Account {
    string username;
    string pin;
    double balance;
};

bool login(const Account& account) {
    string username;
    string pin;

    cout << "===== ATM LOGIN =====\n";

    cout << "Username: ";
    cin >> username;

    cout << "PIN: ";
    cin >> pin;

    if (username == account.username && pin == account.pin) {
        cout << "\nLogin successful!\n";
        return true;
    }

    cout << "\nInvalid username or PIN.\n";
    return false;
}

int main() {
    Account account{
        "customer",
        "1234",
        10000.0
    };

    if (!login(account)) {
        return 0;
    }

    cout << "\nWelcome to the ATM!\n";

    return 0;
}