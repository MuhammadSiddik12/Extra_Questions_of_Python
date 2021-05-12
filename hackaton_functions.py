##### Max Of Three Number #####

# def maxi(first,second,third):
#     number=[first,second,third]
#     print(max(number),'Max')
# first=int(input("first number:"))
# second=int(input("second number:"))
# third=int(input("third number:"))
# maxi(first,second,third)

##### Sum of number in List #####

# def sum_of_number(number):
#     sum=0
#     for i in number:
#         sum+=i
#     print(sum)
# number=[8,2,3,0,7]
# sum_of_number(number)

##### Multiplication of number in List #####

# def li(list):
#     multi=1
#     for i in list:
#         multi=multi*i
#     return multi
# list=[1,2,3,4,5,6,7,8,9]
# print(li(list))

#### Reverse a String #####

# def rever(string):
#     empty_str=''
#     for i in string:
#         empty_str=i+empty_str
#     return empty_str
# string="Siddik"
# print(rever(string))

##### calculate the factorial of number #####

# def factorial(number):
#     factorial = 1
#     for i in range(1,number + 1):
#         factorial = factorial*i
#     return "The factorial of",number,"is",factorial
# number=int(input("Enter a number:"))
# print(factorial(number))

##### input number is in given range or not #####

# def ran(number):
#     range=10
#     if number <=range:
#         return number,"in range"
#     else:
#         return number,"not in range"
# number=int(input("Enter a number:"))
# print(ran(number))
    
##### count a lowercase and uppercase by given string #####

# def cou(letter):
#     l=0
#     u=0
#     for i in letter:
#         if i.islower():
#             l+=1
#         elif i.isupper():
#             u+=1
#     print(l,"lower")
#     print(u,"upper")
# letter=input("Enter a word:")
# cou(letter)

##### remove a duplicate from a given list #####

# def lis(list):
#     single=[]
#     for i in list:
#         if i not in single:
#             single.append(i)
#     print(single)
# list=[1,2,3,3,3,3,4,5]
# lis(list)

##### prime number or not #####

# def prime(number):
#     if number>1:
#         for i in range(2,number):
#             if number%i==0:
#                 print(number,"is not a prime number")
#                 break
#         else:
#             print(number,"is a prime number")
#     else:
#         print(number,"is not a prime number")       
# number=int(input("Enter a number:"))
# prime(number)

##### odd even from a list #####

# def ev_od(list):
#     odd_even=[]
#     for i in list:
#         if i%2==0:
#             odd_even.append(i)
#     return odd_even
# list=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(ev_od(list))

##### perfect number or not #####

# def per(number):
#     sum=0
#     for i in range(1,number):
#         if number%i==0:
#             sum+=i
#     if number==sum:
#         print(number,"is a perfect number")
#     else:
#         print(number,"is not a perfect number")
# number=int(input("Enter a number:"))
# per(number)

##### check if given string is palimdrome or not #####

# def palimdrome(str):
#     revers_str=''
#     for i in str:
#         revers_str=i+revers_str
#     if str==revers_str:
#         print(str," is a palimdrome")
#     else:
#         print(str,"is not a palimdrome")
# str=input("Enter a string:")
# palimdrome(str)

##### print parcal's tringle #####

# def parcal(number):
#     for i in range(number):
#         print(' '*(number-i), end='') 
#         print(' '.join(map(str, str(11**i)))) 
# number=int(input("Enter a number:"))
# parcal(number)

##### pangram (all characteris in or not) #####

# def ispangram(str): 
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     for char in alphabet: 
#         if char not in str.lower(): 
#             return False
#     return True
# string = 'acdfhjlnprtvxsbegikmoqsuwxy'
# if(ispangram(string) == True): 
#     print("Yes") 
# else: 
#     print("No") 

##### sort a string by letter and assign by sort #####

# string= "zebra-green-red-yellow-black-white-apple"
# single_string=[i for i in string.split("-")]
# single_string.sort()
# print("-".join(single_string))

##### squares of a numbers till the range #####

# def squar(number):
#     squares=[]
#     for i in range(1,number+1):
#         multi=i**2
#         squares.append(multi)
#     return squares
# number=int(input("Enter a number:"))
# print(squar(number))

##### execute a comment as code #####

# my_code='''
# def make_bold(fn):
#     def wrapped():
#         return "1.0 " + fn() + "1 "
#     return wrapped

# def make_italic(fn):
#     def wrapped():
#         return  '2.0 ' + fn() + '2 '
#     return wrapped

# def make_underline(fn):
#     def wrapped():
#         return '3.0 ' + fn() + '3 '
#     return wrapped
# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return "hello world"
# print(hello())'''
# # print(exec(my_code))  #exec used for execute a string containing code#

##### access a funtom from inside functon #####

# def make_adder(x):
#       def adder(y):
#         return x+y
#       return adder
# print(make_adder)

# def abc()
#     a=1
#     x = 1
#     y = 1
#     str1= "w3resource"
#     int=2
#     print("Python Exercises")

# print(abc.__code__.co_global)
