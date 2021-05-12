# def greater_or_not(num1):
#     if num1<10:
#         print(num1,"is smaller than 10")
#     elif num1>10 and num1<20:
#         print(num1,"is smaller than 10 and greater than 20")
#     else:
#         print(num1,"greater than 20")
# num1=int(input("Enter a number:"))
# greater_or_not(num1)

# def equal_or_not(num1):
#     varx=300-123
#     if num1==varx:
#         print(num1,"is equal to",varx)
#     else:
#         print(num1,"is not equal to",varx)
# num1=int(input("Enter a number:"))
# equal_or_not(num1)

# def equal_or_greater(num1):
#     number=44*30
#     if num1>=number:
#         print(num1,"is equal or greater than",number)
#     else:
#         print(num1,"smaller than",number)
# num1=int(input("Enter a number:"))
# equal_or_greater(num1)

# def water_filter(water):
#     if water<1:
#         print("Aur paani bharna hai")
#     elif water>1 and water<10:
#         print("Aur nhi bharna hai")
#     else:
#         print("paani overflow kar jata hai")
# water=int(input("Enter a water quantity:"))
# water_filter(water)

# def check(num1):
#     if  num1%2==0:
#         print("Yes it is divisible by 2")
#     else:
#         print("It is not divisible by 2")
# num1=int(input("Enter a number:"))
# check(num1)

# def check_divisible(varx,vary):
#     if varx%vary==0:
#         print(varx,"is divisible by",vary)
#     else:
#         print(varx,"is not divisible by",vary)
# varx=int(input("Enter a first number:"))
# vary=int(input("Enter a second number:"))
# check_divisible(varx,vary)

# def greater_than(num1,num2):
#     if num1 > num2:
#         print(num1,"is greater than",num2)
#     elif num1==num2:
#         print("both are equal")
#     else:
#         print(num2,"is greater than",num1)
# num1=int(input("Enter a firts number:"))
# num2=int(input("Enter a second number:"))
# greater_than(num1,num2)

# def divisible_by(num1):
#     if num1%5==0 and num1%15==0:
#         print("Dono se divisible hai")
#     else:
#         print("not divisible by both")
# num1=int(input("Enter a number:"))
# divisible_by(num1)

# def rules_regulations(age):
#     if age>=5 and age<=5:
#         print("you can go to school")
#     elif age>=18 and age<=18:
#         print("you can go for vote")
#     elif age>=24 and age<=24:
#         print("now you can do a marrige")
#     else:
#         print("now you can drink legally")
# age=int(input("Enter your age:"))
# rules_regulations(age)


# def password(p):
#     if len(p)>=8 and len(p)<=16:
#         if "1" in p  or "2" in p or "3" in p or "4" in p or "5" in p or "6" in p or "7" in p or "8" in p or "9" in p or "0" in p:
#             if "@" in p or "#" in p  or "!" in p or "$" in p or "&" in p or "*" in p or "^" in p:
#                 if "a" in p or "b" in p or "c" in p or "d" in p or "e" in p or "f" in p or "g" in p or "h" in p or "i" in p or "j" in p or "k" in p or "l" in p or "m" in p or "n" in p or "o" in p or "p" in p or "q" in p or "r" in p or "s" in p or "t" in p or "u" in p or "v" in p or "w" in p or "x" in p or "y" in p or "z" in p:
#                     if "A" in p or "B" in p or "C" in p or "D" in p or "E" in p or "F" in p or "G" in p or "H" in p or "I" in p or "J" in p or "K" in p or "L" in p or "M" in p or "N" in p or "O" in p or "P" in p or "Q" in p or "R" in p or "S" in p or "T" in p or "U" in p or "V" in p or "W" in p or "X" in p or "Y" in p or "Z" in p:
#                         print("strong password")
#                     else:
#                         print("Not strong")
#                 else:
#                     print("Not strong")
#             else:
#                 print("Not strong")
#         else:
#             print("Not strong")
#     else:
#         print("not strong")
# p=input("Enter a number:")
# password(p)


######################### Loops ##############################

# def to_100():
#     num1=1
#     while num1<=100:
#         print(num1)
#         num1+=1
# to_100()
    
