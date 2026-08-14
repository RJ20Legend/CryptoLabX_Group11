from utils.logger import write_log
from analysis.file_analyzer import format_analysis
from utils.logger import write_log
from pathlib import Path

def encrypt():
    write_log("Encrypt")
    print("\nEncryption module coming soon.\n")


def decrypt():
    write_log("Decrypt")
    print("\nDecryption module coming soon.\n")


def attack():
    write_log("Attack")
    print("\nAttack module coming soon.\n")


def analyze():
    write_log("Analyze")

    datasets = Path("datasets")

    files = list(datasets.glob("*.txt"))

    if not files:
        print("\nNo text files found in datasets folder.\n")
        return

    print("\nAvailable files:")
    for i, file in enumerate(files, start=1):
        print(f"{i}. {file.name}")

    try:
        choice = int(input("\nSelect a file: "))

        if choice < 1 or choice > len(files):
            print("\nInvalid selection.\n")
            return

        print()
        print(format_analysis(files[choice - 1]))
        print()

    except ValueError:
        print("\nPlease enter a valid number.\n")


def exit_program():
    write_log("Exit")
    print("\nThank you for using CryptoLabX.")
    exit()


def display_menu():
    print("=" * 45)
    print("             CryptoLabX")
    print("=" * 45)
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Attack")
    print("4. Analyze")
    print("5. Exit")
    print("=" * 45)


def start_menu():

    menu = {
        "1": encrypt,
        "2": decrypt,
        "3": attack,
        "4": analyze,
        "5": exit_program
    }

    while True:

        display_menu()

        choice = input("Enter your choice: ").strip()

        action = menu.get(choice)

        if action:
            action()
        else:
            print("\nInvalid choice. Try again.\n")