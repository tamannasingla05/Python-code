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
    list.print_list()