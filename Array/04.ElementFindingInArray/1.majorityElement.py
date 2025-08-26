#program to find the element that appears more than n/2 times in the array
def majorityElement(arr):
    n = len(arr)

    for i in range(n):
        count = 0

        #inner loop to count the frequency of arr[i]
        for j in range(n):
            if (arr[i] == arr[j]):
                count+=1

        #check if count is greater than n/2
        if (count>n//2):
            return arr[i]
        
    return -1

if __name__=="__main__":
    arr = [1,4,6,4,1,4,2,4,6,4,5,4,4]
    print("Majority Element:",majorityElement(arr))