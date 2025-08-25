#program for rotation of an array counterclockwise by d
def rotateArr(arr,d):
    n = len(arr)

    #creating a temporary array
    temp = [0]*n

    #copy the last n-d elements in front of the temp array
    for i in range(n-d):
        temp[i] = arr[d+i]

    #now copy the first d elements in the back of temp array
    for i in range(d):
        temp[n-d+i] = arr[i]

    #finally copy the temp array to original array
    for i in range(n):
        arr[i] = temp[i]

if __name__=="__main__":
    arr = [1,2,3,4,5,6,7,8]
    d = 3

    rotateArr(arr,d)

    #print the array
    for i in range(len(arr)):
        print(arr[i],end="") 