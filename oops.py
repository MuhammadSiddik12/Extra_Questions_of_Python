# class siddik:
#     def __init__(self,fname,lname,phone,password):
#         self.fname=fname
#         self.lname=lname
#         self.phone=phone
#         self.password=password
#     @classmethod
#     def from_str(cls,emp_string):
#         fname,lname,phone,password=emp_string.split('-')
#         return cls(fname,lname,phone,password)


# a=siddik('Muhammad','Siddik','9811073783','Mds@12')
# b=siddik.from_str('Vishal-majumdar-9582300883-Vishal@12')
# print(b.fname,b.lname,b.phone,b.password)

# class Parrot:

#     # class attribute
#     species = "bird"

#     # instance attribute
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # instantiate the Parrot class
# blu = Parrot("Blu", 10)
# woo = Parrot("Woo", 15)
# print(blu.name,blu.age)