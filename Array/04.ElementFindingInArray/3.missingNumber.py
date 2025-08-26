#to find the missing number in the array
def missingNum(arr):
    n = len(arr) + 1

    #iterate through each element to check
    for i in range(1,n+1):
        found = False
        
        for j in range(n-1):
            if (arr[j] == i):
                found = True
                break

        if not found:
            return i
        
    return -1

if __name__=="__main__":
    arr = [3,5,4,7,6,1]
    print("Missing Number:",missingNum(arr))