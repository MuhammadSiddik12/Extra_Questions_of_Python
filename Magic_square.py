magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]] 
sum1,sum2,sum3,sum4=0,0,0,0
for j in magic_square:
    for i in range(len(magic_square)): sum1+=j[i]
for i in range(len(magic_square)): 
    for j in magic_square: sum2+=j[i]
    for k in range(len(magic_square)):
        if i==k: sum3+=magic_square[i][k]
        if i+k==2: sum4+=magic_square[i][k]
print("It is a Magic Square") if sum1//3==sum2//3==sum3==sum4 else print("It is not a Magic Square")