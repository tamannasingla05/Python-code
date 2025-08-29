#program to search an element in the LL
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#function to search element
def search(head,key):
    curr = head
   
    while curr is not None:
        if (curr.data == key):
            return True
        
        curr = curr.next
        

    return False

if __name__=="__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    key = 4

    print(search(head,key))