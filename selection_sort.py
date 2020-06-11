def selection(arr):
    for i in range(len(arr)):
        small=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[small]:
                small=j
        arr[i],arr[small]=arr[small],arr[i]
arr=[]
n=int(input("Enter size of array"))
for i in range(n):
    x=int(input())
    arr.append(x)
selection(arr)
for i in range(len(arr)):
    print(arr[i])