# def to_100_7():
#     num1=1
#     while num1<=100:
#         if num1 % 7==0:
#             print(num1)
#         num1+=1
# to_100_7()

# def sum_100():
#     num1=1
#     sum=0
#     while num1<=100:
#         sum+=num1
#         num1+=1
#     print(sum)
# sum_100()
    

# def sum_10():
#     num1=1
#     sum=0
#     while num1<=10:
#         num2=int(input("Enter a number:"))
#         sum+=num2
#         num1+=1
#     print(sum)
# sum_10()

# def pos_neg_100():
#     num=1
#     while num<=100:
#         if num%2==0:
#             print(-num)
#         else:
#             print(num)
#         num+=1
# pos_neg_100()

# def sum_100():
#     num=556
#     num1=556-num
#     sum=0
#     while num1<=100:
#         sum+=num1
#         num1+=1
#     print(sum)
# sum_100()
    

# def check_100():
#     num=1
#     while num<=100:
#         if num%3==0 and num%7==0:
#             print("navgurukul")
#         elif num%3==0:
#             print("nav")
#         elif num%7==0:
#             print("gurukul")
#         else:
#             print(num)
#         num+=1
# check_100()

# def sum_10():
#     num=50
#     sum=0
#     while num<=59:
#         num1=int(input("Enter a number:"))
#         sum+=num1
#         num+=1
#     print(sum)
# sum_10()

# def number_10():
#     counter=156
#     counter2=157-counter
#     while counter2<=10:
#         print(counter2)
#         counter2+=1
# number_10()

# def user_sum(num):
#     sum=0
#     while num!=0:
#         num1=int(input("Enter a number:"))
#         sum+=num1
#         num-=1
#     print(sum)
# num=int(input("Enter a number how many input you want:"))
# user_sum(num)

# def prime(num):
#     if num>1:
#         for i in range(2,num):
#             if (num%i)==0:
#                 print("not a prime number")
#                 break
#         else:
#             print("prime number")
#     else:
#         print("it is not a prime")
# num=int(input("Enter a number:"))
# prime(num)

# def pattern(num):
#     while num!=0:
#         print(num)
#         num-=1
# num=int(input("Enter a number:"))
# pattern(num)


# def number(n):
# 	num = 5
# 	for i in range(5, 0,-1):
# 		for j in range(0, 5):
# 			print(num,end=" ")
# 		num = num - 1
# 		print("\r")
# n = 5
# number(n)

# def rev(num):
#     while num<=100:
#         if num%2==0:
#             print(num)
#         num+=1
# num=20
# rev(num)

# def rev7(num):
#     while num<=100:
#         if num%7==0:
#             print(num)
#         num+=1
# num=1
# rev7(num)

# def su(num):
#     sum=0
#     while num<=421:
#         sum+=num
#         num+=1
#     print(sum)
# num=20
# su(num)

# def multi(num):
#     sum=0
#     while num<=420:
#         print(num)
#         num+=8
#         sum+=num
#     print(sum)
# num=30+2
# multi(num)

    # def wei(person):
    #     sum=0
    #     while person!=0:
    #         we=int(input("Enter your weight:"))
    #         sum+=we
    #         person-=1
    #     ave=sum/11
    #     print(sum)
    #     print(round(ave,2))
    # person=11
    # wei(person)

# def gueesing():
#     c=5
#     n=5
#     while c!=0:
#         num=int(input("Enter a guees number:"))
#         if num==n:
#             print("You win")
#             break
#         elif num>n:
#             print("you have to choose a small number")
#         elif num<n:
#             print("you have to choose a big number")
#         c-=1
#     else:
#         print("you lose")
# gueesing()


# def multi_without(num1,num2):
#     sum=0
#     for i in range(num1):
#             sum+=num2
#     print("Multiply of",num1,"*",num2,"=",sum)
# num1=int(input("Enter a first number:"))
# num2=int(input("Enter a second number"))
# multi_without(num1,num2)

# def faboo(inp):
#     a=0
#     b=1
#     count=0
#     while count < inp:
#         print(a)
#         c=a+b
#         a=b
#         b=c
#         count+=1
# inp=int(input("Enter how many sequences you want "))
# faboo(inp)

