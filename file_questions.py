"""
"r" - open file for reading - default
"w" - open file for writing 
"x" - Create file if not exits
"a" - add more content to a file
"t" - text mode file - default
"b" - binary mode 
"+" - read and write
"""

# f=open("vishal.txt","w")
# # print(f.read())
# a=f.write("Vishal is the king of the world \n")
# print(a)
# # for i in f:
# #     print(i,end="")
# # print(f.readlines())
# # print(f.readline())
# f.close()

# # handle write and read both
# f=open("vishal.txt","r+")
# f.readline()
# print(f.read())

# # f.write("vishal is the kind")
# # f.close()


# # f=open("vishal.txt","w")
# # # print(f.read())
# # a=f.write("Vishal is the king of the world \n")
# # print(a)
# # # for i in f:
# # #     print(i,end="")
# # # print(f.readlines())
# # # print(f.readline())
# # f.close()

# # handle write and read both
# # f=open("vishal.txt","r+")
# # print(f.read())

# # f=open("people1-exercise.txt","r+")
# # print(f.read())
# # f.write("vishal")
# # f.close()


# f=open("vishal.txt","r")
# c=f.read()
# print(c)

# f.close()

# my_file = open("people1.txt","x")
# # file_data = my_file.read()
# # print (file_data)
# my_file.close() 

# batch1_students = ["Shivam", "Rahul", "Kavay", "Dhannu", "Deepanshu", "Nitin", "Manoj", "Shakrudin", "Tara", "Suraj", "Krishna"]
# students_file = open("navgurukul_students.html", "w")
# students_file.write("<html>\n")
# students_file.write("<head>\n")
# students_file.write("<title>NavGurukul Students</title>\n")
# students_file.write("</head>\n")
# students_file.write("<body>\n")
# students_file.write("<ul>")
# for student in batch1_students:
#     students_file.write("<li>" + student + "</li>\n")
# students_file.write("</ul>\n")
# students_file.write("</body>\n")
# students_file.write("</html>\n")
# students_file.close() 

# v=open("nav.txt", "w")
# v.write("Vishal is smart boy.")
# v.write("Vishal is intelligent boy.")
# v.close()


# my_file3 = open("test_file.txt", "r")

# # my_file3.write("Yahan main kuch likha")
# # my_file3.write("\nYaha maine kuch aur bhi likha.")
# v=my_file3.readlines()
# print(v)
# # print(f.readline())
# my_file3.close() 


# f=open("test_file.txt","rt")
# # print(f.readlines())
# # v=f.readline()
# # d=f.readline()
# # print(d)
# # print(v)
# # r=f.read(111)
# # print(r)
# c=0
# for i in f:
#     c+=1
# #     # print(i,end="")
# print(c)
# f.close()


# f=open("vishal.txt","r")
# co=f.read()
# c=0
# for i in co:
#     c+=i
# print(c)

# f.close()

# f=open("test_file.txt","rt")
# c=0
# for i in f:
#     c+=1
# print(c)
# f.close()


# f=open("vish1.txt","r+")
# print(f.read())
# banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
# for i in banks_list:
#     print(i)
# f.close()


# f=open("vish.txt","w")
# f.write("New File")
# for i in f:
#     if i=="delhi" :
#         print("vihasl")
# f.close()

# def file_read(fname):
#         txt = open(fname)
#         print(txt.read())

# file_read('vish.txt')

# def file_read(fname):
#         from itertools import islice
#         with open(fname, "w") as myfile:
#                 myfile.write("Python Exercises\n")
#                 myfile.write("Java Exercises")
#         txt = open(fname)
#         print(txt.read())
# file_read('abc.txt')

# def file_read(fname):
#         with open (fname, "r") as myfile:
#                 data=myfile.readlines()
#                 print(data)
# file_read('vish.txt')


# f=open("vish1.txt","r+")
# f.write("welcome in new file")
# print(f.read())
# f.close()

# def file_read(fname):
#         content_array = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
#         # with open(fname) as f:
#         f=open(fname,"r")
#                 #Content_list is the list that contains the read lines.     
#         for line in f:
#             print(line)
# file_read("vish.txt")