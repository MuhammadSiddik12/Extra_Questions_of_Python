dic={}
for i in range(3):
    Team_name=input("Enter Your Team Name:")
    player_name=input("Enter your Team Members Name:")
    dic[Team_name]=player_name.split()
print(dic)
first=[]
li=[]
Round=1
new=[]
while Round<=5:
    print()
    indivisual_player=[]
    print(f"Round {Round} \n")
    indivisual_player=[]
    for i in range(1):
        for k in dic.values():
            A=5
            B=4
            C=3
            D=2
            E=1
            F=0
            if Round == 2 :
                A += 1
                B += 1
                C += 1
                D += 1
                E += 1
                F += 0
            elif Round == 3:
                A += 2
                B += 2
                C += 2
                D += 2
                E += 2
                F += 0
            elif Round == 4 :
                A += 3
                B += 3
                C += 3
                D += 3
                E += 3
                F += 0
            elif Round == 5 :
                A += 4
                B += 4
                C += 4
                D += 4
                E += 4
                F += 0
            for j in range(1):
                inp=input(f"Enter Target:A,B,C,D,E,F {k[0]}:")
                sec_inp=input(f"Enter Target:A,B,C,D,E,F {k[1]}")
                if sec_inp=="A" and inp==sec_inp : ## FOR A A
                    A=A+A+2
                    li.append(A)
                    print()
                    indivisual_player.append([A])
                elif sec_inp =="B" and inp == sec_inp: ## FOR B B
                    B=B+B+2
                    li.append(B)
                    print()
                    indivisual_player.append([B])
                elif sec_inp=="C" and inp == sec_inp: ## FOR C C
                    C=C+C+2
                    li.append(C)
                    print()
                    indivisual_player.append([C])
                elif sec_inp=="D" and inp == sec_inp: ## FOR D D
                    D=D+D+2                         
                    li.append(D)
                    print()
                    indivisual_player.append([D])
                elif sec_inp=="E" and inp == sec_inp: ## FOR E E
                    E=E+E+2
                    li.append(E)
                    print()
                    indivisual_player.append([E])
                elif sec_inp=="F" and inp == sec_inp: ## FOR F F
                    F=F+F+F
                    li.append(F)
                    print()
                    indivisual_player.append([F])
                elif inp=="A" and sec_inp == "C" or inp =="C" and sec_inp == "A": ## FOR A C
                    li.append(A+C)
                    print()
                    indivisual_player.append([A,C])
                elif inp=="A" and sec_inp == "D" or inp =="D" and sec_inp == "A": ## FOR A D
                    li.append(A+D)
                    print()
                    indivisual_player.append([A,D])
                elif inp=="A" and sec_inp == "E" or inp =="E" and sec_inp == "E": ## FOR A E
                    li.append(A+E)
                    print()
                    indivisual_player.append([A,E])
                elif inp=="A" and sec_inp == "F" or inp=="F" and sec_inp == "A": ## FOR A F
                    li.append(A+F)
                    print()
                    indivisual_player.append([A,F])  
                elif inp=="A" and sec_inp== "B" or inp == "B" and sec_inp == "A": ## FOR  A B
                    li.append(A+B)
                    print()
                    indivisual_player.append([A,B])     
                elif inp=="B" and sec_inp == "C" or inp=="C" and sec_inp == "B": ## FOR B C 
                    li.append(B+C)
                    print()
                    indivisual_player.append([B,C])
                elif inp=="B" and sec_inp == "D" or inp=="D" and sec_inp == "B": ## FOR B D
                    li.append(B+D)
                    print()
                    indivisual_player.append([B,D])
                elif  inp=="B" and sec_inp == "E" or inp=="E" and sec_inp == "B" : ## FOR B E
                    li.append(B+E)
                    print()
                    indivisual_player.append([B,E])
                elif inp=="B" and sec_inp == "F" or inp=="F" and sec_inp == "B": ## FOR B F
                    li.append(B+F)
                    print()
                    indivisual_player.append([B,F])
                elif inp=="C" and sec_inp == "D" or inp=="D" and sec_inp == "C" : ## FOR C D
                    li.append(C+D)
                    print()
                    indivisual_player.append([C,D])
                elif inp=="C" and sec_inp == "E" or inp=="E" and sec_inp == "C": ## FOR C E
                    li.append(C+E)
                    print()
                    indivisual_player.append([C,E])
                    indivisual_player.append(E)
                elif inp=="C" and sec_inp == "F" or inp=="F" and sec_inp == "C": ## FOR C F
                    li.append(C+F)
                    print()
                    indivisual_player.append([C,F])
                elif inp=="D" and sec_inp == "E" or inp=="E" and sec_inp == "D": ## FOR D E
                    li.append(D+E)
                    print()
                    indivisual_player.append([D,E])
                elif inp=="D" and sec_inp == "F" or inp=="F" and sec_inp == "D": ## FOR D F
                    li.append(D+F)
                    print()
                    indivisual_player.append([D,F])
                elif inp=="E" and sec_inp == "F" or inp=="F" and sec_inp == "E": ## FOR E F
                    li.append(E+F)
                    print()
                    indivisual_player.append([E,F])
                else:
                    print("invalid") 
    for k in li:
        first.append(li[0:3])
        li.clear()
    Round+=1
    new.append(indivisual_player)
a=["First","second","Third","Forth","Fifth"]
for s in first:
    for j in a:
        print(f"score board of {j} Round:",[*s])
        a.remove(j)
        break
print(new)
sum_of_first_team=0
for i in first:
    sum_of_first_team+=i[0]  # print(sum_of_first_team)
sum_of_second_team=0
for K in first:
    sum_of_second_team+=K[1] # print(sum_of_second_team)
sum_of_third_team=0
for N in first:
    sum_of_third_team+=N[2] # print(sum_of_third_team)
if sum_of_first_team>=60:
    print("First team wins","Total Score:",sum_of_first_team)
else:
    print("First team lose","Total Score:",sum_of_first_team)
if sum_of_second_team>=60:
    print("second team wins","Total Score:",sum_of_second_team)
else:
    print("second team lose","Total Score:",sum_of_second_team)
if sum_of_third_team>=60:
    print("third team lose","Total Score:",sum_of_third_team)
else:
    print("third team lose","Total Score:",sum_of_third_team)