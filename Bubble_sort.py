a=[100,3,78,2,8,8,43,98,34,31,5]
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
print(a)
