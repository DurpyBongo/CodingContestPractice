import sys

allofthem = []
while True:
    instruction = input()

    one = []

    temporary = []
    if instruction == '99999':
        break
    direction = int(instruction[0])+int((instruction[1]))
    if direction == 0:
        one.append(allofthem[-1][0])
        for x in range(2,len(instruction)):
            temporary.append(instruction[x])
        steps = ''.join(temporary)
        one.append(steps)
        allofthem.append(one)
    elif direction % 2 == 0 and direction != 0:
        one.append('right')
        for x in range(2,len(instruction)):
            temporary.append(instruction[x])
        steps = ''.join(temporary)
        one.append(steps)
        allofthem.append(one)
    elif direction % 2 != 0 and direction != 0:
        one.append('left')
        for x in range(2,len(instruction)):
            temporary.append(instruction[x])
        steps = ''.join(temporary)
        one.append(steps)
        allofthem.append(one)
    temporary =[]
    one=[]

for i in range(len(allofthem)):
    print(f'{allofthem[i][0]} {allofthem[i][1]}')