# # circle_name_per_round_by_player
# dic={}
# for i in range(3):
#     Team_name=input("Team Name: ")
#     player_name=input("Player's Name: ")
#     dic[Team_name]=player_name.split()
# print('Teams Name :', dic)
# new,first,li=[],[],[]
# Round=1
# while Round <= 3:
#     print(f"\nRound {Round}\n")
#     indivisual_player=[]
#     for k in dic.values():
#         A,B,C,D,E,F=5,4,3,2,1,0
#         if Round == 2 :
#             A += 1
#             B += 1
#             C += 1
#             D += 1
#             E += 1
#             F = 0
#         elif Round == 3:
#             A += 2
#             B += 2
#             C += 2
#             D += 2
#             E += 2
#             F = 0
#         inp=input(f"Enter Target:A,B,C,D,E,F : {k[0]} ").upper()
#         sec_inp=input(f"Enter Target:A,B,C,D,E,F : {k[1]} ").upper()
#         print()
#         if sec_inp=="A" and inp==sec_inp : ## FOR A A
#             indivisual_player.append(A)
#             A=A+A+2
#             li.append(A)
#         elif sec_inp =="B" and inp == sec_inp: ## FOR B B
#             indivisual_player.append(B)
#             B=B+B+2
#             li.append(B)
#         elif sec_inp=="C" and inp == sec_inp: ## FOR C C
#             indivisual_player.append(C)
#             C=C+C+2
#             li.append(C)
#         elif sec_inp=="D" and inp == sec_inp: ## FOR D D
#             indivisual_player.append(D)
#             D=D+D+2                         
#             li.append(D)
#         elif sec_inp=="E" and inp == sec_inp: ## FOR E E
#             indivisual_player.append(E)
#             E=E+E+2
#             li.append(E)
#         elif sec_inp=="F" and inp == sec_inp: ## FOR F F
#             indivisual_player.append(F)
#             F=F+F+0
#             li.append(F)
#         elif inp=="A" and sec_inp== "B" or inp == "B" and sec_inp == "A": ## FOR  A B
#             li.append(A+B)
#             indivisual_player.append(A)
#             indivisual_player.append(B)
#         elif inp=="A" and sec_inp == "C" or inp =="C" and sec_inp == "A": ## FOR A C
#             li.append(A+C)
#             indivisual_player.append(A)
#             indivisual_player.append(C)
#         elif inp=="A" and sec_inp == "D" or inp =="D" and sec_inp == "A": ## FOR A D
#             li.append(A+D)
#             indivisual_player.append(A)
#             indivisual_player.append(D)
#         elif inp=="A" and sec_inp == "E" or inp =="E" and sec_inp == "E": ## FOR A E
#             li.append(A+E)
#             indivisual_player.append(A)
#             indivisual_player.append(E)
#         elif inp=="A" and sec_inp == "F" or inp=="F" and sec_inp == "A": ## FOR A F
#             li.append(A+F)
#             indivisual_player.append(A)
#             indivisual_player.append(F)
#         elif inp=="B" and sec_inp == "C" or inp=="C" and sec_inp == "B": ## FOR B C 
#             li.append(B+C)
#             indivisual_player.append(B)
#             indivisual_player.append(C)
#         elif inp=="B" and sec_inp == "D" or inp=="D" and sec_inp == "B": ## FOR B D
#             li.append(B+D)
#             indivisual_player.append(B)
#             indivisual_player.append(D)
#         elif  inp=="B" and sec_inp == "E" or inp=="E" and sec_inp == "B" : ## FOR B E
#             li.append(B+E)
#             indivisual_player.append(B)
#             indivisual_player.append(E)
#         elif inp=="B" and sec_inp == "F" or inp=="F" and sec_inp == "B": ## FOR B F
#             li.append(B+F)
#             indivisual_player.append(B)
#             indivisual_player.append(F)
#         elif inp=="C" and sec_inp == "D" or inp=="D" and sec_inp == "C" : ## FOR C D
#             li.append(C+D)
#             indivisual_player.append(C)
#             indivisual_player.append(D)
#         elif inp=="C" and sec_inp == "E" or inp=="E" and sec_inp == "C": ## FOR C E
#             li.append(C+E)
#             indivisual_player.append(C)
#             indivisual_player.append(E)
#         elif inp=="C" and sec_inp == "F" or inp=="F" and sec_inp == "C": ## FOR C F
#             li.append(C + F)
#             indivisual_player.append(C)
#             indivisual_player.append(F)
#         elif inp=="D" and sec_inp == "E" or inp=="E" and sec_inp == "D": ## FOR D E
#             li.append(D + E)
#             indivisual_player.append(D)
#             indivisual_player.append(E)
#         elif inp=="D" and sec_inp == "F" or inp=="F" and sec_inp == "D": ## FOR D F
#             li.append(D+F)
#             indivisual_player.append(D)
#             indivisual_player.append(F)
#         elif inp=="E" and sec_inp == "F" or inp=="F" and sec_inp == "E": ## FOR E F
#             li.append(E+F)
#             indivisual_player.append(E)
#             indivisual_player.append(F)
#         else : print("Invalid Input") 
#     for k in li:
#         new.append(li[0:3])
#         li.clear()
#     a=["First","Second","Third","Forth","Fifth"]
#     for s in new:
#         for j in a:
#             print(f"Score Board Of {j} Round : ",*s)
#             a.remove(j)
#             break
#     Round+=1
#     first.append(sum(indivisual_player))
# print('Indivisual Players Score : ',new)
# print('Final Team Score : ',first)
# print("\nFirst team wins","Total Score:",first[0]) if first[0]>=30 else print("\nFirst team lose","Total Score:",first[0])
# print("Second team wins","Total Score:",first[1]) if first[1]>=30 else print("Second team lose","Total Score:",first[1])
# print("Third team lose","Total Score:",first[2]) if first[2]>=30 else print("Third team lose","Total Score:",first[2])