#n=int(input('enter a number: '))
#temp=n
#rev=0
#while(n>0):
#    dig=n%10
 #   rev=rev*10+dig
  #  n=n//10
#if(temp==rev):
 #   print("The number is a palindrome!")
#else:
 #   print("The number isn't a palindrome!")
    
################## END #####################

#################### LIST ##################

# def len_of_list(li):
#     counter=0
#     for i in li:
#         counter+=1
#     return counter
# li=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
# print(len_of_list(li))

# def greater(li):
#     for i in li:
#         if i>20 and i<40:
#             return i
# li=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
# print(greater(li))

# def maxim(li):
#     maxi=li[0]
#     for i in li:
#         if i>maxi:
#             maxi=i
#     print(maxi)
# li=[50, 40, 23, 70, 56, 12, 77, 5, 10, 7]
# maxim(li) 

# def sec_maxim(li):
#     mx=max(li[0],li[1]) 
#     secondmax=min(li[0],li[1]) 
#     n =len(li)
#     for i in range(2,n): 
# 	    if li[i]>mx: 
# 		    secondmax=mx
# 		    mx=li[i] 
# 	    elif li[i]>secondmax and mx != li[i]: 
# 		    secondmax=li[i]
#     print("Second highest number is :",secondmax)
# li=[50, 40, 23, 70, 56, 12, 77, 5, 10, 7]
# sec_maxim(li) 


# def rev(places):
#     print(places[::-1])
# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"] 
# rev(places)

# def palimdrome(s):
#     n=''
#     for i in s:
#         n=i+n
#     if s==n:
#         print("Yes it is a palimdrome")
#     else:
#         print("It is not a plimdrome")
# s=input("Enter a word:")
# palimdrome(s)

# def bina_to_deci(binary_number):
#     dnum = 0
#     m = 1
#     blen = len(str(binary_number))
#     for k in range(blen):
#         rem = binary_number%10
#         dnum = dnum + (rem * m)
#         m = m * 2
#         binary_number = int(binary_number/10)
#     print("\nEquivalent Decimal Value = ", dnum)
# binary_number = int(input("Enter a Binary Number:"))
# bina_to_deci(binary_number)

# def not_present(list1,list2):
#     for i in list2:
#         for j in list1:
#             if i==j:
#                 list1.remove(i)
#     print(list1)
# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# not_present(list1,list2)


# def report(marks):
#     sum=0
#     for i in marks:
#         for k in i:
#             sum+=k
#     print(sum)
# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ] 
# report(marks)

# def report(marks):
#     for i in marks:
#         sum=0
#         for k in i:
#             sum+=k
#         av=sum/len(i)
#         print(f"Total Sum = {sum}")
#         print(f"Total Avearge = {round(av,2)}")
# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ] 
# report(marks)

# def total_sum(n):
#     li=[]
#     for i in n:
#         for j in n:
#             if i+j==number:
#                 li.append([i,j])
#                 n.remove(i)
#                 n.remove(j)
#     print(li)
# number = 30
# n = [10, 11, 12, 13, 14, 17, 18, 19] 
# total_sum(n)

# N = 3
# def isMagicSquare( mat) : 
# 	s = 0
# 	for i in range(0, N) : 
# 		s = s + mat[i][i] 
# 	s2 = 0
# 	for i in range(0, N) : 
# 		s2 = s2 + mat[i][N-i-1] 
# 	if(s!=s2) : 
# 		return False
# 	for i in range(0, N) : 
# 		rowSum = 0;	 
# 		for j in range(0, N) : 
# 			rowSum += mat[i][j] 
# 		if (rowSum != s) : 
# 			return False
# 	for i in range(0, N): 
# 		colSum = 0
# 		for j in range(0, N) : 
# 			colSum += mat[j][i] 
# 		if (s != colSum) : 
# 			return False

# 	return True
# mat = [ [ 2, 7, 6 ], 
# 		[ 9, 5, 1 ], 
# 		[ 4, 3, 8 ] ] 
	
