
# ==========================================
# ASSESSMENT 3.2 - LINEAR DATA STRUCTURES
# LAST NAME: TORRETA
# ==========================================

import subprocess
import sys
from pathlib import Path

LINE = "═" * 42

PROGRAMS = {
    "1": ("ARRAY", "array.py"),
    "2": ("LINKED LIST", "linkedlist.py"),
    "3": ("STACK", "stack.py"),
    "4": ("QUEUE", "queue.py")
}


def main_menu():
    while True:
        print("\n")
        print("╔" + LINE + "╗")
        print("║" + " LINEAR DATA STRUCTURES ".center(42) + "║")
        print("║" + "       T O R R E T A".center(42) + "║")
        print("╠" + LINE + "╣")
        print("║" + " [1]  ARRAY".ljust(42) + "║")
        print("║" + " [2]  LINKED LIST".ljust(42) + "║")
        print("║" + " [3]  STACK".ljust(42) + "║")
        print("║" + " [4]  QUEUE".ljust(42) + "║")
        print("║" + " [5]  EXIT".ljust(42) + "║")
        print("╚" + LINE + "╝")

        choice = input("\n Choose [1-5]: ").strip()

        if choice in PROGRAMS:
            name, filename = PROGRAMS[choice]
            file_path = Path(__file__).resolve().parent / filename

            if file_path.exists():
                subprocess.run([sys.executable, str(file_path)])
            else:
                print(f"\n File not found: {filename}")

        elif choice == "5":
            print("\n Thank you for using the program!")
            break

        else:
            print("\n Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
