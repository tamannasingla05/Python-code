#program to find an element in the doubly LL
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

#function to search the position of element
def search(head,key):
    curr = head
    pos = 0
    while curr is not None and curr.data!=key:
        pos += 1
        curr = curr.next

    #if the element is not present
    if curr is None and curr.data!=key:
        return -1
    
    return pos+1

if __name__=="__main__":
    head = Node(1)
    head.next = Node(10)
    head.next.next = Node(18)
    head.next.next.next = Node(32)
    head.next.next.next.next = Node(45)
    head.next.next.next.next.next = Node(54)
    head.next.prev = head.next
    head.next.next.prev = head.next.next
    head.next.next.next.prev = head.next.next.next
    head.next.next.next.next.prev = head.next.next.next.next
    head.next.next.next.next.next.prev = head.next.next.next.next.next

    key = 32
    print("Element is present at position",search(head,key))