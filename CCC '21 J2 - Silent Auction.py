rounds=int(input())
names = []
bid = []
for i in range(2*rounds):
    cashew = input()
    if i % 2 == 0:
        names.append(cashew)
    else:
        bid.append(int(cashew))

print(names[bid.index(max(bid))])