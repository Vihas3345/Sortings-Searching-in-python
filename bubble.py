def bubble(a):
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
a=[]
n=int(input("Enter the size of array"))
for i in range(0,n):
    x=int(input())
    a.append(x)
bubble(a)
for i in range(0,len(a)):
    print(a[i])