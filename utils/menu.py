from utils.logger import write_log


def coming_soon(option):
    print(f"\n{option} module coming soon...\n")


def start_menu():
    while True:
        print("=" * 40)
        print("         CryptoLabX")
        print("=" * 40)
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Attack")
        print("4. Analyze")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            write_log("Encrypt")
            coming_soon("Encryption")

        elif choice == "2":
            write_log("Decrypt")
            coming_soon("Decryption")

        elif choice == "3":
            write_log("Attack")
            coming_soon("Attack")

        elif choice == "4":
            write_log("Analyze")
            print("\nAnalysis module coming soon (Week 1 teammate module).\n")

        elif choice == "5":
            write_log("Exit")
            print("Goodbye.")
            break

        else:
            print("Invalid choice.\n")