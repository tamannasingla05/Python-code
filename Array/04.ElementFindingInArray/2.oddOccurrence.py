#to find the element which is occurring odd no of times in the array
def oddOccurrence(arr,n):

    for i in range(n):
        count = 0

        #inner loop to count he frequency of element
        for j in range(n):
            if (arr[i] == arr[j]):
                count+=1

        if (count % 2 != 0):
            return arr[i]
        
    return -1

if __name__=="__main__":
    #if you want to take the input from user
    arr = list(map(int,input("Enter the integers: ").split()))
    n = len(arr)
    print(oddOccurrence(arr,n),"is occurring odd no. of times in the array.")
    