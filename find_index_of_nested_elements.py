b,a=int(input("Enter A number:")),[1,2,[3,4],[5,6],[7,8,9],[10,11,12]]
for i in range(len(a)):
    if b == a[i]: print(a.index(b))
    else: 
        if type(a[i])==list:
            for k in a[i]:
                if k == b: print(a.index(a[i]),a[i].index(b))
