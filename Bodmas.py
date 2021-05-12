# def bodmas():
#     inp,li,num = input("enter : "),[],""
#     for i in inp:
#         if i.isdigit():
#             num+=i
#         else:
#             li.append(num)
#             li.append(i)
#             num=""
#     li.append(num)
#     while "/" in li :
#         n = li.index("/")
#         b = float(li[n-1]) / float(li[n+1])
#         li[n-1:n+2]=[b]
#     while "*" in li:
#         n = li.index("*")
#         b = float(li[n-1]) * float(li[n+1])
#         li[n-1:n+2]=[b]
#     while "+" in li :
#         n = li.index("+")
#         b = float(li[n-1]) + float(li[n+1])
#         li[n-1:n+2]=[b]
#     while "-" in li :
#         n = li.index("-")
#         b = float(li[n-1]) - float(li[n+1])
#         li[n-1:n+2]=[b]
#     return int(b)
# print(bodmas())