# if (isMagicSquare(mat)) : 
# 	print( "Magic Square") 
# else : 
# 	print( "Not a magic Square") 


# def kitne_admi(elements):
#     ev=0
#     od=0
#     evsum=0
#     odsum=0
#     for i in elements:
#         if i%2==0:
#             ev+=1
#             evsum=+i
#         else:
#             od+=1
#             odsum=+i
#     print(f"{ev} is the lenght of even number")
#     print(f"{od} is the lenght of odd number")
#     print()
#     print(f"{evsum} is the sum of even number")
#     print(f"{odsum} is the sum of odd number")
#     print()
#     print(f"{evsum/ev} is the average of even number")
#     print(f"{round(odsum/od,2)} is the average of odd number")
# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
# kitne_admi(elements)


# def crorepati(paise):
#     cr=0
#     lak=0
#     dil=0
#     for i in paise:
#         if i>9999999:
#             cr+=1
#         elif i>99999:
#             lak+=1
#         else:
#             dil+=1
#     print(cr,"Crorepati hai")
#     print(lak,"Lakhpati hai")
#     print(dil,"Dilwale hai")
# paise = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
# crorepati(paise)

# def count_occurences(word):
#     b=[]
#     for i in word:
#         a=word.count(i)
#         f=[a,i]
#         if f not in b:
#             b.append(f)
#     print(b)
# word=input("Enter a word:")
# count_occurences(word)

# def duplicate(n):
#     b=[]
#     for i in n:
#         if i not in b:
#             b.append(i)
#     print(b)
# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] 
# duplicate(n)

# def sub_string(main_string):
#     print(main_string.replace("over",""))
# main_string = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# sub_string(main_string)

# def kbc(q,o,s):
#     n=0
#     k=1
#     for i in q:
#         print(i)
#         print("Here is your optins")
#         for m in o[n]:
#             if k==5:
#                 k=1
#             print(k,":",m)
#             k+=1
#         a=int(input("    "))
#         if a==s[n]:
#             print("You win")
#         else:
#             print("You lose")
#         n+=1  
# q= [
#     "How many continents are there?",              
#     "What is the capital of India?",            
#     "NG mei kaun se course padhaya jaata hai?"   
# ]
# o= [
#     ["Four", "Nine", "Seven", "Eight"],
#     ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
#     ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
# ]
# s = [3, 4, 1]
# kbc(q,o,s)

##################### END ###########################

#################### DICTIONARY #####################

# def add(dic1,dic2,dic3):
#     d={}
#     for i in dic1,dic2,dic3:
#         d.update(i)
#     print(d)
# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# add(dic1,dic2,dic3)

# def exist_or_not(dict):
#     if "name" in dict:
#         print("Yes")
#     else:
#         print("No")
# dict={"name":"Raju", "marks":56}
# exist_or_not(dict)

# def sum_of_dict(dic):
#     sum=0
#     for i in dic.values():
#         sum+=i
#     print(sum)
# dic= {
#         'data1':100,
#         'data2': -54,
#         'data3': 247
#        } 
# sum_of_dict(dic)

# def nes_dic(dic):
#     for i in dic.values():
#         if type(i)==dict:
#             for ii in i.keys():
#                 i.pop(ii)
#                 break
#     print(dic)
        
# dic= {
#         1: 'NAVGURUKUL',
#         2: 'IN',  
#   	    3:{    
#              'A' : 'WELCOME',
#              'B' : 'To',
#              'C' : 'DHARAMSALA'
#             }
#         }
# nes_dic(dic)

# def k_v(list1,list2):
#     d={}
#     for i in list1:
#         for j in list2:
#             d[i]=j
#             list2.remove(j)
#             break
#     print(d)
# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]  
# k_v(list1,list2)

# def uniq(li):
#     a=[]
#     b=[]
#     for i in li:
#         for j in i.values():
#             a.append(j)
#     for i in a:
#         if i not in b:
#             b.append(i)
#     print(b)
# li=[
#      {"first":"1"}, 
#      {"second": "2"}, 
#      {"third": "1"}, 
#      {"four": "5"}, 
#      {"five":"5"}, 
#      {"six":"9"},
#      {"seven":"7"}
# ]
# uniq(li)

