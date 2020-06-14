
def bsearch(arr,p,r,search):
    mid=int((p+r)/2)
    if arr[mid]==search:
        print("Element found at",(mid+1),"th place")
    elif arr[mid]>search:
        bsearch(arr,p,mid-1,search)
    else:
        bsearch(arr,mid+1,r,search)
arr=[]
n=int(input("Enter size of input"))
for i in range(n):
    x=int(input())
    arr.append(x)

#for binary search the input array should be sorted order,so we will first sort it by any sorting technique

def bubble(arr):
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
bubble(arr)

search=int(input("Enter element to be searched"))
bsearch(arr,0,len(arr),search)