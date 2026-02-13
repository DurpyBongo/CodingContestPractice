base = int(input())
rounds = int(input())
temp = []
all = []
for i in range(2*rounds):
    rules = input()
    if len(temp)<2:
        temp.append(rules)
    if len(temp) == 2:
        all.append(temp)
        temp = []
for i in range(len(all)):
    if all[i][0] == '+':
        base += int(all[i][1])
    elif all[i][0] == '-':
        base -= int(all[i][1])
print(str(base))
