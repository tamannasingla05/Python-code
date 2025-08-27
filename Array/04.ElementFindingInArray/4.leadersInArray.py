#to find the leaders in an array
def leader(arr):
    result = []
    n = len(arr)

    #statrt the loop to pick elements one by one
    for i in range(n):
        #inner loop to comapre the elements
        for j in range(i+1,n):
            if (arr[i]<arr[j]):
                break

        else:
            result.append(arr[i])

    return result

if __name__=="__main__":
    arr = [12,34,23,12,22,2]
    result = leader(arr)
    print(" ".join(map(str,result)))