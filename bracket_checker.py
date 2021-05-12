# a=input("Enter a brackets for check: ")
# def brackets(a):
#     b=[]
#     for i in a:
#         if i == '('or i=='{' or i=='[': b.append(i) 
#         elif i == ')' or i=='}' or i==']':
#             if len(b)==0: return False
#             element =b.pop()
#             if not check(element,i): return False
#     if len(b) != 0: return False
#     return True
# def check(el,i):
#     if el == '(' and i == ')': return True
#     elif el == '{' and i == '}': return True
#     elif el == '[' and i == ']': return True
#     return False
# print(brackets(a))