# def pattern(number):
#     if number == 1:
#         return 1
#     else:
#         return pattern(number-1) + 3
# print(pattern(7))

# def factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""

#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))
# num =int(input())
# print("The factorial of", num, "is", factorial(num))


# def pattern(number):
#     if number == 1:
#         return 10
#     elif number % 2 == 0:
#         return pattern(number - 1) + 1
#     else:
#         return pattern(number - 1) * 10 
# print(pattern(3))

 
# def ifPalindrome(string):
#     if len(string) == 1:  # BASE CASE CONDITION
#         return True
#     elif string[0] == string[-1]:  # RECURSION
#         return ifPalindrome(string[1:][:-1])
#     else:
#         return False 
# s=input()
# print(ifPalindrome(s))

# def getFibNumber(number):
#     if number == 1:
#         return 0
#     elif number == 2:
#         return 1
#     else:
#         return getFibNumber(number-1) + getFibNumber(number-2) 
# n=int(input())
# print(getFibNumber(n))



# def sum_list(lis):
#     if len(lis)==1:
#         return lis[0]
#     return lis[0] + sum_list(lis[1:])
# print(sum_list([1, 4, 7, 10])) 

 
# def fib(number):
#     if number == 1:
#         return [1]
#     elif number == 2:
#         return [1,1]
#     p=fib(number-1)
#     new=p[-1]+p[-2]
#     p.append(new)
#     return p
# print(fib(10))



# def is_present_in_list(number_to_search, list_to_search):
#     if number_to_search == list_to_search[0]:
#         return True
#     elif number_to_search not in list_to_search:
#         return False
#     return is_present_in_list(number_to_search,list_to_search[1:])
# print(is_present_in_list(3,[ 5, 7, 8, 6, 2, 1]))
# print(is_present_in_list(10, [3, 5, 7, 8, 4, 6, 2, 9]) )

# def ch(f,l):
#     if f==l[0]:
#         return True
#     elif f not in l:
#         return False
#     return ch(f,l[1:])
# print(ch(3,[ 5, 7, 8, 6, 2, 3]))

# def normalsolver():
#     inp = input("enter : ")
#     li = []
#     num = ""
#     for i in inp:
#         if i.isdigit():
#             num+=i
#         else:
#             li.append(num)
#             li.append(i)
#             num=""
#     li.append(num)
#     if "/" in li :
#         n = li.index("/")
#         b = float(li[n-1]) / float(li[n+1])
#         li[n-1:n+2]=[b]
#     if "*" in li:
#         n = a.index("*")
#         b = float(li[n-1]) * float(li[n+1])
#         li[n-1:n+2]=[b]
#     if "+" in li :
#         n = li.index("+")
#         b = float(li[n-1]) + float(li[n+1])
#         li[n-1:n+2]=[b]
#     if "-" in li :
#         n = li.index("-")
#         b = float(li[n-1]) - float(li[n+1])
#         li[n-1:n+2]=[b]
#     return b
# print(normalsolver())


# def nested_to_flat(lis):
#     flat_list = []
#     for i in lis:
#         if type(i) != int:
#             flat_list = flat_list + nested_to_flat(i)
#         else:
#             flat_list.append(i)
#     return flat_list 
# print(nested_to_flat([1,[2,3,[4,[5,[6,[7,[8,9]]]]]]]))

# import random
# def n():
#     return random.randrange(1, 20)
# def l():
#     r = random.randrange(4)
#     if r == 0:
#         return [n()]
#     elif r == 1:
#         return [l(), n()]

#     elif r == 2:
#         return [n(),l()]
#     elif r == 3:
#         return l() + l()
# print(l())