class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class SinglyLL:
    def __init__(self):
        self.head = None

    def insert_at_start(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def insert_at_specific_pos(self,data,pos):
        new_node = Node(data)
        temp = self.head
        current_pos = 0

        while temp is not None and current_pos < pos-1:
            temp = temp.next
            current_pos += 1

        if temp is None:
            print("Position out of bounds!")
            return
        
        new_node.next = temp.next
        temp.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print("Null")

if __name__=="__main__":
    list = SinglyLL()
    list.insert_at_start(10)
    list.insert_at_end(20)
    list.insert_at_end(30)
    list.insert_at_end(50)
    list.insert_at_specific_pos(40,3)
    list.print_list()