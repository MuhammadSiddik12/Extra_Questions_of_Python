
# i=0
# n_l=[]
# while i<10:
#     n=int(input())
#     n_l.append(n)
#     i+=1
# print(n_l)


# n_l=[]
# for i in range(10):
#     n=int(input())
#     n_l.append(n)
# print(n_l)



# n_l=[]
# for i in range(10):
#     n=int(input("Enter your:>"))
#     n_l.append(n)
# print(n_l)
# n1=int(input("Check your number:>"))
# if n1 in n_l:
#     print(n1,"Yes")
# else:
#     print(n1,"No")


# a = []
# for i in range(5):
#   print ("Enter number")
#   num = int(input())
#   a.append(num)
# z = 0
# o = 0
# e = 0
# p = 0
# n = 0
# for i in range(5):
#   if a[i] == 0:
#     z = z+1
#   elif a[i] < 0:
#     n = n + 1
#     if a[i]%2 == 0:
#       e = e + 1
#     else:
#       o = o + 1
#   else:
#     p = p + 1
#     if a[i]%2 == 0:
#       e = e + 1
#     else:
#       o = o + 1
#   i = i-1
# print ("NEGATIVE:",n,"ZERO:",z,"POSITIVE:",p,"ODD:",o,"EVEN:",e)

# n_l=[]
# s=0
# for i in range(10):
#     n=int(input("Enter your:>"))
#     n_l.append(n)
#     s=s+n
# print(s)


# n_l=[]
# for i in range(10):
#     n=int(input("enter your number:> "))
#     n_l.append(n)
# print(n_l)
# # a=list(int(input("enter your iteams:> ")))
# b=[]
# for n in n_l:
#     # v=""
#     # for j in n:
#     v=0
#     v=n+v
#     b.append(v)
# print("this is your recverse list iteams:",b)

# a=["Vishal","suraj","23456"]
# b=[]
# for i in a:
#     v=""
#     for j in i:
#         v=j+v
#     b.append(v)
# print(b)


# n=int(input())
# for i in range(n+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()


# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(j,end="")
#         j+=1
#     print()
#     i+=1



# lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9] 
# lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
# lst3 = [value for value in lst1 if value in lst2]
# print(lst3)
# for i in lst1:
#     for k in lst2:
#         if i ==k:
#             c.append(i)
# for v in lst1:
#     if v in lst2:
#         c.append(v) 
# print(lst1)
# print(c)


# lst1 = [23,16,20,15, 2, 14, 14, 16, 20 ,52] 
# l1=[]
# for i in lst1:
#     l1.append(i)
#     print(l1)
#     for j in l1:
#         if i==j:
#         lst1.remove(i)
# print()





# lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69,3,4,5,6,7,8,89] 
# lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26,67,9,89] 
# c=[]
# v=[]
# for i in lst1:
#     if i in lst2:
#         c.append(i)
#     else:
#         v.append(i)
# for j in lst2:
#     if j in lst1:
#         pass
#     else:
#         v.append(j)

# print("repetation",sorted(c))
# print("intersection",sorted(c+v))

# n=int(input())
# for i in range(n+1):
#     for j in range(6,i,-1):
#         print(j,end="")
#     print()


# lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69,3,4,5,6,7,8,89] 
# v=[]
# for i in lst1:
#     for j in lst1:
#         if i!=j:
#             v.append(j)
# print(lst1)