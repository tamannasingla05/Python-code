def insertSorted(arr,n,key,capacity):
    #check if array has space or not to insert
    if (n>=capacity):
        return n
    
    i = n-1
    while i>=0 and arr[i]>key:
        arr[i+1]= arr[i]
        i-=1

    arr[i+1] = key
    return(n+1)

if __name__=="__main__":
    arr = [12,15,20,25,30]

    for i in range(20):
        arr.append(0)

    capacity = len(arr)
    n = 5
    key = 22

    print("Before Insertion: ",end="")
    for i in range(n):
        print(arr[i],end=" ")

    n = insertSorted(arr,n,key,capacity)

    print("\nAfter Insertion: ",end="")
    for i in range(n):
        print(arr[i],end=" ")