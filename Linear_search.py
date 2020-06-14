def linear(arr, element):
    count=0
    for i in range(len(arr)):
        if arr[i] == element:
            print("Element found at ", (i+1), "th place")
            count=count+1
    if count==0:
            print("Element not found")
arr=[]
n=int(input("Enter length of array"))
for i in range(n):
    x=int(input())
    arr.append(x)
element=int(input("Enter Element to be searched"))
linear(arr,element)