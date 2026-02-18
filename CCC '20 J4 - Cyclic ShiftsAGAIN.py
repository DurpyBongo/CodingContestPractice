import sys
code = input()
base = input()
cashew = list(base)
for i in range(len(base)):
    if base in code:
        print('yes')
        sys.exit()

    else:
        hi = cashew[0]
        cashew.pop(0)
        cashew.append(hi)
        base=''.join(cashew)
print('no')


