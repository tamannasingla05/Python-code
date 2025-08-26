#program to insert element in an unsorted array
def insertUnsorted(arr,n,key,pos):
    arr.append(0)
    #shift elements to the right which are in right side of pos
    for i in range(n-1,pos-1,-1):
        arr[i+1] = arr[i]

    arr[pos] = key

if __name__=="__main__":
    arr = [23,56,34,12,67]
    n = len(arr)

    print("Array before insertion:")
    for i in range(0,n):
        print(arr[i],end=" ")

    print("\n")

    key = 2
    pos = 2

    insertUnsorted(arr,n,key,pos)
    n+=1
    print("Array after insertion:")
    for i in range(0,n):
        print(arr[i],end=" ")