#program to search an element in the array
def searchUnsorted(arr,n,key):
    #check each element in the array
    for i in range(n):
        if(arr[i] == key):
            return i
        
    return -1

if __name__=="__main__":
    arr = [12,56,34,22,89,67,45]
    n = len(arr)
    key = 67
    
    index = searchUnsorted(arr,n,key)
    if (index == -1):
        print("Element not found!")

    else:
        print("Element found at position:", index+1)