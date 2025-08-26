#binary search program
def binarySearch(arr,low,high,key):
    mid = (low+high)//2

    #check if the mid element is the key
    if (key == arr[mid]):
        return mid
    
    if (key>arr[mid]):
        return binarySearch(arr,(mid+1),high,key)
    
    if (key<arr[mid]):
        return binarySearch(arr,low,(mid-1),key)
    
    return 0

if __name__=="__main__":
    arr = [12,34,45,67,78,89]
    n = len(arr)
    key = int(input("Enter the key: "))

    print("Key is present at index",binarySearch(arr,0,(n-1),key))