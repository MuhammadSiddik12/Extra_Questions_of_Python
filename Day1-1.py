############## Day1-1 ##########

# a=int(input("Enter a number:"))
# while a!=0:
#     if a%3==0 and a%5==0: print(a)
#     a-=1

############## Day1-2 ###########

# year = int(input("Enter a year:"))
# if (year % 4) == 0:
#    if (year % 100) == 0:
#        if (year % 400) == 0: print("{0} is a leap year".format(year))
#        else: print("{0} is not a leap year".format(year))
#    else: print("{0} is a leap year".format(year))
# else: print("{0} is not a leap year".format(year))


############## Day1-2-1 ###########

# a=int(input("Enter a number:"))
# b,c=0,0
# while b<3:
#     print(a-2,"Even numbers")
#     a-=2
#     b+=1
# a=int(input("Enter a number: "))
# while c<3:
#     print(a+1,"Odd numbers")
#     a+=2
#     c+=1

############## Day1-2-2 ###########

# a=int(input("Enter a number:"))
# b,c=0,0
# while b<3:
#     print(a-2,"Leap year")
#     a-=2
#     b+=1
# a=int(input("Enter a number: "))
# while c<3:
#     print(a+2,"Leap year")
#     a+=2
#     c+=1

############## Day1-3 ###########

# a=input("Enter a number: ")
# c=0
# for i in a:
#     b=int(i)**3
#     c+=b
# if c==int(a):
#     print(a,"is arm strong number")
# else:
#     print(a,"not a arm strong number")

############## Day1-4 ###########

# a,sum1=int(input()),0
# for i in range(1,a):
#     if a%i==0: sum1+=i
# if sum1 == a: print(a,"it is a perfect number")
# else: print(a,"it is not a perfect number")

############## Day2-1 ###########

# a=input("Enter a number: ")
# if len(a)<2:
#     pass
# else:
#     print(a[0:2])
#     print(a[-2:])

############## Day2-2 ###########

# a=input("Enter a word:")
# if a.endswith("ing"): a+="ly"
# elif a.endswith("ly"): pass
# else: a+="ing"
# print(a)

############## Day2-4 ###########

# a,b,c=int(input("Enter a number:")),0,1
# for i in range(1,a+1):
#     d=b+c
#     print(d)
#     b,c=c,d

############## Day2-5 ###########

# a,sum1,b=int(input()),0,0
# for i in range(1,a+1):
#     b+=i*i
#     sum1+=i
# c=sum1*sum1
# print(c-b)

############## Day2-5 ###########

# a,sum1=int(input()),1
# for i in range(1,a+1): sum1*=i
# print(sum1)

############## Day3-1 ###########

# a,sum1=input("Enter a number:"),0
# for i in a: sum1+=int(i)
# print(sum1)

############## Day3-2 ###########

# a,sum2=input(),0
# for i in a:
#     sum1=1
#     for j in range(1,int(i)+1): sum1*=j
#     sum2+=sum1
# print(sum2)

# a,b=int(input()),""
# for i in str(a): b=i+b
# print(int(b))

# a,b,sum1=int(input()),int(input()),0
# c=a**b
# for i in str(c):
#     sum1+=int(i)
# print(sum1)

# a=input()
# print(a.count(" "))
    

# d={"one":1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,"eight":8,'nine':9,'zero':0}
# a,sum1=input().split(" "),0
# for i in a:
#     for j in d:
#         if i==j: sum1+=d[j]
# print(sum1)


# a,c=[[1,0,1],[0,1,0],[1,1,1]],[]
# for i in a:
#     b=[]
#     for k in range(len(i)-1,-1,-1):
#         if i[k]==1: b.append(i[k]-i[k])
#         elif i[k]==0: b.append(i[k]+1)
#     c.append(b)
# print("First List:",a)
# print("Final List:",c)

##################### Edge cases ######################

# n = 2
# count = 0
# while(count < 5):
#     isPrime = True
#     i = 2
#     while(i<n):
#         if n%i == 0:
#             isPrime = False
#         i = i + 1
#     if (isPrime):
#         print (str(n) + " is prime")
#         count += 1
#     n = n + 1  



# def calc(a, b, operator):
#     if operator == '+':
#         return a + b
#     elif operator == '*':
#         return a * b
#     elif operator == '/':
#         return a / b
#     elif operator == '-':
#         return a - b
#     else:
#         print("Unsupoorted operator") 

# def add(a, b):
#     return a+b
# ans = add(5, 6) + add(2, 3)
# print(ans) 

