# dic={"vishal":20,"suraj":15,"tushar":19,"siddik":18}
# for x in dic:
#     print(x)

# for x in dic:
#     print(dic[x])

# for x in dic.values():
#     print(x)

# for x,y in dic.items():
#     print(x,y)

# dic["siddik"]=12
# print(dic)


# dic[12]="sid"
# print(dic)

# if "vishal" in dic:
#     print("yes! it is eixt in dictionary")
# else:
#     print("no! it is eixt in dictionary")

# x=len(dic)
# print(x)

# dic.pop("vishal")
# print(dic)

# dic.popitem()
# print(dic)

# del dic["vishal"]
# print(dic)


# del dic
# print(dic)

# dic.clear()
# print(dic)

# x=dic.copy()
# print(x)
# print(dic)

# x=("vishu","s","t")
# y=0
# dic=dict.fromkeys(x,y)
# print(dic)

# x=dic.setdefault("vishu","19.5")
# print(x)

# d={"day":"black"}
# dic.update(d)
# print(dic)

# d = {1: "one", 2: "three"}
# d1 = {2: "two"}

# # updates the value of key 2
# d.update(d1)
# print(d)

# d1 = {3: "three"}

# # adds element with key 3
# d.update(d1)
# print(d)

# student={}
# while True:
#     l=input("enter your name and Id:>")
#     if l=="q":
#         break
#     Id,name=l.split(",")
#     student.update({Id:name})
# for x,y in student.items():
#     print(x,y)
# key=input("enter Id to search:")
# if key in student:
#     print("key=",key,"value=",student[key])
# else:
#     print("key is not found:")


# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {}
# for d in (dic1, dic2, dic3): 
#     dic4.update(d)
# print(dic4)


# dic1={1:10, 2:20,3:30, 4:40,5:50,6:60}
# if 4 in dic1:
#     print("yes it already exits")
# else:
#     print("no it already exits")

# my_dict = {
#         'data1':100,
#         'data2': -54,
#         'data3': 247
#        }
# s=0
# for i in my_dict.values():
#     s=s+i
# print(s)

# CAR_DETAILS={
#     "brand": "Ford",
#     "model": "jason",
#     "year": 1964
# }
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS)

# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }
# person.popitem()
# print(person)

 
# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }

# del person['name']
# print(person)

# states_capitals = {
#   'Gujarat' : 'Gandhinagar',
#   'Maharashtra' : 'Mumbai',
#   'Rajasthan' : 'Jaipur',
#   'Bihar' : 'Patna'
#   }
# for state in states_capitals:
#       print(state)


# states_capitals = {
#     'Gujarat' : 'Gandhinagar',
#     'Maharashtra' : 'Mumbai',
#     'Rajasthan' : 'Jaipur',
#     'Bihar' : 'Patna'
#     }

# for state in states_capitals:
#     print(states_capitals[state])

# details ={
#     "name":  "Bijender",
#     "age":  17,
#     "class":  "10th"
#     }
# for x in details.values():
#     print(x)

# movie ={
#     "name":  "Puli",
#     "hero":  "Vijay",
#     "rating":  7.5
#     }
# for x,y in movie.items():
#     print(x,y)

# d1={1:10, 2:20}
# d2={3:30,2:40}
# d3={5:50,6:60}
# d4={}
# for i in (d1,d2,d3):
#     d4.update(i)
# print(d4)
    
# dict={"name":"Raju", "marks":56}
# n=input()
# if n in dict:
#     print("exit")
# else:
#     print("not exit")


# my_dict = {
#     'data1':100,
#     'data2': -54,
#     'data3': 247
# }

# s=0
# print(s)
# for i in my_dict.values():
#     s+=i
# print(s)

# details={
#     "name":"Shanti",
#     "age":12,
#     "email":"shanti@navgurukul.org",
#     }
# print(details["name"])
# print(details["email"])
# print(details["age"])

# d= {
#     1: 'NAVGURUKUL',
#     2: 'IN',  
#     3:{    
#         'A' : 'WELCOME',
#         'B' : 'To',
#         'C' : 'DHARAMSALA'
#     }
# }
# for i in d:
#     if i==3:
#         del d[3]['A']
# print(d)

      
# l1=["one","two","three","four","five"]
# l2=[1,2,3,4,5,]
# d=dict(zip(l1,l2))
# print(d)

