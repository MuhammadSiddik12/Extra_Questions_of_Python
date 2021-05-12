#####################  QUESTION NO 1 #################

# def sum_nested(a):
#     s=0
#     for i in a:
#         if type(i) is list:
#             s+=sum_nested(i)
#         else:
#             u=lambda i,s:i+s
#             s=u(s,i)
#     return s
# a=[1,[2,[3,[4,[5,[6,[7,[8,[9]]]]]]]]]
# print(sum_nested(a))

################### QUESTION NO 2 ##############################

# from functools import reduce
# a=[1,2,[3,4,[5,6,[7,8,[9]]]]]
# b=reduce(lambda a:sum_nested,a)
# def sum_nested(l):
#     s = 0
#     for i in l:
#         if type(i) is list:
#             s += sum_nested(i)
#         else:
#             s += i
#     return s
# print(sum_nested([1,[2,[3,[4,[5,[6,[7,[8,[9]]]]]]]]]))
# print(b)

############## QUESTION NO 3 #######################

# x=input()
# y=x.split(" ")
# u=open("excercise.txt","r")
# u=u.readlines()
# for i in y:
#     for a in u:
#         print(a)
#         if i in a:
#             re=open(f"{i}.txt","a")
#             re.write(a)

############### QUESTION NO 4 ####################

# import csv
# def csv_write():
#     with open("new.csv","w") as new1:
#         new2=csv.writer(new1)
#         new2.writerow(['name','roll','total_marks'])
#         while True:
#             name=input("Enter your name:")
#             roll=int(input("Enter your age:"))
#             total_marks=int(input("Enter your total marks:"))
#             re=[name,roll,total_marks]
#             new2.writerow(re)
#             ch=int(input("1 for more \n2 for exit"))
#             if ch==2:
#                 break
#             else:
#                 continue
# csv_write()
        
# def csv_read():
#     with open("new.csv","r") as read:
#         boj=csv.reader(read)
#         for i in boj:
#             print(i)
# csv_read()