# def student():
#     d={}
#     for i in range(1,11):
#         b=input("Enter student name:")
#         c=int(input("Enter student marks:"))
#         d[b]=c
#     print(d)
# student()

# def count_occ(a):
#     d={}
#     for i in a:
#         b=a.count(i)
#         d[i]=b
#     print(d)
# a=input("")
# count_occ(a)

# def coou(dic):
#     c=0
#     for i in dic.values():
#         for j in i:
#             c+=1
#     print(c)
# dic =  {
#    'Alex': ['subj1', 'subj2', 'subj3'], 
#    'David': ['subj1', 'subj2',"sdg"]}
# coou(dic)

# def highest(dic):
#     a=[]
#     for i in dic.values():
#         a.append(i)
#     p=max(a)
#     a.remove(p)
#     b=max(a)
#     a.remove(b)
#     c=max(a)
#     print([p,b,c])
# dic = {
#     'a':50, 
#     'b':58, 
#     'c':56,
#     'd':40, 
#     'e':100, 
#     'f':20
#     }
# highest(dic)
        
# def Square():
#     d={}
#     for i in range(1,16):
#         d[i]=i*i
#     print(d)
# Square()

# def highest(a):
#     b=[]
#     mx=max(a,key=a.get)
#     b.append(mx)
#     del a["e"]
#     maxi=max(a,key=a.get)
#     b.append(maxi)
#     del a["b"]
#     maxim=max(a,key=a.get)
#     b.append(maxim)
#     print(b)
# a = {
#     'a':50, 
#     'b':58, 
#     'c':56,
#     'd':40, 
#     'e':100, 
#     'f':20
#     }
# highest(a)

# def as_dec(a):
#     p={}
#     c=[]
#     d={}
#     for k in a:
#         h=a[k]
#         p[h]=k
#     for i in p:
#         c.append(i)
#     for i in range(len(c)):
#         for j in range(len(c)-1):
#             if c[i]>c[j]:
#                 c[i],c[j]=c[j],c[i]
#     for i in c:
#         s=p[i]
#         d[s]=i
#     print(d)
# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# as_dec(a)

######################### END ################################

########################### START ######################

#### ask function and call it 5 times #####

# def ask_question():
#     print("hello")
# ask_question()
# ask_question()
# ask_question()
# ask_question()
# ask_question()

##### using while loop ######

# def ask_question():
#     a=0
#     while a<100:
#         print("hello")
#         a+=1
# ask_question()

#### vote eligiblity ####

# def eligible_for_vote(a):
#     if a>=18:
#         print("You are eligible for voting")
#     else:
#         print("You are not eligible for voting")
# a=int(input(""))
# eligible_for_vote(a)

# def function_print_lines(a,b):
#     print( a +" is a good boy")
#     print(b)
# a=input()
# b=input()
# function_print_lines(a,b)

# def sumofdigits(number):
#     sum = 0
#     modulus = 0
#     while number!=0 :
#         modulus = number%10
#         sum+=modulus
#         number/=10
#     return sum
# print(sumofdigits(123))

# def greet(*names):
#     for name in names:
#         print("Welcome", name)
# greet("Rinki", "Vishal", "Kartik", "Bijender") 

# def ev(b,c):
#     if b%2==0 and c%2==0:
#         print("is even")
#     else:
#         print("is not even")
# b=int(input(  ))
# c=int(input(  ))
# ev(b,c)

# def clculator(a,b,c):
#     if b == "+":
#         return a+c
#     elif b== "-":
#         return a-c    
#     elif b=="/":
#         return a/c
#     elif b=="*":
#         return a*c
# a=int(input("Enter a first number:"))
# b=input("Enter a operation +,-,/,* = ")
# c=int(input("Enter a second number:"))
# print(clculator(a,b,c))

# def perfect():
#     for i in range(1,1000):
#         sum=0
#         for j in range(1,i):
#             if i%j==0:
#                 sum+=j
#         if i==j:
#             print(i)

# def perfect():
#     for Number in range(1,1000):
#         Sum = 0
#         for n in range(1, Number):
#             if(Number % n == 0):
#                 Sum = Sum + n
#         if(Sum == Number):
#             print(Number,"Is a perfect number")
# perfect()

