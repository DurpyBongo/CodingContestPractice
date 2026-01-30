all_extra_rules = []
temporary = []
all_extra_rules.append([1,7])
all_extra_rules.append([1,4])
all_extra_rules.append([2,1])
all_extra_rules.append([3,4])
all_extra_rules.append([3,5])

final_print = []


while True:
    x = int(input())
    y = int(input())
    temporary.append(x)
    temporary.append(y)
    if temporary != [0,0]:
        all_extra_rules.append(temporary)
        temporary = []
    else:
        break

all_extra_rules.sort()


intial_no_arrows = []

for i in all_extra_rules:
    intial_no_arrows.append(i[1])
intial_no_arrows = list(set(intial_no_arrows))

ohio = [1,2,3,4,5,6,7]

c = list(set(ohio) - set(intial_no_arrows))

first_number = min(c)

final_print.append(min(c))
c.remove(min(c))

for l in range(6):
    for i in range(len(all_extra_rules)):
        if all_extra_rules[i][0] == first_number:
            candidate = all_extra_rules[i][1]
            blocked = False

            for rule in all_extra_rules:
                if rule[1] == candidate and rule[0] not in final_print:
                    blocked = True
                    break

            if not blocked and candidate not in final_print:
                c.append(candidate)
    c = list(c)
    try:
        for bahaha in final_print:
            if bahaha == min(c):
                c.remove(bahaha)
        final_print.append(min(c))
        first_number = min(c)
        c.remove(min(c))

        last = [str(item) for item in final_print]
        print(' '.join(last))
    except ValueError:
        print("Cannot complete these tasks. Going to bed.")
        break
    

    