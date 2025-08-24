def binarySearch(arr,key):
    #pointing lo & hi as the start and end of the array
    lo = 0
    hi = len(arr)-1
    #finding the middle element
    while lo<=hi:
        mid = lo+(hi-lo)//2
        
        #if middle element is the key
        if arr[mid]==key:
            return mid

        #checking if the left half of array is sorted
        if arr[mid]>=arr[lo]:
            if key>=arr[0] and key<=arr[mid]:
                hi = mid-1
            else:
                lo = mid+1

        #if the right half is sorted
        else:
            if key>=arr[mid] and key<=arr[hi]:
                lo = mid+1
            else:
                hi = mid-1

    return -1

if __name__=="__main__":
    arr = [5,6,7,8,9,1,2,3,4]
    key = 6
    print(binarySearch(arr,key))