# def su_ave():
#     sum=0
#     for i in range(3):
#         b=int(input("Enter a number:"))
#         sum+=b
#     c=sum/3
#     print(sum,"average of three number",c,"average of three number")
# su_ave()


# def show_num(a):
#     for i in range(a+1):
#         if i%2==0:
#             print(i,"Even number")
#         else:
#             print(i,"Odd number")
# a=int(input("Enter a number:"))
# show_num(a)

# def sum_num(a):
#     sum=0
#     for i in range(1,a+1):
#         if i%5==0 or i%3 ==0:
#             sum+=i
#     return sum
# a=int(input('Ener a number:'))
# print(sum_num(a))

# def speed(a):
#     if a<70:
#         print("ok")
#     elif a>69:
#         points=0
#         for i in range(a):
#             if i%5==0:
#                 points+=1
#         if points>12:
#             print(points, "License suspended")
# a=int(input("Enter a number:"))
# speed(a)        

# def le(a,b):
#     if len(a)>len(b):
#         print(a,"length is greater than ",b)
#     elif len(a)==len(b):
#         print(a,"are equal",b)
#     else:
#         print(b,"length is greater than ",a)
# a=input("Enter a first word:")
# b=input("Enter a second word:")
# le(a,b)

# def squar(a):
#     d={}
#     for i in range(1,a+1):
#         d[i]=i*i
#     print(d)
# a=int(input("Enter a number:"))
# squar(a)
        
########### Code Output ###############

# def employee(name,salary=2000):
#         print(name,"your salary is:-",salary)

# employee("kartik")
# employee("deepak") 

# def primeorNot(num):     
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#                 print(i,"times",num//i,"is",num)
#                 break
#             else:
#                 print(num,"is a prime number")

#     else:
#            print(num,"is not a prime number")
# primeorNot(3) 


# def greet(*names):
#     for name in names:
#                print("Hello", name)
# greet("sonu", "kartik", "umesh", "bijender")



# def sumofdigits(number):
#     sum = 0
#     modulus = 0
#     while number!=0 :
#         modulus = number%10
#         sum+=modulus
#         number/=10
#     return sum

# print(sumofdigits(123))

# def  meal(day,time):
#     if day=="sunday":
#         if time=="breakfast":
#             return "dosa"
#         elif time=="lunch":
#             return "dal rice"
#         elif time=="dinner":
#             return "paneer and  chapati"
#         else :
#             return "time not found"
#     elif day=="monday":
#         if time=="breakfast":
#             return "fried rice"
#         elif time=="lunch":
#             return "aloo rice"
#         elif time=="dinner":
#             return "chhole bhature"
#         else :
#             return "time not found"
#     elif day=="other":
#         if time=="breakfast":
#             return "aloo"
#         elif time=="lunch":
#             return "rajma rice"
#         elif time=="dinner"    :
#             return "veg-chapati"
#         else :
#             return "time not found"

# print(meal("sunday","lunch"))
# print(meal("monday","dinner")) 


############## Debug The code ###############

# def calculate_sum(a,b):
#     sum = a+b
#     print(sum)
# calculate_sum(4,5)

# def multi(a,b):
#     multiply=a*b
#     return multiply
# print(multi(3,4)) \



# def Avg(number1,number2,number3):
#     avg=number1+number2+number3/3
#     print(avg)
# Avg(1,3,2)


# def voter(age):
#     if age > 18:
#         print("eligible")
#     else:
#         print("not eligible")
# voter(20)

# def distance(kms):
#         if kms < 20:
#             print("close")
#         elif kms < 50:
#             print("median")
#         else:
#             Print("far")
# distance(20) 


# names=['siddik','vishal','suraj','ranjan']
# proper=[name.capitalize() for name in names]
# print(proper)

# proper=list(map(lambda .capitalize(),names))
# print(proper)


# find the max using lambda with reduce

# from functools import reduce
# a=[5,7,3,9,2,4,6,10,4,2,5,2]
# p=reduce((lambda x,y: y if (y>x) else x)   ,a)
# print(p)
