
# ==========================================
# ASSESSMENT 3.2 - LINKED LIST
# LAST NAME: TORRETA
# ==========================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def delete_beginning(self):
        if self.head is None:
            return None

        removed = self.head.data
        self.head = self.head.next
        return removed

    def display(self):
        if self.head is None:
            return "Empty"

        elements = []
        current = self.head

        while current:
            elements.append(str(current.data))
            current = current.next

        return " -> ".join(elements) + " -> None"

    def clear(self):
        self.head = None

    def restore(self):
        self.clear()

        for letter in "TORRETA":
            self.insert_end(letter)


def linked_list_program():
    linked = LinkedList()
    linked.restore()

    while True:
        print("\n" + "═" * 42)
        print("              LINKED LIST")
        print("═" * 42)
        print(" Current List:")
        print(" ", linked.display())
        print("─" * 42)
        print(" [1] INSERT LETTER")
        print(" [2] DELETE FIRST NODE")
        print(" [3] DELETE ALL NODES")
        print(" [4] RESET LIST")
        print(" [5] BACK")
        print("═" * 42)

        choice = input("\n Choose an option (1-5): ").strip()

        if choice == "1":
            letter = input(" Enter a letter: ").strip().upper()

            if len(letter) == 1 and letter.isalpha():
                linked.insert_end(letter)
                print(f"\n + Node '{letter}' inserted successfully!")
            else:
                print("\n Please enter one valid letter.")

        elif choice == "2":
            removed = linked.delete_beginning()

            if removed is not None:
                print(f"\n - Node '{removed}' deleted successfully!")
            else:
                print("\n The linked list is empty!")

        elif choice == "3":
            if linked.head is not None:
                linked.clear()
                print("\n All nodes deleted successfully!")
            else:
                print("\n The linked list is already empty!")

        elif choice == "4":
            linked.restore()
            print("\n Linked list restored to TORRETA!")

        elif choice == "5":
            break

        else:
            print("\n Invalid choice. Please try again.")

        print("\n Updated List:")
        print(" ", linked.display())


if __name__ == "__main__":
    linked_list_program()
