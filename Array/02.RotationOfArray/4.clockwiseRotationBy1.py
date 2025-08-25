#rotating the array clockwise by 1
def rotation(arr,n):
    #storing the last element in a variable
    last = arr[-1]

    #shifting the other values
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]

    arr[0] = last

if __name__=="__main__":
    arr = [1,3,5,7,9,15]
    n = len(arr)
    rotation(arr,n)
    for i in range(0,n):
        print(arr[i],end="")