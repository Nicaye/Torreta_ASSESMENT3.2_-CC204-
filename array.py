
# ==========================================
# ASSESSMENT 3.2 - ARRAY
# LAST NAME: TORRETA
# ==========================================

def array_program():
    original = ["T", "O", "R", "R", "E", "T", "A"]
    letters = original.copy()

    while True:
        print("\n" + "═" * 42)
        print("             ARRAY OPERATIONS")
        print("═" * 42)
        print(" Current Array:", letters)
        print("─" * 42)
        print(" [1] ADD LETTER")
        print(" [2] REMOVE LAST LETTER")
        print(" [3] REMOVE ALL LETTERS")
        print(" [4] RESET ARRAY")
        print(" [5] BACK")
        print("═" * 42)

        choice = input("\n Choose an option (1-5): ").strip()

        if choice == "1":
            letter = input(" Enter a letter: ").strip().upper()

            if len(letter) == 1 and letter.isalpha():
                letters.append(letter)
                print(f"\n + {letter} added successfully!")
            else:
                print("\n Please enter one valid letter.")

        elif choice == "2":
            if letters:
                removed = letters.pop()
                print(f"\n - {removed} removed successfully!")
            else:
                print("\n The array is empty!")

        elif choice == "3":
            if letters:
                while letters:
                    removed = letters.pop()
                    print(f" Removed: {removed}")
                print("\n Array cleared successfully!")
            else:
                print("\n The array is already empty!")

        elif choice == "4":
            letters = original.copy()
            print("\n Array restored to TORRETA!")

        elif choice == "5":
            break

        else:
            print("\n Invalid choice. Please try again.")

        print("\n Current Array:", letters)


if __name__ == "__main__":
    array_program()
