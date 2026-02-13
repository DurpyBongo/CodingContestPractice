
rounds = int(input())
empty = []
for i in range(rounds):
    ligma = int(input())
    empty.append(ligma)

x = empty.count(max(empty))
empty.sort()
for i in range(x):
    empty.pop(-1)

y = empty.count(max(empty))
for i in range(y):
    empty.pop(-1)
b = empty.count(max(empty))

print(f'{max(empty)} {b}')