direction = []
steps = []

while True:
    code = input()
    ligma = int(code[0])+int(code[1])
    temp = []
    if code == '99999':
        break
    
    if ligma ==0:
        cashew = direction[-1]
        direction.append(cashew)
        temp.append(code[2])
        temp.append(code[3])
        temp.append(code[4])
        steps.append(''.join(temp))
    elif ligma % 2 ==0:
        direction.append('right')
        temp.append(code[2])
        temp.append(code[3])
        temp.append(code[4])
        steps.append(''.join(temp))
    else:
        direction.append('left')
        temp.append(code[2])
        temp.append(code[3])
        temp.append(code[4])
        steps.append(''.join(temp))

for i in range(len(direction)):
    print(f'{direction[i]} {steps[i]}')