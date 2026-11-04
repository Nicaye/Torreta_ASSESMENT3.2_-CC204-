
# ==========================================
# ASSESSMENT 3.2 - STACK (LIFO)
# LAST NAME: TORRETA
# ==========================================

class Stack:
    def __init__(self):
        self.items = []

    def push(self, letter):
        self.items.append(letter)

    def pop(self):
        if self.is_empty():
            return None

        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None

        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def clear(self):
        self.items.clear()

    def restore(self):
        self.items = list("TORRETA")

    def display(self):
        if self.is_empty():
            return "Empty"

        return "BOTTOM [" + ", ".join(self.items) + "] TOP"


def stack_program():
    stack = Stack()
    stack.restore()

    while True:
        print("\n" + "═" * 42)
        print("               STACK (LIFO)")
        print("═" * 42)
        print(" Current Stack:")
        print(" ", stack.display())
        print("─" * 42)
        print(" [1] PUSH LETTER")
        print(" [2] POP LETTER")
        print(" [3] PEEK TOP")
        print(" [4] CLEAR STACK")
        print(" [5] RESET STACK")
        print(" [6] BACK")
        print("═" * 42)

        choice = input("\n Choose an option (1-6): ").strip()

        if choice == "1":
            letter = input(" Enter a letter: ").strip().upper()

            if len(letter) == 1 and letter.isalpha():
                stack.push(letter)
                print(f"\n + '{letter}' pushed onto the stack!")
            else:
                print("\n Please enter one valid letter.")

        elif choice == "2":
            removed = stack.pop()

            if removed is not None:
                print(f"\n - '{removed}' popped from the stack!")
            else:
                print("\n The stack is empty!")

        elif choice == "3":
            top = stack.peek()

            if top is not None:
                print(f"\n TOP ELEMENT: {top}")
            else:
                print("\n The stack is empty!")

        elif choice == "4":
            stack.clear()
            print("\n Stack cleared successfully!")

        elif choice == "5":
            stack.restore()
            print("\n Stack restored to TORRETA!")

        elif choice == "6":
            break

        else:
            print("\n Invalid choice. Please try again.")

        print("\n Updated Stack:")
        print(" ", stack.display())


if __name__ == "__main__":
    stack_program()
