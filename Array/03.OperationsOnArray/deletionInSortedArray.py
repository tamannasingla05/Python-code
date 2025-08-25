#deleting an element in the sorted array
def deleteSorted(arr,n,key):
    #pos of element to be deleted
    pos = binarySearch(arr,0,n-1,key)

    if (pos == -1):
        print("Element not found")
        return n
    
    #deleting element
    for i in range(pos,n-1):
        arr[i] = arr[i+1]

    return n-1

#function to find the position of element using binary search
def binarySearch(arr,low,high,key):
    if (high<low):
        return -1
    
    mid = (low+high)//2

    if (key == arr[mid]):
        return mid
    
    if (key>arr[mid]):
        return binarySearch(arr,(mid+1),high,key)
    
    return binarySearch(arr,low,(mid-1),key)

if __name__=="__main__":
    arr = [10,15,20,25,30,35]
    n = len(arr)
    key = 25

    print("Before Deletion: ",end="")
    for i in range(n):
        print(arr[i],end=" ")

    #calling function
    n = deleteSorted(arr,n,key)

    print("\nAfter Deletion: ",end="")
    for i in range(n):
        print(arr[i],end=" ")