# l1=["one","two","three","four","five"]
# l2=[1,2,3,4,5,]
# my={}
# for l,v in zip(l1,l2):
#     my[l]=v
# print(my)

# l1=["one","two","three","four","five"]
# l2=[1,2,3,4,5,]
# m={}
# for i in l1:
#     m[i]=l2[0]
# print(m)

# dic={
#     "ball":"red",
#     "bat":4,
#     "wickets":8,
#     "ball":"greem",
#     "bat":3
# }
# print(dic)

# a=[
#     {"first":"1"}, 
#     {"second": "2"}, 
#     {"third": "1"}, 
#     {"four": "5"}, 
#     {"five":"5"}, 
#     {"six":"9"},
#     {"seven":"5"},
#     {"vishal":12},
#     {"visha":12},
#     {"vish":16}
# ]
# b=[]
# for i in a:
#     for j in i.values():
#         if j not in b:
#             b.append(j)
# print(b)

# # v="MISSISSIPPI"
# v="vishal"
# n=0
# m={}
# for i in v:
#     m[i]=n
#     n+=1
# print(m)
# student={}
# while True:
#     n=input("enter your name and marks: ")
#     if n=="v":
#         break
#     Id,name=n.split(",")
#     student.update({Id:name})
# print(student)

# s={}
# for i in range(10):
#     n=input("Enter students name and marks: ")
#     if n=="v":
#         break
#     m,name=n.split(",")
#     s.update({m:name})
# print(s)


# d =  {
#    'Alex': ['subj1', 'subj2', 'subj3'], 
#    'David': ['subj1', 'subj2']}
# c=0
# for i in d:
#     for v in d[i]:
#         c+=1
# print(c)

# m = {
#     'a':50, 
#     'b':58, 
#     'c':56,
#     'd':40, 
#     'e':100, 
#     'f':20
# }
# k=[]
# ma=[]
# for i in m.values():
#     k.append(i)   
#     a=k[0] 
#     for j in k:
#         if a<j:
#             a=j
#             ma.append(a)
#             k.remove(a)
# print(ma)

# d={}
# s=1
# for i in range(1,16):
#     s=i*i
#     d[i]=s
# print(d)

# m = {
#     'a':50, 
#     'b':58,
#     'c': 56,
#     'd':40,
#     'e':100, 
#     'f':20
# }
# k=[]
# ma=[]
# for i in m.values():
#     k.append(i)   
#     a=k[0] 
#     for j in k:
#         if a<j:
#             a=j
#             ma.append(a)
#             k.remove(a)
# h=[]
# for i in m:
#     for j in ma:
#         if m[i]==j:
#             h.append(i)
# print(h)     
# print(ma)

# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# for i in a.values():
#     for j in :
#         if a[i]>a[j]:
#             v=a[i]
#             a[i]=a[j]
#             a[j]=v
# print(a)



# d={"v":6,"i":1,"s":3,"h":4,"a":5,"l":2}
# for  i in d.



# D = {}   
# n = int(input('How many student record you want to store?? ')) 
# ls = [] 
# for i in range(0, n): 
#     x,y = input("Enter the student name and it's percentage: ").split()  
#     ls.append((y,x)) 
# ls = sorted(ls, reverse = True)  
# for i in ls:  
#     print(i[1], i[0])


# a = ["no bun","bug bun bug bun bug bug","bunny bug","buggy bug bug buggy"]
# b = "bug"
# c = {}
# for i in a:
#   count = 0
#   for j in i.split():
#     if j == b:
#       count = count+1
#   c[count]=i
# d = []
# for s in sorted(c):
#   d.append(c[s])
# d.reverse()
# print (d)


# num=int(input("enter your num:"))
# n=num//2
# b=1
# while b<=n:
#     print((" "*(n-b)+"* "*b)+("  "*(n-b)+"* "*b))
#     b+=1

# for i in range(num,0,-1):
#     print(" "*(num-i)+"* "*i)

# num=int(input("enter your num:"))
# n=num//2
# b=0
# while b<n:
#     b+=1
#     if b==1:
#         continue
#     print((" "*(n-b)+"* "*b)+("  "*(n-b)+"* "*b))
    
# for i in range(num,0,-2):
#     print(" "*(num-i)+"* "*i)
        





  
