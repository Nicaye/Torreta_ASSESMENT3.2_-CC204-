
# ==========================================
# ASSESSMENT 3.2 - QUEUE (FIFO)
# LAST NAME: TORRETA
# ==========================================

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, letter):
        self.items.append(letter)

    def dequeue(self):
        if self.is_empty():
            return None

        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return None

        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def clear(self):
        self.items.clear()

    def restore(self):
        self.items = list("TORRETA")

    def display(self):
        if self.is_empty():
            return "Empty"

        return "FRONT [" + ", ".join(self.items) + "] REAR"


def queue_program():
    queue = Queue()
    queue.restore()

    while True:
        print("\n" + "═" * 42)
        print("               QUEUE (FIFO)")
        print("═" * 42)
        print(" Current Queue:")
        print(" ", queue.display())
        print("─" * 42)
        print(" [1] ENQUEUE LETTER")
        print(" [2] DEQUEUE LETTER")
        print(" [3] VIEW FRONT")
        print(" [4] CLEAR QUEUE")
        print(" [5] RESET QUEUE")
        print(" [6] BACK")
        print("═" * 42)

        choice = input("\n Choose an option (1-6): ").strip()

        if choice == "1":
            letter = input(" Enter a letter: ").strip().upper()

            if len(letter) == 1 and letter.isalpha():
                queue.enqueue(letter)
                print(f"\n + '{letter}' added to the rear!")
            else:
                print("\n Please enter one valid letter.")

        elif choice == "2":
            removed = queue.dequeue()

            if removed is not None:
                print(f"\n - '{removed}' removed from the front!")
            else:
                print("\n The queue is empty!")

        elif choice == "3":
            first = queue.front()

            if first is not None:
                print(f"\n FRONT ELEMENT: {first}")
            else:
                print("\n The queue is empty!")

        elif choice == "4":
            queue.clear()
            print("\n Queue cleared successfully!")

        elif choice == "5":
            queue.restore()
            print("\n Queue restored to TORRETA!")

        elif choice == "6":
            break

        else:
            print("\n Invalid choice. Please try again.")

        print("\n Updated Queue:")
        print(" ", queue.display())


if __name__ == "__main__":
    queue_program()
