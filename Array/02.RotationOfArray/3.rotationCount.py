#findind the count by which a array is rotated by right
def kCount(arr,n):
    #set the first element as min
    min = arr[0]
    minIndex = 0

    #find the min element in the array
    for i in range(0,n):
        if (min>arr[i]):
            min = arr[i]
            minIndex = i

    return minIndex

if __name__=="__main__":
    arr = [14,15,18,1,3,7]
    n = len(arr)
    print(kCount(arr,n))