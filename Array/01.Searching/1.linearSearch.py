def search(arr, key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1

if __name__=="__main__":
    arr=[3,5,7,2,9,4,1]
    key=2

    index=search(arr,key)
    print(index)