# def list_sum(num):
#         i=num.pop(0)
#         if len(num)==0:
#             return i
#         else:
#             return i + list_sum(num)
# print(list_sum([1,3,5,7,9]))


# n=[1,2,6,12,23,7,3,9]
# l=len(n)
# for j in range(l):
#     for i in range(l):
#         if n[i]>n[j]:
#             m=n[i]
#             n[i]=n[j]
#             n[i]=m
# print(n)

# a=[12,66,55,88,45,47,64,81,20]
# l=len(a)
# i=0
# for i in range(l):
#     for j in range(i+1,l):
#         if a[i]>a[j]:
#             v=a[i]
#             a[i]=a[j]
#             a[j]=v
# print(a)
