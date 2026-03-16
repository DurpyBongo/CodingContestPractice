one = int(input())
two = int(input())
three = int(input())
four = int(input())
five = int(input())

difficulty = int(input())

empty = []
empty.append(one)
empty.append(two)
empty.append(three)
empty.append(four)
empty.append(five)

empty.sort()
empty.pop(0)
empty.pop(-1)

count = 0
for i in empty:
    count+=i
ligma = count*difficulty

print(ligma)