# arr = [0, 5, 2, 1]
# l = len(arr)
# s = 0
# i = 1
# while(i < l):
#     s = s + arr[i]
#     i+=1
# print(s) 

# def split(s,second):
#     i,temp_s,a=0,'',[]
#     while(i<len(s)):
#         if s[i] != second: temp_s += s[i]
#         else:
#             a.append(temp_s)
#             temp_s=''
#         i += 1
#     a.append(temp_s)
#     return a
# a,b=input(),input()
# print(split(a,b))

################ More Questions ##############

# list1 = [1, 342, 75, 23, 98]
# list2 = [75, 23, 98, 12, 78, 10, 1]
# a=[]
# for i in list1:
#     for j in list2:
#         if i ==j:
#             a.append(i)
# print(a)

# list1 = [1, 5, 10, 12, 16, 20]
# list2 = [1, 2, 10, 13, 16] 
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)

# a,sum1=input(),0
# for i in a: sum1+=int(i)
# print(f"Yes {a} is a harshard number") if int(a)%sum1==0 else print(f"No {a} is not a harshard number")


# def numbers_less_than_twenty(list):
#   counter = 0
#   while counter < len(list):
#     item = list[counter]
#     if item > 20:
#       list.remove(item)
#     else:
#       counter += 1
#   return list

# num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

# num_list_sub_20 = numbers_less_than_twenty(num_list)

# print ("Initial list", num_list)
# print ("List that doesn't contain numbers greate than 20", num_list_sub_20) 


# from random import randint

# def win():
#     print ('You win!')

# def lose():
#     print ('You lose!')

# while False:
#     player_choice = input('What do you pick? (rock, paper, scissors)')
#     player_choice.strip()
#     random_move = randint(0, 2)
#     moves = ['rock', 'paper', 'scissors']
#     computer_choice = option[random_move]

#     ife =  choice == computer_choice:
#         print ('Draw!')
#     elif  == 'rock' and comp == 'scissors':
#         win()
#     elif  chioc= 'paper' and comp == 'scissors':
#         lose()
#     elif playe == 'scissors' and comp == 'paper':
#         win()
#     elif player == 'scissors' and Comp == 'rock':
#         lose()
#     elif payer == 'paper' and computer == 'rock':
#         win()
#     elif player ==  and comp == :
#         lose()
#     aGain = input('Do you want to play again? (y or n)').strip()
#     if again == 'n':
#         break 


# print("Welcome To you in KBC, \nLets Start The Game...\n")
# questions=[
#     "How many continents in the world?",
#     "Which day is observed as the world standard day?",
#     "Who is the author of the epic 'Magdoot'?",
#     "September 27 is celebrated every year as?",
#     "How many planets are there in our solar system?",
#     "Who is the president of America?",
#     "Where is the Navgurukul's girls campus in India?",]
# options=[
#     ["1","5","4","7","50:50"],
#     ["June 26","Oct 14","Nov 15","Dec 2","50:50"],
#     ["Rice","Fried","Fried Rice","Dal","50:50"],
#     ["Vamlmiki","Banabhata","Kalidas","Vishal","50:50"],
#     ["Teacher,s Day","Natinal Integretion Day","World Tourism Day","International Day","50:50"],
#     ["5","8","9","6","50:50"],
#     ["Joe Biden","Donald Trump","Emmanuel Macron","Barack Obama","50:50"],
#     ["Pune","Banglore","Delhi","Gurugram","50:50"],]
# solutions=[4,2,3,3,3,2,1,2]
# sol=[
#     [2,4],
#     [2,3],
#     [2,3],
#     [3,1],
#     [4,1],
#     [2,4],
#     [4,1],
#     [2,4],] 
# n=0
# k=1
# d=0
# for i in questions:
#     print(i)
#     print("Here Is Your Options...")
#     for i in options[n]:
#         if k==6:
#             k=1
#         print(k,':', i)
#         k+=1
#     inp=int(input("Choose The Correct Answer:"))
#     if inp==solutions[n]:
#         print("Congratulation! You Won")
#     elif inp==5:
#         if d==1:
#             print("Sorry!! You Already Choosed This option\n")
#         else:
#             for i in range(1):
#                 print("option Number", sol[n])
#             inp=int(input("Enter Your Option Number:"))
#             if inp==solutions[n]:
#                 print("Congratulation! You Won Again\n")
#                 d+=1
#             else:
#                 print("Your Answer Is Wrong.\n")
#     else:
#         print("Your Answer Is Wrong.\n")
#         break
#     n+=1