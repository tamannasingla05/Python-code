#program for creation and traversal of singly LL
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def print_list(node):
    #iterate till node reaches none
    while node is not None:
        print(node.data,end=" ")
        node = node.next

if __name__=="__main__":
    head = Node(1)
    second = Node(2)
    third = Node(3)

    head.next = second
    second.next = third
    print_list(head)