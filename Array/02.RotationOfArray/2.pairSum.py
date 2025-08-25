#to find if the pair sum exists in the rotated & sorted array
def pairSum(arr,target):
    s = set()
    for num in arr:
        complement = target - num
        
        #check if the pair exists
        if complement in s:
            return True
        
        #add the current element to the set
        s.add(num)

    return False
    
if __name__=="__main__":
    arr = [10,12,13,4,6,7]
    target = 15

    if pairSum(arr,target):
        print("True")

    else:
        print("False")