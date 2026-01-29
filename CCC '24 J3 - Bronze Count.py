rounds = int(input())

scores = []
for i in range(rounds):
    ligma = input()
    scores.append(int(ligma))

scores.sort(reverse=True)

winnie = scores.copy()

for x in range(2):
    for u in range(len(scores)):
        if scores[u] == max(scores):
            winnie.pop(u)

hahaha = scores.count(max(scores))
print(f'{str(max(scores))} {str(hahaha)}')

