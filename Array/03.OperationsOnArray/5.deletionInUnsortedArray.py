#program to delete an element from the array
if __name__=="__main__":
    #declare the array and the key to be deleted
    arr = [12,56,43,23,89,77,90,22]
    key = 77

    print("Array before deletion:")
    print(arr)

    arr.remove(key)

    print("Array after deletion:")
    print(arr)