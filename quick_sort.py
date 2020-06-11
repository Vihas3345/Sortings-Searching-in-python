def partition(arr,p,r):
    x=arr[r]
    i=p-1
    for j in range(p,r):
        if arr[j]<=x:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return (i+1)
def quick(arr,p,r):
    if p<=r:
        q=partition(arr,p,r)
        quick(arr,p,q-1)
        quick(arr,q+1,r)
arr=[]
n=int(input("enter number of inputs required"))
for i in range(n):
    x=int(input())
    arr.append(x)
quick(arr,0,n-1)
for i in range(n):
    print(arr[i])