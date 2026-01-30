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

tasks = [1,2,3,4,5,6,7]
final_print = []

while len(final_print) < 7:
    available = []

    for task in tasks:
        if task in final_print:
            continue

        blocked = False
        for rule in all_extra_rules:
            if rule[1] == task and rule[0] not in final_print:
                blocked = True
                break

        if not blocked:
            available.append(task)

    if not available:
        print("Cannot complete these tasks. Going to bed.")
        break

    next_task = min(available)
    final_print.append(next_task)

if len(final_print) == 7:
    print(" ".join(str(x) for x in final_print))
    

    