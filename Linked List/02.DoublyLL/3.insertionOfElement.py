class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_start(data)
            return

        new_node = Node(data)
        temp = self.head
        current_pos = 0

        # Traverse to the node just before the position
        while temp and current_pos < position - 1:
            temp = temp.next
            current_pos += 1

        if not temp:
            print("Position out of bounds.")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node

    def display_forward(self):
        temp = self.head
        print("Forward:", end=" ")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def display_backward(self):
        temp = self.head
        if not temp:
            print("Backward: None")
            return
        # Go to the last node
        while temp.next:
            temp = temp.next

        print("Backward:", end=" ")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


# Example usage
dLL = DoublyLinkedList()

# Create initial list
dLL.insert_at_end(10)
dLL.insert_at_end(20)
dLL.insert_at_end(30)
dLL.insert_at_end(40)

dLL.insert_at_position(35,3)

dLL.display_forward()
dLL.display_backward()