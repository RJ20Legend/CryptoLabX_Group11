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

    if (username == "customer" && pin == "1234") {
        cout << "\nLogin successful!\n";
        return true;
    }

    cout << "\nInvalid username or PIN.\n";
    return false;
}

void checkBalance(const Account& account) {
    cout << "\nCurrent balance: Rs. "
         << account.balance << "\n";
}

void deposit(Account& account) {
    double amount;

    cout << "Enter deposit amount: ";
    cin >> amount;

    account.balance += amount;

    cout << "Deposit successful.\n";
}

void withdraw(Account& account) {
    double amount;

    cout << "Enter withdrawal amount: ";
    cin >> amount;

    if (amount <= account.balance) {
        account.balance -= amount;
        cout << "Withdrawal successful.\n";
    } else {
        cout << "Insufficient balance.\n";
    }
}

void changePin(Account& account) {
    string newPin;

    cout << "Enter new PIN: ";
    cin >> newPin;

    account.pin = newPin;

    cout << "PIN changed successfully.\n";
}

void showMenu(Account& account) {
    int choice;

    do {
        cout << "\n===== ATM MENU =====\n";
        cout << "1. Balance Inquiry\n";
        cout << "2. Deposit\n";
        cout << "3. Withdraw\n";
        cout << "4. Change PIN\n";
        cout << "5. Exit\n";
        cout << "Enter choice: ";

        cin >> choice;

        switch (choice) {
            case 1:
                checkBalance(account);
                break;

            case 2:
                deposit(account);
                break;

            case 3:
                withdraw(account);
                break;

            case 4:
                changePin(account);
                break;

            case 5:
                cout << "Thank you for using the ATM.\n";
                break;

            default:
                cout << "Invalid choice.\n";
        }

    } while (choice != 5);
}

int main() {
    Account account;

    account.username = "customer";
    account.pin = "1234";
    account.balance = 10000.0;

    // Authenticate user
    bool authenticated = login(account);

    if (!authenticated) {
        cout << "Access denied. Exiting ATM...\n";
        return 0;
    }

    showMenu(account);

    return 0;
}
